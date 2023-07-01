import "forge-std/console.sol";

contract Shaman {
    function peek() external {}

    // attack entrypoint
    function beat() external {
        console.log("[>*BOOM*<] Profit =");
    }
}