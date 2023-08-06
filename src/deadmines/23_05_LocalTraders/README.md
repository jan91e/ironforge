# LocalTraders

> Time: bsc#28460898
>
> Tag: `ACL`, `Price Oracle`
>
> Malicious Txs:
> 1. [Access gain] 0x57b589f631f8ff20e2a89a649c4ec2e35be72eaecf155fdfde981c0fec2be5ba
> 2. [Price change] 0xbea605b238c85aabe5edc636219155d8c4879d6b05c48091cf1f7286bd4702ba
> 3. [Profit] 0x49a3038622bf6dc3672b1b7366382a2c513d713e06cb7c91ebb8e256ee300dfb

## Code snippet:

oracle bytecode (0x312DC37075646c7e0DBA21DF5BdFe69E76475fdc) decompile results:
```
uint256 stor_0_0_19; // STORAGE[0x0] bytes 0 to 19
uint256 owner_1_0_19; // STORAGE[0x1] bytes 0 to 19
uint256 owner_2_0_19; // STORAGE[0x2] bytes 0 to 19
uint256 _getTokenPrice; // STORAGE[0x2] bytes 20 to 20
```

```
function 0xb5863c10(address varg0) public payable { 
    require(4 + (msg.data.length - 4) - 4 >= 32);
    require(varg0 == varg0);
    stor_0_0_19 = varg0;
    owner_1_0_19 = msg.sender;
    owner_2_0_19 = msg.sender;
    stor_3 = 0x2a1766f5d000;
}
```

```
function 0x925d400c(uint256 varg0) public payable { 
    require(4 + (msg.data.length - 4) - 4 >= 32);
    0xcac(varg0);
    require(msg.sender == owner_1_0_19, Error('You are not admin'));
    stor_3 = varg0;
    return varg0;
}
```

```
function getTokenPrice() public payable { 
    if (_getTokenPrice != bool(1)) {
        v0 = v1 = stor_3;
    } else {
        require(bool(stor_0_0_19.code.size));
        v2, /* uint80 */ v3, v4, v5, v6, /* uint80 */ v7 = stor_0_0_19.latestRoundData().gas(msg.gas);
        require(bool(v2), 0, RETURNDATASIZE()); // checks call status, propagates error data on error
        require(MEM[64] + RETURNDATASIZE() - MEM[64] >= 160);
        require(v3 == uint80(v3));
        0xcac(v4);
        require(v5 == v5);
        require(v6 == v6);
        require(v7 == uint80(v7));
        require(!((v4 > 0) & (0x2540be400 > 0) & (v4 > 0x36f9bfb3af7b756fad5cd10396a21346cbefc1bf33a44ab72e36108b)), Panic(17)); // arithmetic overflow or underflow
        require(!((v4 > 0) & (0x2540be400 < 0) & (0x2540be400 < 0x8000000000000000000000000000000000000000000000000000000000000000 / v4)), Panic(17)); // arithmetic overflow or underflow
        require(!((v4 < 0) & (0x2540be400 > 0) & (v4 < 0x36f9bfb3af7b756fad5cd10396a21346cbefc1bf33a44ab72e36108b)), Panic(17)); // arithmetic overflow or underflow
        require(!((v4 < 0) & (0x2540be400 < 0) & (v4 < 0x36f9bfb3af7b756fad5cd10396a21346cbefc1bf33a44ab72e36108b)), Panic(17)); // arithmetic overflow or underflow
        v0 = v4 * 0x2540be400;
    }
    return v0;
}
```

## Attack steps:

1. Triger the function `0xb5863c10` to control the oracle privilage address `owner_1_0_19`

2. Triger the function `0x925d400c` to modify the global price storage variable `stor_3` to 1, which is used in the function `getTokenPrice`

3. Buy out LCT tokens in the LCTExchange with an unfair price 1 (fetch from the controlled oracle)

4. Sell LCT to get profits

## Root Cause:
The privileged functions in the price oracle do not have access control.

## Refs
- https://neptunemutual.com/blog/understanding-local-traders-exploit/

- https://twitter.com/LOCALTRADERSCL/status/1661082091499421696

- https://archive.ph/QH2lY