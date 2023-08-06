// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "../src/deadmines/23_05_CS/Shaman.sol";

import "forge-std/Test.sol";

contract ShamanTest is Test, RuinLocation {
    Shaman public shaman;

    function setUp() public {
        vm.createSelectFork("bsc", 28466976);

        vm.label(USDT, "USDT");
        vm.label(CS, "CS");
        vm.label(CS_HOLDER, "CS_HOLDER");
        vm.label(RECV, "RECV");
        vm.label(PANCAKE_ROUTER, "PANCAKE_ROUTER");
        vm.label(USDT_CS_PAIR, "USDT_CS_PAIR");
        vm.label(USDT_BUSD_PAIR, "USDT_BUSD_PAIR");

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
