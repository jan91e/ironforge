# Curve

> Time: ETH#17806056
>
> Tag: `Vyper Compiler Bug`, `Reentrancy`
> 
> Malicious Txs:
> 
> - ETH#17806056 | Curve.fi Factory Pool: pETH/ETH | 0xa84aa065ce61dbb1eb50ab6ae67fc31a9da50dd2c74eefd561661bfce2f1620c
>   Note: pETH (i.e. 0x836A808d4828586A69364065A1e064609F5078c7 | JPEG’d ETH)
> 
> - ETH#17806772 | Curve.fi Factory Pool: alETH/ETH | 0xb676d789bb8b66a08105c844a49c2bcffb400e5c1cfabd4bc30cca4bff3c9801
>   Note: alETH (i.e. 0x0100546F2cD4C9D97f798fFC9755E47865FF7Ee6 | Alchemix ETH)
> 
> - ETH#17806550 | Curve.fi Factory Pool: msETH/ETH | 0xc93eb238ff42632525e990119d3edc7775299a70b56e54d83ec4f53736400964
>   Note: msETH (i.e. 0x64351fC9810aDAd17A690E4e1717Df5e7e085160 | Metronome Synth ETH)
>
> - ETH#17807830 | Curve.fi CryptoSwap Pool: CRV/ETH | 0x2e7dc8b2fb7e25fd00ed9565dcc0ad4546363171d5e00f196d48103983ae477c
> 
> - ETH#17808683 | Arbitrage in Curve.fi CryptoSwap Pool: CRV/ETH | 0xcd99fadd7e28a42a063e07d9d86f67c88e10a7afe5921bd28cd1124924ae2052
> 
> - ETH#17827741 | Curve.fi: sBTC Swap | 0xe928d5de53bea42231d0dd140a3f761adb93081038a368591eb1166168297bdc
> 
> - ETH#17845588 | Arbitrage in CryptoSwap Pool: CRV/ETH  | 0x006763dff653ecddfd3681181a29e7e6d6c2aaa7bafb27fe1376f3f7ce367c1e
>
> - BSC#30419439 | Curve.fi: StableSwap Horizon Protocol zBNB/BNB | 0x58ebe3bc31014e711624fd61b1aa26c625a9148790b5b60495cd727e3fc107ea
> 
> - BSC#30419557 | Curve.fi: StableSwap Elliupsis.finance BNB/BNBL | 0xf7b3d0f2853ae06374b68efe2ed13f0b6d17c8f6b85164e5b43f6d8d68b5e2d1
> 
> - BSC#30419578 | Curve.fi: StableSwap BNBx/BNB | 0xe190c4eddf67b262be137329c8cbc8897d3ae6b19ee37e9300c160d830beea69
> 

## Code snippet:


- vyper compiler with version 0.2.15

```github_permalink@https://github.com/vyperlang/vyper/blob/6e7dba7a8b5f29762d3470da4f44634b819c808d/vyper/semantics/validation/data_positions.py#L20C1-L44C60
def set_storage_slots(vyper_module: vy_ast.Module) -> None:
    """
    Parse module-level Vyper AST to calculate the layout of storage variables.
    """
    # Allocate storage slots from 0
    # note storage is word-addressable, not byte-addressable
    storage_slot = 0

    for node in vyper_module.get_children(vy_ast.FunctionDef):
        type_ = node._metadata["type"]
        if type_.nonreentrant is not None:
            type_.set_reentrancy_key_position(StorageSlot(storage_slot))
            # TODO use one byte - or bit - per reentrancy key
            # requires either an extra SLOAD or caching the value of the
            # location in memory at entrance
            storage_slot += 1

    for node in vyper_module.get_children(vy_ast.AnnAssign):
        type_ = node.target._metadata["type"]
        type_.set_position(StorageSlot(storage_slot))
        # CMC 2021-07-23 note that HashMaps get assigned a slot here.
        # I'm not sure if it's safe to avoid allocating that slot
        # for HashMaps because downstream code might use the slot
        # ID as a salt.
        storage_slot += math.ceil(type_.size_in_bytes / 32)
```


- vyper compiler with version 0.2.16, 0.3.0

