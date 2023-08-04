// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {CheatCodes} from "./ICheatCodes.sol";

import "../src/deadmines/23_07_Carson/Shaman.sol";

import "forge-std/Test.sol";

contract ShamanTest is Test {
    Shaman public shaman;
    CheatCodes cheats = CheatCodes(0x7109709ECfa91a80626fF3989D68f67F5b1DD12D);

    function setUp() public {
        cheats.createSelectFork("bsc", 30306324);

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