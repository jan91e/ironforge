import {IERC20} from "../../../interfaces/tokens/IERC20.sol";
import {IDppFlashloan} from "../../../interfaces/flashloan/dodo/IDppFlashloan.sol";
import {IDppFlashloanReceiver} from "../../../interfaces/flashloan/dodo/IDppFlashloanReceiver.sol";

import {
    WBNB,
    BTCB,
    WETH,
    BSC_USD as USDT,
    DPP_ORACLE_BTCB,
    DPP_ORACLE_WBNB,
    DPP_ORACLE_WETH,
    DPP_WBNB,
    DPP_ADVANCED_WBNB
} from "../../../constants/bsc.sol";

// DODO Flashloan Doc: https://docs.dodoex.io/english/contracts/dodo-v1-v2/guides/flash-loan
// TODO: if the quoteToken of DODO is always the USDT? -> Nope
abstract contract BscDppSingleFlashloanHelper is IDppFlashloanReceiver {
    // mapping(address => bool) _isProvider;
    bytes constant private FLASHLOAN_PROVIDERS = abi.encodePacked([
        DPP_ORACLE_BTCB,
        DPP_ORACLE_WBNB,
        DPP_ORACLE_WETH,
        DPP_WBNB,
        DPP_ADVANCED_WBNB
    ]);

    // bitMap for flashloan provider order using
    // uint64 = uint8 (number of providers) +  uint28 (quoteToken or baseToken for the provider) +  uint28 (valid providers)
    // USDT = 00000101 + 0...011111 + 0...011111
    uint64 constant private USDT_BITMAP = 360287978511138847;
    // WBNB = 00000011 + 0...000000 + 0...011010 
    uint64 constant private WBNB_BITMAP = 216172782113783834;
    // WETH = 00000001 + 0...000000 + 0...000100
    uint64 constant private WETH_BITMAP = 72057594037927940;
    // BTCB = 00000001 + 0...000000 + 0...000001
    uint64 constant private BTCB_BITMAP = 72057594037927937;

    function _getFlashLoanProviders() private returns(address[5] memory _providers) {
        return abi.decode(FLASHLOAN_PROVIDERS, (address[5]));
    }

    modifier onlyDppFlashloanProvider {
        address[5] memory _providers = _getFlashLoanProviders();
        uint _providersLen = _providers.length;
        for(uint i; i < _providersLen;) {
            if (msg.sender == _providers[i]) {
                _;
                return;
            }
        }
        revert("Not valid dodo flashloan provider");
    }

    function borrow(address _token, uint256 _amount) internal {
        if (_token == USDT) {
            _launchDppFlashloan(_token, _amount, USDT_BITMAP, 0, uint8(USDT_BITMAP >> 56));
        } else if (_token == BTCB) {
            _launchDppFlashloan(BTCB, _amount, BTCB_BITMAP, 0, uint8(BTCB_BITMAP >> 56));
        } else if (_token == WETH) {
            _launchDppFlashloan(WETH, _amount, WETH_BITMAP, 2, uint8(WETH_BITMAP >> 56));
        } else if (_token == WBNB) {
            _launchDppFlashloan(WBNB, _amount, WBNB_BITMAP, 1, uint8(WBNB_BITMAP >> 56));
        }
    }

    struct DppFlashloanParam {
        uint256 remaining;
        address assetBorrow;
        uint64 bitMp;
        bool isQuote;
        uint8 nextProviderIndex;
        uint8 remainingProviders;
    }

    function _getNextProvider(
        uint64 _bitMp, 
        uint8 _currentIndex
    ) private returns(bool, address, bool, uint8) {
        address[5] memory _providers = _getFlashLoanProviders();
        uint _providersLengthTotal = _providers.length;

        for(uint i = _currentIndex; i < _providersLengthTotal;) {
            bool isValid;
            bool isQuote;
            assembly {
                isValid := and(shr(i, _bitMp), 1)
                isQuote := and(shr(add(i, 28), _bitMp), 1)
            }
            if (isValid) {
                return (true, _providers[i], isQuote, uint8(i + 1));
            }
            unchecked {
                ++i;
            }
        }

        return (false, address(0), false, 0);
    }

    function _launchDppFlashloan(address _asset, uint256 _amount, uint64 _bitMp, uint8 _currentIndex, uint8 _remainingProviders) private {
        (bool _ok, address _provider, bool _isQuote, uint8 _nextIndex) = _getNextProvider(_bitMp, _currentIndex);
        if (_ok && _remainingProviders > 0) {
            _remainingProviders--;
        }

        uint256 _providerReserve = IERC20(_asset).balanceOf(_provider);
        uint256 _borrowAmount = _providerReserve >= _amount ? _amount : _providerReserve;
        uint256 _remaining = _providerReserve >= _amount ? 0 : _amount - _providerReserve;
        
        bytes memory _data = abi.encode(DppFlashloanParam({
            assetBorrow: _asset,
            remaining: _remaining,
            bitMp: _bitMp,
            isQuote: _isQuote,
            nextProviderIndex: _nextIndex,
            remainingProviders: _remainingProviders
        }));
        
        if (_isQuote) {
            IDppFlashloan(_provider).flashLoan(
                0, 
                _borrowAmount, 
                address(this), 
                _data
            );
        } else {
            IDppFlashloan(_provider).flashLoan(
                _borrowAmount, 
                0, 
                address(this), 
                _data
            );
        }

    }

    function DPPFlashLoanCall(
        address sender,
        uint256 baseAmount,
        uint256 quoteAmount,
        bytes calldata data
    ) external {
        DppFlashloanParam memory params = abi.decode(data, (DppFlashloanParam));
        if (params.remaining == 0 || params.remainingProviders == 0) {
            _flashloanLogic(data);
        } else if (msg.sender == DPP_ORACLE_BTCB) {
            _launchDppFlashloan(params.assetBorrow, params.remaining, params.bitMp, params.nextProviderIndex, params.remainingProviders);
        } else if (msg.sender == DPP_ORACLE_WBNB) {
            _launchDppFlashloan(params.assetBorrow, params.remaining, params.bitMp, params.nextProviderIndex, params.remainingProviders);
        } else if (msg.sender == DPP_ORACLE_WETH) {
            _launchDppFlashloan(params.assetBorrow, params.remaining, params.bitMp, params.nextProviderIndex, params.remainingProviders);
        } else if (msg.sender == DPP_WBNB) {
            _launchDppFlashloan(params.assetBorrow, params.remaining, params.bitMp, params.nextProviderIndex, params.remainingProviders);
        } else if (msg.sender == DPP_ADVANCED_WBNB) {
            _flashloanLogic(data);
        } else {
            revert("not valid flashloan provider");
        }

        if (params.isQuote) {
            IERC20(params.assetBorrow).transfer(msg.sender, quoteAmount);
        } else {
            IERC20(params.assetBorrow).transfer(msg.sender, baseAmount);
        }
    }

    function _flashloanLogic(bytes calldata data) internal virtual;
}

