# CS Token

> Time: BSC#28466976

> Tag: `Flashloan`, `Rebasing Token`, `Public Burn`

> Malicious Txs: 0x906394b2ee093720955a7d55bff1666f6cf6239e46bea8af99d6352b9687baa4

## Code snippet:

```solidity
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) private {
        ...
        if(canSell &&from != address(this) &&from != uniswapV2Pair &&from != owner() && to != owner() && !_isLiquidity(from,to)){
            sync();
        }
        ...
        if(takeSellFee){
            ...
            sellAmount = amount;
            ...
        }
        ...
    }
```

```solidity
    function sync() private lockTheSync{
        if (totalBurnAmount>=maxBurnAmount){
            return;
        }
        uint256 burnAmount = sellAmount.mul(800).div(1000);
        sellAmount = 0;
        ...
        if (_tOwned[uniswapV2Pair]>burnAmount ){
            ...
            _tOwned[uniswapV2Pair] -= burnAmount;
            _tOwned[address(burnAddress)] += burnAmount;
            ...
        }
    } 
```

## Attack steps:

1. Borrow $USDT using flashswap from the pool BUSD_USDT pool
2. [Buy CS] swap exact amount (LIMIT_BUY = 5000e18) CS using USDT repeatly
    - Note: CS transfer from pair to user (BUY) take 1% transfer amount from user. (i.e transfer 100, user can receive only 99)
3. Swap remaining USDT for CS to pump the price of CS
    - Note: recepient should be in the feeWhitelist #why?
4. [Sell CS] swap exact amount (LIMIT_SELL = 3000e18) for USDT
    - Note: in this step, the `SellAmount` is setted to LIMIT_SELL
5. transfer 1 CS to self, which burns 80% * LIMIT_SELL amount CS tokens in the pool
6. Repeat step 4 and step 5 many times to drain the pool

There is a simplified example (Suppose the initial liquidity of the pool is 10,000 USDT : 10,000 CS):
1. swap 10,000 USDT for 5,000 CS (now: 20,000 USDT : 5,000 CS)
2. swap 3,000 CS for 7,500 USDT (now: 12,500 USDT : 8,000 CS)
3. transfer and burn 3,000 * 80% = 2,400 CS (now: 12,500 USDT : 5,600 CS)
4. swap 2,000 CS for 3,290 USDT (now: 9,210 USDT : 7,600 CS)
profit: 3,290 + 7,500 - 10,000 = 790 USDT

## Root cause:
The reserve of uniswap pool can be burn by its underlying token. 

## Refs
- https://twitter.com/DeDotFiSecurity/status/1661092709392629783

- https://twitter.com/BlockSecTeam/status/1661098394130198528

- https://twitter.com/numencyber/status/1661207123102167041