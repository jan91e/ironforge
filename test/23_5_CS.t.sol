// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import { CheatCodes } from "./ICheatCodes.sol";

import "../src/deadmines/23_05_CS/Shaman.sol";

import "forge-std/Test.sol";
import "forge-std/Vm.sol";
import "forge-std/console.sol";

contract ShamanTest is Test, RuinLocation {
    Shaman public shaman;
    CheatCodes cheats = CheatCodes(0x7109709ECfa91a80626fF3989D68f67F5b1DD12D);

    function setUp() public {
        cheats.createSelectFork("bsc", 28466976);

        cheats.label(USDT, "USDT");
        cheats.label(CS, "CS");
        cheats.label(CS_HOLDER, "CS_HOLDER");
        cheats.label(RECV, "RECV");
        cheats.label(PANCAKE_ROUTER, "PANCAKE_ROUTER");
        cheats.label(USDT_CS_PAIR, "USDT_CS_PAIR");
        cheats.label(USDT_BUSD_PAIR, "USDT_BUSD_PAIR");

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
