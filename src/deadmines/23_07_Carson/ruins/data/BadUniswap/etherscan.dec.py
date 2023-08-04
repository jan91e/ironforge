# Palkeoramix decompiler. 

const name = ''
const decimals = 18
const symbol = ''
const unknownba9a7a56 = 1000
const PERMIT_TYPEHASH = 0x6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c9

def storage:
  totalSupply is uint256 at storage 0
  balanceOf is mapping of uint256 at storage 1
  allowance is mapping of uint256 at storage 2
  DOMAIN_SEPARATOR is uint256 at storage 3
  nonces is mapping of uint256 at storage 4
  factoryAddress is addr at storage 5
  unknown0dfe1681Address is addr at storage 6
  token1Address is addr at storage 7
  stor8 is uint32 at storage 8 offset 224
  stor8 is uint128 at storage 8
  stor8 is uint128 at storage 8 offset 112
  unknown5909c0d5 is uint256 at storage 9
  unknown5a3d5493 is uint256 at storage 10
  unknown7464fc3d is uint256 at storage 11
  stor12 is uint256 at storage 12

def unknown0dfe1681() payable: 
  return unknown0dfe1681Address

def totalSupply() payable: 
  return totalSupply

def DOMAIN_SEPARATOR() payable: 
  return DOMAIN_SEPARATOR

def unknown5909c0d5() payable: 
  return unknown5909c0d5

def unknown5a3d5493() payable: 
  return unknown5a3d5493

def balanceOf(address _owner) payable: 
  require calldata.size - 4 >= 32
  return balanceOf[_owner]

def unknown7464fc3d() payable: 
  return unknown7464fc3d

def nonces(address _param1) payable: 
  require calldata.size - 4 >= 32
  return nonces[_param1]

def factory() payable: 
  return factoryAddress

def token1() payable: 
  return token1Address

def allowance(address _owner, address _spender) payable: 
  require calldata.size - 4 >= 64
  return allowance[_owner][_spender]

#
#  Regular functions
#

def _fallback() payable: # default function
  revert

def getReserves() payable: 
  return Mask(112, 0, stor8.field_0), Mask(112, 0, stor8.field_0), uint32(stor8.field_224)

def initialize(address _torchRunner, address _tokenAddress) payable: 
  require calldata.size - 4 >= 64
  if factoryAddress != caller:
      revert with 0, 'UniswapV2: FORBIDDEN'
  unknown0dfe1681Address = _torchRunner
  token1Address = _tokenAddress

def approve(address _spender, uint256 _value) payable: 
  require calldata.size - 4 >= 64
  allowance[caller][addr(_spender)] = _value
  log Approval(
        address tokenOwner=_value,
        address spender=caller,
        uint256 tokens=_spender)
  return 1

def transfer(address _to, uint256 _value) payable: 
  require calldata.size - 4 >= 64
  if balanceOf[caller] - _value > balanceOf[caller]:
      revert with 0, 'ds-math-sub-underflow'
  balanceOf[caller] -= _value
  if balanceOf[_to] + _value < balanceOf[_to]:
      revert with 0, 'ds-math-add-overflow'
  balanceOf[addr(_to)] = balanceOf[_to] + _value
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 tokens=_to)
  return 1

def unknownd505accf(addr _param1, addr _param2, uint256 _param3, uint256 _param4, uint8 _param5, uint256 _param6, uint256 _param7) payable: 
  require calldata.size - 4 >= 224
  if _param4 < block.timestamp:
      revert with 0, 'UniswapV2: EXPIRED'
  nonces[addr(_param1)]++
  signer = erecover(sha3(0, DOMAIN_SEPARATOR, sha3(0x6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c9, addr(_param1), addr(_param2), _param3, nonces[addr(_param1)], _param4)), _param5 << 248, _param6, _param7) # precompiled
  if not erecover.result:
      revert with ext_call.return_data[0 len return_data.size]
  if not addr(signer):
      revert with 0, 'UniswapV2: INVALID_SIGNATURE'
  if addr(signer) != _param1:
      revert with 0, 'UniswapV2: INVALID_SIGNATURE'
  allowance[addr(_param1)][addr(_param2)] = _param3
  log Approval(
        address tokenOwner=_param3,
        address spender=_param1,
        uint256 tokens=_param2)

def transferFrom(address _from, address _to, uint256 _value) payable: 
  require calldata.size - 4 >= 96
  if allowance[addr(_from)][caller] != -1:
      if allowance[addr(_from)][caller] - _value > allowance[addr(_from)][caller]:
          revert with 0, 'ds-math-sub-underflow'
      allowance[addr(_from)][caller] -= _value
  if balanceOf[addr(_from)] - _value > balanceOf[addr(_from)]:
      revert with 0, 'ds-math-sub-underflow'
  balanceOf[addr(_from)] -= _value
  if balanceOf[_to] + _value < balanceOf[_to]:
      revert with 0, 'ds-math-add-overflow'
  balanceOf[addr(_to)] = balanceOf[_to] + _value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 tokens=_to)
  return 1

def unknownfff6cae9() payable: 
  if stor12 != 1:
      revert with 0, 'UniswapV2: LOCKED'
  stor12 = 0
  require ext_code.size(unknown0dfe1681Address)
  static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(token1Address)
  static call token1Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
      revert with 0, 'UniswapV2: OVERFLOW'
  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
      revert with 0, 'UniswapV2: OVERFLOW'
  if uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
      if Mask(112, 0, stor8.field_0):
          if Mask(112, 0, stor8.field_112):
              require Mask(112, 0, stor8.field_0)
              unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
              require Mask(112, 0, stor8.field_112)
              unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
  uint32(stor8.field_224) = uint32(block.timestamp)
  log 0x1c411e9a: ext_call.return_data
  stor12 = 1

def unknownbc25cf77(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if stor12 != 1:
      revert with 0, 'UniswapV2: LOCKED'
  stor12 = 0
  require ext_code.size(unknown0dfe1681Address)
  static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_datastor8.field_0) > ext_call.return_data[0]:
      revert with 0, 'ds-math-sub-underflow'
  mem[260 len 64] = transfer(address to, uint256 tokens), addr(_param1) << 64, 0, Mask(224, 32, ext_call.return_datastor8.field_0)) >> 32
  call unknown0dfe1681Address with:
       gas gas_remaining wei
      args Mask(224, 32, ext_call.return_datastor8.field_0)) << 224, mem[324 len 4]
  if not return_data.size:
      require not ext_call.success
      revert with 0, 'UniswapV2: TRANSFER_FAILED'
  mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
  if not ext_call.success:
      revert with 0, 'UniswapV2: TRANSFER_FAILED'
  if return_data.size:
      require return_data.size >= 32
      if not mem[292]:
          revert with 0, 'UniswapV2: TRANSFER_FAILED'
  require ext_code.size(token1Address)
  static call token1Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_datastor8.field_112) > ext_call.return_data[0]:
      revert with 0, 'ds-math-sub-underflow'
  mem[ceil32(return_data.size) + 425 len 64] = 0, addr(_param1), Mask(224, 32, ext_call.return_datastor8.field_112)) >> 32
  call token1Address with:
       gas gas_remaining wei
      args ext_call.return_datastor8.field_112), Mask(224, 32, addr(_param1), Mask(224, 32, ext_call.return_datastor8.field_112)) >> 32) >> 32, mem[ceil32(return_data.size) + 489 len 4]
  if not return_data.size:
      require not ext_call.success
      revert with 0, 'UniswapV2: TRANSFER_FAILED'
  mem[ceil32(return_data.size) + 457 len return_data.size] = ext_call.return_data[0 len return_data.size]
  if not ext_call.success:
      revert with 0, 'UniswapV2: TRANSFER_FAILED'
  if return_data.size:
      require return_data.size >= 32
      if not mem[ceil32(return_data.size) + 457]:
          revert with 0, 'UniswapV2: TRANSFER_FAILED'
  stor12 = 1

