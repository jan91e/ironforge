import "../src/Shaman.sol";

import {CheatCodes} from "./ICheatCodes.sol";
import "forge-std/Test.sol";

contract ShamanTest is Test {
    Shaman public shaman;
    CheatCodes cheats = CheatCodes(0x7109709ECfa91a80626fF3989D68f67F5b1DD12D);

    function setUp() public {
        // cheats.createSelectFork("bsc", 29469406);

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