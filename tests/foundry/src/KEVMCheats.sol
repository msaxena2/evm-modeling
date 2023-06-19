// SPDX-License-Identifier: MIT
pragma solidity >=0.6.2 <0.9.0;
pragma experimental ABIEncoderV2;

interface KEVMCheatsBase {
    // Expects a call using the CALL opcode to an address with the specified calldata.
    function expectRegularCall(address,bytes calldata) external;
    // Expects a call using the CALL opcode to an address with the specified msg.value and calldata.
    function expectRegularCall(address,uint256,bytes calldata) external;
    // Expects a static call to an address with the specified calldata.
    function expectStaticCall(address,bytes calldata) external;
    // Expects a delegate call to an address with the specified calldata.
    function expectDelegateCall(address,bytes calldata) external;
    // Expects that no contract calls are made after invoking the cheatcode.
    function expectNoCall() external;
    // Expects the given address to deploy a new contract, using the CREATE opcode, with the specified value and bytecode.
    function expectCreate(address,uint256,bytes calldata) external;
    // Expects the given address to deploy a new contract, using the CREATE2 opcode, with the specified value and bytecode (appended with a bytes32 salt).
    function expectCreate2(address,uint256,bytes calldata) external;
    // Makes the storage of the given address completely symbolic.
    function symbolicStorage(address) external;
    // Adds an address to the whitelist.
    function allowCallsToAddress(address) external;
    // Adds an address and a storage slot to the whitelist.
    function allowChangesToStorage(address,uint256) external;
    // Set the current <gas> cell
    function infiniteGas() external;
    // Returns a symbolic unsigned integer
    function freshUInt(uint8) external returns (uint256);
    // Returns a symbolic signed integer
    function freshSInt(uint8) external returns (int256);
    // Returns a symbolic boolean value
    function freshBool() external returns (bool);
}

abstract contract SymbolicWords {
    address internal constant KEVM_CHEATS = address(uint160(uint256(keccak256("hevm cheat code"))));

    KEVMCheatsBase internal constant kevm = KEVMCheatsBase(KEVM_CHEATS);

    function freshUInt256() external returns (uint256) {
        return kevm.freshUInt(32);
    }

    function freshUInt248() external returns (uint248) {
        return uint248(kevm.freshUInt(31));
    }

    function freshUInt240() external returns (uint240) {
        return uint240(kevm.freshUInt(30));
    }

    function freshUInt232() external returns (uint232) {
        return uint232(kevm.freshUInt(29));
    }

    function freshUInt224() external returns (uint224) {
        return uint224(kevm.freshUInt(28));
    }

    function freshUInt216() external returns (uint216) {
        return uint216(kevm.freshUInt(27));
    }

    function freshUInt208() external returns (uint208) {
        return uint208(kevm.freshUInt(26));
    }

    function freshUInt200() external returns (uint200) {
        return uint200(kevm.freshUInt(25));
    }

    function freshUInt192() external returns (uint192) {
        return uint192(kevm.freshUInt(24));
    }

    function freshUInt184() external returns (uint184) {
        return uint184(kevm.freshUInt(23));
    }

    function freshUInt176() external returns (uint176) {
        return uint176(kevm.freshUInt(22));
    }

    function freshUInt168() external returns (uint168) {
        return uint168(kevm.freshUInt(21));
    }

    function freshUInt160() external returns (uint160) {
        return uint160(kevm.freshUInt(20));
    }

    function freshUInt152() external returns (uint152) {
        return uint152(kevm.freshUInt(19));
    }

    function freshUInt144() external returns (uint144) {
        return uint144(kevm.freshUInt(18));
    }

    function freshUInt136() external returns (uint136) {
        return uint136(kevm.freshUInt(17));
    }

    function freshUInt128() external returns (uint128) {
        return uint128(kevm.freshUInt(16));
    }

    function freshUInt120() external returns (uint120) {
        return uint120(kevm.freshUInt(15));
    }

    function freshUInt112() external returns (uint112) {
        return uint112(kevm.freshUInt(14));
    }

    function freshUInt104() external returns (uint104) {
        return uint104(kevm.freshUInt(13));
    }

    function freshUInt96() external returns (uint96) {
        return uint96(kevm.freshUInt(12));
    }

    function freshUInt88() external returns (uint88) {
        return uint88(kevm.freshUInt(11));
    }

    function freshUInt80() external returns (uint80) {
        return uint80(kevm.freshUInt(10));
    }

    function freshUInt72() external returns (uint72) {
        return uint72(kevm.freshUInt(9));
    }

    function freshUInt64() external returns (uint64) {
        return uint64(kevm.freshUInt(8));
    }

    function freshUInt56() external returns (uint56) {
        return uint56(kevm.freshUInt(7));
    }

    function freshUInt48() external returns (uint48) {
        return uint48(kevm.freshUInt(6));
    }

    function freshUInt40() external returns (uint40) {
        return uint40(kevm.freshUInt(5));
    }

    function freshUInt32() external returns (uint32) {
        return uint32(kevm.freshUInt(4));
    }

    function freshUInt24() external returns (uint24) {
        return uint24(kevm.freshUInt(3));
    }

    function freshUInt16() external returns (uint16) {
        return uint16(kevm.freshUInt(2));
    }

    function freshUInt8() external returns (uint8) {
        return uint8(kevm.freshUInt(1));
    }

    function freshAddress() external returns (address) {
        return address(uint160(kevm.freshUInt(20)));
    }

    function freshBool() external returns (bool) {
        return kevm.freshBool();
    }

    function freshSInt256() external returns (int256) {
        return kevm.freshSInt(32);
    }
}

abstract contract KEVMUtils {
    // @notice Checks if an address matches one of the built-in addresses.
    function notBuiltinAddress(address addr) internal pure returns (bool) {
        return (addr != address(645326474426547203313410069153905908525362434349) &&
                addr != address(728815563385977040452943777879061427756277306518));
    }
}

abstract contract KEVMBase {
    address internal constant KEVM_CHEATS = address(uint160(uint256(keccak256("hevm cheat code"))));

    KEVMCheatsBase internal constant kevm = KEVMCheatsBase(KEVM_CHEATS);
}

abstract contract KEVMCheats is KEVMBase, KEVMUtils {}
