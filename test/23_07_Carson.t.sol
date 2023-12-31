// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "../src/deadmines/23_07_Carson/Shaman.sol";

import "forge-std/Test.sol";

contract ShamanTest is Test {
    Shaman public shaman;

    function setUp() public {
        vm.createSelectFork("bsc", 30306324);

        shaman = new Shaman();
    }
    
    function testPeek() public {
        shaman.peek();
    }

    function testBeat() public {
        deal(address(this), 0);
        shaman.beat();
    }
}