// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.5.0 <0.9.0;

interface DVM {
  function flashLoan(
    uint256 baseAmount,
    uint256 quoteAmount,
    address assetTo,
    bytes calldata data
  ) external;

  function init(
    address maintainer,
    address baseTokenAddress,
    address quoteTokenAddress,
    uint256 lpFeeRate,
    address mtFeeRateModel,
    uint256 i,
    uint256 k,
    bool isOpenTWAP
  ) external;

  function _BASE_TOKEN_() external returns(address);
  function _QUOTE_TOKEN_() external returns(address);
}