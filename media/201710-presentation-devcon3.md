---
title: 'KEVM: Overview and Progress Report'
subtitle: 'K by Example'
author:
-   Everett Hildenbrandt
-   Manasvi Saxena
-   Nishant Rodrigues
-   Lucas Peña
institute:
-   University of Illinois, Urbana-Champaign
date: '\today'
theme: metropolis
fontsize: 8pt
---

EVM Words
=========

Utilities
---------

. . .

### Modulo Arithmetic

``` {.k .uiuck .rvk}
    syntax Int ::= chop ( Int ) [function]
 // --------------------------------------
    rule chop ( I:Int ) => I %Int pow256
      requires I <Int 0  orBool I >=Int pow256

    rule chop ( I:Int ) => I
      requires I >=Int 0 andBool I <Int pow256
```

. . .

### Word Arithmetic

`<op>Word` operations incorporate the behavior for EVM arithmetic:

``` {.k .uiuck .rvk}
    syntax Int ::= Int "+Word" Int [function]
                 | Int "/Word" Int [function]
 // -----------------------------------------
    rule W0 +Word W1 => chop( W0 +Int W1 )
    rule W0 /Word 0  => 0
    rule W0 /Word W1 => chop( W0 /Int W1 ) requires W1 =/=K 0
```

Data-Structures over `Word`
===========================

A WordStack for EVM
-------------------

. . .

### As a cons-list

A cons-list is used for the EVM wordstack.

-   `.WordStack` serves as the empty worstack, and
-   `_:_` serves as the "cons" operator.

``` {.k .uiuck .rvk}
    syntax WordStack [flatPredicate]
    syntax WordStack ::= ".WordStack" | Int ":" WordStack
 // -----------------------------------------------------
```

This can be thought of as a singly linked-list.

. . .

### WordStack Append

``` {.k .uiuck .rvk}
    syntax WordStack ::= WordStack "++" WordStack [function]
 // --------------------------------------------------------
    rule .WordStack ++ WS' => WS'
    rule (W : WS)   ++ WS' => W : (WS ++ WS')
```

EVM Configuration
=================

Keeping Track of World and VM state
-----------------------------------

The actual configuration contains $60+$ cells.

### VM Execution State

Subconfiguration `<evm>` contains the execution state of a single VM.

```
configuration
  <k> $PGM:EthereumSimulation </k>
  <evm>
    <program>   .Map       </program>   // I_b
    <wordStack> .WordStack </wordStack> // \mu_s
    <localMem>  .Map       </localMem>  // \mu_m
    <gas>       0          </gas>       // \mu_g
    ...
  </evm>
  ...
```

Keeping Track of World and VM state
-----------------------------------

### Network/World State

Subconfiguration `<network>` contains the network/world state.

-   `multiplicity="*"` allows for multiple co-existing `<account>` cells.

```
configuration
  ...
  <network>
    <activeAccounts> .Map </activeAccounts>
    <accounts>
      <account multiplicity="*" type="Bag">
        <acctID>  0          </acctID>
        <balance> 0          </balance>
        <code>    .WordStack </code>
        <storage> .Map       </storage>
        <nonce>   0          </nonce>
      </account>
    </accounts>
    ...
  </network>
```

EVM Execution
=============

OpCode Execution
----------------

. . .

### Single Step

The `#next` operator executes a single step by:

1.  performing some quick checks for exceptional opcodes,
2.  executes the opcode if it is not immediately exceptional,
3.  increments the program counter, and finally
4.  reverts state if any of the above steps threw an exception.

. . .

``` {.k .uiuck .rvk}
    rule <mode> EXECMODE </mode>
         <k> #next
          => #pushCallStack ~> #exceptional? [ OP ]
                            ~> #exec         [ OP ]
                            ~> #pc           [ OP ]
          ~> #? #dropCallStack : #popCallStack ~> #exception ?#
         ...
         </k>
         <pc> PCOUNT </pc>
         <program> ... PCOUNT |-> OP ... </program>
      requires EXECMODE in (SetItem(NORMAL) SetItem(VMTESTS))
```

EVM Programs
============

EVM OpCodes
-----------

. . .

### Expressions

Expression opcodes call the corresponding `<op>Word` operators, then `#push` the
result:

``` {.k .uiuck .rvk}
    syntax BinStackOp ::= "SUB" | "DIV"
 // -----------------------------------
    rule <k> SUB W0 W1 => W0 -Word W1 ~> #push ... </k>
    rule <k> DIV W0 W1 => W0 /Word W1 ~> #push ... </k>
```

. . .

### Local Memory

``` {.k .uiuck .rvk}
    syntax UnStackOp ::= "MLOAD"
 // ----------------------------
    rule <k> MLOAD INDEX => #asWord(#range(LM, INDEX, 32)) ~> #push ... </k>
         <localMem> LM </localMem>

    syntax BinStackOp ::= "MSTORE"
 // ------------------------------
    rule <k> MSTORE I V => . ... </k>
         <localMem> LM => LM [ I := #padToWidth(32, #asByteStack(V)) ]
         </localMem>
```

