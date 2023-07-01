// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.5.0 <0.9.0;

interface IDaiFlashloan {
    function flashLoan(
        address receiver,
        address token,
        uint256 amount,
        bytes calldata data
    ) external returns (bool);
}