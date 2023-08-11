abstract contract  RuinLocation {
    address internal constant MEV_BOT = 0x8DB0eFEE6A7622CD9F46A2CF1aEdC8505341A1a7;
    address internal constant MEV_BOT_IMPL = 0xd614927AcFB9744441180c2525faf4cEdB70207f;
    bytes internal constant CALLDATA_512b7351 = hex"512b73510000000000000000000000008db0efee6a7622cd9f46a2cf1aedc8505341a1a7000000000000000000000000912ce59144191c1204e64559fe8253a0e49e6548000000000000000000000000000000000000000000000004ff587a043dd62a4000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000010000000000000000000930c3aca019d2f311dd4b2ad2eede5bb1933661000004000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000180000000000000000005f39ee8000000000000000000000000000000000174d1020000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c9b8a3fdecb9d5b218d02555a8baf332e5b740d59ea522292ed9e3cc345bac4fbdbc199e638f8ad00000000000402000000640cb00000000000000000000000000000000000000005e0d443fddc1f59d040004010000000000000000000000000000000000000000000053612a88be542fc54323000000000000000000000000489ee077994b6658eafa855c308275ead8097c4a9ea522292ed9e3cc345bac4fbdbc199e638f8ad00000000000604400000000930000000000000000000000000000000000000000000000000000000500010612000000000000000000000000000000000000000000000004ff587a043dd62a400000000000000000000000000000000000000000000000000000000000000003000000000000000000000000f1970a61a04b1ca14834a43f5de4533ebddb5cc80000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc0000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc";

    address internal constant MAI_USDC_POOL = 0x6976f5Fe2791B31bF64C0e7Ace807c9299D3863A;
    address internal constant CORRELATED_RAMM_MAI_USDC_POOL = 0x3c6eF5Ed8ad5DF0d5e3D05C6e607c60F987fB735;
    address internal constant MAI = 0x3F56e0c36d275367b8C502090EDF38289b3dEa0d;
}

// ARB
// 0x0000000000000000000000008db0efee6a7622cd9f46a2cf1aedc8505341a1a7000000000000000000000000912ce59144191c1204e64559fe8253a0e49e6548000000000000000000000000000000000000000000000004ff587a043dd62a4000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000010000000000000000000930c3aca019d2f311dd4b2ad2eede5bb1933661000004000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000180000000000000000005f39ee8000000000000000000000000000000000174d1020000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c9b8a3fdecb9d5b218d02555a8baf332e5b740d59ea522292ed9e3cc345bac4fbdbc199e638f8ad00000000000402000000640cb00000000000000000000000000000000000000005e0d443fddc1f59d040004010000000000000000000000000000000000000000000053612a88be542fc54323000000000000000000000000489ee077994b6658eafa855c308275ead8097c4a9ea522292ed9e3cc345bac4fbdbc199e638f8ad00000000000604400000000930000000000000000000000000000000000000000000000000000000500010612000000000000000000000000000000000000000000000004ff587a043dd62a400000000000000000000000000000000000000000000000000000000000000003000000000000000000000000f1970a61a04b1ca14834a43f5de4533ebddb5cc80000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc0000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc
// Method: 512b7351
// ------------
// [000]: 0000000000000000000000008db0efee6a7622cd9f46a2cf1aedc8505341a1a7
// [020]: 000000000000000000000000912ce59144191c1204e64559fe8253a0e49e6548
// [040]: 000000000000000000000000000000000000000000000004ff587a043dd62a40
// [060]: 00000000000000000000000000000000000000000000000000000000000000a0
// [080]: 00000000000000000000000000000000000000000000000000000000000000e0
// [0a0]: 0000000000000000000000000000000000000000000000000000000000000001
// [0c0]: 0000000000000000000930c3aca019d2f311dd4b2ad2eede5bb1933661000004
// [0e0]: 0000000000000000000000000000000000000000000000000000000000000200
// [100]: 0000000000000000000000000000000000000000000000000000000000000060
// [120]: 0000000000000000000000000000000000000000000000000000000000000180
// [140]: 000000000000000005f39ee8000000000000000000000000000000000174d102
// [160]: 0000000000000000000000000000000000000000000000000000000000000002
// [180]: 000000000000000000000000c9b8a3fdecb9d5b218d02555a8baf332e5b740d5
// [1a0]: 9ea522292ed9e3cc345bac4fbdbc199e638f8ad00000000000402000000640cb
// [1c0]: 00000000000000000000000000000000000000005e0d443fddc1f59d04000401
// [1e0]: 0000000000000000000000000000000000000000000053612a88be542fc54323
// [200]: 000000000000000000000000489ee077994b6658eafa855c308275ead8097c4a
// [220]: 9ea522292ed9e3cc345bac4fbdbc199e638f8ad0000000000060440000000093
// [240]: 0000000000000000000000000000000000000000000000000000000500010612
// [260]: 000000000000000000000000000000000000000000000004ff587a043dd62a40
// [280]: 0000000000000000000000000000000000000000000000000000000000000003
// [2a0]: 000000000000000000000000f1970a61a04b1ca14834a43f5de4533ebddb5cc8
// [2c0]: 0000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc
// [2e0]: 0000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc

