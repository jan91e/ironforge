import "src/deadmines/23_07_LibertiVault/Shaman.sol";

import "forge-std/Test.sol";

contract ShamanTest is Test {
    Shaman public shaman;

    function setUp() public {
        vm.createSelectFork("mainnet", 17668993);

        deal(address(this), 2000000000000000);
        shaman = new Shaman{value: 2000000000000000}();
    }
    
    function testPeek() public {
        shaman.peek();
    }

    function testBeat() public {
        shaman.beat();
    }
}