import "../src/deadmines/23_08_EarningFarm/Shaman.sol";

import "forge-std/Test.sol";

contract ShamanTest is Test {
    Shaman public shaman;

    function setUp() public {
        vm.createSelectFork("mainnet", 17875885);

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