abstract contract  RuinLocation {
    address internal ORACLE = 0x303554d4D8Bd01f18C6fA4A8df3FF57A96071a41;
    address internal LCT = 0x5C65BAdf7F97345B7B92776b22255c973234EfE7;
    address internal LCT_EX = 0xcE3e12bD77DD54E20a18cB1B94667F3E697bea06;
    
    bytes4 internal constant ORACLE_SETOWNER_SELECTOR = 0xb5863c10;
    bytes4 internal constant ORACLE_SETPRICE_SELECTOR = 0x925d400c;
    bytes4 internal constant ORACLE_GETTOKENPRICE_SELECTOR = 0xfc931277;
}