# Carson

> Time: BSC#30306325
> 
> Tag: `Price Manipulation`, `Custom Bad Pair`
>
> Malicious Txs:
> 
> - 0x37d921a6bb0ecdd8f1ec918d795f9c354727a3ff6b0dba98a512fceb9662a3ac
> 
> - 0x6a94a644856c3aa1db8249b700956379b6b3a18de9b8811566fbd56c89240a01
> 
> - 0xed52a42b2f45e4dea8d07f70d645931e4f6da65e9ab281cd3dbb9d9d21febb45
> 
> - 0xcd781fec34b46f8c7372a9fcc7604c210b40442dc4f1a5c274fc3f9283df39ce

## Code snippet:

- decompile result (simplify) for dedaub:
```solidiy
function swap(uint256 amount0Out, uint256 amount1Out, address to, bytes data) public payable lock { 
    v6 = _factory.staticcall(0x64a115b400000000000000000000000000000000000000000000000000000000, this);
    require(msg.sender == address(v6), Error('UniswapV2: FORBIDDEN'));
    require(amount0Out > 0 || amount1Out > 0, Error('UniswapV2: INSUFFICIENT_OUTPUT_AMOUNT'));
    (_reserve0, _reserve1) = getReserves();
    require(amount0Out < _reserve0 && amount1Out < _reserve1, Error('UniswapV2: INSUFFICIENT_LIQUIDITY'));
    require(_token0 != address(to) && _token1 != address(to), Error('UniswapV2: INVALID_TO'));
    if (amount0Out > 0) _safeTransfer(amount0Out, v2, _token0);
    if (amount1Out > 0) _safeTransfer(amount1Out, v2, _token1);
    if (data.length != 0) address(to).uniswapV2Call(msg.sender, amount0Out, amount1Out, data);
    uint balance0 = _token0.balanceOf(this);
    uint balance1 = _token1.balanceOf(this);
    
    uint amount0In = balance0 > _reserve0 - amount0Out ? balance0 - (_reserve0 - amount0Out) : 0;
    uint amount1In = balance1 > _reserve1 - amount1Out ? balance1 - (_reserve1 - amount1Out) : 0;

    require(amount0In > 0 || amount1In > 0, Error('UniswapV2: INSUFFICIENT_INPUT_AMOUNT', v31, v31, 128));

    uint balance0Adjusted = balance0.mul(1000).sub(amount0In.mul(3));
    uint balance1Adjusted = balance1.mul(1000).sub(amount1In.mul(3));
    require(balance0Adjusted.mul(balance1Adjusted) >= uint(_reserve0).mul(_reserve1).mul(1000**2), Error('UniswapV2: K'));

// v43 = v45 = 300000000000000000 = 0.3
// v44 = 0x4d9bd49b7383b88477724428556c7fe36d7e6bc4
    (address v42, uint v43, address v44, uint v45) = _factory.staticcall(0x918b6c8d, this, _token0);
    uint fee0 = amount0In.mul(v43).div(1e18);
    uint fee1 = amount0In.mul(v45).div(1e18);
    if (fee0 > 0) {
        _token0.transfer(address(v42), v46 / 1e18);
        _token0.transfer(address(v44), v47 / 1e18);
    }

    (address v51, uint v52, address v53, uint v54) = _factory.staticcall(0x918b6c8d, this, _token1);
    fee0 = amount0In.mul(v43).div(1e18);
    fee1 = amount0In.mul(v45).div(1e18);
    if (fee1 > 0) {
        _token1.transfer(address(v51), fee1);
        _token1.transfer(address(v53), fee1);
    }

    uint _balance0 = _token0.balanceOf(this);
    uint _balance1 = _token1.balanceOf(this);
    _update(_reserve1, _reserve0, _balance1, _balance0);
}

function _update(uint112 _reserve1, uint112 _reserve0, uint256 balance1, uint256 balance0) private { 
    require(balance0 < uint112(-1) && balance1 < uint112(-1), Error('UniswapV2: OVERFLOW'));
    uint timeElapsed = bool(uint32(uint32(block.timestamp) - blockTimestampLast));
    if (timeElapsed > 0 && _reserve0 != 0 && _reserve1 != 0) {
        price0CumulativeLast += uint(UQ112x112.encode(_reserve1).uqdiv(_reserve0)) * timeElapsed;
        price1CumulativeLast += uint(UQ112x112.encode(_reserve0).uqdiv(_reserve1)) * timeElapsed;
    }
    reserve0 = balance0;
    reserve1 = balance1;
    blockTimestampLast = uint32(block.timestamp);
    return;
}
```

## Attack steps:

Step 1: swap WETH for Carson

Step 2: swap Carson for WETH repeatly, to lower the K of the pair. 

Step 3: swap all remaining Carson for WETH

## Root Cause:
The unverified uniswap pair 0xe0a3 may transfer out underlying tokens to sell after the K-invariant check and before the reserves are updated.
This could cause the K of the pair lower than it should be, breaking the invariant.


## Refs

- https://twitter.com/hexagate_/status/1684475526663004160?s=61&t=uKMzufX1Pir1kdDqOFggug