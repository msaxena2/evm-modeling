ERC20-ish Verification
======================

```k
requires "edsl.md"
requires "optimizations.md"
requires "lemmas/lemmas.k"
requires "lemmas/infinite-gas.k"
```

Solidity Code
-------------

File [`ERC20.sol`](ERC20.sol) contains some code snippets we want to verify the functional correctness of.
Call `kevm solc ERC20.sol ERC20 > erc20-bin-runtime.k`, to generate the helper K files.

Verification Module
-------------------

Helper module for verification tasks.

-   Add any lemmas needed for our proofs.
-   Import a large body of existing lemmas from KEVM.

```k
requires "erc20-bin-runtime.k"

module VERIFICATION
    imports EDSL
    imports LEMMAS
    imports INFINITE-GAS
    imports EVM-OPTIMIZATIONS
    imports ERC20-BIN-RUNTIME

    syntax Step ::= ByteArray | Int
    syntax KItem ::= runLemma ( Step ) | doneLemma ( Step )
 // -------------------------------------------------------
    rule <k> runLemma(S) => doneLemma(S) ... </k>

 // decimals lemmas
 // ---------------

    rule         255 &Int X <Int 256 => true requires 0 <=Int X [simplification, smt-lemma]
    rule 0 <=Int 255 &Int X          => true requires 0 <=Int X [simplification, smt-lemma]

endmodule
```

K Specifications
----------------

Formal specifications (using KEVM) of the correctness properties for our Solidity code.

```k
module ERC20-SPEC
    imports VERIFICATION
```

### Calling decimals() works

-   Everything from `<mode>` to `<callValue>` is boilerplate.
-   We are setting `<callData>` to `decimals()`.
-   We ask the prover to show that in all cases, we will end in `EVMC_SUCCESS` (rollback) when this happens.
-   The `<output>` cell specifies that we correctly lookup the `DECIMALS` value from the account storage.

```k
    claim [decimals]:
          <mode>     NORMAL   </mode>
          <schedule> ISTANBUL </schedule>

          <callStack> .List                                      </callStack>
          <program>   #binRuntime(ERC20)                         </program>
          <jumpDests> #computeValidJumpDests(#binRuntime(ERC20)) </jumpDests>

          <id>         ACCTID      => ?_ </id>
          <localMem>   .Memory     => ?_ </localMem>
          <memoryUsed> 0           => ?_ </memoryUsed>
          <wordStack>  .WordStack  => ?_ </wordStack>
          <pc>         0           => ?_ </pc>
          <endPC>      _           => ?_ </endPC>
          <gas>        #gas(_VGAS) => ?_ </gas>
          <callValue>  0           => ?_ </callValue>

          <callData> #abiCallData("decimals", .TypedArgs) </callData>
          <k>          #execute   => #halt ...            </k>
          <output>     .ByteArray => #buf(32, DECIMALS)   </output>
          <statusCode> _          => EVMC_SUCCESS         </statusCode>

          <account>
            <acctID> ACCTID </acctID>
            <storage> ACCT_STORAGE </storage>
            ...
          </account>

       requires DECIMALS_KEY ==Int #hashedLocation("Solidity", 3, .IntList)
        andBool DECIMALS     ==Int 255 &Int #lookup(ACCT_STORAGE, DECIMALS_KEY)
```

### Calling totalSupply() works

-   Everything from `<mode>` to `<callValue>` is boilerplate.
-   We are setting `<callData>` to `totalSupply()`.
-   We ask the prover to show that in all cases, we will end in `EVMC_SUCCESS` (rollback) when this happens.
-   The `<output>` cell specifies that we correctly lookup the `TS` value from the account storage.


```k
    claim [totalSupply]:
          <mode>     NORMAL   </mode>
          <schedule> ISTANBUL </schedule>

          <callStack> .List                                      </callStack>
          <program>   #binRuntime(ERC20)                         </program>
          <jumpDests> #computeValidJumpDests(#binRuntime(ERC20)) </jumpDests>

          <id>         ACCTID      => ?_ </id>
          <localMem>   .Memory     => ?_ </localMem>
          <memoryUsed> 0           => ?_ </memoryUsed>
          <wordStack>  .WordStack  => ?_ </wordStack>
          <pc>         0           => ?_ </pc>
          <endPC>      _           => ?_ </endPC>
          <gas>        #gas(_VGAS) => ?_ </gas>
          <callValue>  0           => ?_ </callValue>

          <callData> #abiCallData("totalSupply", .TypedArgs) </callData>
          <k>          #execute   => #halt ...               </k>
          <output>     .ByteArray => #buf(32, TOTALSUPPLY)   </output>
          <statusCode> _          => EVMC_SUCCESS            </statusCode>

          <account>
            <acctID> ACCTID </acctID>
            <storage> ACCT_STORAGE </storage>
            ...
          </account>

       requires TOTALSUPPLY_KEY ==Int #hashedLocation("Solidity", 2, .IntList)
        andBool TOTALSUPPLY     ==Int #lookup(ACCT_STORAGE,  TOTALSUPPLY_KEY)
```