Ethereum Network OpCodes
------------------------

. . .

### Account Storage Operations

These rules reach into the network state and load/store from account storage:

``` {.k .uiuck .rvk}
    syntax UnStackOp ::= "SLOAD"
 // ----------------------------
    rule <k> SLOAD INDEX => VALUE ~> #push ... </k> <id> ACCT </id>
         <account>
           <acctID> ACCT </acctID>
           <storage> ... INDEX |-> VALUE ... </storage>
           ...
         </account>
```

. . .

``` {.k .uiuck .rvk}
    syntax BinStackOp ::= "SSTORE"
 // ------------------------------
    rule <k> SSTORE INDEX VALUE => . ... </k> <id> ACCT </id>
         <account>
           <acctID> ACCT </acctID>
           <storage> STORAGE => STORAGE [ INDEX <- VALUE ] </storage>
           ...
         </account>
      requires notBool (INDEX in_keys(STORAGE))
```

Ethereum Network OpCodes
------------------------

. . .

### Call Operations

For each `CALL*` operation, we make a corresponding call to `#call` and a
state-change to setup the custom parts of the calling environment.

``` {.k .uiuck .rvk}
    syntax CallOp ::= "CALL"
 // ------------------------
    rule <k> CALL GCAP ACCTTO VALUE ARGSTART ARGWIDTH RETSTART RETWIDTH
          => #checkCall ACCTFROM VALUE
          ~> #call ACCTFROM ACCTTO ACCTTO Ccallgas(SCHED, ACCTTO, ACCTS, GCAP, GAVAIL, VALUE) VALUE VALUE #range(LM, ARGSTART, ARGWIDTH)
          ~> #return RETSTART RETWIDTH
         ...
         </k>
         <schedule> SCHED </schedule>
         <id> ACCTFROM </id>
         <localMem> LM </localMem>
         <activeAccounts> ACCTS </activeAccounts>
         <previousGas> GAVAIL </previousGas>
```

Ethereum Gas Calculation
========================

Execution Gas
-------------

The intrinsic gas calculation mirrors the style of the YellowPaper (appendix H).

. . .

### SSTORE Gas

``` {.k .uiuck .rvk}
    syntax InternalOp ::= #gasExec ( Schedule , OpCode )
 // ----------------------------------------------------
    rule <k> #gasExec(SCHED, SSTORE INDEX VALUE)
          => Csstore(SCHED, VALUE, #lookup(STORAGE, INDEX))
         ...
         </k>
         <id> ACCT </id>
         <account>
           <acctID> ACCT </acctID>
           <storage> STORAGE </storage>
           ...
         </account>
```

Gas Calculation Functions
-------------------------

The following functions are defined in the YellowPaper.

### Csstore

``` {.k .uiuck .rvk}
    syntax Int ::= Csstore ( Schedule , Int , Int ) [function]
 // ----------------------------------------------------------
    rule Csstore(SCHED, VALUE, OLD)
      => #ifInt VALUE =/=Int 0 andBool OLD ==Int 0
            #then Gsstoreset   < SCHED >
            #else Gsstorereset < SCHED >
         #fi
```

. . .

### Others

``` {.k .uiuck .rvk}
    syntax Int ::= Ccall    (Schedule, Int, Map, Int, Int, Int) [function]
                 | Ccallgas (Schedule, Int, Map, Int, Int, Int) [function]
                 | Cgascap  (Schedule, Int, Int, Int)           [function]
                 | Cextra   (Schedule, Int, Map, Int)           [function]
                 | Cxfer    (Schedule, Int)                     [function]
                 | Cnew     (Schedule, Int, Map, Int)           [function]
 // ----------------------------------------------------------------------
```

Fee Schedule from C++ Implementation
------------------------------------

. . .

### Schedule Constants

A `ScheduleConst` is a constant determined by the fee schedule.

``` {.k .uiuck .rvk}
    syntax Int ::= ScheduleConst "<" Schedule ">" [function]

    syntax ScheduleConst ::= "Gzero" | "Gbase" | "Gverylow"
 // -------------------------------------------------------
```

. . .

### Default Schedule

``` {.k .uiuck .rvk}
    syntax Schedule ::= "DEFAULT"
 // -----------------------------
    rule Gzero < DEFAULT > => 0
    rule Gbase < DEFAULT > => 2
```

. . .

### EIP150 Schedule

``` {.k .uiuck .rvk}
    syntax Schedule ::= "EIP150"
 // ----------------------------
    rule Gbalance < EIP150 > => 400
    rule Gsload   < EIP150 > => 200
```

The Sum To N Specification
==========================

Sum To N Program and Claim
--------------------------

. . .

### High Level

Canonical "hello world" verification example, in no particular language:

    s = 0;
    n = N;
    while (n > 0) {
        s = s + n;
        n = n - 1;
    }
    return s;

. . .

