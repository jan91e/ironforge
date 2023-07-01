// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.5.0 <0.9.0;

interface IUniswapV2Pair {
    function swap(
      uint256 amount0Out,
      uint256 amount1Out,
      address to,
      bytes calldata data
    ) external;
    function skim(address to) external;
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function price0CumulativeLast() external view returns (uint);
    function price1CumulativeLast() external view returns (uint);
}