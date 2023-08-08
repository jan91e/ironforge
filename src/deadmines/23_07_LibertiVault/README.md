# LibertiVault

> Time: ETH#17668993
>
> Tag: `Reentrancy`, `Inaccurate calculation`
>
> Malicious Txs:
> 
> ETH: 0xcb0ad9da33ecabf75df0a24aabf8a4517e4a7c5b1b2f11fee3b6a1ad9299a282
> 
> POLYGON: 0x7320accea0ef1d7abca8100c82223533b624c82d3e8d445954731495d4388483

## Code snippet:


- 1nch AggregationRouterV4

```solidity
/// @notice Performs a swap, delegating all calls encoded in `data` to `caller`. See tests for usage examples
/// @param caller Aggregation executor that executes calls described in `data`
/// @param desc Swap description
/// @param data Encoded calls that `caller` should execute in between of swaps
/// @return returnAmount Resulting token amount
/// @return spentAmount Source token amount
/// @return gasLeft Gas left
function swap(
    IAggregationExecutor caller,
    SwapDescription calldata desc,
    bytes calldata data
)
    external
    payable
    returns (
        uint256 returnAmount,
        uint256 spentAmount,
        uint256 gasLeft
    )
{
    require(desc.minReturnAmount > 0, "Min return should not be 0");
    require(data.length > 0, "data should not be empty");

    uint256 flags = desc.flags;
    IERC20 srcToken = desc.srcToken;
    IERC20 dstToken = desc.dstToken;

    bool srcETH = srcToken.isETH();
    if (flags & _REQUIRES_EXTRA_ETH != 0) {
        require(msg.value > (srcETH ? desc.amount : 0), "Invalid msg.value");
    } else {
        require(msg.value == (srcETH ? desc.amount : 0), "Invalid msg.value");
    }

    if (!srcETH) {
        _permit(address(srcToken), desc.permit);
        srcToken.safeTransferFrom(msg.sender, desc.srcReceiver, desc.amount);
    }

    {
        bytes memory callData = abi.encodePacked(caller.callBytes.selector, bytes12(0), msg.sender, data);
        // solhint-disable-next-line avoid-low-level-calls
        (bool success, bytes memory result) = address(caller).call{value: msg.value}(callData);
        if (!success) {
            revert(RevertReasonParser.parse(result, "callBytes failed: "));
        }
    }

    spentAmount = desc.amount;
    returnAmount = dstToken.uniBalanceOf(address(this));

    if (flags & _PARTIAL_FILL != 0) {
        uint256 unspentAmount = srcToken.uniBalanceOf(address(this));
        if (unspentAmount > 0) {
            spentAmount = spentAmount.sub(unspentAmount);
            srcToken.uniTransfer(msg.sender, unspentAmount);
        }
        require(returnAmount.mul(desc.amount) >= desc.minReturnAmount.mul(spentAmount), "Return amount is not enough");
    } else {
        require(returnAmount >= desc.minReturnAmount, "Return amount is not enough");
    }

    address payable dstReceiver = (desc.dstReceiver == address(0)) ? msg.sender : desc.dstReceiver;
    dstToken.uniTransfer(dstReceiver, returnAmount);

    gasLeft = gasleft();
}
```

- LibertiVault

```solidity
function deposit(
    uint256 assets,
    address receiver,
    bytes calldata data
) external returns (uint256 shares) {
    uint256 nav = getNavInNumeraire(MathUpgradeable.Rounding.Up);
    SafeERC20Upgradeable.safeTransferFrom(asset, _msgSender(), address(this), assets);
    shares = _deposit(assets, receiver, data, nav);
    emit Deposit(_msgSender(), receiver, assets, shares);
}
```

```solidity
function _deposit(
    uint256 assets,
    address receiver,
    bytes calldata data,
    uint256 nav
) private returns (uint256 shares) {
    if (0 == assets) {
        revert ZeroDepositError();
    }
    if (SANCTIONS_LIST.isSanctioned(_msgSender())) {
        revert SanctionedError();
    }
    if (assets < minDeposit) {
        revert MinDepositError();
    }
    if (assets > maxDeposit) {
        revert MaxDepositError();
    }
    uint256 returnAmount = 0;
    uint256 swapAmount = 0;
    if (BASIS_POINT_MAX > invariant) {
        swapAmount = assetsToToken1(assets);
        returnAmount = userSwap(
            data,
            address(this),
            swapAmount,
            address(asset),
            address(other)
        );
    }
    uint256 supply = totalSupply();
    if (0 < supply) {
        uint256 valueToken0 = getValueInNumeraire(
            asset,
            assets - swapAmount,
            MathUpgradeable.Rounding.Down
        );
        uint256 valueToken1 = getValueInNumeraire(
            other,
            returnAmount,
            MathUpgradeable.Rounding.Down
        );
        shares = supply.mulDiv(
            valueToken0 + valueToken1, // Rounded down
            nav, // Rounded up
            MathUpgradeable.Rounding.Down
        );
    } else {
        shares = INITIAL_SHARE;
    }
    uint256 feeAmount = shares.mulDiv(entryFee, BASIS_POINT_MAX, MathUpgradeable.Rounding.Down);
    _mint(receiver, shares - feeAmount);
    _mint(owner(), feeAmount); // mint(feeTo)
}
```

