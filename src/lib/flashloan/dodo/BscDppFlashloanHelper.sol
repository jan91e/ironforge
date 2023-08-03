import {IERC20} from "../../../interfaces/tokens/IERC20.sol";
import {IDppFlashloan} from "../../../interfaces/flashloan/dodo/IDppFlashloan.sol";
import {IDppFlashloanReceiver} from "../../../interfaces/flashloan/dodo/IDppFlashloanReceiver.sol";

import {
    BSC_USD as USDT,
    DPP_ORACLE_BTCB,
    DPP_ORACLE_WBNB,
    DPP_ORACLE_WETH,
    DPP_WBNB,
    DPP_ADVANCED_WBNB
} from "../../../constants/bsc.sol";

abstract contract BscDppFlashloanHelper is IDppFlashloanReceiver {
    mapping(address => bool) _isProvider;

    modifier onlyDppFlashloanProvider {
        require(_isProvider[msg.sender]);
        _;
    }

    function borrowUSDT(uint256 _amount) internal {
        _isProvider[DPP_ORACLE_BTCB] = true;
        _isProvider[DPP_ORACLE_WBNB] = true;
        _isProvider[DPP_ORACLE_WETH] = true;
        _isProvider[DPP_WBNB] = true;
        _isProvider[DPP_ADVANCED_WBNB] = true;
        _launchDppFlashloan(DPP_ORACLE_BTCB, _amount);
    }

    struct DppFlashloanParam {
        uint256 remaining;
    }

    function _launchDppFlashloan(address _provider, uint256 _amount) private {
        uint256 _providerReserve = IERC20(USDT).balanceOf(_provider);
        uint256 _borrowAmount = _providerReserve >= _amount ? _amount : _providerReserve;
        uint256 _remaining = _providerReserve >= _amount ? 0 : _amount - _providerReserve;
        
        bytes memory _data = abi.encode(DppFlashloanParam({
            remaining: _remaining
        }));

        IDppFlashloan(_provider).flashLoan(
            0, 
            _borrowAmount, 
            address(this), 
            _data
        );
    }

    function DPPFlashLoanCall(
        address sender,
        uint256 baseAmount,
        uint256 quoteAmount,
        bytes calldata data
    ) external onlyDppFlashloanProvider {
        DppFlashloanParam memory params = abi.decode(data, (DppFlashloanParam));
        if (params.remaining == 0) {
            _flashloanLogic(data);
            return;
        }

        if (msg.sender == DPP_ORACLE_BTCB) {
            _launchDppFlashloan(DPP_ORACLE_WBNB, params.remaining);
        } else if (msg.sender == DPP_ORACLE_WBNB) {
            _launchDppFlashloan(DPP_ORACLE_WETH, params.remaining);
        } else if (msg.sender == DPP_ORACLE_WETH) {
            _launchDppFlashloan(DPP_WBNB, params.remaining);
        } else if (msg.sender == DPP_WBNB) {
            _launchDppFlashloan(DPP_ADVANCED_WBNB, params.remaining);
        } else if (msg.sender == DPP_ADVANCED_WBNB) {
            _flashloanLogic(data);
        } else {
            revert("not valid flashloan provider");
        }

        IERC20(USDT).transfer(msg.sender, quoteAmount);
    }

    function _flashloanLogic(bytes calldata data) internal virtual;
}