// WETH:
// 0x512b73510000000000000000000000008db0efee6a7622cd9f46a2cf1aedc8505341a1a700000000000000000000000082af49447d8a07e3bd95bd0d56f35241523fbab100000000000000000000000000000000000000000000000cb87c8e89d4e6fb8600000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000010000000000000000000930c3aca019d2f311dd4b2ad2eede5bb1933661000004000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000180000000000000000005f39ee8000000000000000000000000000000000174d1020000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c9b8a3fdecb9d5b218d02555a8baf332e5b740d59ea522292ed9e3cc345bac4fbdbc199e638f8ad00000000000402000000640cb00000000000000000000000000000000000000005e0d443fddc1f59d040004010000000000000000000000000000000000000000000053612a88be542fc54323000000000000000000000000489ee077994b6658eafa855c308275ead8097c4a9ea522292ed9e3cc345bac4fbdbc199e638f8ad0000000000060440000000093000000000000000000000000000000000000000000000000000000050001061200000000000000000000000000000000000000000000000cb87c8e89d4e6fb860000000000000000000000000000000000000000000000000000000000000003000000000000000000000000f1970a61a04b1ca14834a43f5de4533ebddb5cc80000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc0000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc
// Method: 512b7351
// ------------
// [000]: 0000000000000000000000008db0efee6a7622cd9f46a2cf1aedc8505341a1a7
// [020]: 00000000000000000000000082af49447d8a07e3bd95bd0d56f35241523fbab1
// [040]: 00000000000000000000000000000000000000000000000cb87c8e89d4e6fb86
// [060]: 00000000000000000000000000000000000000000000000000000000000000a0
// [080]: 00000000000000000000000000000000000000000000000000000000000000e0
// [0a0]: 0000000000000000000000000000000000000000000000000000000000000001
// [0c0]: 0000000000000000000930c3aca019d2f311dd4b2ad2eede5bb1933661000004
// [0e0]: 0000000000000000000000000000000000000000000000000000000000000200
// [100]: 0000000000000000000000000000000000000000000000000000000000000060
// [120]: 0000000000000000000000000000000000000000000000000000000000000180
// [140]: 000000000000000005f39ee8000000000000000000000000000000000174d102
// [160]: 0000000000000000000000000000000000000000000000000000000000000002
// [180]: 000000000000000000000000c9b8a3fdecb9d5b218d02555a8baf332e5b740d5
// [1a0]: 9ea522292ed9e3cc345bac4fbdbc199e638f8ad00000000000402000000640cb
// [1c0]: 00000000000000000000000000000000000000005e0d443fddc1f59d04000401
// [1e0]: 0000000000000000000000000000000000000000000053612a88be542fc54323
// [200]: 000000000000000000000000489ee077994b6658eafa855c308275ead8097c4a
// [220]: 9ea522292ed9e3cc345bac4fbdbc199e638f8ad0000000000060440000000093
// [240]: 0000000000000000000000000000000000000000000000000000000500010612
// [260]: 00000000000000000000000000000000000000000000000cb87c8e89d4e6fb86
// [280]: 0000000000000000000000000000000000000000000000000000000000000003
// [2a0]: 000000000000000000000000f1970a61a04b1ca14834a43f5de4533ebddb5cc8
// [2c0]: 0000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc
// [2e0]: 0000000000000000000000001270e7694d38f3f80e0e033703c1272a80b914fc