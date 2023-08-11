import {
    BALANCER_VAULT as ARB_BALANCER_VAULT
} from "../../../constants/arbitrum.sol";

import {IERC20} from "../../../interfaces/tokens/IERC20.sol";
import {IBalancerVaultFlashloan} from "../../../interfaces/flashloan/balancer/IBalancerVaultFlashloan.sol";
import {IBalancerVaultFlashloanReceiver} from "../../../interfaces/flashloan/balancer/IBalancerVaultFlashloanReceiver.sol";

abstract contract BalancerVaultFlashloanHelper is IBalancerVaultFlashloanReceiver {

    function borrow(address _provider, address[] memory _tokens, uint256[] memory _amounts) internal {
        IBalancerVaultFlashloan(_provider).flashLoan(this, _tokens, _amounts, "");
    }

    function receiveFlashLoan(
        address[] memory tokens,
        uint256[] memory amounts,
        uint256[] memory feeAmounts,
        bytes memory userData
    ) external {
        
        _flashloanLogic(userData);

        uint _tokensLen = tokens.length;
        for (uint i; i < _tokensLen;) {
            uint256 _repayAmount = amounts[i] - feeAmounts[i];
            IERC20(tokens[i]).transfer(msg.sender, _repayAmount);
            unchecked {
                ++i;
            }
        }
    }

    function _flashloanLogic(bytes memory data) internal virtual;
}

abstract contract ArbitrumBalancerVaultFlashloanHelper is BalancerVaultFlashloanHelper {
    function borrow(address[] memory _tokens, uint256[] memory _amounts) internal {
        IBalancerVaultFlashloan(ARB_BALANCER_VAULT).flashLoan(this, _tokens, _amounts, "");
    }
}