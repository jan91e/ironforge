// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.5.0 <0.9.0;

interface IChildLiquidityGauge {
    function deposit(
        uint256 _value,
        address _user
    ) external;

    function deposit(uint256 _value) external;
}