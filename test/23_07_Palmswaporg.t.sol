import "../src/deadmines/23_07_Palmswaporg/Shaman.sol";

import "forge-std/Test.sol";

contract ShamanTest is RuinLocation, Test {
    Shaman public shaman;

    function setUp() public {
        vm.createSelectFork("bsc", 30248637);
        
        vm.label(PLP_VAULT, "PLP_VAULT");
        vm.label(PLP_LIQUIDITY_EVENT, "PLP_LIQUIDITY_EVENT");
        vm.label(PLP_MANAGER, "PLP_MANAGER");
        vm.label(PLP, "PLP");
        vm.label(USDP, "USDP");

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