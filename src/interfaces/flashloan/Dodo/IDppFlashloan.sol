interface IDppFlashloan {
    function flashLoan(
        uint256 baseAmount,
        uint256 quoteAmount,
        address _assetTo,
        bytes calldata data
    ) external;
}