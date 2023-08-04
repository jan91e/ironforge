// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "solmate/auth/Owned.sol";

contract Dwarf is Owned(msg.sender) {
    uint256 public immutable param;

    constructor(uint256 param_) {
        param = param_;
    }
}