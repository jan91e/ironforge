// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "../src/deadmines/23_05_LocalTraders/Shaman.sol";

import "forge-std/Test.sol";

contract ShamanTest is Test, RuinLocation {
    Shaman public shaman;

    function setUp() public {
        vm.createSelectFork("bsc", 28460898);

        shaman = new Shaman{value: IERC20(LCT).balanceOf(LCT_EX) / 1000000000000000000}();
    }
    
    function testPeek() public {
        shaman.peek();
    }

    function testBeat() public {
        deal(address(this), 0);
        shaman.beat();
    }
}
