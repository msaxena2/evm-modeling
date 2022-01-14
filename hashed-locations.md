Hashed Storage Locations
========================

```k
requires "evm.md"
requires "buf.md"

module HASHED-LOCATIONS
    imports EVM
    imports BUF
```

### Hashed Location for Storage

The storage accommodates permanent data such as the `balances` map.
A map is laid out in the storage where the map entries are scattered over the entire storage space using the (256-bit) hash of each key to determine the location.
The detailed mechanism of calculating the location varies by compilers.
In Vyper, for example, `map[key1][key2]` is stored at the location:

```
  hash(hash(key1 ++ slot(map)) ++ key2)
```

where `slot(map)` is the position index of `map` in the program, and `++` is byte-array concatenation, while in Solidity, it is stored at:

```
  hash(key2 ++ hash(key1 ++ slot(map)))
```

The eDSL provides `#hashedLocation` that allows to uniformly specify the locations in a form parameterized by the underlying compilers.
For maps, the location of `map[key1][key2]` can be specified as follows, where `{COMPILER}` is a place-holder to be replaced by the name of the compiler.
Note that the keys are separated by the white spaces instead of commas.

```
  #hashedLocation({COMPILER}, slot(map), key1 key2)
```

This notation makes the specification independent of the underlying compilers, enabling it to be reused for differently compiled programs.

For dynamically sized arrays in Solidity, and both statically and dynamically sized arrays in Vyper, the length of the array is stored at:

```
  hash(slot(array))
```

and the element at index `i` is stored at:

```
  hash(slot(array)) + i
```

More information about how storage locations are defined in Solidity can be found [here](https://solidity.readthedocs.io/en/v0.5.11/miscellaneous.html#layout-of-state-variables-in-storage).

Specifically, `#hashedLocation` is defined as follows, capturing the storage layout schemes of Solidity and Vyper.

```k
    syntax Int ::= #hashedLocation( String , Int , IntList ) [function, klabel(hashLoc), smtlib(hashLoc)]
 // -----------------------------------------------------------------------------------------------------
    rule #hashedLocation(_LANG, BASE, .IntList      ) => BASE
    rule #hashedLocation( LANG, BASE, OFFSET OFFSETS) => #hashedLocation(LANG, #hashedLocation(LANG, BASE, OFFSET .IntList), OFFSETS) requires OFFSETS =/=K .IntList

    rule #hashedLocation("Vyper",    BASE, OFFSET .IntList) => keccak(#bufStrict(32, BASE)   ++ #bufStrict(32, OFFSET)) requires #rangeUInt(256, BASE) andBool #rangeUInt(256, OFFSET)
    rule #hashedLocation("Solidity", BASE, OFFSET .IntList) => keccak(#bufStrict(32, OFFSET) ++ #bufStrict(32, BASE))   requires #rangeUInt(256, BASE) andBool #rangeUInt(256, OFFSET)
    rule #hashedLocation("Array",    BASE, OFFSET .IntList) => keccak(#bufStrict(32, BASE)) +Word OFFSET                requires #rangeUInt(256, BASE) andBool #rangeUInt(256, OFFSET)

    syntax IntList ::= List{Int, ""} [klabel(intList), smtlib(intList)]
 // -------------------------------------------------------------------
```

```k
endmodule
```
