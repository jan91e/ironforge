// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.5.0 <0.9.0;

interface IDOODLENFTXVault {

  function flashLoan(
    address receiver,
    address token,
    uint256 amount,
    bytes memory data
  ) external returns (bool);
  
  function redeem(uint256 amount, uint256[] calldata specificIds) external returns (uint256[] calldata);
  
  function balanceOf(address account) external view returns (uint256);
  
  function mint(
    uint256[] calldata tokenIds,
    uint256[] calldata amounts /* ignored for ERC721 vaults */
  ) external returns (uint256);
}