def burn(address _payTo) payable: 
  require calldata.size - 4 >= 32
  if stor12 != 1:
      revert with 0, 'UniswapV2: LOCKED'
  stor12 = 0
  require ext_code.size(unknown0dfe1681Address)
  static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(token1Address)
  static call token1Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(factoryAddress)
  static call factoryAddress.0x17e7e58 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[12 len 20]:
      if unknown7464fc3d:
          unknown7464fc3d = 0
      if not ext_call.return_data[0]:
          require totalSupply
          if not ext_call.return_data[0]:
              require totalSupply
              if 0 / totalSupply <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                              mem[204 len 24]
          else:
              require ext_call.return_data[0]
              if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                  revert with 0, 'ds-math-mul-overflow'
              require totalSupply
              if 0 / totalSupply <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                              mem[204 len 24]
              if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                              mem[204 len 24]
      else:
          require ext_call.return_data[0]
          if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
              revert with 0, 'ds-math-mul-overflow'
          require totalSupply
          if not ext_call.return_data[0]:
              require totalSupply
              if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                              mem[204 len 24]
              if 0 / totalSupply <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                              mem[204 len 24]
          else:
              require ext_call.return_data[0]
              if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                  revert with 0, 'ds-math-mul-overflow'
              require totalSupply
              if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                              mem[204 len 24]
              if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                              mem[204 len 24]
      if balanceOf[addr(this.address)] - balanceOf[this.address] > balanceOf[addr(this.address)]:
          revert with 0, 'ds-math-sub-underflow'
      balanceOf[addr(this.address)] -= balanceOf[this.address]
      if totalSupply - balanceOf[this.address] > totalSupply:
          revert with 0, 'ds-math-sub-underflow'
      totalSupply -= balanceOf[this.address]
      log Transfer(
            address from=balanceOf[this.address],
            address to=this.address,
            uint256 tokens=0)
  else:
      if not unknown7464fc3d:
          if not ext_call.return_data[0]:
              require totalSupply
              if not ext_call.return_data[0]:
                  require totalSupply
                  if 0 / totalSupply <= 0:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  40,
                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                  mem[204 len 24]
              else:
                  require ext_call.return_data[0]
                  if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                      revert with 0, 'ds-math-mul-overflow'
                  require totalSupply
                  if 0 / totalSupply <= 0:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  40,
                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                  mem[204 len 24]
                  if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  40,
                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                  mem[204 len 24]
          else:
              require ext_call.return_data[0]
              if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                  revert with 0, 'ds-math-mul-overflow'
              require totalSupply
              if not ext_call.return_data[0]:
                  require totalSupply
                  if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  40,
                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                  mem[204 len 24]
                  if 0 / totalSupply <= 0:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  40,
                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                  mem[204 len 24]
              else:
                  require ext_call.return_data[0]
                  if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                      revert with 0, 'ds-math-mul-overflow'
                  require totalSupply
                  if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  40,
                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                  mem[204 len 24]
                  if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  40,
                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                  mem[204 len 24]
          if balanceOf[addr(this.address)] - balanceOf[this.address] > balanceOf[addr(this.address)]:
              revert with 0, 'ds-math-sub-underflow'
          balanceOf[addr(this.address)] -= balanceOf[this.address]
          if totalSupply - balanceOf[this.address] > totalSupply:
              revert with 0, 'ds-math-sub-underflow'
          totalSupply -= balanceOf[this.address]
          log Transfer(
                address from=balanceOf[this.address],
                address to=this.address,
                uint256 tokens=0)
      else:
          if not Mask(112, 0, stor8.field_112):
              if unknown7464fc3d <= 3:
                  if not ext_call.return_data[0]:
                      require totalSupply
                      if not ext_call.return_data[0]:
                          require totalSupply
                          if 0 / totalSupply <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                          mem[204 len 24]
                      else:
                          require ext_call.return_data[0]
                          if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                              revert with 0, 'ds-math-mul-overflow'
                          require totalSupply
                          if 0 / totalSupply <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                          mem[204 len 24]
                          if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                          mem[204 len 24]
                  else:
                      require ext_call.return_data[0]
                      if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                          revert with 0, 'ds-math-mul-overflow'
                      require totalSupply
                      if not ext_call.return_data[0]:
                          require totalSupply
                          if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                          mem[204 len 24]
                          if 0 / totalSupply <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                          mem[204 len 24]
                      else:
                          require ext_call.return_data[0]
                          if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                              revert with 0, 'ds-math-mul-overflow'
                          require totalSupply
                          if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                          mem[204 len 24]
                          if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                          mem[204 len 24]
                  if balanceOf[addr(this.address)] - balanceOf[this.address] > balanceOf[addr(this.address)]:
                      revert with 0, 'ds-math-sub-underflow'
                  balanceOf[addr(this.address)] -= balanceOf[this.address]
                  if totalSupply - balanceOf[this.address] > totalSupply:
                      revert with 0, 'ds-math-sub-underflow'
                  totalSupply -= balanceOf[this.address]
                  log Transfer(
                        address from=balanceOf[this.address],
                        address to=this.address,
                        uint256 tokens=0)
          else:
              require Mask(112, 0, stor8.field_112)
              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                  revert with 0, 'ds-math-mul-overflow'
              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) <= 3:
                  if not Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112):
                      if unknown7464fc3d <= 3:
                          if not ext_call.return_data[0]:
                              require totalSupply
                              if not ext_call.return_data[0]:
                                  require totalSupply
                                  if 0 / totalSupply <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                  mem[204 len 24]
                              else:
                                  require ext_call.return_data[0]
                                  if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                                      revert with 0, 'ds-math-mul-overflow'
                                  require totalSupply
                                  if 0 / totalSupply <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                  mem[204 len 24]
                                  if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                  mem[204 len 24]
                          else:
                              require ext_call.return_data[0]
                              if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                                  revert with 0, 'ds-math-mul-overflow'
                              require totalSupply
                              if not ext_call.return_data[0]:
                                  require totalSupply
                                  if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                  mem[204 len 24]
                                  if 0 / totalSupply <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                  mem[204 len 24]
                              else:
                                  require ext_call.return_data[0]
                                  if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                                      revert with 0, 'ds-math-mul-overflow'
                                  require totalSupply
                                  if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                  mem[204 len 24]
                                  if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                  mem[204 len 24]
                          if balanceOf[addr(this.address)] - balanceOf[this.address] > balanceOf[addr(this.address)]:
                              revert with 0, 'ds-math-sub-underflow'
                          balanceOf[addr(this.address)] -= balanceOf[this.address]
                          if totalSupply - balanceOf[this.address] > totalSupply:
                              revert with 0, 'ds-math-sub-underflow'
                          totalSupply -= balanceOf[this.address]
                          log Transfer(
                                address from=balanceOf[this.address],
                                address to=this.address,
                                uint256 tokens=0)
                  else:
                      if unknown7464fc3d <= 3:
                          if not unknown7464fc3d:
                              if totalSupply != totalSupply:
                                  revert with 0, 'ds-math-mul-overflow'
                              if not totalSupply / 5:
                                  if not ext_call.return_data[0]:
                                      require totalSupply
                                      if not ext_call.return_data[0]:
                                          require totalSupply
                                          if 0 / totalSupply <= 0:
                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                          32,
                                                          40,
                                                          0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                          mem[204 len 24]
                                      else:
                                          require ext_call.return_data[0]
                                          if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                                              revert with 0, 'ds-math-mul-overflow'
                                          require totalSupply
                                  else:
                                      require ext_call.return_data[0]
                                      if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                                          revert with 0, 'ds-math-mul-overflow'
                                      require totalSupply
                                      if not ext_call.return_data[0]:
                                          require totalSupply
                                      else:
                                          require ext_call.return_data[0]
                                          if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                                              revert with 0, 'ds-math-mul-overflow'
                              else:
                                  if totalSupply + (totalSupply / 5) < totalSupply:
                                      revert with 0, 'ds-math-add-overflow'
                                  totalSupply += totalSupply / 5
                                  if balanceOf[ext_call.return_data] + (totalSupply / 5) < balanceOf[ext_call.return_data]:
                                      revert with 0, 'ds-math-add-overflow'
                                  balanceOf[addr(ext_call.return_data)] = balanceOf[ext_call.return_data] + (totalSupply / 5)
                                  log Transfer(
                                        address from=(totalSupply / 5),
                                        address to=0,
                                        uint256 tokens=addr(ext_call.return_data
                                  if ext_call.return_data[0]:
                                      require ext_call.return_data[0]
                          else:
                              if not ext_call.return_data[0]:
                                  require totalSupply
                                  if not ext_call.return_data[0]:
                                      require totalSupply
                                      if 0 / totalSupply <= 0:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      40,
                                                      0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                      mem[204 len 24]
                                  else:
                                      require ext_call.return_data[0]
                                      if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                                          revert with 0, 'ds-math-mul-overflow'
                                      require totalSupply
                                      if 0 / totalSupply <= 0:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      40,
                                                      0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                      mem[204 len 24]
                                      if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      40,
                                                      0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                      mem[204 len 24]
                              else:
                                  require ext_call.return_data[0]
                                  if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                                      revert with 0, 'ds-math-mul-overflow'
                                  require totalSupply
                                  if not ext_call.return_data[0]:
                                      require totalSupply
                                      if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      40,
                                                      0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                      mem[204 len 24]
                                      if 0 / totalSupply <= 0:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      40,
                                                      0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                      mem[204 len 24]
                                  else:
                                      require ext_call.return_data[0]
                                      if balanceOf[this.address] * ext_call.return_data / ext_call.return_databalanceOf[this.address]:
                                          revert with 0, 'ds-math-mul-overflow'
                                      require totalSupply
                                      if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      40,
                                                      0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                      mem[204 len 24]
                                      if balanceOf[this.address] * ext_call.return_data / totalSupply <= 0:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      40,
                                                      0x59556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4255524e45,
                                                      mem[204 len 24]
                              if balanceOf[addr(this.address)] - balanceOf[this.address] > balanceOf[addr(this.address)]:
                                  revert with 0, 'ds-math-sub-underflow'
                              balanceOf[addr(this.address)] -= balanceOf[this.address]
                              if totalSupply - balanceOf[this.address] > totalSupply:
                                  revert with 0, 'ds-math-sub-underflow'
                              totalSupply -= balanceOf[this.address]
                              log Transfer(
                                    address from=balanceOf[this.address],
                                    address to=this.address,
                                    uint256 tokens=0)
  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)

def unknown022c0d9f(uint256 _param1, uint256 _param2, addr _param3, array _param4) payable: 
  require calldata.size - 4 >= 128
  require _param4 <= 4294967296
  require _param4 + 36 <= calldata.size
  require _param4.length <= 4294967296 and _param4 + _param4.length + 36 <= calldata.size
  if stor12 != 1:
      revert with 0, 'UniswapV2: LOCKED'
  stor12 = 0
  require ext_code.size(factoryAddress)
  static call factoryAddress.0x64a115b4 with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[12 len 20]:
      if _param1 > 0:
          if _param1 >= Mask(112, 0, stor8.field_0):
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x54556e697377617056323a20494e53554646494349454e545f4c49515549444954,
                          mem[197 len 31]
          if _param2 >= Mask(112, 0, stor8.field_112):
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x54556e697377617056323a20494e53554646494349454e545f4c49515549444954,
                          mem[197 len 31]
          if unknown0dfe1681Address == _param3:
              revert with 0, 'UniswapV2: INVALID_TO'
          if _param3 == token1Address:
              revert with 0, 'UniswapV2: INVALID_TO'
          if not _param1:
              if not _param2:
                  if not _param4.length:
                      require ext_code.size(unknown0dfe1681Address)
                      static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(token1Address)
                      static call token1Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data <= Mask(112, 0, stor8.field_0) - _param1:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          36,
                                          0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                          mem[200 len 28]
                          if ext_call.return_datastor8.field_112) + _param2 <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          36,
                                          0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                          mem[200 len 28]
                          if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                              revert with 0, 'ds-math-mul-overflow'
                          if 1000 * ext_call.return_data > 1000 * ext_call.return_data[0]:
                              revert with 0, 'ds-math-sub-underflow'
                      else:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              36,
                                              0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                              mem[200 len 28]
                          else:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  if ext_call.return_datastor8.field_112) + _param2 <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  36,
                                                  0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                                  mem[200 len 28]
                          if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                              revert with 0, 'ds-math-mul-overflow'
                          if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                              revert with 0, 'ds-math-mul-overflow'
                          if (997 * ext_call.return_data * Mask(112, 0, stor8.field_0)) - (3 * _param1) > 1000 * ext_call.return_data[0]:
                              revert with 0, 'ds-math-sub-underflow'
                  else:
                      mem[260 len _param4.length] = _param4[all]
                      mem[_param4.length + 260] = 0
                      require ext_code.size(_param3)
                      call _param3.0x10d1e85c with:
                           gas gas_remaining wei
                          args 0, uint32(caller), _param1, _param2, 128, _param4.length, _param4[all], mem[_param4.length + 260 len ceil32(_param4.length) - _param4.length]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require ext_code.size(unknown0dfe1681Address)
                      static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(token1Address)
                      static call token1Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data <= Mask(112, 0, stor8.field_0) - _param1:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          if ext_call.return_datastor8.field_112) + _param2 <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                              revert with 0, 'ds-math-mul-overflow'
                      else:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                              if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                                  revert with 0, 'ds-math-mul-overflow'
                              if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                                  revert with 0, 'ds-math-mul-overflow'
                              if (997 * ext_call.return_data * Mask(112, 0, stor8.field_0)) - (3 * _param1) > 1000 * ext_call.return_data[0]:
                                  revert with 0, 'ds-math-sub-underflow'
                          else:
                              if ext_call.return_datastor8.field_0) + _param1 > 0:
                                  if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                                      revert with 0, 'ds-math-mul-overflow'
                                  if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                                      revert with 0, 'ds-math-mul-overflow'
                                  if (997 * ext_call.return_data * Mask(112, 0, stor8.field_0)) - (3 * _param1) > 1000 * ext_call.return_data[0]:
                                      revert with 0, 'ds-math-sub-underflow'
                              else:
                                  if ext_call.return_datastor8.field_112) + _param2 <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                                  if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                                      revert with 0, 'ds-math-mul-overflow'
                                  if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                                      revert with 0, 'ds-math-mul-overflow'
      else:
          if _param2 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          37,
                          0xfe556e697377617056323a20494e53554646494349454e545f4f55545055545f414d4f554e,
                          mem[201 len 27]
          if _param1 >= Mask(112, 0, stor8.field_0):
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x54556e697377617056323a20494e53554646494349454e545f4c49515549444954,
                          mem[197 len 31]
          if _param2 >= Mask(112, 0, stor8.field_112):
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x54556e697377617056323a20494e53554646494349454e545f4c49515549444954,
                          mem[197 len 31]
          if unknown0dfe1681Address == _param3:
              revert with 0, 'UniswapV2: INVALID_TO'
          if _param3 == token1Address:
              revert with 0, 'UniswapV2: INVALID_TO'
          if not _param1:
              if not _param2:
                  if not _param4.length:
                      require ext_code.size(unknown0dfe1681Address)
                      static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(token1Address)
                      static call token1Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data <= Mask(112, 0, stor8.field_0) - _param1:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          36,
                                          0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                          mem[200 len 28]
                          if ext_call.return_datastor8.field_112) + _param2 <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          36,
                                          0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                          mem[200 len 28]
                          if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                              revert with 0, 'ds-math-mul-overflow'
                          if 1000 * ext_call.return_data > 1000 * ext_call.return_data[0]:
                              revert with 0, 'ds-math-sub-underflow'
                      else:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              36,
                                              0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                              mem[200 len 28]
                          else:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  if ext_call.return_datastor8.field_112) + _param2 <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  36,
                                                  0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                                  mem[200 len 28]
                          if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                              revert with 0, 'ds-math-mul-overflow'
                          if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                              revert with 0, 'ds-math-mul-overflow'
                          if (997 * ext_call.return_data * Mask(112, 0, stor8.field_0)) - (3 * _param1) > 1000 * ext_call.return_data[0]:
                              revert with 0, 'ds-math-sub-underflow'
                  else:
                      mem[260 len _param4.length] = _param4[all]
                      mem[_param4.length + 260] = 0
                      require ext_code.size(_param3)
                      call _param3.0x10d1e85c with:
                           gas gas_remaining wei
                          args 0, uint32(caller), _param1, _param2, 128, _param4.length, _param4[all], mem[_param4.length + 260 len ceil32(_param4.length) - _param4.length]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require ext_code.size(unknown0dfe1681Address)
                      static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(token1Address)
                      static call token1Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data <= Mask(112, 0, stor8.field_0) - _param1:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          if ext_call.return_datastor8.field_112) + _param2 <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                      else:
                          if ext_call.return_data > Mask(112, 0, stor8.field_112) - _param2:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  if ext_call.return_datastor8.field_112) + _param2 <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          else:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                              revert with 0, 'ds-math-mul-overflow'
                      if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                          revert with 0, 'ds-math-mul-overflow'
  else:
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'UniswapV2: FORBIDDEN'
      if _param1 > 0:
          if _param1 >= Mask(112, 0, stor8.field_0):
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x54556e697377617056323a20494e53554646494349454e545f4c49515549444954,
                          mem[197 len 31]
          if _param2 >= Mask(112, 0, stor8.field_112):
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x54556e697377617056323a20494e53554646494349454e545f4c49515549444954,
                          mem[197 len 31]
          if unknown0dfe1681Address == _param3:
              revert with 0, 'UniswapV2: INVALID_TO'
          if _param3 == token1Address:
              revert with 0, 'UniswapV2: INVALID_TO'
          if not _param1:
              if not _param2:
                  if not _param4.length:
                      require ext_code.size(unknown0dfe1681Address)
                      static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(token1Address)
                      static call token1Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data <= Mask(112, 0, stor8.field_0) - _param1:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          36,
                                          0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                          mem[200 len 28]
                          if ext_call.return_datastor8.field_112) + _param2 <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          36,
                                          0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                          mem[200 len 28]
                          if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                              revert with 0, 'ds-math-mul-overflow'
                          if 1000 * ext_call.return_data > 1000 * ext_call.return_data[0]:
                              revert with 0, 'ds-math-sub-underflow'
                      else:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              36,
                                              0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                              mem[200 len 28]
                          else:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  if ext_call.return_datastor8.field_112) + _param2 <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  36,
                                                  0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                                  mem[200 len 28]
                          if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                              revert with 0, 'ds-math-mul-overflow'
                          if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                              revert with 0, 'ds-math-mul-overflow'
                          if (997 * ext_call.return_data * Mask(112, 0, stor8.field_0)) - (3 * _param1) > 1000 * ext_call.return_data[0]:
                              revert with 0, 'ds-math-sub-underflow'
                  else:
                      mem[260 len _param4.length] = _param4[all]
                      mem[_param4.length + 260] = 0
                      require ext_code.size(_param3)
                      call _param3.0x10d1e85c with:
                           gas gas_remaining wei
                          args 0, uint32(caller), _param1, _param2, 128, _param4.length, _param4[all], mem[_param4.length + 260 len ceil32(_param4.length) - _param4.length]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require ext_code.size(unknown0dfe1681Address)
                      static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(token1Address)
                      static call token1Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data <= Mask(112, 0, stor8.field_0) - _param1:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          if ext_call.return_datastor8.field_112) + _param2 <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                      else:
                          if ext_call.return_data > Mask(112, 0, stor8.field_112) - _param2:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  if ext_call.return_datastor8.field_112) + _param2 <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          else:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                              revert with 0, 'ds-math-mul-overflow'
                      if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                          revert with 0, 'ds-math-mul-overflow'
      else:
          if _param2 <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          37,
                          0xfe556e697377617056323a20494e53554646494349454e545f4f55545055545f414d4f554e,
                          mem[201 len 27]
          if _param1 >= Mask(112, 0, stor8.field_0):
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x54556e697377617056323a20494e53554646494349454e545f4c49515549444954,
                          mem[197 len 31]
          if _param2 >= Mask(112, 0, stor8.field_112):
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x54556e697377617056323a20494e53554646494349454e545f4c49515549444954,
                          mem[197 len 31]
          if unknown0dfe1681Address == _param3:
              revert with 0, 'UniswapV2: INVALID_TO'
          if _param3 == token1Address:
              revert with 0, 'UniswapV2: INVALID_TO'
          if not _param1:
              if not _param2:
                  if not _param4.length:
                      require ext_code.size(unknown0dfe1681Address)
                      static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(token1Address)
                      static call token1Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data <= Mask(112, 0, stor8.field_0) - _param1:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          36,
                                          0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                          mem[200 len 28]
                          if ext_call.return_datastor8.field_112) + _param2 <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          36,
                                          0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                          mem[200 len 28]
                          if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                              revert with 0, 'ds-math-mul-overflow'
                          if 1000 * ext_call.return_data > 1000 * ext_call.return_data[0]:
                              revert with 0, 'ds-math-sub-underflow'
                      else:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              36,
                                              0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                              mem[200 len 28]
                          else:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  if ext_call.return_datastor8.field_112) + _param2 <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  36,
                                                  0x54556e697377617056323a20494e53554646494349454e545f494e5055545f414d4f554e,
                                                  mem[200 len 28]
                          if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                              revert with 0, 'ds-math-mul-overflow'
                          if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                              revert with 0, 'ds-math-mul-overflow'
                          if (997 * ext_call.return_data * Mask(112, 0, stor8.field_0)) - (3 * _param1) > 1000 * ext_call.return_data[0]:
                              revert with 0, 'ds-math-sub-underflow'
                  else:
                      mem[260 len _param4.length] = _param4[all]
                      mem[_param4.length + 260] = 0
                      require ext_code.size(_param3)
                      call _param3.0x10d1e85c with:
                           gas gas_remaining wei
                          args 0, uint32(caller), _param1, _param2, 128, _param4.length, _param4[all], mem[_param4.length + 260 len ceil32(_param4.length) - _param4.length]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require ext_code.size(unknown0dfe1681Address)
                      static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(token1Address)
                      static call token1Address.balanceOf(address tokenOwner) with:
                              gas gas_remaining wei
                             args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data <= Mask(112, 0, stor8.field_0) - _param1:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          if ext_call.return_datastor8.field_112) + _param2 <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                      else:
                          if ext_call.return_data <= Mask(112, 0, stor8.field_112) - _param2:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          else:
                              if ext_call.return_datastor8.field_0) + _param1 <= 0:
                                  if ext_call.return_datastor8.field_112) + _param2 <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'TUniswapV2: INSUFFICIENT_INPUT_AMOUN'
                          if (3 * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (3 * _param1) / 3 != ext_call.return_datastor8.field_0) + _param1:
                              revert with 0, 'ds-math-mul-overflow'
                      if 1000 * ext_call.return_data / 1000 != ext_call.return_data[0]:
                          revert with 0, 'ds-math-mul-overflow'
  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)

