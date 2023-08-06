# Palmswaporg

> Time: BSC#30248638
> 
> Tag: `Price Manipulation`, `ACL`
> 
> Malicious Txs:
> 
> - 0x62dba55054fa628845fecded658ff5b1ec1c5823f1a5e0118601aa455a30eac9

## Code snippet:


- the PLPManager contract:

```solidity
function _removeLiquidity(
    address _account,
    uint256 _plpAmount,
    uint256 _minOut,
    address _receiver
) private returns (uint256) {
    require(_plpAmount > 0, "PlpManager: invalid _plpAmount");
    require(
        lastAddedAt[_account] + cooldownDuration <= block.timestamp,
        "PlpManager: cooldown duration not yet passed"
    );

    // calculate aum before sellUSDP
    uint256 aumInUsdp = getAumInUsdp(false);
    uint256 plpSupply = IERC20Upgradeable(plp).totalSupply();

    uint256 usdpAmount = (_plpAmount * aumInUsdp) / plpSupply;
    uint256 usdpBalance = IERC20Upgradeable(usdp).balanceOf(address(this));
    if (usdpAmount > usdpBalance) {
        IUSDP(usdp).mint(address(this), usdpAmount - usdpBalance);
    }

    IMintable(plp).burn(_account, _plpAmount);

    IERC20Upgradeable(usdp).safeTransfer(address(vault), usdpAmount);
    uint256 amountOut = vault.sellUSDP(_receiver);
    require(amountOut >= _minOut, "PlpManager: insufficient output");

    emit RemoveLiquidity(
        _account,
        _plpAmount,
        aumInUsdp,
        plpSupply,
        usdpAmount,
        amountOut
    );

    return amountOut;
}
```

```solidity
function getAumInUsdp(bool maximise)
    public
    view
    override
    returns (uint256)
{
    uint256 aum = getAum(maximise);
    return (aum * (10**USDP_DECIMALS)) / PRICE_PRECISION;
}
```

```solidity
function getAum(bool maximise) public view returns (uint256) {
    uint256 length = vault.allWhitelistedTokensLength();
    uint256 aum = aumAddition;
    IVault _vault = vault;

    uint256 collateralTokenPrice = maximise
        ? _vault.getMaxPrice(collateralToken)
        : _vault.getMinPrice(collateralToken);

    uint256 collateralDecimals = _vault.tokenDecimals(collateralToken);

    uint256 currentAmmDeduction = (vault.permanentPoolAmount() *
        collateralTokenPrice) / (10**collateralDecimals);
    aum +=
        (vault.poolAmount() * collateralTokenPrice) /
        (10**collateralDecimals);
    ...
}
```

- the Vault contract:

```solidity
function buyUSDP(address _receiver)
    external
    override
    nonReentrant
    returns (uint256)
{
    _validateManager();
    _validateAddr(_receiver);

    address _collateralToken = collateralToken;
    useSwapPricing = true;

    uint256 tokenAmount = _transferIn(_collateralToken);
    _validate(tokenAmount > 0, 13);

    uint256 price = getMinPrice(_collateralToken);

    uint256 _usdpAmount = (tokenAmount * price) / PRICE_PRECISION;
    _usdpAmount = adjustForDecimals(_usdpAmount, _collateralToken, usdp);
    _validate(_usdpAmount > 0, 14);

    uint256 feeBasisPoints = vaultUtils.getBuyUsdpFeeBasisPoints(
        _collateralToken,
        _usdpAmount
    );
    uint256 amountAfterFees = _collectSwapFees(
        _collateralToken,
        tokenAmount,
        feeBasisPoints
    );
    uint256 mintAmount = (amountAfterFees * price) / PRICE_PRECISION;
    mintAmount = adjustForDecimals(mintAmount, _collateralToken, usdp);

    _increaseUsdpAmount(mintAmount);
    _increasePoolAmount(tokenAmount);

    IUSDP(usdp).mint(_receiver, mintAmount);

    emit BuyUSDP(_receiver, tokenAmount, mintAmount, feeBasisPoints);

    useSwapPricing = false;
    return mintAmount;
}
```

```solidity
function _increasePoolAmount(uint256 _amount) private {
    poolAmount += _amount;
    uint256 balance = IERC20Upgradeable(collateralToken).balanceOf(
        address(this)
    );
    _validate(poolAmount <= balance, 40);
    emit IncreasePoolAmount(_amount);
}
```

## Attack steps:

1. purchase ~996,324 PLP using 1,000,000 USDT (IN)

2. buy ~1,993,538 USDP using 2,000,000 USDT (IN)
Note: inflate the pool amount in the Vault contract, which lifts the price of the PLP

3. unstake all PLP (~996,324) and withdraw ~1,962,472 USDT (OUT)

4. sell all USDP (~1,993,538) for ~1,947,570 USDT (OUT)

## Root Cause:
The price of PLP is determined based on the balance of USDT in the contract Vault. It has the potential to be artificially inflated through the purchase of USDP using USDT.

## Refs