```github_permalink@https://github.com/vyperlang/vyper/blob/8a23febbb2d523f3701f9a7d0aaf361c104a2a37/vyper/semantics/validation/data_positions.py#L22C1-L66C15
def set_storage_slots(vyper_module: vy_ast.Module) -> StorageLayout:
    """
    Parse module-level Vyper AST to calculate the layout of storage variables.
    Returns the layout as a dict of variable name -> variable info
    """
    # Allocate storage slots from 0
    # note storage is word-addressable, not byte-addressable
    storage_slot = 0

    ret = {}

    for node in vyper_module.get_children(vy_ast.FunctionDef):
        type_ = node._metadata["type"]
        if type_.nonreentrant is not None:
            type_.set_reentrancy_key_position(StorageSlot(storage_slot))

            # TODO this could have better typing but leave it untyped until
            # we nail down the format better
            variable_name = f"nonreentrant.{type_.nonreentrant}"
            ret[variable_name] = {
                "type": "nonreentrant lock",
                "location": "storage",
                "slot": storage_slot,
            }

            # TODO use one byte - or bit - per reentrancy key
            # requires either an extra SLOAD or caching the value of the
            # location in memory at entrance
            storage_slot += 1

    for node in vyper_module.get_children(vy_ast.AnnAssign):
        type_ = node.target._metadata["type"]
        type_.set_position(StorageSlot(storage_slot))

        # this could have better typing but leave it untyped until
        # we understand the use case better
        ret[node.target.id] = {"type": str(type_), "location": "storage", "slot": storage_slot}

        # CMC 2021-07-23 note that HashMaps get assigned a slot here.
        # I'm not sure if it's safe to avoid allocating that slot
        # for HashMaps because downstream code might use the slot
        # ID as a salt.
        storage_slot += math.ceil(type_.size_in_bytes / 32)

    return ret
```

- Curve.fi Factory Pool (alETH/ETH)

```etherscan@https://etherscan.io/address/0x6326debbaa15bcfe603d831e7d75f4fc10d9b43e#code#L613-L660
@external
@nonreentrant('lock')
def remove_liquidity(
    _burn_amount: uint256,
    _min_amounts: uint256[N_COINS],
    _receiver: address = msg.sender
) -> uint256[N_COINS]:
    """
    @notice Withdraw coins from the pool
    @dev Withdrawal amounts are based on current deposit ratios
    @param _burn_amount Quantity of LP tokens to burn in the withdrawal
    @param _min_amounts Minimum amounts of underlying coins to receive
    @param _receiver Address that receives the withdrawn coins
    @return List of amounts of coins that were withdrawn
    """
    total_supply: uint256 = self.totalSupply
    amounts: uint256[N_COINS] = empty(uint256[N_COINS])

    for i in range(N_COINS):
        old_balance: uint256 = self.balances[i]
        value: uint256 = old_balance * _burn_amount / total_supply
        assert value >= _min_amounts[i], "Withdrawal resulted in fewer coins than expected"
        self.balances[i] = old_balance - value
        amounts[i] = value

        if i == 0:
            raw_call(_receiver, b"", value=value)
        else:
            response: Bytes[32] = raw_call(
                self.coins[1],
                concat(
                    method_id("transfer(address,uint256)"),
                    convert(_receiver, bytes32),
                    convert(value, bytes32),
                ),
                max_outsize=32,
            )
            if len(response) > 0:
                assert convert(response, bool)

    total_supply -= _burn_amount
    self.balanceOf[msg.sender] -= _burn_amount
    self.totalSupply = total_supply
    log Transfer(msg.sender, ZERO_ADDRESS, _burn_amount)

    log RemoveLiquidity(msg.sender, amounts, empty(uint256[N_COINS]), total_supply)

    return amounts
```

## Attack steps:

- Factory Pool Expolit Steps:

1. add liquidity and remove all liquidity subsequently.

2. reenter the function add_liquditiy in the `Curve.fi Factory Pool` contract in the `fallback` function of the receiver (due to the untrusted externall call in the function `remove_liquidity`).

3. remove all liquidity.


## Root Cause:
There exists a legacy bug (malfunctioning reentrancy locks) in the Vyper compiler affecting certain versions: 0.2.15, 0.2.16, 0.3.0.
In these vulnerable versions, the Vyper compiler allocates an increment slot for the `@nonreentrant` decorator even if the key of the reentrant lock is the same.
The reentrancy lock doesn't work as expected. Specifically, functions that use the `@nonreentrant("lock")` are prevented from re-entering themselves, but can still re-enter each other.

## Refs

- https://osec.io/blog/2023-08-01-vyper-timeline