def mint(address _to) payable: 
  require calldata.size - 4 >= 32
  if stor12 != 1:
      revert with 0, 'UniswapV2: LOCKED'
  stor12 = 0
  require ext_code.size(unknown0dfe1681Address)
  static call unknown0dfe1681Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(token1Address)
  static call token1Address.balanceOf(address tokenOwner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_datastor8.field_0) > ext_call.return_data[0]:
      revert with 0, 'ds-math-sub-underflow'
  if ext_call.return_datastor8.field_112) > ext_call.return_data[0]:
      revert with 0, 'ds-math-sub-underflow'
  require ext_code.size(factoryAddress)
  static call factoryAddress.0x17e7e58 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20]:
      if unknown7464fc3d:
          if not Mask(112, 0, stor8.field_112):
              if unknown7464fc3d <= 3:
                  if not totalSupply:
                      if ext_call.return_datastor8.field_112):
                          require ext_call.return_datastor8.field_112)
                          if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / ext_call.return_datastor8.field_112) != ext_call.return_datastor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) > 3:
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      revert with 0, 'ds-math-sub-underflow'
                  if unknown7464fc3d:
                      require totalSupply
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / totalSupply != ext_call.return_datastor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      require Mask(112, 0, stor8.field_0)
                      if not totalSupply:
                          require Mask(112, 0, stor8.field_112)
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < 0 / Mask(112, 0, stor8.field_112):
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              40,
                                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                              mem[204 len 24]
                              if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                                  revert with 0, 'ds-math-add-overflow'
                              totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                              if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                                  revert with 0, 'ds-math-add-overflow'
                              balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                              log Transfer(
                                    address from=((ext_call.return_data
                                    address to=0,
                                    uint256 tokens=_to)
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  require Mask(112, 0, stor8.field_112)
                                  if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                      revert with 0, 'ds-math-mul-overflow'
                                  unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                              else:
                                  if not Mask(112, 0, stor8.field_0):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                      if not Mask(112, 0, stor8.field_112):
                                          unknown7464fc3d = 0
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                                  else:
                                      if Mask(112, 0, stor8.field_112):
                                          require Mask(112, 0, stor8.field_0)
                                          unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                                      else:
                                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                          uint32(stor8.field_224) = uint32(block.timestamp)
                                          log 0x1c411e9a: ext_call.return_data
                                          if not addr(ext_call.return_data):
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                                              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                          if Mask(112, 0, stor8.field_112):
                                              require Mask(112, 0, stor8.field_112)
                                              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                                  revert with 0, 'ds-math-mul-overflow'
                                          else:
                                              unknown7464fc3d = 0
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                          else:
                              if 0 / Mask(112, 0, stor8.field_112) <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              40,
                                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                              mem[204 len 24]
                              if totalSupply + (0 / Mask(112, 0, stor8.field_112)) < totalSupply:
                                  revert with 0, 'ds-math-add-overflow'
                              totalSupply += 0 / Mask(112, 0, stor8.field_112)
                              if balanceOf[addr(_to)] + (0 / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                                  revert with 0, 'ds-math-add-overflow'
                              balanceOf[addr(_to)] += 0 / Mask(112, 0, stor8.field_112)
                              log Transfer(
                                    address from=(0 / Mask(112, 0, stor8.field_112)),
                                    address to=0,
                                    uint256 tokens=_to)
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return (0 / Mask(112, 0, stor8.field_112))
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return (0 / Mask(112, 0, stor8.field_112))
                                  require Mask(112, 0, stor8.field_112)
                                  if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                      revert with 0, 'ds-math-mul-overflow'
                                  unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                              else:
                                  if not Mask(112, 0, stor8.field_0):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return (0 / Mask(112, 0, stor8.field_112))
                                      if not Mask(112, 0, stor8.field_112):
                                          unknown7464fc3d = 0
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return (0 / Mask(112, 0, stor8.field_112))
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                                  else:
                                      if Mask(112, 0, stor8.field_112):
                                          require Mask(112, 0, stor8.field_0)
                                          unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                                      else:
                                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                          uint32(stor8.field_224) = uint32(block.timestamp)
                                          log 0x1c411e9a: ext_call.return_data
                                          if not addr(ext_call.return_data):
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                                              return (0 / Mask(112, 0, stor8.field_112))
                                          if Mask(112, 0, stor8.field_112):
                                              require Mask(112, 0, stor8.field_112)
                                              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                                  revert with 0, 'ds-math-mul-overflow'
                                          else:
                                              unknown7464fc3d = 0
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      require totalSupply
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / totalSupply != ext_call.return_datastor8.field_112):
                          revert with 0, 'ds-math-mul-overflow'
                      require Mask(112, 0, stor8.field_112)
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112):
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                          mem[204 len 24]
                          if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                              revert with 0, 'ds-math-add-overflow'
                          totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                          if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                              revert with 0, 'ds-math-add-overflow'
                          balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                          log Transfer(
                                address from=((ext_call.return_data
                                address to=0,
                                uint256 tokens=_to)
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                              if Mask(112, 0, stor8.field_112):
                                  require Mask(112, 0, stor8.field_112)
                                  if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                      revert with 0, 'ds-math-mul-overflow'
                              else:
                                  unknown7464fc3d = 0
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          if not Mask(112, 0, stor8.field_0):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                              if not Mask(112, 0, stor8.field_112):
                                  unknown7464fc3d = 0
                              else:
                                  require Mask(112, 0, stor8.field_112)
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          if Mask(112, 0, stor8.field_112):
                              require Mask(112, 0, stor8.field_0)
                              unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                          uint32(stor8.field_224) = uint32(block.timestamp)
                          log 0x1c411e9a: ext_call.return_data
                          if not addr(ext_call.return_data):
                              log Mint(
                                    address owner=ext_call.return_data
                                    uint256 newTokenId=ext_call.return_data
                                    uint256 genes=caller)
                              stor12 = 1
                              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                      else:
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112) <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                          mem[204 len 24]
                          if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < totalSupply:
                              revert with 0, 'ds-math-add-overflow'
                          totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                          if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                              revert with 0, 'ds-math-add-overflow'
                          balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                          log Transfer(
                                address from=((ext_call.return_data
                                address to=0,
                                uint256 tokens=_to)
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                              if Mask(112, 0, stor8.field_112):
                                  require Mask(112, 0, stor8.field_112)
                                  if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                      revert with 0, 'ds-math-mul-overflow'
                              else:
                                  unknown7464fc3d = 0
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          if not Mask(112, 0, stor8.field_0):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                              if not Mask(112, 0, stor8.field_112):
                                  unknown7464fc3d = 0
                              else:
                                  require Mask(112, 0, stor8.field_112)
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          if Mask(112, 0, stor8.field_112):
                              require Mask(112, 0, stor8.field_0)
                              unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                          uint32(stor8.field_224) = uint32(block.timestamp)
                          log 0x1c411e9a: ext_call.return_data
                          if not addr(ext_call.return_data):
                              log Mint(
                                    address owner=ext_call.return_data
                                    uint256 newTokenId=ext_call.return_data
                                    uint256 genes=caller)
                              stor12 = 1
                              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                      ('bool', ('mask_shl', 160, 0, 0, ('ext_call.return_data', 0, 32)))
                      if not Mask(112, 0, stor8.field_112):
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      require Mask(112, 0, stor8.field_112)
                      ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                  require totalSupply
                  if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / totalSupply != ext_call.return_datastor8.field_0):
                      revert with 0, 'ds-math-mul-overflow'
                  require Mask(112, 0, stor8.field_0)
                  if not totalSupply:
                      require Mask(112, 0, stor8.field_112)
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < 0 / Mask(112, 0, stor8.field_112):
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                          mem[204 len 24]
                          if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                              revert with 0, 'ds-math-add-overflow'
                          totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                          if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                              revert with 0, 'ds-math-add-overflow'
                          balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                          log Transfer(
                                address from=((ext_call.return_data
                                address to=0,
                                uint256 tokens=_to)
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if addr(ext_call.return_data):
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                  else:
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                              log Mint(
                                    address owner=ext_call.return_data
                                    uint256 newTokenId=ext_call.return_data
                                    uint256 genes=caller)
                              stor12 = 1
                              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                          if Mask(112, 0, stor8.field_0):
                              if Mask(112, 0, stor8.field_112):
                                  require Mask(112, 0, stor8.field_0)
                                  unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                              else:
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  require Mask(112, 0, stor8.field_112)
                                  if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                      revert with 0, 'ds-math-mul-overflow'
                                  unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                          else:
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                              if not Mask(112, 0, stor8.field_112):
                                  unknown7464fc3d = 0
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                              require Mask(112, 0, stor8.field_112)
                              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                  revert with 0, 'ds-math-mul-overflow'
                              unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                              log Mint(
                                    address owner=ext_call.return_data
                                    uint256 newTokenId=ext_call.return_data
                                    uint256 genes=caller)
                              stor12 = 1
                      else:
                          if 0 / Mask(112, 0, stor8.field_112) <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                          mem[204 len 24]
                          if totalSupply + (0 / Mask(112, 0, stor8.field_112)) < totalSupply:
                              revert with 0, 'ds-math-add-overflow'
                          totalSupply += 0 / Mask(112, 0, stor8.field_112)
                          if balanceOf[addr(_to)] + (0 / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                              revert with 0, 'ds-math-add-overflow'
                          balanceOf[addr(_to)] += 0 / Mask(112, 0, stor8.field_112)
                          log Transfer(
                                address from=(0 / Mask(112, 0, stor8.field_112)),
                                address to=0,
                                uint256 tokens=_to)
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if addr(ext_call.return_data):
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                  else:
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                              log Mint(
                                    address owner=ext_call.return_data
                                    uint256 newTokenId=ext_call.return_data
                                    uint256 genes=caller)
                              stor12 = 1
                              return (0 / Mask(112, 0, stor8.field_112))
                          if Mask(112, 0, stor8.field_0):
                              if Mask(112, 0, stor8.field_112):
                                  require Mask(112, 0, stor8.field_0)
                                  unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                              else:
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return (0 / Mask(112, 0, stor8.field_112))
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return (0 / Mask(112, 0, stor8.field_112))
                                  require Mask(112, 0, stor8.field_112)
                                  if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                      revert with 0, 'ds-math-mul-overflow'
                                  unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                          else:
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return (0 / Mask(112, 0, stor8.field_112))
                              if not Mask(112, 0, stor8.field_112):
                                  unknown7464fc3d = 0
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return (0 / Mask(112, 0, stor8.field_112))
                              require Mask(112, 0, stor8.field_112)
                              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                  revert with 0, 'ds-math-mul-overflow'
                              unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                              log Mint(
                                    address owner=ext_call.return_data
                                    uint256 newTokenId=ext_call.return_data
                                    uint256 genes=caller)
                              stor12 = 1
                  else:
                      require totalSupply
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / totalSupply != ext_call.return_datastor8.field_112):
                          revert with 0, 'ds-math-mul-overflow'
                      require Mask(112, 0, stor8.field_112)
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112):
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                          mem[204 len 24]
                          if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                              revert with 0, 'ds-math-add-overflow'
                          totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                          if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                              revert with 0, 'ds-math-add-overflow'
                          balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                          log Transfer(
                                address from=((ext_call.return_data
                                address to=0,
                                uint256 tokens=_to)
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                              if not Mask(112, 0, stor8.field_112):
                                  unknown7464fc3d = 0
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                              require Mask(112, 0, stor8.field_112)
                              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                  revert with 0, 'ds-math-mul-overflow'
                              unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                          else:
                              if not Mask(112, 0, stor8.field_0):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  if Mask(112, 0, stor8.field_112):
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                  else:
                                      unknown7464fc3d = 0
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                              else:
                                  if Mask(112, 0, stor8.field_112):
                                      require Mask(112, 0, stor8.field_0)
                                      unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                                  else:
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                      if not Mask(112, 0, stor8.field_112):
                                          unknown7464fc3d = 0
                                      else:
                                          require Mask(112, 0, stor8.field_112)
                      else:
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112) <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                          mem[204 len 24]
                          if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < totalSupply:
                              revert with 0, 'ds-math-add-overflow'
                          totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                          if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                              revert with 0, 'ds-math-add-overflow'
                          balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                          log Transfer(
                                address from=((ext_call.return_data
                                address to=0,
                                uint256 tokens=_to)
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                              if not Mask(112, 0, stor8.field_112):
                                  unknown7464fc3d = 0
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                              require Mask(112, 0, stor8.field_112)
                              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                  revert with 0, 'ds-math-mul-overflow'
                              unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                          else:
                              if not Mask(112, 0, stor8.field_0):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                                  if Mask(112, 0, stor8.field_112):
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                  else:
                                      unknown7464fc3d = 0
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                              else:
                                  if Mask(112, 0, stor8.field_112):
                                      require Mask(112, 0, stor8.field_0)
                                      unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                                  else:
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                                      if not Mask(112, 0, stor8.field_112):
                                          unknown7464fc3d = 0
                                      else:
                                          require Mask(112, 0, stor8.field_112)
          else:
              require Mask(112, 0, stor8.field_112)
              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                  revert with 0, 'ds-math-mul-overflow'
              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) <= 3:
                  if not Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112):
                      if unknown7464fc3d > 3:
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if not totalSupply:
                          if ext_call.return_datastor8.field_112):
                              require ext_call.return_datastor8.field_112)
                              if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / ext_call.return_datastor8.field_112) != ext_call.return_datastor8.field_0):
                                  revert with 0, 'ds-math-mul-overflow'
                              if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) > 3:
                                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          revert with 0, 'ds-math-sub-underflow'
                      require totalSupply
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / totalSupply != ext_call.return_datastor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      require Mask(112, 0, stor8.field_0)
                      if not unknown7464fc3d:
                          if not totalSupply:
                              require Mask(112, 0, stor8.field_112)
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < 0 / Mask(112, 0, stor8.field_112):
                                  if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                                  mem[204 len 24]
                                  if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                                      revert with 0, 'ds-math-add-overflow'
                                  totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                                  if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                                      revert with 0, 'ds-math-add-overflow'
                                  balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                                  log Transfer(
                                        address from=((ext_call.return_data
                                        address to=0,
                                        uint256 tokens=_to)
                                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                      revert with 0, 'UniswapV2: OVERFLOW'
                                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                      revert with 0, 'UniswapV2: OVERFLOW'
                                  if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                      if not Mask(112, 0, stor8.field_112):
                                          unknown7464fc3d = 0
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                                  else:
                                      if not Mask(112, 0, stor8.field_0):
                                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                          uint32(stor8.field_224) = uint32(block.timestamp)
                                          log 0x1c411e9a: ext_call.return_data
                                          if not addr(ext_call.return_data):
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                                              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                          if Mask(112, 0, stor8.field_112):
                                              require Mask(112, 0, stor8.field_112)
                                              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                                  revert with 0, 'ds-math-mul-overflow'
                                          else:
                                              unknown7464fc3d = 0
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                                      else:
                                          if Mask(112, 0, stor8.field_112):
                                              require Mask(112, 0, stor8.field_0)
                                              unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                                          else:
                                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                              uint32(stor8.field_224) = uint32(block.timestamp)
                                              log 0x1c411e9a: ext_call.return_data
                                              if not addr(ext_call.return_data):
                                                  log Mint(
                                                        address owner=ext_call.return_data
                                                        uint256 newTokenId=ext_call.return_data
                                                        uint256 genes=caller)
                                                  stor12 = 1
                                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                              if not Mask(112, 0, stor8.field_112):
                                                  unknown7464fc3d = 0
                                              else:
                                                  require Mask(112, 0, stor8.field_112)
                              else:
                                  if 0 / Mask(112, 0, stor8.field_112) <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                                  mem[204 len 24]
                                  if totalSupply + (0 / Mask(112, 0, stor8.field_112)) < totalSupply:
                                      revert with 0, 'ds-math-add-overflow'
                                  totalSupply += 0 / Mask(112, 0, stor8.field_112)
                                  if balanceOf[addr(_to)] + (0 / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                                      revert with 0, 'ds-math-add-overflow'
                                  balanceOf[addr(_to)] += 0 / Mask(112, 0, stor8.field_112)
                                  log Transfer(
                                        address from=(0 / Mask(112, 0, stor8.field_112)),
                                        address to=0,
                                        uint256 tokens=_to)
                                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                      revert with 0, 'UniswapV2: OVERFLOW'
                                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                      revert with 0, 'UniswapV2: OVERFLOW'
                                  if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return (0 / Mask(112, 0, stor8.field_112))
                                      if not Mask(112, 0, stor8.field_112):
                                          unknown7464fc3d = 0
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return (0 / Mask(112, 0, stor8.field_112))
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                                  else:
                                      if not Mask(112, 0, stor8.field_0):
                                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                          uint32(stor8.field_224) = uint32(block.timestamp)
                                          log 0x1c411e9a: ext_call.return_data
                                          if not addr(ext_call.return_data):
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                                              return (0 / Mask(112, 0, stor8.field_112))
                                          if Mask(112, 0, stor8.field_112):
                                              require Mask(112, 0, stor8.field_112)
                                              if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                                  revert with 0, 'ds-math-mul-overflow'
                                          else:
                                              unknown7464fc3d = 0
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                                      else:
                                          if Mask(112, 0, stor8.field_112):
                                              require Mask(112, 0, stor8.field_0)
                                              unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                                          else:
                                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                              uint32(stor8.field_224) = uint32(block.timestamp)
                                              log 0x1c411e9a: ext_call.return_data
                                              if not addr(ext_call.return_data):
                                                  log Mint(
                                                        address owner=ext_call.return_data
                                                        uint256 newTokenId=ext_call.return_data
                                                        uint256 genes=caller)
                                                  stor12 = 1
                                                  return (0 / Mask(112, 0, stor8.field_112))
                                              if not Mask(112, 0, stor8.field_112):
                                                  unknown7464fc3d = 0
                                              else:
                                                  require Mask(112, 0, stor8.field_112)
                          else:
                              require totalSupply
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / totalSupply != ext_call.return_datastor8.field_112):
                                  revert with 0, 'ds-math-mul-overflow'
                              require Mask(112, 0, stor8.field_112)
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112):
                                  if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                                  mem[204 len 24]
                                  if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                                      revert with 0, 'ds-math-add-overflow'
                                  totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                                  if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                                      revert with 0, 'ds-math-add-overflow'
                                  balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                                  log Transfer(
                                        address from=((ext_call.return_data
                                        address to=0,
                                        uint256 tokens=_to)
                                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                      revert with 0, 'UniswapV2: OVERFLOW'
                                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                      revert with 0, 'UniswapV2: OVERFLOW'
                                  if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                      if not Mask(112, 0, stor8.field_112):
                                          unknown7464fc3d = 0
                                      else:
                                          require Mask(112, 0, stor8.field_112)
                                  else:
                                      if not Mask(112, 0, stor8.field_0):
                                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                          uint32(stor8.field_224) = uint32(block.timestamp)
                                          log 0x1c411e9a: ext_call.return_data
                                          if not addr(ext_call.return_data):
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                                              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                          if not Mask(112, 0, stor8.field_112):
                                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                          require Mask(112, 0, stor8.field_112)
                                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                      if Mask(112, 0, stor8.field_112):
                                          require Mask(112, 0, stor8.field_0)
                                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                      if Mask(112, 0, stor8.field_112):
                              else:
                                  if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112) <= 0:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                  32,
                                                  40,
                                                  0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                                  mem[204 len 24]
                                  if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < totalSupply:
                                      revert with 0, 'ds-math-add-overflow'
                                  totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                                  if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                                      revert with 0, 'ds-math-add-overflow'
                                  balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                                  log Transfer(
                                        address from=((ext_call.return_data
                                        address to=0,
                                        uint256 tokens=_to)
                                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                      revert with 0, 'UniswapV2: OVERFLOW'
                                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                      revert with 0, 'UniswapV2: OVERFLOW'
                                  if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                                      if not Mask(112, 0, stor8.field_112):
                                          unknown7464fc3d = 0
                                      else:
                                          require Mask(112, 0, stor8.field_112)
                                  else:
                                      if not Mask(112, 0, stor8.field_0):
                                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                          uint32(stor8.field_224) = uint32(block.timestamp)
                                          log 0x1c411e9a: ext_call.return_data
                                          if not addr(ext_call.return_data):
                                              log Mint(
                                                    address owner=ext_call.return_data
                                                    uint256 newTokenId=ext_call.return_data
                                                    uint256 genes=caller)
                                              stor12 = 1
                                              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                                          if not Mask(112, 0, stor8.field_112):
                                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                          require Mask(112, 0, stor8.field_112)
                                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                      if Mask(112, 0, stor8.field_112):
                                          require Mask(112, 0, stor8.field_0)
                                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                                      if Mask(112, 0, stor8.field_112):
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if not totalSupply:
                          require Mask(112, 0, stor8.field_112)
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < 0 / Mask(112, 0, stor8.field_112):
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              40,
                                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                              mem[204 len 24]
                              if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                                  revert with 0, 'ds-math-add-overflow'
                              totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                              if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                                  revert with 0, 'ds-math-add-overflow'
                              balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                              log Transfer(
                                    address from=((ext_call.return_data
                                    address to=0,
                                    uint256 tokens=_to)
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  if Mask(112, 0, stor8.field_112):
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                  else:
                                      unknown7464fc3d = 0
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                              if not Mask(112, 0, stor8.field_0):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                  else:
                                      require Mask(112, 0, stor8.field_112)
                                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                              if Mask(112, 0, stor8.field_112):
                                  require Mask(112, 0, stor8.field_0)
                                  unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                          else:
                              if 0 / Mask(112, 0, stor8.field_112) <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              40,
                                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                              mem[204 len 24]
                              if totalSupply + (0 / Mask(112, 0, stor8.field_112)) < totalSupply:
                                  revert with 0, 'ds-math-add-overflow'
                              totalSupply += 0 / Mask(112, 0, stor8.field_112)
                              if balanceOf[addr(_to)] + (0 / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                                  revert with 0, 'ds-math-add-overflow'
                              balanceOf[addr(_to)] += 0 / Mask(112, 0, stor8.field_112)
                              log Transfer(
                                    address from=(0 / Mask(112, 0, stor8.field_112)),
                                    address to=0,
                                    uint256 tokens=_to)
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return (0 / Mask(112, 0, stor8.field_112))
                                  if Mask(112, 0, stor8.field_112):
                                      require Mask(112, 0, stor8.field_112)
                                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                  else:
                                      unknown7464fc3d = 0
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                              if not Mask(112, 0, stor8.field_0):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return (0 / Mask(112, 0, stor8.field_112))
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                  else:
                                      require Mask(112, 0, stor8.field_112)
                                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                              if Mask(112, 0, stor8.field_112):
                                  require Mask(112, 0, stor8.field_0)
                                  unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return (0 / Mask(112, 0, stor8.field_112))
                          ('bool', ('mask_shl', 160, 0, 0, ('ext_call.return_data', 0, 32)))
                          if not Mask(112, 0, stor8.field_112):
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          require Mask(112, 0, stor8.field_112)
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      require totalSupply
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / totalSupply != ext_call.return_datastor8.field_112):
                          revert with 0, 'ds-math-mul-overflow'
                      require Mask(112, 0, stor8.field_112)
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112):
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                          32,
                                          40,
                                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                          mem[204 len 24]
                          if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                              revert with 0, 'ds-math-add-overflow'
                          totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                          if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                              revert with 0, 'ds-math-add-overflow'
                          balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                          log Transfer(
                                address from=((ext_call.return_data
                                address to=0,
                                uint256 tokens=_to)
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                              revert with 0, 'UniswapV2: OVERFLOW'
                          if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                              if not Mask(112, 0, stor8.field_112):
                                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                              require Mask(112, 0, stor8.field_112)
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          if not Mask(112, 0, stor8.field_0):
                              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                              uint32(stor8.field_224) = uint32(block.timestamp)
                              log 0x1c411e9a: ext_call.return_data
                              if not addr(ext_call.return_data):
                                  log Mint(
                                        address owner=ext_call.return_data
                                        uint256 newTokenId=ext_call.return_data
                                        uint256 genes=caller)
                                  stor12 = 1
                                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                              if Mask(112, 0, stor8.field_112):
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          if Mask(112, 0, stor8.field_112):
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                          uint32(stor8.field_224) = uint32(block.timestamp)
                          log 0x1c411e9a: ext_call.return_data
                          if addr(ext_call.return_data):
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          log Mint(
                                address owner=ext_call.return_data
                                uint256 newTokenId=ext_call.return_data
                                uint256 genes=caller)
                          stor12 = 1
                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112) <= 0:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                      32,
                                      40,
                                      0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                      mem[204 len 24]
                      if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < totalSupply:
                          revert with 0, 'ds-math-add-overflow'
                      totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                      if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                          revert with 0, 'ds-math-add-overflow'
                      balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                      log Transfer(
                            address from=((ext_call.return_data
                            address to=0,
                            uint256 tokens=_to)
                      if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                          revert with 0, 'UniswapV2: OVERFLOW'
                      if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                          revert with 0, 'UniswapV2: OVERFLOW'
                      if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                          uint32(stor8.field_224) = uint32(block.timestamp)
                          log 0x1c411e9a: ext_call.return_data
                          if not addr(ext_call.return_data):
                              log Mint(
                                    address owner=ext_call.return_data
                                    uint256 newTokenId=ext_call.return_data
                                    uint256 genes=caller)
                              stor12 = 1
                              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                          if not Mask(112, 0, stor8.field_112):
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          require Mask(112, 0, stor8.field_112)
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if not Mask(112, 0, stor8.field_0):
                          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                          uint32(stor8.field_224) = uint32(block.timestamp)
                          log 0x1c411e9a: ext_call.return_data
                          if not addr(ext_call.return_data):
                              log Mint(
                                    address owner=ext_call.return_data
                                    uint256 newTokenId=ext_call.return_data
                                    uint256 genes=caller)
                              stor12 = 1
                              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                          if Mask(112, 0, stor8.field_112):
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if Mask(112, 0, stor8.field_112):
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                      uint32(stor8.field_224) = uint32(block.timestamp)
                      log 0x1c411e9a: ext_call.return_data
                      if addr(ext_call.return_data):
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      log Mint(
                            address owner=ext_call.return_data
                            uint256 newTokenId=ext_call.return_data
                            uint256 genes=caller)
                      stor12 = 1
                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                  if unknown7464fc3d <= 3:
                      if not unknown7464fc3d:
                          if totalSupply != totalSupply:
                              revert with 0, 'ds-math-mul-overflow'
                          if not totalSupply / 5:
                              if not totalSupply:
                                  if ext_call.return_datastor8.field_112):
                                      require ext_call.return_datastor8.field_112)
                                      if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / ext_call.return_datastor8.field_112) != ext_call.return_datastor8.field_0):
                                          revert with 0, 'ds-math-mul-overflow'
                                      if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) > 3:
                                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                  revert with 0, 'ds-math-sub-underflow'
                              require totalSupply
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / totalSupply != ext_call.return_datastor8.field_0):
                                  revert with 0, 'ds-math-mul-overflow'
                              require Mask(112, 0, stor8.field_0)
                              if not totalSupply:
                                  require Mask(112, 0, stor8.field_112)
                                  if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < 0 / Mask(112, 0, stor8.field_112):
                                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      40,
                                                      0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                                      mem[204 len 24]
                                  else:
                                      if 0 / Mask(112, 0, stor8.field_112) <= 0:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                                      32,
                                                      40,
                                                      0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                                      mem[204 len 24]
                              else:
                                  require totalSupply
                                  if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / totalSupply != ext_call.return_datastor8.field_112):
                                      revert with 0, 'ds-math-mul-overflow'
                                  require Mask(112, 0, stor8.field_112)
                                  if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) >= (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112):
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          if totalSupply + (totalSupply / 5) < totalSupply:
                              revert with 0, 'ds-math-add-overflow'
                          totalSupply += totalSupply / 5
                          if balanceOf[ext_call.return_data] + (totalSupply / 5) < balanceOf[ext_call.return_data]:
                              revert with 0, 'ds-math-add-overflow'
                          balanceOf[addr(ext_call.return_data)] = balanceOf[ext_call.return_data] + (totalSupply / 5)
                          log Transfer(
                                address from=(totalSupply / 5),
                                address to=0,
                                uint256 tokens=addr(ext_call.return_data
                          if totalSupply:
                              require totalSupply
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / totalSupply != ext_call.return_datastor8.field_0):
                                  revert with 0, 'ds-math-mul-overflow'
                              require Mask(112, 0, stor8.field_0)
                              if totalSupply:
                                  require totalSupply
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          if not ext_call.return_datastor8.field_112):
                              revert with 0, 'ds-math-sub-underflow'
                          require ext_call.return_datastor8.field_112)
                          if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / ext_call.return_datastor8.field_112) != ext_call.return_datastor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) <= 3:
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          if ((ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / 2) + 1 >= (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)):
                              ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          require ((ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / 2) + 1
                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                      if not totalSupply:
                          if ext_call.return_datastor8.field_112):
                              require ext_call.return_datastor8.field_112)
                              if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / ext_call.return_datastor8.field_112) != ext_call.return_datastor8.field_0):
                                  revert with 0, 'ds-math-mul-overflow'
                              if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) > 3:
                                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                          revert with 0, 'ds-math-sub-underflow'
                      require totalSupply
                      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / totalSupply != ext_call.return_datastor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      require Mask(112, 0, stor8.field_0)
                      if not totalSupply:
                          require Mask(112, 0, stor8.field_112)
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < 0 / Mask(112, 0, stor8.field_112):
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              40,
                                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                              mem[204 len 24]
                              if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                                  revert with 0, 'ds-math-add-overflow'
                              totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                              if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                                  revert with 0, 'ds-math-add-overflow'
                              balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                              log Transfer(
                                    address from=((ext_call.return_data
                                    address to=0,
                                    uint256 tokens=_to)
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                  else:
                                      require Mask(112, 0, stor8.field_112)
                              else:
                                  if not Mask(112, 0, stor8.field_0):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                      if not Mask(112, 0, stor8.field_112):
                                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                      require Mask(112, 0, stor8.field_112)
                                      ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                  if Mask(112, 0, stor8.field_112):
                                      require Mask(112, 0, stor8.field_0)
                                      ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  if Mask(112, 0, stor8.field_112):
                          else:
                              if 0 / Mask(112, 0, stor8.field_112) <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              40,
                                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                              mem[204 len 24]
                              if totalSupply + (0 / Mask(112, 0, stor8.field_112)) < totalSupply:
                                  revert with 0, 'ds-math-add-overflow'
                              totalSupply += 0 / Mask(112, 0, stor8.field_112)
                              if balanceOf[addr(_to)] + (0 / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                                  revert with 0, 'ds-math-add-overflow'
                              balanceOf[addr(_to)] += 0 / Mask(112, 0, stor8.field_112)
                              log Transfer(
                                    address from=(0 / Mask(112, 0, stor8.field_112)),
                                    address to=0,
                                    uint256 tokens=_to)
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return (0 / Mask(112, 0, stor8.field_112))
                                  if not Mask(112, 0, stor8.field_112):
                                      unknown7464fc3d = 0
                                  else:
                                      require Mask(112, 0, stor8.field_112)
                              else:
                                  if not Mask(112, 0, stor8.field_0):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                                          return (0 / Mask(112, 0, stor8.field_112))
                                      if not Mask(112, 0, stor8.field_112):
                                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                      require Mask(112, 0, stor8.field_112)
                                      ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                  if Mask(112, 0, stor8.field_112):
                                      require Mask(112, 0, stor8.field_0)
                                      ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return (0 / Mask(112, 0, stor8.field_112))
                                  if Mask(112, 0, stor8.field_112):
                      else:
                          require totalSupply
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / totalSupply != ext_call.return_datastor8.field_112):
                              revert with 0, 'ds-math-mul-overflow'
                          require Mask(112, 0, stor8.field_112)
                          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112):
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              40,
                                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                              mem[204 len 24]
                              if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                                  revert with 0, 'ds-math-add-overflow'
                              totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                              if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                                  revert with 0, 'ds-math-add-overflow'
                              balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                              log Transfer(
                                    address from=((ext_call.return_data
                                    address to=0,
                                    uint256 tokens=_to)
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  if Mask(112, 0, stor8.field_112):
                              else:
                                  if not Mask(112, 0, stor8.field_0):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if addr(ext_call.return_data):
                                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
                                  if not Mask(112, 0, stor8.field_112):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
                          else:
                              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112) <= 0:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                              32,
                                              40,
                                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                              mem[204 len 24]
                              if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < totalSupply:
                                  revert with 0, 'ds-math-add-overflow'
                              totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                              if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                                  revert with 0, 'ds-math-add-overflow'
                              balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
                              log Transfer(
                                    address from=((ext_call.return_data
                                    address to=0,
                                    uint256 tokens=_to)
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                                  revert with 0, 'UniswapV2: OVERFLOW'
                              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                  uint32(stor8.field_224) = uint32(block.timestamp)
                                  log 0x1c411e9a: ext_call.return_data
                                  if not addr(ext_call.return_data):
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                                  if Mask(112, 0, stor8.field_112):
                              else:
                                  if not Mask(112, 0, stor8.field_0):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if addr(ext_call.return_data):
                                          ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
                                      log Mint(
                                            address owner=ext_call.return_data
                                            uint256 newTokenId=ext_call.return_data
                                            uint256 genes=caller)
                                      stor12 = 1
                                      return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
                                  if not Mask(112, 0, stor8.field_112):
                                      Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                                      Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                                      uint32(stor8.field_224) = uint32(block.timestamp)
                                      log 0x1c411e9a: ext_call.return_data
                                      if not addr(ext_call.return_data):
                                          log Mint(
                                                address owner=ext_call.return_data
                                                uint256 newTokenId=ext_call.return_data
                                                uint256 genes=caller)
                                          stor12 = 1
      else:
          if not totalSupply:
              if ext_call.return_datastor8.field_112):
                  require ext_call.return_datastor8.field_112)
                  if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / ext_call.return_datastor8.field_112) != ext_call.return_datastor8.field_0):
                      revert with 0, 'ds-math-mul-overflow'
                  if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) > 3:
                      ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              revert with 0, 'ds-math-sub-underflow'
          require totalSupply
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / totalSupply != ext_call.return_datastor8.field_0):
              revert with 0, 'ds-math-mul-overflow'
          require Mask(112, 0, stor8.field_0)
          if not totalSupply:
              require Mask(112, 0, stor8.field_112)
              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < 0 / Mask(112, 0, stor8.field_112):
                  if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  40,
                                  0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                  mem[204 len 24]
                  if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                      revert with 0, 'ds-math-add-overflow'
                  totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                  if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                      revert with 0, 'ds-math-add-overflow'
                  balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                  log Transfer(
                        address from=((ext_call.return_data
                        address to=0,
                        uint256 tokens=_to)
                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                      revert with 0, 'UniswapV2: OVERFLOW'
                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                      revert with 0, 'UniswapV2: OVERFLOW'
                  if uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                      if Mask(112, 0, stor8.field_0):
                          if Mask(112, 0, stor8.field_112):
                              require Mask(112, 0, stor8.field_0)
                              unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                              require Mask(112, 0, stor8.field_112)
                              unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                  uint32(stor8.field_224) = uint32(block.timestamp)
                  log 0x1c411e9a: ext_call.return_data
                  if addr(ext_call.return_data):
                      if not Mask(112, 0, stor8.field_112):
                          unknown7464fc3d = 0
                      else:
                          require Mask(112, 0, stor8.field_112)
                          if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
              if 0 / Mask(112, 0, stor8.field_112) <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                              mem[204 len 24]
              if totalSupply + (0 / Mask(112, 0, stor8.field_112)) < totalSupply:
                  revert with 0, 'ds-math-add-overflow'
              totalSupply += 0 / Mask(112, 0, stor8.field_112)
              if balanceOf[addr(_to)] + (0 / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                  revert with 0, 'ds-math-add-overflow'
              balanceOf[addr(_to)] += 0 / Mask(112, 0, stor8.field_112)
              log Transfer(
                    address from=(0 / Mask(112, 0, stor8.field_112)),
                    address to=0,
                    uint256 tokens=_to)
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                  if Mask(112, 0, stor8.field_0):
                      if Mask(112, 0, stor8.field_112):
                          require Mask(112, 0, stor8.field_0)
                          unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                          require Mask(112, 0, stor8.field_112)
                          unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return (0 / Mask(112, 0, stor8.field_112))
          require totalSupply
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / totalSupply != ext_call.return_datastor8.field_112):
              revert with 0, 'ds-math-mul-overflow'
          require Mask(112, 0, stor8.field_112)
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112):
              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                              mem[204 len 24]
              if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                  revert with 0, 'ds-math-add-overflow'
              totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
              if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                  revert with 0, 'ds-math-add-overflow'
              balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
              log Transfer(
                    address from=((ext_call.return_data
                    address to=0,
                    uint256 tokens=_to)
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                  uint32(stor8.field_224) = uint32(block.timestamp)
                  log 0x1c411e9a: ext_call.return_data
                  if addr(ext_call.return_data):
                      if not Mask(112, 0, stor8.field_112):
                          unknown7464fc3d = 0
                      else:
                          require Mask(112, 0, stor8.field_112)
                          if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
              if not Mask(112, 0, stor8.field_0):
                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                  uint32(stor8.field_224) = uint32(block.timestamp)
                  log 0x1c411e9a: ext_call.return_data
                  if addr(ext_call.return_data):
                      if not Mask(112, 0, stor8.field_112):
                          unknown7464fc3d = 0
                      else:
                          require Mask(112, 0, stor8.field_112)
                          if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
              if not Mask(112, 0, stor8.field_112):
                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                  uint32(stor8.field_224) = uint32(block.timestamp)
                  log 0x1c411e9a: ext_call.return_data
                  if addr(ext_call.return_data):
                      if not Mask(112, 0, stor8.field_112):
                          unknown7464fc3d = 0
                      else:
                          require Mask(112, 0, stor8.field_112)
                          if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
              require Mask(112, 0, stor8.field_0)
              unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
              require Mask(112, 0, stor8.field_112)
              unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if not addr(ext_call.return_data):
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
              if not Mask(112, 0, stor8.field_112):
                  unknown7464fc3d = 0
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
          else:
              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112) <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                              mem[204 len 24]
              if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < totalSupply:
                  revert with 0, 'ds-math-add-overflow'
              totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
              if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                  revert with 0, 'ds-math-add-overflow'
              balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
              log Transfer(
                    address from=((ext_call.return_data
                    address to=0,
                    uint256 tokens=_to)
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                  uint32(stor8.field_224) = uint32(block.timestamp)
                  log 0x1c411e9a: ext_call.return_data
                  if addr(ext_call.return_data):
                      if not Mask(112, 0, stor8.field_112):
                          unknown7464fc3d = 0
                      else:
                          require Mask(112, 0, stor8.field_112)
                          if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
              if not Mask(112, 0, stor8.field_0):
                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                  uint32(stor8.field_224) = uint32(block.timestamp)
                  log 0x1c411e9a: ext_call.return_data
                  if addr(ext_call.return_data):
                      if not Mask(112, 0, stor8.field_112):
                          unknown7464fc3d = 0
                      else:
                          require Mask(112, 0, stor8.field_112)
                          if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
              if not Mask(112, 0, stor8.field_112):
                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                  uint32(stor8.field_224) = uint32(block.timestamp)
                  log 0x1c411e9a: ext_call.return_data
                  if addr(ext_call.return_data):
                      if not Mask(112, 0, stor8.field_112):
                          unknown7464fc3d = 0
                      else:
                          require Mask(112, 0, stor8.field_112)
                          if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
              require Mask(112, 0, stor8.field_0)
              unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
              require Mask(112, 0, stor8.field_112)
              unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if not addr(ext_call.return_data):
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
              if not Mask(112, 0, stor8.field_112):
                  unknown7464fc3d = 0
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
          ('bool', ('type', 112, ('field', 112, ('stor', ('name', 'stor8', 8)))))
          require Mask(112, 0, stor8.field_112)
          if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
              revert with 0, 'ds-math-mul-overflow'
          unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
          log Mint(
                address owner=ext_call.return_data
                uint256 newTokenId=ext_call.return_data
                uint256 genes=caller)
          stor12 = 1
  else:
      if not unknown7464fc3d:
          if not totalSupply:
              if ext_call.return_datastor8.field_112):
                  require ext_call.return_datastor8.field_112)
                  if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / ext_call.return_datastor8.field_112) != ext_call.return_datastor8.field_0):
                      revert with 0, 'ds-math-mul-overflow'
                  if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) > 3:
                      ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
              revert with 0, 'ds-math-sub-underflow'
          require totalSupply
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / totalSupply != ext_call.return_datastor8.field_0):
              revert with 0, 'ds-math-mul-overflow'
          require Mask(112, 0, stor8.field_0)
          if not totalSupply:
              require Mask(112, 0, stor8.field_112)
              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < 0 / Mask(112, 0, stor8.field_112):
                  if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  40,
                                  0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                                  mem[204 len 24]
                  if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                      revert with 0, 'ds-math-add-overflow'
                  totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                  if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                      revert with 0, 'ds-math-add-overflow'
                  balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
                  log Transfer(
                        address from=((ext_call.return_data
                        address to=0,
                        uint256 tokens=_to)
                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                      revert with 0, 'UniswapV2: OVERFLOW'
                  if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                      revert with 0, 'UniswapV2: OVERFLOW'
                  if uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                      if Mask(112, 0, stor8.field_0):
                          if Mask(112, 0, stor8.field_112):
                              require Mask(112, 0, stor8.field_0)
                              unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                              require Mask(112, 0, stor8.field_112)
                              unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                  Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
                  Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
                  uint32(stor8.field_224) = uint32(block.timestamp)
                  log 0x1c411e9a: ext_call.return_data
                  if addr(ext_call.return_data):
                      if not Mask(112, 0, stor8.field_112):
                          unknown7464fc3d = 0
                      else:
                          require Mask(112, 0, stor8.field_112)
                          if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                              revert with 0, 'ds-math-mul-overflow'
                          unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
                  log Mint(
                        address owner=ext_call.return_data
                        uint256 newTokenId=ext_call.return_data
                        uint256 genes=caller)
                  stor12 = 1
                  return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
              if 0 / Mask(112, 0, stor8.field_112) <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                              mem[204 len 24]
              if totalSupply + (0 / Mask(112, 0, stor8.field_112)) < totalSupply:
                  revert with 0, 'ds-math-add-overflow'
              totalSupply += 0 / Mask(112, 0, stor8.field_112)
              if balanceOf[addr(_to)] + (0 / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
                  revert with 0, 'ds-math-add-overflow'
              balanceOf[addr(_to)] += 0 / Mask(112, 0, stor8.field_112)
              log Transfer(
                    address from=(0 / Mask(112, 0, stor8.field_112)),
                    address to=0,
                    uint256 tokens=_to)
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                  if Mask(112, 0, stor8.field_0):
                      if Mask(112, 0, stor8.field_112):
                          require Mask(112, 0, stor8.field_0)
                          unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                          require Mask(112, 0, stor8.field_112)
                          unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return (0 / Mask(112, 0, stor8.field_112))
          require totalSupply
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / totalSupply != ext_call.return_datastor8.field_112):
              revert with 0, 'ds-math-mul-overflow'
          require Mask(112, 0, stor8.field_112)
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112):
              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                              mem[204 len 24]
              if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                  revert with 0, 'ds-math-add-overflow'
              totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
              if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                  revert with 0, 'ds-math-add-overflow'
              balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
              log Transfer(
                    address from=((ext_call.return_data
                    address to=0,
                    uint256 tokens=_to)
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                  if Mask(112, 0, stor8.field_0):
                      if Mask(112, 0, stor8.field_112):
                          require Mask(112, 0, stor8.field_0)
                          unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                          require Mask(112, 0, stor8.field_112)
                          unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112) <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          40,
                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                          mem[204 len 24]
          if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < totalSupply:
              revert with 0, 'ds-math-add-overflow'
          totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
          if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
              revert with 0, 'ds-math-add-overflow'
          balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
          log Transfer(
                address from=((ext_call.return_data
                address to=0,
                uint256 tokens=_to)
          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
              revert with 0, 'UniswapV2: OVERFLOW'
          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
              revert with 0, 'UniswapV2: OVERFLOW'
          if uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
              if Mask(112, 0, stor8.field_0):
                  if Mask(112, 0, stor8.field_112):
                      require Mask(112, 0, stor8.field_0)
                      unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                      require Mask(112, 0, stor8.field_112)
                      unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
          uint32(stor8.field_224) = uint32(block.timestamp)
          log 0x1c411e9a: ext_call.return_data
          if addr(ext_call.return_data):
              if not Mask(112, 0, stor8.field_112):
                  unknown7464fc3d = 0
              else:
                  require Mask(112, 0, stor8.field_112)
                  if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                      revert with 0, 'ds-math-mul-overflow'
                  unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
          log Mint(
                address owner=ext_call.return_data
                uint256 newTokenId=ext_call.return_data
                uint256 genes=caller)
          stor12 = 1
          return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
      unknown7464fc3d = 0
      if not totalSupply:
          if ext_call.return_datastor8.field_112):
              require ext_call.return_datastor8.field_112)
              if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) / ext_call.return_datastor8.field_112) != ext_call.return_datastor8.field_0):
                  revert with 0, 'ds-math-mul-overflow'
              if (ext_call.return_data * ext_call.return_datastor8.field_112) * ext_call.return_data * Mask(112, 0, stor8.field_0)) + (Mask(112, 0, stor8.field_112) * Mask(112, 0, stor8.field_0)) > 3:
                  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)
          revert with 0, 'ds-math-sub-underflow'
      require totalSupply
      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / totalSupply != ext_call.return_datastor8.field_0):
          revert with 0, 'ds-math-mul-overflow'
      require Mask(112, 0, stor8.field_0)
      if not totalSupply:
          require Mask(112, 0, stor8.field_112)
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < 0 / Mask(112, 0, stor8.field_112):
              if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              40,
                              0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                              mem[204 len 24]
              if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
                  revert with 0, 'ds-math-add-overflow'
              totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
              if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
                  revert with 0, 'ds-math-add-overflow'
              balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
              log Transfer(
                    address from=((ext_call.return_data
                    address to=0,
                    uint256 tokens=_to)
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if ext_call.return_data > 0xffffffffffffffffffffffffffff:
                  revert with 0, 'UniswapV2: OVERFLOW'
              if uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
                  if Mask(112, 0, stor8.field_0):
                      if Mask(112, 0, stor8.field_112):
                          require Mask(112, 0, stor8.field_0)
                          unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                          require Mask(112, 0, stor8.field_112)
                          unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
          if 0 / Mask(112, 0, stor8.field_112) <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          40,
                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                          mem[204 len 24]
          if totalSupply + (0 / Mask(112, 0, stor8.field_112)) < totalSupply:
              revert with 0, 'ds-math-add-overflow'
          totalSupply += 0 / Mask(112, 0, stor8.field_112)
          if balanceOf[addr(_to)] + (0 / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
              revert with 0, 'ds-math-add-overflow'
          balanceOf[addr(_to)] += 0 / Mask(112, 0, stor8.field_112)
          log Transfer(
                address from=(0 / Mask(112, 0, stor8.field_112)),
                address to=0,
                uint256 tokens=_to)
          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
              revert with 0, 'UniswapV2: OVERFLOW'
          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
              revert with 0, 'UniswapV2: OVERFLOW'
          if uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
              if Mask(112, 0, stor8.field_0):
                  if Mask(112, 0, stor8.field_112):
                      require Mask(112, 0, stor8.field_0)
                      unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
                      require Mask(112, 0, stor8.field_112)
                      unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
          uint32(stor8.field_224) = uint32(block.timestamp)
          log 0x1c411e9a: ext_call.return_data
          if addr(ext_call.return_data):
              if not Mask(112, 0, stor8.field_112):
                  unknown7464fc3d = 0
              else:
                  require Mask(112, 0, stor8.field_112)
                  if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                      revert with 0, 'ds-math-mul-overflow'
                  unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
          log Mint(
                address owner=ext_call.return_data
                uint256 newTokenId=ext_call.return_data
                uint256 genes=caller)
          stor12 = 1
          return (0 / Mask(112, 0, stor8.field_112))
      require totalSupply
      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / totalSupply != ext_call.return_datastor8.field_112):
          revert with 0, 'ds-math-mul-overflow'
      require Mask(112, 0, stor8.field_112)
      if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) < (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112):
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0) <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          40,
                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                          mem[204 len 24]
          if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < totalSupply:
              revert with 0, 'ds-math-add-overflow'
          totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
          if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)) < balanceOf[addr(_to)]:
              revert with 0, 'ds-math-add-overflow'
          balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0)
          log Transfer(
                address from=((ext_call.return_data
                address to=0,
                uint256 tokens=_to)
          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
              revert with 0, 'UniswapV2: OVERFLOW'
          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
              revert with 0, 'UniswapV2: OVERFLOW'
          if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
          if not Mask(112, 0, stor8.field_0):
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
          if not Mask(112, 0, stor8.field_112):
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
          require Mask(112, 0, stor8.field_0)
          unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
          require Mask(112, 0, stor8.field_112)
          unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
          uint32(stor8.field_224) = uint32(block.timestamp)
          log 0x1c411e9a: ext_call.return_data
          if not addr(ext_call.return_data):
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
          if not Mask(112, 0, stor8.field_112):
              unknown7464fc3d = 0
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_0) * totalSupply) / Mask(112, 0, stor8.field_0))
      else:
          if (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112) <= 0:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          40,
                          0x44556e697377617056323a20494e53554646494349454e545f4c49515549444954595f4d494e5445,
                          mem[204 len 24]
          if totalSupply + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < totalSupply:
              revert with 0, 'ds-math-add-overflow'
          totalSupply += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
          if balanceOf[addr(_to)] + ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)) < balanceOf[addr(_to)]:
              revert with 0, 'ds-math-add-overflow'
          balanceOf[addr(_to)] += (ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112)
          log Transfer(
                address from=((ext_call.return_data
                address to=0,
                uint256 tokens=_to)
          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
              revert with 0, 'UniswapV2: OVERFLOW'
          if ext_call.return_data > 0xffffffffffffffffffffffffffff:
              revert with 0, 'UniswapV2: OVERFLOW'
          if not uint32(uint32(block.timestamp) - uint32(stor8.field_224)):
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
          if not Mask(112, 0, stor8.field_0):
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
          if not Mask(112, 0, stor8.field_112):
              Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
              Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
              uint32(stor8.field_224) = uint32(block.timestamp)
              log 0x1c411e9a: ext_call.return_data
              if addr(ext_call.return_data):
                  if not Mask(112, 0, stor8.field_112):
                      unknown7464fc3d = 0
                  else:
                      require Mask(112, 0, stor8.field_112)
                      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
                          revert with 0, 'ds-math-mul-overflow'
                      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
          require Mask(112, 0, stor8.field_0)
          unknown5909c0d5 += Mask(224, 0, Mask(112, 0, Mask(112, 0, stor8.field_112)) << 112 / Mask(112, 0, stor8.field_0)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
          require Mask(112, 0, stor8.field_112)
          unknown5a3d5493 += Mask(224, 0, Mask(112, 0, stor8.field_0) / Mask(112, 0, stor8.field_112)) * uint32(uint32(block.timestamp) - uint32(stor8.field_224))
          Mask(112, 0, stor8.field_0) = Mask(112, 0, ext_call.return_data[0])
          Mask(112, 0, stor8.field_112) = Mask(112, 0, ext_call.return_data[0])
          uint32(stor8.field_224) = uint32(block.timestamp)
          log 0x1c411e9a: ext_call.return_data
          if not addr(ext_call.return_data):
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
          if not Mask(112, 0, stor8.field_112):
              unknown7464fc3d = 0
              log Mint(
                    address owner=ext_call.return_data
                    uint256 newTokenId=ext_call.return_data
                    uint256 genes=caller)
              stor12 = 1
              return ((ext_call.return_data * totalSupply) - (Mask(112, 0, stor8.field_112) * totalSupply) / Mask(112, 0, stor8.field_112))
      ('bool', ('type', 112, ('field', 112, ('stor', ('name', 'stor8', 8)))))
      require Mask(112, 0, stor8.field_112)
      if Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112) / Mask(112, 0, stor8.field_112) != Mask(112, 0, stor8.field_0):
          revert with 0, 'ds-math-mul-overflow'
      unknown7464fc3d = Mask(112, 0, stor8.field_0) * Mask(112, 0, stor8.field_112)
      log Mint(
            address owner=ext_call.return_data
            uint256 newTokenId=ext_call.return_data
            uint256 genes=caller)
      stor12 = 1
  ...  # Decompilation aborted, sorry: ("decompilation didn't finish",)


