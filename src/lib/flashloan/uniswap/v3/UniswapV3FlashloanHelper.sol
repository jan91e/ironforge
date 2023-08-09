import {IUniswapV3Flashloan} from "../../../../interfaces/flashloan/uniswap/v3/IUniswapV3Flashloan.sol";
import {IUniswapV3FlashloanReceiver} from "../../../../interfaces/flashloan/uniswap/v3/IUniswapV3FlashLoanReceiver.sol";
import {IUniswapV3PoolImmutables} from "../../../../interfaces/dex/uniswap/v3/uniswapV3pool/IUniswapV3PoolImmutables.sol";
import {IERC20} from "../../../../interfaces/tokens/IERC20.sol";

abstract contract UniswapV3FlashloanHelper is IUniswapV3FlashloanReceiver {
    
    struct UniswapV3FlashloanParam {
        address token0;
        uint256 amount0Borrow;
        address token1;
        uint256 amount1Borrow;
        bytes callbackData;
    }

    function borrow(address _provider, uint256 _amount0, uint256 _amount1, bytes memory data) internal {
        
        address _token0 = IUniswapV3PoolImmutables(_provider).token0();
        if (_amount0 > 0) {
            uint256 _bal0 = IERC20(_token0).balanceOf(_provider);
            _amount0 = _amount0 > _bal0 ? _bal0 : _amount0;
        }

        address _token1 = IUniswapV3PoolImmutables(_provider).token1();
        if (_amount1 > 0) {
            uint256 _bal1 = IERC20(_token1).balanceOf(_provider);
            _amount1 = _amount1 > _bal1 ? _bal1 : _amount1;
        }
        
        bytes memory _data = abi.encode(UniswapV3FlashloanParam({
            token0: _token0,
            amount0Borrow: _amount0,
            token1: _token1,
            amount1Borrow: _amount1,
            callbackData: data
        }));
        
        IUniswapV3Flashloan(_provider).flash(
            address(this),
            _amount0,
            _amount1,
            _data            
        );
    }

    function uniswapV3FlashCallback(
        uint256 fee0,
        uint256 fee1,
        bytes calldata data
    ) external {
        UniswapV3FlashloanParam memory p = abi.decode(data, (UniswapV3FlashloanParam));

        _flashloanLogic(p.callbackData);
        
        if (fee0 > 0) {
            IERC20(p.token0).transfer(msg.sender, fee0 + p.amount0Borrow);
        }

        if (fee1 > 0) {
            IERC20(p.token1).transfer(msg.sender, fee1 + p.amount1Borrow);
        }
    }

    function _flashloanLogic(bytes memory data) internal virtual;
}