### Calling Approve works

-   Everything from `<mode>` to `<substate>` is boilerplate.
-   We are setting `<callData>` to `approve(SPENDER, AMOUNT)`.
-   We ask the prover to show that in all cases, we will end in `EVMC_SUCCESS` when `SENDER` or `OWNER` is not `address(0)`, and that we will end in `EVMC_REVERT` (rollback) when either one of them is.
-   We take the OWNER from the `<caller>` cell, which is the `msg.sender`.
-   The `<output>` should be `#buf(32, bool2Word(True))` if the function does not revert.
-   The storage locations for Allowance should be updated accordingly.

```k
    claim [approve.success]:
          <mode>     NORMAL   </mode>
          <schedule> ISTANBUL </schedule>

          <callStack> .List                                      </callStack>
          <program>   #binRuntime(ERC20)                         </program>
          <jumpDests> #computeValidJumpDests(#binRuntime(ERC20)) </jumpDests>
          <static>    false                                      </static>

          <id>         ACCTID      => ?_ </id>
          <caller>     OWNER       => ?_ </caller>
          <localMem>   .Memory     => ?_ </localMem>
          <memoryUsed> 0           => ?_ </memoryUsed>
          <wordStack>  .WordStack  => ?_ </wordStack>
          <pc>         0           => ?_ </pc>
          <endPC>      _           => ?_ </endPC>
          <gas>        #gas(_VGAS) => ?_ </gas>
          <callValue>  0           => ?_ </callValue>
          <substate> _             => ?_ </substate>

          <callData> #abiCallData("approve", #address(SPENDER), #uint256(AMOUNT)) </callData>
          <k>          #execute   => #halt ...            </k>
          <output>     .ByteArray => #buf(32, 1)          </output>
          <statusCode> _          => EVMC_SUCCESS         </statusCode>

          <account>
            <acctID> ACCTID </acctID>
            <storage> ACCT_STORAGE => ACCT_STORAGE [ ALLOWANCE_KEY <- AMOUNT ] </storage>
            ...
          </account>

       requires ALLOWANCE_KEY ==Int #hashedLocation("Solidity", 1, OWNER SPENDER .IntList)
        andBool #rangeAddress(OWNER)
        andBool #rangeAddress(SPENDER)
        andBool #rangeUInt(256, AMOUNT)
        andBool OWNER =/=Int 0
        andBool SPENDER =/=Int 0
```

```k
    claim [approve.revert]:
          <mode>     NORMAL   </mode>
          <schedule> ISTANBUL </schedule>

          <callStack> .List                                      </callStack>
          <program>   #binRuntime(ERC20)                         </program>
          <jumpDests> #computeValidJumpDests(#binRuntime(ERC20)) </jumpDests>
          <static>    false                                      </static>

          <id>         ACCTID      => ?_ </id>
          <caller>     OWNER       => ?_ </caller>
          <localMem>   .Memory     => ?_ </localMem>
          <memoryUsed> 0           => ?_ </memoryUsed>
          <wordStack>  .WordStack  => ?_ </wordStack>
          <pc>         0           => ?_ </pc>
          <endPC>      _           => ?_ </endPC>
          <gas>        #gas(_VGAS) => ?_ </gas>
          <callValue>  0           => ?_ </callValue>
          <substate> _             => ?_ </substate>

          <callData> #abiCallData("approve", #address(SPENDER), #uint256(AMOUNT)) </callData>
          <k>          #execute   => #halt ...   </k>
          <output>     _          => ?_          </output>
          <statusCode> _          => EVMC_REVERT </statusCode>

          <account>
            <acctID> ACCTID </acctID>
            <storage> _ACCT_STORAGE </storage>
            ...
          </account>

       requires #rangeAddress(OWNER)
        andBool #rangeAddress(SPENDER)
        andBool #rangeUInt(256, AMOUNT)
        andBool (OWNER ==Int 0 orBool SPENDER ==Int 0)
```

```k
endmodule
```