### Claim

$$s = \sum_{i = 1}^N i = \frac{N * (N + 1)}{2}$$

Proof Claims
------------

. . .

### Main Claim

-   We start at program counter 0 and end at 53.
-   The `<wordStack>` starts small enough and ends with the correct sum.
-   The gas consumed is no more than `(52 * N) + 27`.
-   `N` is sufficiently low that overflow will not occur in execution.

. . .

``` {.k .sum-to-n}
     <pc>        0  => 53                                </pc>
     <wordStack> WS => 0 : N *Int (N +Int 1) /Int 2 : WS </wordStack>
     <gas>       G  => G -Int (52 *Int N +Int 27)        </gas>

  requires N >=Int 0
   andBool N <=Int 340282366920938463463374607431768211455
   andBool #sizeWordStack(WS) <Int 1021
   andBool G >=Int 52 *Int N +Int 27
```

Proof Claims
------------

. . .

### Circularity (Loop Invariant)

We specify the behaviour of the rest of the program any time it reaches the loop
head:

-   We start at program counter 35 (beginning of loop) and end at 53.
-   `<wordStack>` starts with the counter `I` and the partial sum `S`, and
-   `<wordStack>` ends with the correct sum.
-   The gas consumed for this fragment is no more than `(52 * I) + 21`.
-   `S` and `I` are sufficiently low that overflow will not occur
    during execution.

. . .

``` {.k .sum-to-n}
     <pc> 35 => 53                         </pc>
     <gas> G => G -Int (52 *Int I +Int 21) </gas>

     <wordStack> I : S                               : WS
              => 0 : S +Int I *Int (I +Int 1) /Int 2 : WS </wordStack>

  requires I >=Int 0
   andBool S >=Int 0
   andBool S +Int I *Int (I +Int 1) /Int 2 <Int pow256
   andBool #sizeWordStack(WS) <Int 1021
   andBool G >=Int 52 *Int I +Int 21
```

Verifying ABI compliant contracts
--------------------------------

. . .

`#abiCallData` generates ABI compliant `callData`:

```
    syntax WordStack ::= #abiCallData ( String , TypedArgs ) [function]
 // -------------------------------------------------------------------
    rule #abiCallData( FNAME , ARGS ) =>
        #parseByteStack(substrString(
            Keccak256(#generateSignature(FNAME +String "(", ARGS)), 0, 8))
            ++ #encodeArgs(.WordStack | ARGS)
```

. . .

Here, we generate `callData` for call the `transfer` function:

```
<callData>
    #abiCallData("transfer",#address(%ACCOUNT_TO),#uint256(TRANSFER))
</callData>
```

Note that `TRANSFER` is a symbolic word,

ERC20: Specifying `transfer`
----------------------------

. . .

-   Execution reaches a `RETURN` op code
-   Account balances are updated correctly if balances are sufficient.

```
   <k> #execute => (RETURN _ _ ~> _) </k>
   <callData>  #abiCallData("transfer", ...) </callData>
   <accounts>
     <account>
       <storage> (%ACCT_1_BALANCE |-> (B1 => B1 -Int TRANSFER))
                 (%ACCT_2_BALANCE |-> (B2 => B2 +Int TRANSFER))
       </storage>
       ...
     </account>
   </accounts>

  requires TRANSFER >Int 0 andBool TRANSFER <Int pow256
   andBool B1 >=Int 0      andBool B1 <Int pow256
   andBool B2 >=Int 0      andBool B2 <Int pow256
   andBool B2 +Int TRANSFER <Int pow256
   andBool B1 -Int TRANSFER >=Int 0
   andBool #sizeWordStack(WS) <Int 1017
```

Other Work
==========

KEVM
----

Too much to present here (ask offline).

### Tests

-   Pass all of VMTests (deprecated) and GeneralStateTests.
-   Almost passing BlockchainTests.
-   Within an order of magnitude the performance of cpp-ethereum.

### Verification

-   Verified ERC20 specification over (fixed) HKG Token (see Github repository).
-   Added ABI-level abstractions for easier specification of proofs (in progress).

### High Level Languages (not discussed here)

-   `EVM-PRIME` from IC3 Bootcamp.
-   Extending with more primitives to give semantics to Viper.

K Framework
-----------

### Language Independent PL/FM Toolkit

-   Parser/interpreter/debugger/model-checker/verification tools all exist.
-   Work towards semantics-based compiler (for even better performance).

### Future Directions

-   More analysis tools built on KEVM.
-   Other blockchain language semantics in progress.
-   Other (non-blockchain) language/systems/network semantics in progress.

The End
=======

Acknowledgments
---------------

-   Formal Systems Lab (FSL) at UIUC for K support: <http://fsl.cs.illinois.edu>
-   Runtime Verification, Inc. for K support: <http://runtimeverification.com>
-   IOHK for funding and ideas: <http://iohk.io>
-   Ethereum Foundation/Devcon3 Teams for hosting: <https://ethereum.org>