```solidity
function userSwap(
    bytes calldata data,
    address receiver,
    uint256 swapAmount,
    address srcToken,
    address dstToken
) internal returns (uint256 returnAmount) {
    (, SwapDescription memory desc, ) = abi.decode(data[4:], (address, SwapDescription, bytes));
    if (desc.dstReceiver != receiver) {
        revert ReceiverError(desc.dstReceiver, receiver);
    }
    if (desc.amount != swapAmount) {
        revert AmountError(desc.amount, swapAmount);
    }
    if ((address(desc.srcToken) != srcToken) || (address(desc.dstToken) != dstToken)) {
        revert TokenError();
    }
    return _swap(data, swapAmount, srcToken);
}
```

```solidity
function _swap(
    bytes calldata data,
    uint256 amount,
    address srcToken
) private returns (uint256 returnAmount) {
    SafeERC20.safeIncreaseAllowance(IERC20(srcToken), AGGREGATION_ROUTER_V4, amount);
    // solhint-disable-next-line avoid-low-level-calls
    (bool success, bytes memory returndata) = AGGREGATION_ROUTER_V4.call(data);
    if (!success) {
        // solhint-disable-next-line no-inline-assembly
        assembly {
            revert(add(returndata, 32), mload(returndata))
        }
    }
    if (1 == block.chainid) {
        (returnAmount, , ) = abi.decode(returndata, (uint256, uint256, uint256));
    } else if ((56 == block.chainid) || (137 == block.chainid)) {
        (returnAmount, ) = abi.decode(returndata, (uint256, uint256));
    } else {
        revert NetworkError();
    }
}
```

```solidity
/// @notice Returns the total value in USD of all asset and stablecoin owned by the vault.
function getNavInNumeraire(MathUpgradeable.Rounding rounding) public view returns (uint256) {
    uint256 navToken0 = getValueInNumeraire(asset, asset.balanceOf(address(this)), rounding);
    uint256 navToken1 = getValueInNumeraire(other, other.balanceOf(address(this)), rounding);
    return navToken0 + navToken1;
}

/// @notice Returns the value in USD for a given token and a given amount. The quote used in
/// @notice the calculation of the value is fetched from a Chainlink price feed.
function getValueInNumeraire(
    IERC20Upgradeable token,
    uint256 amount,
    MathUpgradeable.Rounding rounding
) private view returns (uint256) {
    uint256 tokenDecimals = 10 ** IERC20Metadata(address(token)).decimals();
    uint256 tokenPrice = priceFeed.getPrice(address(token));
    return tokenPrice.mulDiv(amount, tokenDecimals, rounding);
}
```

## Attack steps:

1. borrow 6,000,000 USDT using flashloan

2. deposit 0.001 WETH + 3,000,000 USDT to the `LibertiVault` and reenter the function `deposit` in the callback of the 1nch ArrgrgationRouterV4 and mint 4,540 shares (with 0.001 WETH + 3,000,000 USDT), mint 76,954 shares after the untrusted external call return

4. burn all shares and withdraw 34.9 WETH + 6,076,078 USDT by trigering the function `exit`

## Root Cause:

The function `deposit` in the contract `LibertiVault` first swaps $amount \times (1 - \frac{invariant}{BASIS_POINT_MAX})$ amount $AssetTokens (i.e. WETH) for the $OtherTokens (i.e. USDT) by trigering the function `swap` in 1nch AggregationRouterV4, and then mints shares based on the formula: $shares = totalSupply \times \frac{USDVaule_{asset} + USDVaule_{other}}{nav} = totalSupply \times \frac{\Delta{TVL}}{TVL}$. However, the function `swap` of 1nch AggregationRouterV4 will triger the callback function in the contract `caller` (parsed from `data`, which is controllable). 

An attacker can reenter the function `deposit` to inflate the totalSupply and mint more shares than expected due to the totalSupply is updated after this untrusted external call. Finally, more underlying tokens can be withdrawn via the function `exit`.


## Refs