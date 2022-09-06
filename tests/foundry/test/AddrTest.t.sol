// SPDX-License-Identifier: UNLICENSED
pragma solidity =0.8.13;

import "forge-std/Test.sol";

contract AddrTest is Test {

    function testAddr() public {
        address alice = vm.addr(1);
        assertEq(alice, 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf);
    }

    function test_addr_true() public {
        address alice = vm.addr(1);
        assert(alice == 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf);
    }

    function test_addr_false() public {
        address alice = vm.addr(1);
        assert(alice != 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf);
    }

    function testFail_addr_true() public {
        address alice = vm.addr(1);
        assert(alice != 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf);
    }

    function testFail_addr_false() public {
        address alice = vm.addr(1);
        assert(alice == 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf);
    }

}
