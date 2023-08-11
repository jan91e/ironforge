import "../src/deadmines/23_08_MEVBot/Shaman.sol";

import "forge-std/Test.sol";

contract ShamanTest is Test, RuinLocation {
    Shaman public shaman;

    function setUp() public {
        vm.createSelectFork("arbitrum", 117708228);

        vm.label(MEV_BOT, "MEV_BOT");
        vm.label(MEV_BOT_IMPL, "MEV_BOT_IMPL");
        vm.label(USDC, "USDC");
        vm.label(WBTC, "WBTC");
        vm.label(WETH, "WETH");
        vm.label(ARB, "ARB");
        vm.label(DAI, "DAI");
        vm.label(USDT, "USDT");
        
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