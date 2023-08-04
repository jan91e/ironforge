import {RuinLocation} from "./ruins/RuinLocation.sol";
import "forge-std/console.sol";

contract Shaman is RuinLocation {
    function peek() external {}

    // attack entrypoint
    function beat() external {
        console.log("[>*BOOM*<] Profit =");
    }
}