abstract contract BscDppUniFlashloanHelper is IDppFlashloanReceiver {
    address[] private _providers;
    mapping(address => bool) private _providerUsed;

    constructor() {
        address[5] memory _flashLoanProviders = [
            DPP_ORACLE_BTCB,
            DPP_ORACLE_WBNB,
            DPP_ORACLE_WETH,
            DPP_WBNB,
            DPP_ADVANCED_WBNB
        ];
        _providers = _flashLoanProviders;
    }
    

    modifier onlyDppFlashloanProvider {
        require(_providerUsed[msg.sender], "Not valid dodo flashloan provider");
        _;
    }

    function borrow(address[] memory _tokens, uint256[] memory _amounts, bytes memory data) internal {
        _launchDppFlashloan(DppFlashloanParam({
            assets: _tokens,
            remainings: _amounts,
            nextProviderIndex: 0,
            end: false,
            callbackData: data
        }));
    }

    struct DppFlashloanParam {
        address[] assets;
        uint256[] remainings;
        uint256 nextProviderIndex;
        bool end;
        bytes callbackData;
    }

    function _noRemainingsToBorrow(uint256[] memory _remainings) private returns(bool) {
        uint256 _remainingsLen = _remainings.length;
        for (uint i; i < _remainingsLen;) {
            if (_remainings[i] != 0) {
                return false;
            }
            unchecked {
                ++i;
            }
        }

        return true;
    }

    function _launchDppFlashloan(DppFlashloanParam memory p) private {
        address[] memory _assets = p.assets;
        uint _assetLen = _assets.length;
        uint _remainingsLen = p.remainings.length;
        uint256[] memory _remainings = new uint256[](_remainingsLen);
        for(uint i; i < _remainingsLen;) {
            _remainings[i] = p.remainings[i];
            unchecked {
                ++i;
            }
        }
        uint _totalProvidersCount = _providers.length;
        uint _currentProviderIndex = p.nextProviderIndex;

        address _nextProvider;
        uint _baseAmount;
        uint _quoteAmount;
        while (_currentProviderIndex < _totalProvidersCount) {
            address _provider = _providers[_currentProviderIndex];
            address _bToken = IDppFlashloan(_provider)._BASE_TOKEN_();
            address _qToken = IDppFlashloan(_provider)._QUOTE_TOKEN_();

            for (uint j; j < _assetLen; ++j) {
                address _asset = _assets[j];
                uint256 _amount = _remainings[j];
                if (_amount == 0) {
                    continue;
                }
                if (_asset == _bToken) {
                    uint _bReserve = IERC20(_bToken).balanceOf(_provider);
                    _baseAmount += _bReserve >= _amount ? _amount : _bReserve;
                    
                    _remainings[j] = _bReserve >= _amount ? 0 : _amount - _bReserve;
                } else if (_asset == _qToken) {
                    uint _qReserve = IERC20(_qToken).balanceOf(_provider);
                    _quoteAmount += _qReserve >= _amount ? _amount : _qReserve;

                    _remainings[j] = _qReserve >= _amount ? 0 : _amount - _qReserve;
                }
            }

            if (_baseAmount != 0 || _quoteAmount != 0) {
                _providerUsed[_provider] = true;
                _nextProvider = _provider;
                break;
            }

            unchecked {
                ++_currentProviderIndex;
            }
        }
        
        p.remainings = _remainings;

        if (_currentProviderIndex != _totalProvidersCount) {
            p.nextProviderIndex = _currentProviderIndex + 1;
        } else {
            // no more providers
            return;
        }

        if (_noRemainingsToBorrow(_remainings)) {
            // no more assets to borrow or all providers are used
            p.end = true;
        }

        IDppFlashloan(_nextProvider).flashLoan(
            _baseAmount, 
            _quoteAmount, 
            address(this), 
            abi.encode(p)
        );
    }

    function DPPFlashLoanCall(
        address sender,
        uint256 baseAmount,
        uint256 quoteAmount,
        bytes calldata data
    ) external onlyDppFlashloanProvider {

        DppFlashloanParam memory params = abi.decode(data, (DppFlashloanParam));
        if (params.end || params.nextProviderIndex == _providers.length) {
            _flashloanLogic(params.callbackData);
        } else {
            _launchDppFlashloan(params);
        }


        // Repay flashloan
        if(quoteAmount > 0) {
            address _qToken = IDppFlashloan(msg.sender)._QUOTE_TOKEN_();
            IERC20(_qToken).transfer(msg.sender, quoteAmount);
        } 

        if (baseAmount > 0) {
            address _bToken = IDppFlashloan(msg.sender)._BASE_TOKEN_();
            IERC20(_bToken).transfer(msg.sender, baseAmount);
        }
       
    }

    function _flashloanLogic(bytes memory data) internal virtual;
}