# EarningFarm

> Time: ETH#17875885
> 
> Tag: `Reentrancy`
> 
> Malicious Txs:
> - 0x6e6e556a5685980317cb2afdb628ed4a845b3cbd1c98bdaffd0561cb2c4790fa
> 
> - 0x25567821ea31a8efd395654b7fafbab8511e777420803b99b08ca8500dcc3e95
> 
> - 0x878d8986ed05ab32cc01e05663d27ea471576d2baff1081b15ed5fb550f9d81b
> 
> - 0x8454beb56ca22f710706c00ac4b969caa7b8848b4a45202cf52715f10a09fc0f
> 
> - 0xb35faeee64205e3018a1331e59abf7fa7a20bd0163dd2eed4657a9693e9c7ecf
> 
> - 0x2b492dd5184f2c0f5049923ea61036bc3aee44dd3aa5454dd3de2be2f354c2b6
>
> - 0x0d5106d4fa1bddee97a3ed0cb78f5ee6cf08bac4e7201883b63a7b4e71e5fddc
>
> - 0xefb27bfca4bfb0111b8d858340178ccb936c2872026fdfaaabb15eb306e70e4f
>
> - 0x09349d03e1961cd067f3a049ddef27e6d4b2b516e0252fb885854ba109089301
>
> - 0x8e12959dc243c3ff24dfae0ea7cdad48f6cfc1117c349cdc1742df3ae3a3279b
>

## Code snippet:

- the ENF_ETHLEV contract
```solidity
    function deposit(uint256 assets, address receiver)
        public
        payable
        virtual
        override
        nonReentrant
        unPaused
        returns (uint256 shares)
    {
        require(assets != 0, "ZERO_ASSETS");
        require(assets <= maxDeposit, "EXCEED_ONE_TIME_MAX_DEPOSIT");

        require(msg.value >= assets, "INSUFFICIENT_TRANSFER");

        console.log("ETH Vault: ", address(this).balance);
        // Need to transfer before minting or ERC777s could reenter.
        TransferHelper.safeTransferETH(address(controller), assets);
        console.log("ETH transferred to cont");

        // Total Assets amount until now
        uint256 totalDeposit = IController(controller).totalAssets();
        console.log("Current Total: ", totalDeposit);

        // Calls Deposit function on controller
        uint256 newDeposit = IController(controller).deposit(assets);

        require(newDeposit > 0, "INVALID_DEPOSIT_SHARES");

        // Calculate share amount to be mint
        shares = totalSupply() == 0 || totalDeposit == 0 ? assets : (totalSupply() * newDeposit) / totalDeposit;

        // Mint ENF token to receiver
        _mint(receiver, shares);

        emit Deposit(address(asset), msg.sender, receiver, assets, shares);
    }
```

```solidity
    function withdraw(uint256 assets, address receiver) public virtual nonReentrant unPaused returns (uint256 shares) {
        require(assets != 0, "ZERO_ASSETS");
        require(assets <= maxWithdraw, "EXCEED_ONE_TIME_MAX_WITHDRAW");

        // Total Assets amount until now
        uint256 totalDeposit = convertToAssets(balanceOf(msg.sender));

        require(assets <= totalDeposit, "EXCEED_TOTAL_DEPOSIT");

        // Calculate share amount to be burnt
        shares = (totalSupply() * assets) / totalAssets();

        // Calls Withdraw function on controller
        (uint256 withdrawn, uint256 fee) = IController(controller).withdraw(assets, receiver);

        require(withdrawn > 0, "INVALID_WITHDRAWN_SHARES");

        // Shares could exceed balance of caller
        if (balanceOf(msg.sender) < shares) shares = balanceOf(msg.sender);

        _burn(msg.sender, shares);

        emit Withdraw(address(asset), msg.sender, receiver, assets, shares, fee);
    }
```

- the Controller contract

```solidity
   function withdraw(uint256 _amount, address _receiver)
        external
        override
        onlyVault
        returns (uint256 withdrawAmt, uint256 fee)
    {
        // Check input amount
        require(_amount > 0, "ZERO AMOUNT");

        // Check substrategy length
        require(subStrategies.length > 0, "INVALID_POOL_LENGTH");

        // Todo: withdraw as much as possible
        uint256 toWithdraw = _amount;

        for (uint256 i = 0; i < subStrategies.length; i++) {
            uint256 withdrawFromSS = ISubStrategy(subStrategies[apySort[i]].subStrategy).withdrawable(_amount);
            if (withdrawFromSS == 0) {
                // If there is no to withdraw, skip this SS.
                continue;
            } else if (withdrawFromSS >= toWithdraw) {
                // If the SS can withdraw requested amt, then withdraw all and finish
                withdrawAmt += ISubStrategy(subStrategies[apySort[i]].subStrategy).withdraw(toWithdraw);
                toWithdraw = 0;
            } else {
                // Withdraw max withdrawble amt and
                withdrawAmt += ISubStrategy(subStrategies[apySort[i]].subStrategy).withdraw(withdrawFromSS);
                // Todo deduct by withdrawAmt or withdrawFromSS
                toWithdraw -= withdrawFromSS;
            }

            // If towithdraw equals to zero, break
            if (toWithdraw == 0) break;
        }

        if (withdrawAmt > 0) {
            console.log("Cont Withdraw: ", address(this).balance, withdrawAmt);
            require(address(this).balance >= withdrawAmt, "INVALID_WITHDRAWN_AMOUNT");

            // Pay Withdraw Fee to treasury and send rest to user
            fee = (withdrawAmt * withdrawFee) / magnifier;
            TransferHelper.safeTransferETH(treasury, fee);

            // Transfer withdrawn token to receiver
            uint256 toReceive = withdrawAmt - fee;
            TransferHelper.safeTransferETH(_receiver, toReceive);
        }
    }
```

## Attack steps:

1. borrow 10,000 WETH using flashloan from uniswapV3: USDC/WETH Pool

2. deposit ~320.56 WETH (i.e. totalAssets for the ENF_ETHLEV) into the ENF_ETHLEV contract and mint ~295.76 ENF_ETHLEV (i.e. shares)

3. withdraw all shares and after the eth received the attack-contract transfer (i.e. reenter the `transfer` function in ENF_ETHLEV) away shares to the attacker-contract-2 in advance in its fallback function.

4. withdraw all shares within the attack-contract-2, and receive eth assets again.

## Root Cause:
The `withdraw` function in the `EFVault` contract first calls the `withdraw` function in the `Controller` contract, which transfers the underlying token (i.e. ETH) to the user. And then the function `withdraw` in the contract `EFVault` **adjusts the shares to be burned based on the instantaneous balance of the user**.

However, an attacker can reenter the `EFVault` contract to transfer away his LP tokens in advance in the `fallback` function when ETHs are received from the `Controller`. This enables the attacker to redeem more underlying tokens with fewer Lp tokens burned. Due to the LP tokens has been moved already, the attacker can reuse them to `withdraw` from the contract `EFVault`.

## Refs

- https://twitter.com/Phalcon_xyz/status/1689182459269644288