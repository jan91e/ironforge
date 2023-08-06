// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "../../../../src/constants/bsc/tokens/tokens.sol";

import {IERC20} from "../../../../src/interfaces/tokens/IERC20.sol";

import {
    BscDppSingleFlashloanHelper,
    BscDppUniFlashloanHelper
} from "../../../../src/lib/flashloan/dodo/BscDppFlashloanHelper.sol";

import "forge-std/Test.sol";
import "forge-std/console.sol";

contract BscDppSingleFlashloanHelperExample is BscDppSingleFlashloanHelper {
    address assetBorrow;
    uint256 public amountBorrowed;

    function Tborrow(address _token, uint256 _amount) external {
        assetBorrow = _token;
        borrow(_token, _amount);
    }

    function _flashloanLogic(bytes calldata data) internal override {
        amountBorrowed = IERC20(assetBorrow).balanceOf(address(this));
    }
}

contract BscDppSingleFlashloanHelperTest is Test {
    BscDppSingleFlashloanHelperExample private t;

    function setUp() public {
        vm.createSelectFork("bsc", 29668034);

        t = new BscDppSingleFlashloanHelperExample();
    }
    uint constant USDT_RESERVES_MAX = 1960152691723488871255523;
    uint constant WBNB_RESERVES_MAX = 4042067177748204800679;
    uint constant WETH_RESERVES_MAX = 213720786561209145571;
    uint constant BTCB_RESERVES_MAX = 10064509255477516960;

    function testBorrowUSDTFixedAmount() public {
        deal(address(this), 0);

        t.Tborrow(BSC_USD, 1000e18);
        assertEq(t.amountBorrowed(), 1000e18);

        t.Tborrow(BSC_USD, 10000e18);
        assertEq(t.amountBorrowed(), 10000e18);
        
        t.Tborrow(BSC_USD, 100000e18);
        assertEq(t.amountBorrowed(), 100000e18);

        t.Tborrow(BSC_USD, 1000000e18);
        assertEq(t.amountBorrowed(), 1000000e18);

        t.Tborrow(BSC_USD, 10000000e18);
        assertEq(t.amountBorrowed(), USDT_RESERVES_MAX);
    }

    function testBorrowUSDTMAX() public {
        deal(address(this), 0);
        
        t.Tborrow(BSC_USD, type(uint).max);
        assertEq(t.amountBorrowed(), USDT_RESERVES_MAX);
    }

    function testBorrowWBNBFixedAmount() public {
        deal(address(this), 0);
        
        t.Tborrow(WBNB, 100e18);
        assertEq(t.amountBorrowed(), 100e18);

        t.Tborrow(WBNB, 1000e18);
        assertEq(t.amountBorrowed(), 1000e18);

        t.Tborrow(WBNB, 10000e18);
        assertEq(t.amountBorrowed(), WBNB_RESERVES_MAX);
    }

    function testBorrowWBNBMAX() public {
        deal(address(this), 0);

        t.Tborrow(WBNB, type(uint).max);
        assertEq(t.amountBorrowed(), WBNB_RESERVES_MAX);
    }

    function testBorrowWETHFixedAmount() public {
        deal(address(this), 0);

        t.Tborrow(WETH, 1e18);
        assertEq(t.amountBorrowed(), 1e18);

        t.Tborrow(WETH, 10e18);
        assertEq(t.amountBorrowed(), 10e18);
        
        t.Tborrow(WETH, 100e18);
        assertEq(t.amountBorrowed(), 100e18);

        t.Tborrow(WETH, 1000e18);
        assertEq(t.amountBorrowed(), WETH_RESERVES_MAX);
    }

    function testBorrowWETHMAX() public {
        deal(address(this), 0);

        t.Tborrow(WETH, type(uint).max);
        assertEq(t.amountBorrowed(), WETH_RESERVES_MAX);
    }

    function testBorrowBTCBFixedAmount() public {
        deal(address(this), 0);

        t.Tborrow(BTCB, 1e18);
        assertEq(t.amountBorrowed(), 1e18);

        t.Tborrow(BTCB, 10e18);
        assertEq(t.amountBorrowed(), 10e18);
        
        t.Tborrow(BTCB, 100e18);
        assertEq(t.amountBorrowed(), BTCB_RESERVES_MAX);
    }

    function testBorrowBTCBAX() public {
        deal(address(this), 0);
        
        t.Tborrow(BTCB, type(uint).max);
        assertEq(t.amountBorrowed(), BTCB_RESERVES_MAX);
    }    
}

contract BscDppUniFlashloanHelperExample is BscDppUniFlashloanHelper {
    address[] private assets;
    mapping(address => uint) public amountBorrowed;

    function Tborrow(address[] memory _tokens, uint256[] memory _amounts) external {
        assets = _tokens;
        borrow(_tokens, _amounts, "ff");
    }

    function _flashloanLogic(bytes memory data) internal override {
        for(uint i; i < assets.length;++i) {
            address asset = assets[i];
            amountBorrowed[asset] = IERC20(asset).balanceOf(address(this));
        }
    }
}

contract BscDppUniFlashloanHelperTest is Test {
    BscDppUniFlashloanHelperExample private t;

    function setUp() public {
        vm.createSelectFork("bsc", 29668034);

        t = new BscDppUniFlashloanHelperExample();
    }
    uint constant USDT_RESERVES_MAX = 1960152691723488871255523;
    uint constant WBNB_RESERVES_MAX = 4042067177748204800679;
    uint constant WETH_RESERVES_MAX = 213720786561209145571;
    uint constant BTCB_RESERVES_MAX = 10064509255477516960;

    function testBorrowTFixedAmounts() public {
        deal(address(this), 0);

        address[] memory tokens = new address[](4);
        {
            tokens[0] = BSC_USD;
            tokens[1] = WBNB;
            tokens[2] = WETH;
            tokens[3] = BTCB;
        }
        uint256[] memory amounts = new uint256[](4);
        {
            amounts[0] = 1e18;
            amounts[1] = 1e18;
            amounts[2] = 1e18;
            amounts[3] = 1e18;
        }
        
        t.Tborrow(tokens, amounts);
        for(uint i; i < tokens.length;++i){
            address token = tokens[i];
            assertEq(t.amountBorrowed(token), 1e18);
        }
    }

    function testBorrowMAX() public {
        deal(address(this), 0);
        

        address[] memory tokens = new address[](4);
        {
            tokens[0] = BSC_USD;
            tokens[1] = WBNB;
            tokens[2] = WETH;
            tokens[3] = BTCB;
        }
        uint256[] memory amounts = new uint256[](4);
        {
            amounts[0] = type(uint).max;
            amounts[1] = type(uint).max;
            amounts[2] = type(uint).max;
            amounts[3] = type(uint).max;
        }
        uint256[] memory Tamounts = new uint256[](4);
        {
            Tamounts[0] = USDT_RESERVES_MAX;
            Tamounts[1] = WBNB_RESERVES_MAX;
            Tamounts[2] = WETH_RESERVES_MAX;
            Tamounts[3] = BTCB_RESERVES_MAX;
        }
        
        t.Tborrow(tokens, amounts);
        for(uint i; i < tokens.length;++i){
            address token = tokens[i];
            assertEq(t.amountBorrowed(token), Tamounts[i]);
        }
    }
}