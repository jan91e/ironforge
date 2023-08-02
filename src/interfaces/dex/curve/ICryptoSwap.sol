//  @version 0.3.0
// (c) Curve.Fi, 2021
// Pool for two crypto assets

// Expected coins:
// eth/whatever

interface ICryptoSwap {
    function coins(uint256 i) external view returns(address coin);
    function A() external view returns(uint256 a);
    function fee() external view returns(uint256 fee);
    function get_virtual_price() external view returns(uint256 price);

    function exchange_underlying(
        uint256 i, 
        uint256 j, 
        uint256 dx, 
        uint256 min_dy
    ) external returns(uint256);

    function exchange(
        uint256 i, 
        uint256 j,
        uint256 dx,
        uint256 min_dy,
        bool use_eth
    ) external payable returns(uint256); 

    // use_eth = Fasle
    function exchange(
        uint256 i, 
        uint256 j,
        uint256 dx,
        uint256 min_dy
    ) external payable returns(uint256); 

    function get_dy(
        uint256 i,
        uint256 j,
        uint256 dx
    ) external view returns(uint256 dy);

    function add_liquidity(
        uint256[2] memory amounts,
        uint256 min_mint_amount,
        bool use_eth
    ) external payable returns(uint256 d_token);

    // use_eth = False
    function add_liquidity(
        uint256[2] memory amounts,
        uint256 min_mint_amount
    ) external payable returns(uint256 d_token);

    function remove_liquidity(
        uint256 _amount, 
        uint256[2] memory min_amounts, 
        bool use_eth
    ) external;

    function remove_liquidity(
        uint256 _amount, 
        uint256[2] memory min_amounts
    ) external;

    function calc_token_amount(uint256[2] memory amounts) external returns(uint256);

    function calc_withdraw_one_coin(
        uint256 token_amount,
        uint256 i
    ) external returns(uint256);

    function remove_liquidity_one_coin(
        uint256 token_amount,
        uint256 i, 
        uint256 min_amount,
        bool use_eth
    ) external returns(uint256);

    function remove_liquidity_one_coin(
        uint256 token_amount,
        uint256 i, 
        uint256 min_amount
    ) external returns(uint256);

    function claim_admin_fees() external;

    // Admin parameters
    function ramp_A_gamma(
        uint256 future_A,
        uint256 future_gamma,
        uint256 future_time
    ) external;

    function stop_ramp_A_gamma() external;

    function commit_new_parameters(
        uint256 _new_mid_fee,
        uint256 _new_out_fee,
        uint256 _new_admin_fee,
        uint256 _new_fee_gamma,
        uint256 _new_allowed_extra_profit,
        uint256 _new_adjustment_step,
        uint256 _new_ma_half_time
    ) external;

    function apply_new_parameters() external;

    function revert_new_parameters() external;

    function commit_transfer_ownership(address _owner) external;

    function apply_transfer_ownership() external;

    function revert_transfer_ownership() external;

    function kill_me() external;

    function unkill_me() external;

    function set_admin_fee_receiver(address _admin_fee_receiver) external;

    function lp_price() external returns(uint256);
}