# Bamboo

> Time: BSC#29668035
> 
> Tag: `Price Manipulation`, `Public Burn`, `Deflation Token`
> 
> Malicious Txs: 
> 
> - 0x88a6c2c3ce86d4e0b1356861b749175884293f4302dbfdbfb16a5e373ab58a10
> 
> - 0xda41af9d60d62eef28444b4c42f80754140767efb8ecef1b68b4fb1c11baa789
> 
> - 0x5abde3804002e3625dddb48407204d107eae65069df938489737eadcd79f282f


## Code snippet:

```solidity
function updatePool(uint256 amount) private {
    if (amount > 10000 && balanceOf(uniswapPair) > amount) {
        uint256 fA = amount / 100;
        _balances[uniswapPair] = _balances[uniswapPair].sub(fA);
        _balances[Factory] = _balances[Factory].add(fA);
        try IUniswapV2Pair(uniswapPair).sync() {} catch {}
    }
}
```

## Attack steps:

1. transfer Bamboo to the BAMBOO/WBNB pool directly and then skim all from the pool

2. repeat the step 1 many times

2. swap all Bamboo tokens for WBNB to drain all WBNB in the BAMBOO/WBNB pool

## Root Cause:

The BAMBOO token burn 1% fee on transfer amounts of the pool, when tokens are sent to the pool.
By transfering the BAMBOO tokens directly to the pool and immediately removeing them by trigering the function `skim` in the pool, the BAMBOO reserve in the pool continues to decrease, which inflates the price of the BAMBOO in the pool.

## Refs
