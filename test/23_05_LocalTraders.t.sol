// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import { CheatCodes } from "./ICheatCodes.sol";

import "../src/deadmines/23_05_LocalTraders/Shaman.sol";

import "forge-std/Test.sol";
import "forge-std/Vm.sol";
import "forge-std/console.sol";

contract ShamanTest is Test, RuinLocation {
    Shaman public shaman;
    CheatCodes cheats = CheatCodes(0x7109709ECfa91a80626fF3989D68f67F5b1DD12D);

    function setUp() public {
        cheats.createSelectFork("bsc", 28460898);

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
