EVM Execution
=============

### Overview

The EVM is a stack machine over some simple opcodes.
Most of the opcodes are "local" to the execution state of the machine, but some of them must interact with the world state.
This file only defines the local execution operations, the file `driver.md` will define the interactions with the world state.

```k
requires "data.md"
requires "network.md"
requires "gas.md"

module EVM
    imports STRING
    imports EVM-DATA
    imports NETWORK
    imports GAS
```

Configuration
-------------

The configuration has cells for the current account id, the current opcode, the program counter, the current gas, the gas price, the current program, the word stack, and the local memory.
In addition, there are cells for the callstack and execution substate.

We've broken up the configuration into two components; those parts of the state that mutate during execution of a single transaction and those that are static throughout.
In the comments next to each cell, we've marked which component of the YellowPaper state corresponds to each cell.

```k
    configuration
      <kevm>
        <k> $PGM:EthereumSimulation </k>
        <exit-code exit=""> 1 </exit-code>
        <mode> $MODE:Mode </mode>
        <schedule> $SCHEDULE:Schedule </schedule>
        <useGas> $USEGAS:Bool </useGas>

        <ethereum>

          // EVM Specific
          // ============

          <evm>

            // Mutable during a single transaction
            // -----------------------------------

            <output>          .Bytes      </output>           // H_RETURN
            <statusCode>      .StatusCode </statusCode>
            <callStack>       .List       </callStack>
            <interimStates>   .List       </interimStates>
            <touchedAccounts> .Set        </touchedAccounts>

            <callState>
              <program>   .Bytes </program>
              <jumpDests> .Bytes </jumpDests>

              // I_*
              <id>        .Account </id>                    // I_a
              <caller>    .Account </caller>                // I_s
              <callData>  .Bytes   </callData>              // I_d
              <callValue> 0        </callValue>             // I_v

              // \mu_*
              <wordStack>   .WordStack </wordStack>           // \mu_s
              <localMem>    .Bytes     </localMem>            // \mu_m
              <pc>          0          </pc>                  // \mu_pc
              <gas>         0:Gas      </gas>                 // \mau_g
              <memoryUsed>  0          </memoryUsed>          // \mu_i
              <callGas>     0:Gas      </callGas>

              <static>    false </static>
              <callDepth> 0     </callDepth>
            </callState>

            <versionedHashes> .List </versionedHashes>

            // A_* (execution substate)
            <substate>
              <selfDestruct>     .Set  </selfDestruct>            // A_s
              <log>              .List </log>                     // A_l
              <refund>           0     </refund>                  // A_r
              <accessedAccounts> .Set  </accessedAccounts>
              <accessedStorage>  .Map  </accessedStorage>
              <createdAccounts>  .Set  </createdAccounts>
            </substate>

            // Immutable during a single transaction
            // -------------------------------------

            <gasPrice> 0        </gasPrice>                   // I_p
            <origin>   .Account </origin>                     // I_o

            // I_H* (block information)
            <blockhashes> .List </blockhashes>
            <block>
              <previousHash>     0      </previousHash>     // I_Hp
              <ommersHash>       0      </ommersHash>       // I_Ho
              <coinbase>         0      </coinbase>         // I_Hc
              <stateRoot>        0      </stateRoot>        // I_Hr
              <transactionsRoot> 0      </transactionsRoot> // I_Ht
              <receiptsRoot>     0      </receiptsRoot>     // I_He
              <logsBloom>        .Bytes </logsBloom>        // I_Hb
              <difficulty>       0      </difficulty>       // I_Hd
              <number>           0      </number>           // I_Hi
              <gasLimit>         0      </gasLimit>         // I_Hl
              <gasUsed>          0:Gas  </gasUsed>          // I_Hg
              <timestamp>        0      </timestamp>        // I_Hs
              <extraData>        .Bytes </extraData>        // I_Hx
              <mixHash>          0      </mixHash>          // I_Hm
              <blockNonce>       0      </blockNonce>       // I_Hn
              <baseFee>          0      </baseFee>
              <withdrawalsRoot>  0      </withdrawalsRoot>
              <blobGasUsed>      0      </blobGasUsed>
              <excessBlobGas>    0      </excessBlobGas>
              <beaconRoot>       0      </beaconRoot>

              <ommerBlockHeaders> [ .JSONs ] </ommerBlockHeaders>
            </block>

          </evm>

          // Ethereum Network
          // ================

          <network>

            // Chain identifier
            // ----------------
            <chainID> $CHAINID:Int </chainID>

            // Accounts Record
            // ---------------

            <accounts>
              <account multiplicity="*" type="Map">
                <acctID>           0                  </acctID>
                <balance>          0                  </balance>
                <code>             .Bytes:AccountCode </code>
                <storage>          .Map               </storage>
                <origStorage>      .Map               </origStorage>
                <transientStorage> .Map               </transientStorage>
                <nonce>            0                  </nonce>
              </account>
            </accounts>

            // Transactions Record
            // -------------------

            <txOrder>   .List </txOrder>
            <txPending> .List </txPending>

            <messages>
              <message multiplicity="*" type="Map">
                <msgID>         0          </msgID>
                <txNonce>       0          </txNonce>       // T_n
                <txGasPrice>    0          </txGasPrice>    // T_p
                <txGasLimit>    0          </txGasLimit>    // T_g
                <to>            .Account   </to>            // T_t
                <value>         0          </value>         // T_v
                <sigV>          0          </sigV>          // T_w
                <sigR>          .Bytes     </sigR>          // T_r
                <sigS>          .Bytes     </sigS>          // T_s
                <data>          .Bytes     </data>          // T_i/T_e
                <txAccess>      [ .JSONs ] </txAccess>      // T_a
                <txChainID>     0          </txChainID>     // T_c
                <txPriorityFee> 0          </txPriorityFee> // T_f
                <txMaxFee>      0          </txMaxFee>      // T_m
                <txType>        .TxType    </txType>        // T_x
                <txMaxBlobFee>  0          </txMaxBlobFee>
                <txVersionedHashes> .List  </txVersionedHashes>
              </message>
            </messages>

            // Withdrawals Record
            // ------------------

            <withdrawalsPending> .List </withdrawalsPending>
            <withdrawalsOrder>   .List </withdrawalsOrder>

            <withdrawals>
              <withdrawal multiplicity="*" type="Map">
                <withdrawalID>   0        </withdrawalID>
                <index>          0        </index>
                <validatorIndex> 0        </validatorIndex>
                <address>        .Account </address>
                <amount>         0        </amount>
              </withdrawal>
            </withdrawals>

          </network>

        </ethereum>
      </kevm>

    syntax EthereumSimulation
 // -------------------------
```

Modal Semantics
---------------

Our semantics is modal, with the initial mode being set on the command line via `-cMODE=EXECMODE`.

-   `NORMAL` executes as a client on the network would.
-   `VMTESTS` skips `CALL*` and `CREATE` operations.

```k
    syntax Mode ::= "NORMAL"  [symbol(NORMAL) ]
                  | "VMTESTS" [symbol(VMTESTS)]
 // -------------------------------------------
```

State Stacks
------------

### The CallStack

The `callStack` cell stores a list of previous VM execution states.

-   `#pushCallStack` saves a copy of VM execution state on the `callStack`.
-   `#popCallStack` restores the top element of the `callStack`.
-   `#dropCallStack` removes the top element of the `callStack`.

```k
    syntax InternalOp ::= "#pushCallStack"
 // --------------------------------------
    rule <k> #pushCallStack => .K ... </k>
         <callStack> STACK => ListItem(<callState> CALLSTATE </callState>) STACK </callStack>
         <callState> CALLSTATE </callState>

    syntax InternalOp ::= "#popCallStack"
 // -------------------------------------
    rule <k> #popCallStack => .K ... </k>
         <callStack> ListItem(<callState> CALLSTATE </callState>) REST => REST </callStack>
         <callState> _ => CALLSTATE </callState>

    syntax InternalOp ::= "#dropCallStack"
 // --------------------------------------
    rule <k> #dropCallStack => .K ... </k>
         <callStack> ListItem(_) REST => REST </callStack>
```

### The StateStack

The `interimStates` cell stores a list of previous world states.

-   `#pushWorldState` stores a copy of the current accounts and the substate at the top of the `interimStates` cell.
-   `#popWorldState` restores the top element of the `interimStates`.
-   `#dropWorldState` removes the top element of the `interimStates`.

```k
    syntax Accounts ::= "{" AccountsCell "|" SubstateCell "}"
 // ---------------------------------------------------------

    syntax InternalOp ::= "#pushWorldState"
 // ---------------------------------------
    rule <k> #pushWorldState => .K ... </k>
         <interimStates> STATES => ListItem({ <accounts> ACCTDATA </accounts> | <substate> SUBSTATE </substate> }) STATES </interimStates>
         <accounts> ACCTDATA </accounts>
         <substate> SUBSTATE </substate>

    syntax InternalOp ::= "#popWorldState"
 // --------------------------------------
    rule <k> #popWorldState => .K ... </k>
         <interimStates> ListItem({ <accounts> ACCTDATA </accounts> | <substate> SUBSTATE </substate> }) REST => REST </interimStates>
         <accounts> _ => ACCTDATA </accounts>
         <substate> _ => SUBSTATE </substate>

    syntax InternalOp ::= "#dropWorldState"
 // ---------------------------------------
    rule <k> #dropWorldState => .K ... </k> <interimStates> ListItem(_) REST => REST </interimStates>
```

Control Flow
------------

### Exception Based

-   `#halt` indicates end of execution.
    It will consume anything related to the current computation behind it on the `<k>` cell.
-   `#end_` sets the `statusCode` and the program counter of the last executed opcode, then halts execution.

```k
    syntax KItem ::= "#halt"           [symbol(halt)]
                   | "#end" StatusCode [symbol(end) ]
 // -------------------------------------------------
    rule [end]:
         <k> #end SC => #halt ... </k>
         <statusCode> _ => SC </statusCode>

    rule <k> #halt ~> (_:Int    => .K) ... </k>
    rule <k> #halt ~> (_:OpCode => .K) ... </k>
```

OpCode Execution
----------------

### Execution Macros

-   `#lookupOpCode` reads an `OpCode` from the program `Bytes` if the program-counter is within the bounds of the program, meaning that it points to an actual opcode.
    It will return `.NoOpCode` otherwise.

```k
    syntax MaybeOpCode ::= ".NoOpCode" | OpCode

    syntax MaybeOpCode ::= "#lookupOpCode" "(" Bytes "," Int "," Schedule ")" [function, total]
 // -------------------------------------------------------------------------------------------
    rule #lookupOpCode(BA, I, SCHED) => #dasmOpCode(BA[I], SCHED) requires 0 <=Int I andBool I <Int lengthBytes(BA)
    rule #lookupOpCode(_, _, _)  => .NoOpCode [owise]
```

-   `#execute` loads the next opcode.

```k
    syntax KItem ::= "#execute" [symbol(execute)]
 // ---------------------------------------------
    rule [halt]:
         <k> #halt ~> (#execute => .K) ... </k>

    rule [step]:
         <k> (.K => #next [ #lookupOpCode(PGM, PCOUNT, SCHED) ]) ~> #execute ... </k>
         <program> PGM </program>
         <pc> PCOUNT </pc>
         <schedule> SCHED </schedule>
```

### Single Step

If the program-counter points to an actual opcode, it's loaded into the `#next [_]` operator.
If `.NoOpCode` is loaded into `#next [_]`, then it means that there is no next opcode and the execution will halt with an `EVMC_SUCCESS` status code.
The `#next [_]` operator initiates execution by:

1.  checking if there will be a stack over/underflow, or a static mode violation,
2.  calculate any address conversions needed for items on the wordstack,
3.  executing the opcode (which includes any gas deduction needed), and
4.  adjusting the program counter.

```k
    syntax InternalOp ::= "#next" "[" MaybeOpCode "]"
 // -------------------------------------------------
    rule <k> #next [ .NoOpCode ] => #end EVMC_SUCCESS ... </k>
         <output> _ => .Bytes </output>

    rule <k> #next [ OP:OpCode ]
          => #addr [ OP ]
          ~> #exec [ OP ]
          ~> #pc   [ OP ]
         ...
         </k>
         <wordStack> WS </wordStack>
         <static> STATIC:Bool </static>
      requires notBool ( #stackUnderflow(WS, OP) orBool #stackOverflow(WS, OP) )
       andBool notBool ( STATIC andBool #changesState(OP, WS) )

    rule <k> #next [ OP ] => #end EVMC_STACK_UNDERFLOW ... </k>
         <wordStack> WS </wordStack>
      requires #stackUnderflow(WS, OP)

    rule <k> #next [ OP ] => #end EVMC_STACK_OVERFLOW ... </k>
         <wordStack> WS </wordStack>
      requires #stackOverflow(WS, OP)

    rule <k> #next [ OP ] => #end EVMC_STATIC_MODE_VIOLATION ... </k>
         <wordStack> WS </wordStack>
         <static> STATIC:Bool </static>
      requires STATIC andBool #changesState(OP, WS)
       andBool notBool ( #stackUnderflow(WS, OP) orBool #stackOverflow(WS, OP) )
```

### Exceptional Checks

-   `#stackNeeded` is how many arguments that opcode will need off the top of the stack.
-   `#stackAdded` is how many arguments that opcode will push onto the top of the stack.
-   `#stackDelta` is the delta the stack will have after the opcode executes.

```k
    syntax Bool ::= #stackUnderflow ( WordStack , OpCode ) [symbol(#stackUnderflow), macro]
                  | #stackOverflow  ( WordStack , OpCode ) [symbol(#stackOverflow), macro]
 // --------------------------------------------------------------------------------------
    rule #stackUnderflow(WS, OP:OpCode) => #sizeWordStack(WS) <Int #stackNeeded(OP)
    rule #stackOverflow (WS, OP) => #sizeWordStack(WS) +Int #stackDelta(OP) >Int 1024

    syntax Int ::= #stackNeeded ( OpCode ) [symbol(#stackNeeded), function]
 // -----------------------------------------------------------------------
    rule #stackNeeded(_POP:PushOp)      => 0
    rule #stackNeeded(_IOP:InvalidOp)   => 0
    rule #stackNeeded(_NOP:NullStackOp) => 0
    rule #stackNeeded(_UOP:UnStackOp)   => 1
    rule #stackNeeded(BOP:BinStackOp)   => 2 requires notBool isLogOp(BOP)
    rule #stackNeeded(_TOP:TernStackOp) => 3
    rule #stackNeeded(_QOP:QuadStackOp) => 4
    rule #stackNeeded(DUP(N))           => N
    rule #stackNeeded(SWAP(N))          => N +Int 1
    rule #stackNeeded(LOG(N))           => N +Int 2
    rule #stackNeeded(_CSOP:CallSixOp)  => 6
    rule #stackNeeded(COP:CallOp)       => 7 requires notBool isCallSixOp(COP)

    syntax Int ::= #stackAdded ( OpCode ) [symbol(#stackAdded), function]
 // ---------------------------------------------------------------------
    rule #stackAdded(CALLDATACOPY)   => 0
    rule #stackAdded(RETURNDATACOPY) => 0
    rule #stackAdded(CODECOPY)       => 0
    rule #stackAdded(EXTCODECOPY)    => 0
    rule #stackAdded(POP)            => 0
    rule #stackAdded(MSTORE)         => 0
    rule #stackAdded(MSTORE8)        => 0
    rule #stackAdded(SSTORE)         => 0
    rule #stackAdded(JUMP)           => 0
    rule #stackAdded(JUMPI)          => 0
    rule #stackAdded(JUMPDEST)       => 0
    rule #stackAdded(STOP)           => 0
    rule #stackAdded(RETURN)         => 0
    rule #stackAdded(REVERT)         => 0
    rule #stackAdded(SELFDESTRUCT)   => 0
    rule #stackAdded(PUSH(_))        => 1
    rule #stackAdded(LOG(_))         => 0
    rule #stackAdded(SWAP(N))        => N +Int 1
    rule #stackAdded(DUP(N))         => N +Int 1
    rule #stackAdded(_IOP:InvalidOp) => 0
    rule #stackAdded(_OP)            => 1 [owise]

    syntax Int ::= #stackDelta ( OpCode ) [symbol(#stackDelta), function]
 // ---------------------------------------------------------------------
    rule #stackDelta(OP) => #stackAdded(OP) -Int #stackNeeded(OP)
```

-   `#changesState` is true if the given opcode will change `<network>` state given the arguments.

```k
    syntax Bool ::= #changesState ( OpCode , WordStack ) [symbol(#changesState), function]
 // --------------------------------------------------------------------------------------
```

```k
    rule #changesState(CALL         , _ : _ : VALUE : _) => true  requires VALUE =/=Int 0
    rule #changesState(LOG(_)       , _)                 => true
    rule #changesState(SSTORE       , _)                 => true
    rule #changesState(CREATE       , _)                 => true
    rule #changesState(CREATE2      , _)                 => true
    rule #changesState(SELFDESTRUCT , _)                 => true
    rule #changesState(TSTORE       , _)                 => true
    rule #changesState(_            , _)                 => false [owise]
```

### Execution Step

-   `#exec` will load the arguments of the opcode (it assumes `#stackNeeded?` is accurate and has been called) and trigger the subsequent operations.

```k
    syntax InternalOp ::= "#exec" "[" OpCode "]"
 // --------------------------------------------
    rule <k> #exec [ IOP:InvalidOp ] => IOP ... </k>

    rule <k> #exec [ OP ] => #gas [ OP , OP ] ~> OP ... </k> requires isNullStackOp(OP) orBool isPushOp(OP)
```

Here we load the correct number of arguments from the `wordStack` based on the sort of the opcode.

```k
    syntax KItem  ::= OpCode
    syntax OpCode ::= NullStackOp | UnStackOp | BinStackOp | TernStackOp | QuadStackOp
                    | InvalidOp | StackOp | InternalOp | CallOp | CallSixOp | PushOp
 // --------------------------------------------------------------------------------

    syntax InternalOp ::= UnStackOp   Int
                        | BinStackOp  Int Int
                        | TernStackOp Int Int Int
                        | QuadStackOp Int Int Int Int
 // -------------------------------------------------
    rule <k> #exec [ UOP:UnStackOp   ] => #gas [ UOP , UOP W0          ] ~> UOP W0          ... </k> <wordStack> W0 : WS                => WS </wordStack>
    rule <k> #exec [ BOP:BinStackOp  ] => #gas [ BOP , BOP W0 W1       ] ~> BOP W0 W1       ... </k> <wordStack> W0 : W1 : WS           => WS </wordStack>
    rule <k> #exec [ TOP:TernStackOp ] => #gas [ TOP , TOP W0 W1 W2    ] ~> TOP W0 W1 W2    ... </k> <wordStack> W0 : W1 : W2 : WS      => WS </wordStack>
    rule <k> #exec [ QOP:QuadStackOp ] => #gas [ QOP , QOP W0 W1 W2 W3 ] ~> QOP W0 W1 W2 W3 ... </k> <wordStack> W0 : W1 : W2 : W3 : WS => WS </wordStack>
```

`StackOp` is used for opcodes which require a large portion of the stack.

```k
    syntax InternalOp ::= StackOp WordStack
 // ---------------------------------------
    rule <k> #exec [ SO:StackOp ] => #gas [ SO , SO WS ] ~> SO WS ... </k> <wordStack> WS </wordStack>
```

The `CallOp` opcodes all interpret their second argument as an address.

```k
    syntax InternalOp ::= CallSixOp Int Int     Int Int Int Int
                        | CallOp    Int Int Int Int Int Int Int
 // -----------------------------------------------------------
    rule <k> #exec [ CSO:CallSixOp ] => #gas [ CSO , CSO W0 W1    W2 W3 W4 W5 ] ~> CSO W0 W1    W2 W3 W4 W5 ... </k> <wordStack> W0 : W1 : W2 : W3 : W4 : W5 : WS      => WS </wordStack>
    rule <k> #exec [ CO:CallOp     ] => #gas [ CO  , CO  W0 W1 W2 W3 W4 W5 W6 ] ~> CO  W0 W1 W2 W3 W4 W5 W6 ... </k> <wordStack> W0 : W1 : W2 : W3 : W4 : W5 : W6 : WS => WS </wordStack>
```

### Address Conversion

Some opcodes require accessing elements of the state at different addresses.
We make sure the given arguments (to be interpreted as addresses) are with 160 bits ahead of time.

```k
    syntax InternalOp ::= "#addr" "[" OpCode "]"
 // --------------------------------------------
    rule <k> #addr [ OP:OpCode ] => .K ... </k>
         <wordStack> (W0 => #addr(W0)) : _WS </wordStack>
      requires isAddr1Op(OP)

    rule <k> #addr [ OP:OpCode ] => .K ... </k>
         <wordStack> _W0 : (W1 => #addr(W1)) : _WS </wordStack>
      requires isAddr2Op(OP)

    rule <k> #addr [ OP:OpCode ] => .K ... </k>
      requires notBool ( isAddr1Op(OP) orBool isAddr2Op(OP) )

    syntax Bool ::= isAddr1Op ( OpCode ) [symbol(isAddr1Op), function, total]
                  | isAddr2Op ( OpCode ) [symbol(isAddr2Op), function, total]
 // -------------------------------------------------------------------------
    rule isAddr1Op(BALANCE)      => true
    rule isAddr1Op(SELFDESTRUCT) => true
    rule isAddr1Op(EXTCODEHASH)  => true
    rule isAddr1Op(EXTCODESIZE)  => true
    rule isAddr1Op(EXTCODECOPY)  => true
    rule isAddr1Op(_)            => false [owise]

    rule isAddr2Op(_:CallOp)    => true
    rule isAddr2Op(_:CallSixOp) => true
    rule isAddr2Op(_)           => false [owise]
```

### Program Counter

All operators except for `PUSH` and `JUMP*` increment the program counter by 1.
The arguments to `PUSH` must be skipped over (as they are inline), and the opcode `JUMP` already affects the program counter in the correct way.

-   `#pc` calculates the next program counter of the given operator.

```k
    syntax InternalOp ::= "#pc" "[" OpCode "]" [symbol(pc)]
 // -------------------------------------------------------
    rule [pc.inc]:
         <k> #pc [ OP ] => .K ... </k>
         <pc> PCOUNT => PCOUNT +Int #widthOp(OP) </pc>

    syntax Int ::= #widthOp ( OpCode ) [symbol(#widthOp), function, total]
 // ----------------------------------------------------------------------
    rule #widthOp(PUSH(N)) => 1 +Int N
    rule #widthOp(_)       => 1        [owise]
```

After executing a transaction, it's necessary to have the effect of the substate log recorded.

-   `#finalizeStorage` updates the origStorage cell with the new values of storage.
-   `#finalizeTx` makes the substate log actually have an effect on the state.
-   `#deleteAccounts` deletes the accounts specified by the self destruct list.
-   `#finalizeWithdrawals` increases the balance of the `address` specified by the `amount` given, for each withdrawal.
-   `#gweiToWei` does the conversion from GWEI to WEI.

```k
    syntax Int ::= #gweiToWei ( Int ) [symbol(#gweiToWei), function]
 // ----------------------------------------------------------------
   rule #gweiToWei(V) => V *Int 10 ^Int 9

    syntax InternalOp ::= "#finalizeWithdrawals" [symbol(#finalizeWithdrawals)]
 // ---------------------------------------------------------------------------
    rule <k> #finalizeWithdrawals => .K ... </k>
         <withdrawalsPending> .List </withdrawalsPending>

    rule <k> #finalizeWithdrawals ... </k>
         <withdrawalsPending> ListItem(WDID) LS => LS </withdrawalsPending>
         <withdrawal>
           <withdrawalID> WDID </withdrawalID>
           <address> ACCT </address>
           <amount> VALUE </amount>
           ...
         </withdrawal>
         <account>
           <acctID> ACCT </acctID>
           <balance> B => B +Int #gweiToWei(VALUE) </balance>
           ...
         </account>

    rule <k> (.K => #newAccount ACCT) ~> #finalizeWithdrawals ... </k>
         <withdrawalsPending> ListItem(WDID) _ </withdrawalsPending>
         <withdrawal>
           <withdrawalID> WDID </withdrawalID>
           <address> ACCT </address>
           ...
         </withdrawal> [owise]

    syntax InternalOp ::= #finalizeStorage ( List ) [symbol(#finalizeStorage)]
 // --------------------------------------------------------------------------
    rule <k> #finalizeStorage(ListItem(ACCT) REST => REST) ... </k>
         <account>
           <acctID> ACCT </acctID>
           <storage> STORAGE </storage>
           <origStorage> _ => STORAGE </origStorage>
           ...
         </account>

    rule <k> #finalizeStorage(.List) => .K ... </k>

    rule <k> (.K => #newAccount ACCT) ~> #finalizeStorage(ListItem(ACCT) _ACCTS) ... </k> [owise]

    syntax InternalOp ::= #finalizeTx ( Bool )     [symbol(#finalizeTx)]
                        | #deleteAccounts ( List ) [symbol(#deleteAccounts)]
 // ------------------------------------------------------------------------
    rule <k> #finalizeTx(true) => #finalizeStorage(Set2List(SetItem(MINER) |Set ACCTS)) ... </k>
         <selfDestruct> .Set </selfDestruct>
         <coinbase> MINER </coinbase>
         <touchedAccounts> ACCTS => .Set </touchedAccounts>
         <accessedAccounts> _ => .Set </accessedAccounts>
         <accessedStorage> _ => .Map </accessedStorage>
         <createdAccounts> _ => .Set </createdAccounts>

    rule <k> #finalizeTx(false) ... </k>
         <useGas> true </useGas>
         <schedule> SCHED </schedule>
         <gas> GAVAIL => G*(GAVAIL, GLIMIT, REFUND, SCHED) </gas>
         <refund> REFUND => 0 </refund>
         <txPending> ListItem(MSGID:Int) ... </txPending>
         <message>
            <msgID> MSGID </msgID>
            <txGasLimit> GLIMIT </txGasLimit>
            ...
         </message>
      requires REFUND =/=Int 0

    rule <k> #finalizeTx(false => true) ... </k>
         <useGas> true </useGas>
         <baseFee> BFEE </baseFee>
         <origin> ORG </origin>
         <coinbase> MINER </coinbase>
         <gas> GAVAIL </gas>
         <gasUsed> GUSED => GUSED +Gas GLIMIT -Gas GAVAIL </gasUsed>
         <gasPrice> GPRICE </gasPrice>
         <refund> 0 </refund>
         <account>
           <acctID> ORG </acctID>
           <balance> ORGBAL => ORGBAL +Int GAVAIL *Int GPRICE </balance>
           ...
         </account>
         <account>
           <acctID> MINER </acctID>
           <balance> MINBAL => MINBAL +Int (GLIMIT -Int GAVAIL) *Int (GPRICE -Int BFEE) </balance>
           ...
         </account>
         <txPending> ListItem(TXID:Int) REST => REST </txPending>
         <message>
           <msgID> TXID </msgID>
           <txGasLimit> GLIMIT </txGasLimit>
           ...
         </message>
      requires ORG =/=Int MINER

    rule <k> #finalizeTx(false => true) ... </k>
         <useGas> true </useGas>
         <baseFee> BFEE </baseFee>
         <origin> ACCT </origin>
         <coinbase> ACCT </coinbase>
         <gas> GAVAIL </gas>
         <gasUsed> GUSED => GUSED +Gas GLIMIT -Gas GAVAIL </gasUsed>
         <gasPrice> GPRICE </gasPrice>
         <refund> 0 </refund>
         <account>
           <acctID> ACCT </acctID>
           <balance> BAL => BAL +Int GLIMIT *Int GPRICE -Int (GLIMIT -Int GAVAIL) *Int BFEE </balance>
           ...
         </account>
         <txPending> ListItem(MsgId:Int) REST => REST </txPending>
         <message>
           <msgID> MsgId </msgID>
           <txGasLimit> GLIMIT </txGasLimit>
           ...
         </message>

    rule <k> #finalizeTx(false => true) ... </k>
         <useGas> false </useGas>
         <txPending> ListItem(MsgId:Int) REST => REST </txPending>
         <message>
           <msgID> MsgId </msgID>
           ...
         </message>

    rule <k> (.K => #deleteAccounts(Set2List(ACCTS))) ~> #finalizeTx(true) ... </k>
         <selfDestruct> ACCTS => .Set </selfDestruct>
      requires size(ACCTS) >Int 0

    rule <k> (.K => #newAccount MINER) ~> #finalizeTx(_) ... </k>
         <coinbase> MINER </coinbase> [owise]

    rule <k> #deleteAccounts(ListItem(ACCT) ACCTS) => #deleteAccounts(ACCTS) ... </k>
         <accounts>
           ( <account>
               <acctID> ACCT </acctID>
               ...
             </account>
          => .Bag
           )
           ...
         </accounts>

    rule <k> #deleteAccounts(.List) => .K ... </k>
```

### Block processing

-   `#startBlock` is used to signal that we are about to start mining a block and block initialization should take place (before transactions are executed).
-   `#finalizeBlock` is used to signal that block finalization procedures should take place (after transactions have executed).
-   `#rewardOmmers(_)` pays out the reward to uncle blocks so that blocks are orphaned less often in Ethereum.

```k
    syntax EthereumCommand ::= "#startBlock"
 // ----------------------------------------
    rule <k> #startBlock => #executeBeaconRoots ... </k>
         <gasUsed> _ => 0 </gasUsed>
         <log> _ => .List </log>
         <logsBloom> _ => #padToWidth(256, .Bytes) </logsBloom>

    syntax EthereumCommand ::= "#finalizeBlock"
                             | #rewardOmmers ( JSONs ) [symbol(#rewardOmmers)]
 // --------------------------------------------------------------------------
    rule <k> #finalizeBlock => #if Ghaswithdrawals << SCHED >> #then #finalizeWithdrawals #else .K #fi ~> #rewardOmmers(OMMERS) ... </k>
         <schedule> SCHED </schedule>
         <ommerBlockHeaders> [ OMMERS ] </ommerBlockHeaders>
         <coinbase> MINER </coinbase>
         <account>
           <acctID> MINER </acctID>
           <balance> MINBAL => MINBAL +Int Rb < SCHED > </balance>
           ...
         </account>
         <log> LOGS </log>
         <logsBloom> _ => #bloomFilter(LOGS) </logsBloom>

    rule <k> (.K => #newAccount MINER) ~> #finalizeBlock ... </k>
         <coinbase> MINER </coinbase> [owise]

    rule <k> #rewardOmmers(.JSONs) => .K ... </k>
    rule <k> #rewardOmmers([ _ , _ , OMMER , _ , _ , _ , _ , _ , OMMNUM , _ ] , REST) => #rewardOmmers(REST) ... </k>
         <schedule> SCHED </schedule>
         <coinbase> MINER </coinbase>
         <number> CURNUM </number>
         <account>
           <acctID> MINER </acctID>
           <balance> MINBAL => MINBAL +Int Rb < SCHED > /Int 32 </balance>
          ...
         </account>
         <account>
           <acctID> OMMER </acctID>
           <balance> OMMBAL => OMMBAL +Int Rb < SCHED > +Int (OMMNUM -Int CURNUM) *Int (Rb < SCHED > /Int 8) </balance>
          ...
         </account>

    syntax Bytes ::= #bloomFilter(List)      [symbol(#bloomFilter), function]
                   | #bloomFilter(List, Int) [symbol(#bloomFilterAux), function]
 // ----------------------------------------------------------------------------
    rule #bloomFilter(L) => #bloomFilter(L, 0)

    rule #bloomFilter(.List, B) => #padToWidth(256, #asByteStack(B))
    rule #bloomFilter(ListItem({ ACCT | TOPICS | _ }) L, B) => #bloomFilter(ListItem(#padToWidth(20, #asByteStack(ACCT))) listAsBytes(TOPICS) L, B)

    syntax List ::= listAsBytes(List) [symbol(listAsBytes), function]
 // -----------------------------------------------------------------
    rule listAsBytes(.List) => .List
    rule listAsBytes(ListItem(TOPIC) L) => ListItem(#padToWidth(32, #asByteStack(TOPIC))) listAsBytes(L)

    rule #bloomFilter(ListItem(WS:Bytes) L, B) => #bloomFilter(L, B |Int M3:2048(WS))
```

- `M3:2048` computes the 2048-bit hash of a log entry in which exactly 3 bits are set. This is used to compute the Bloom filter of a log entry.

```k
    syntax Int ::= "M3:2048" "(" Bytes ")" [function]
 // -------------------------------------------------
    rule M3:2048(WS) => setBloomFilterBits(#parseByteStack(Keccak256(WS)))

    syntax Int ::= setBloomFilterBits(Bytes) [symbol(setBloomFilterBits), function]
 // -------------------------------------------------------------------------------
    rule setBloomFilterBits(HASH) => (1 <<Int getBloomFilterBit(HASH, 0)) |Int (1 <<Int getBloomFilterBit(HASH, 2)) |Int (1 <<Int getBloomFilterBit(HASH, 4))

    syntax Int ::= getBloomFilterBit(Bytes, Int) [symbol(getBloomFilterBit), function]
 // ----------------------------------------------------------------------------------
    rule getBloomFilterBit(X, I) => #asInteger(#range(X, I, 2)) %Int 2048
```

If `block.timestamp >= CANCUN_FORK_TIMESTAMP`:
Before executing any transaction, the `BEACON_ROOTS_ADDRESS` (`0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02`) storage is modified as following:
 - Set the storage value at `header.timestamp % HISTORY_BUFFER_LENGTH` to be `header.timestamp`
 - Set the storage value at `header.timestamp % HISTORY_BUFFER_LENGTH + HISTORY_BUFFER_LENGTH` to be `header.parent_beacon_root_hash`
where `HISTORY_BUFFER_LENGTH == 8191`.

Read more about EIP-4788 here [https://eips.ethereum.org/EIPS/eip-4788](https://eips.ethereum.org/EIPS/eip-4788).

```k
    syntax EthereumCommand ::= "#executeBeaconRoots" [symbol(#executeBeaconRoots)]
 // ------------------------------------------------------------------------------
    rule <k> #executeBeaconRoots => .K ... </k>
         <schedule> SCHED </schedule>
         <timestamp> TS </timestamp>
         <beaconRoot> BR </beaconRoot>
         <account>
           <acctID> 339909022928299415537769066420252604268194818 </acctID>
           <storage> M:Map => M [(TS modInt 8191) <- TS] [(TS modInt 8191 +Int 8191) <- BR] </storage>
           ...
         </account>
      requires Ghasbeaconroot << SCHED >>

    rule <k> #executeBeaconRoots => .K ... </k> [owise]
```

EVM Programs
============

EVM OpCodes
-----------


### Internal Operations

These are just used by the other operators for shuffling local execution state around on the EVM.

-   `#push` will push an element to the `wordStack` without any checks.
-   `#setStack_` will set the current stack to the given one.

```k
    syntax InternalOp ::= "#push" | "#setStack" WordStack
 // -----------------------------------------------------
    rule <k> W0:Int ~> #push => .K ... </k> <wordStack> WS => W0 : WS </wordStack>
    rule <k> #setStack WS    => .K ... </k> <wordStack> _  => WS      </wordStack>
```

-   `#newAccount_` allows declaring a new empty account with the given address (and assumes the rounding to 160 bits has already occurred).
    If the account already exists with non-zero nonce or non-empty code, an exception is thrown.
    Otherwise, if the account already exists, the storage is cleared.

```k
    syntax InternalOp ::= "#newAccount" Int
                        | "#newExistingAccount" Int
 // -----------------------------------------------
    rule <k> #newAccount ACCT => #newExistingAccount ACCT ... </k> <account> <acctID> ACCT </acctID> ... </account>
    rule <k> #newAccount ACCT => .K    ... </k>
             <accounts>
               ( .Bag
                  =>
                 <account>
                    <acctID> ACCT </acctID>
                    <balance>           0                  </balance>
                    <code>              .Bytes:AccountCode </code>
                    <storage>           .Map               </storage>
                    <origStorage>       .Map               </origStorage>
                    <nonce>             0                  </nonce>
                    <transientStorage> .Map          </transientStorage>
                 </account>
               )
               ...
             </accounts> [owise, preserves-definedness]

    rule <k> #newExistingAccount ACCT => #end EVMC_ACCOUNT_ALREADY_EXISTS ... </k>
         <account>
           <acctID> ACCT  </acctID>
           <code>   CODE  </code>
           <nonce>  NONCE </nonce>
           <storage> STORAGE </storage>
           ...
         </account>
      requires CODE =/=K .Bytes orBool NONCE =/=Int 0 orBool STORAGE =/=K .Map

    rule <k> #newExistingAccount ACCT => .K ... </k>
         <account>
           <acctID>      ACCT      </acctID>
           <code>        CODE      </code>
           <nonce>       0         </nonce>
           <storage>     .Map   </storage>
           <origStorage> _ => .Map </origStorage>
           ...
         </account>
      requires lengthBytes(CODE) ==Int 0
```

-   `#transferFunds` moves money from one account into another, creating the destination account if it doesn't exist.

```k
    syntax InternalOp ::= "#transferFunds" Int Int Int
                        | "#transferFundsToNonExistent" Int Int Int
 // ---------------------------------------------------------------
    rule <k> #transferFunds ACCT ACCT VALUE => .K ... </k>
         <account>
           <acctID> ACCT </acctID>
           <balance> ORIGFROM </balance>
           ...
         </account>
      requires VALUE <=Int ORIGFROM

    rule <k> #transferFunds ACCTFROM ACCTTO VALUE => .K ... </k>
         <account>
           <acctID> ACCTFROM </acctID>
           <balance> ORIGFROM => ORIGFROM -Word VALUE </balance>
           ...
         </account>
         <account>
           <acctID> ACCTTO </acctID>
           <balance> ORIGTO => ORIGTO +Word VALUE </balance>
           ...
         </account>
      requires ACCTFROM =/=K ACCTTO andBool VALUE <=Int ORIGFROM
      [preserves-definedness]

    rule <k> #transferFunds ACCTFROM _ACCTTO VALUE => #end EVMC_BALANCE_UNDERFLOW ... </k>
         <account>
           <acctID> ACCTFROM </acctID>
           <balance> ORIGFROM </balance>
           ...
         </account>
      requires VALUE >Int ORIGFROM

    rule <k> #transferFunds ACCTFROM ACCTTO VALUE => #transferFundsToNonExistent ACCTFROM ACCTTO VALUE ... </k> [owise]

    rule <k> #transferFundsToNonExistent ACCTFROM ACCTTO VALUE => #newAccount ACCTTO ~> #transferFunds ACCTFROM ACCTTO VALUE ... </k>
         <schedule> SCHED </schedule>
      requires ACCTFROM =/=K ACCTTO
       andBool (VALUE >Int 0 orBool notBool Gemptyisnonexistent << SCHED >>)

    rule <k> #transferFundsToNonExistent ACCTFROM ACCTTO 0 => .K ... </k>
         <schedule> SCHED </schedule>
      requires ACCTFROM =/=K ACCTTO
       andBool Gemptyisnonexistent << SCHED >>
```

- `#baseFeePerBlobGas` will compute the blob base fee as specified by EIPs 4844 and 7516

```k
    syntax Int ::= #baseFeePerBlobGas( Int ) [symbol(#baseFeePerBlobGas), function]
 // -------------------------------------------------------------------------------
    rule #baseFeePerBlobGas(BLOBGAS) => #fakeExponential(MIN_BASE_FEE_PER_BLOB_GAS, BLOBGAS, BLOB_BASE_FEE_UPDATE_FRACTION)
    syntax Int ::= "MIN_BASE_FEE_PER_BLOB_GAS" [macro] | "BLOB_BASE_FEE_UPDATE_FRACTION" [macro]
    rule MIN_BASE_FEE_PER_BLOB_GAS => 1
    rule BLOB_BASE_FEE_UPDATE_FRACTION => 3338477

    syntax Int ::= #fakeExponential(Int, Int, Int) [symbol(#fakeExponential), function]
                 | #fakeExponential(Int, Int, Int, Int, Int) [function]
 // -------------------------------------------------------------------
    rule #fakeExponential(FACTOR, NUMER, DENOM) => #fakeExponential(1, 0, FACTOR *Int DENOM, NUMER, DENOM)

    rule #fakeExponential(I, OUTPUT, ACCUM, NUMER, DENOM)
      => #fakeExponential(I +Int 1, OUTPUT +Int ACCUM, ACCUM *Int NUMER /Int (DENOM *Int I), NUMER, DENOM) requires ACCUM >Int 0
    rule #fakeExponential(_, OUTPUT, _, _, DENOM) => OUTPUT /Int DENOM [owise]
```

### Invalid Operator

We use `INVALID` both for marking the designated invalid operator, and `UNDEFINED(_)` for garbage bytes in the input program.

```k
    syntax InvalidOp ::= "INVALID" | "UNDEFINED" "(" Int ")"
 // --------------------------------------------------------
    rule <k> INVALID      => #end EVMC_INVALID_INSTRUCTION   ... </k>
    rule <k> UNDEFINED(_) => #end EVMC_UNDEFINED_INSTRUCTION ... </k>
```

### Stack Manipulations

Some operators don't calculate anything, they just push the stack around a bit.

```k
    syntax UnStackOp ::= "POP"
 // --------------------------
    rule <k> POP _ => .K ... </k>

    syntax StackOp ::= DUP  ( Int ) [symbol(DUP)]
                     | SWAP ( Int ) [symbol(SWAP)]
 // ----------------------------------------------
    rule <k> DUP(N)  WS:WordStack => #setStack ((WS [ N -Int 1 ]) : WS)                      ... </k>
    rule <k> SWAP(N) (W0 : WS)    => #setStack ((WS [ N -Int 1 ]) : (WS [ N -Int 1 := W0 ])) ... </k>

    syntax PushOp ::= "PUSHZERO"
                    | PUSH ( Int ) [symbol(PUSH)]
 // ---------------------------------------------
    rule <k> PUSHZERO => 0 ~> #push ... </k>

    rule <k> PUSH(N) => #asWord(#range(PGM, PCOUNT +Int 1, N)) ~> #push ... </k>
         <pc> PCOUNT </pc>
         <program> PGM </program>
```

### Local Memory

These operations are getters/setters of the local execution memory.

```k
    syntax UnStackOp ::= "MLOAD"
 // ----------------------------
    rule <k> MLOAD INDEX => #asWord(#range(LM, INDEX, 32)) ~> #push ... </k>
         <localMem> LM </localMem>

    syntax BinStackOp ::= "MSTORE" | "MSTORE8"
 // ------------------------------------------
    rule <k> MSTORE INDEX VALUE => .K ... </k>
         <localMem> LM => LM [ INDEX := #padToWidth(32, #asByteStack(VALUE)) ] </localMem>

    rule <k> MSTORE8 INDEX VALUE => .K ... </k>
         <localMem> LM => #write(LM, INDEX, (VALUE modInt 256)) </localMem>

    syntax TernStackOp ::= "MCOPY"
 // ------------------------------
     rule <k> MCOPY DST SRC LEN => .K ... </k>
          <localMem> LM => LM [ DST := #range(LM, SRC, LEN) ] </localMem>
```

### Expressions

Expression calculations are simple and don't require anything but the arguments from the `wordStack` to operate.

NOTE: We have to call the opcode `OR` by `EVMOR` instead, because K has trouble parsing it/compiling the definition otherwise.

```k
    syntax UnStackOp ::= "ISZERO" | "NOT"
 // -------------------------------------
    rule <k> ISZERO W => W ==Word 0 ~> #push ... </k>
    rule <k> NOT    W => ~Word W    ~> #push ... </k>

    syntax BinStackOp ::= "ADD" | "MUL" | "SUB" | "DIV" | "EXP" | "MOD"
 // -------------------------------------------------------------------
    rule <k> ADD W0 W1 => W0 +Word W1 ~> #push ... </k>
    rule <k> MUL W0 W1 => W0 *Word W1 ~> #push ... </k>
    rule <k> SUB W0 W1 => W0 -Word W1 ~> #push ... </k>
    rule <k> DIV W0 W1 => W0 /Word W1 ~> #push ... </k>
    rule <k> EXP W0 W1 => W0 ^Word W1 ~> #push ... </k>
    rule <k> MOD W0 W1 => W0 %Word W1 ~> #push ... </k>

    syntax BinStackOp ::= "SDIV" | "SMOD"
 // -------------------------------------
    rule <k> SDIV W0 W1 => W0 /sWord W1 ~> #push ... </k>
    rule <k> SMOD W0 W1 => W0 %sWord W1 ~> #push ... </k>

    syntax TernStackOp ::= "ADDMOD" | "MULMOD"
 // ------------------------------------------
    rule <k> ADDMOD W0 W1 W2 => (W0 +Int W1) %Word W2 ~> #push ... </k>
    rule <k> MULMOD W0 W1 W2 => (W0 *Int W1) %Word W2 ~> #push ... </k>

    syntax BinStackOp ::= "BYTE" | "SIGNEXTEND"
 // -------------------------------------------
    rule <k> BYTE INDEX W     => byte(INDEX, W)     ~> #push ... </k>
    rule <k> SIGNEXTEND W0 W1 => signextend(W0, W1) ~> #push ... </k>

    syntax BinStackOp ::= "SHL" | "SHR" | "SAR"
 // -------------------------------------------
    rule <k> SHL W0 W1 => W1 <<Word  W0 ~> #push ... </k>
    rule <k> SHR W0 W1 => W1 >>Word  W0 ~> #push ... </k>
    rule <k> SAR W0 W1 => W1 >>sWord W0 ~> #push ... </k>

    syntax BinStackOp ::= "AND" | "EVMOR" | "XOR"
 // ---------------------------------------------
    rule <k> AND   W0 W1 => W0 &Word W1   ~> #push ... </k>
    rule <k> EVMOR W0 W1 => W0 |Word W1   ~> #push ... </k>
    rule <k> XOR   W0 W1 => W0 xorWord W1 ~> #push ... </k>

    syntax BinStackOp ::= "LT" | "GT" | "EQ"
 // ----------------------------------------
    rule <k> LT W0 W1 => W0 <Word  W1 ~> #push ... </k>
    rule <k> GT W0 W1 => W0 >Word  W1 ~> #push ... </k>
    rule <k> EQ W0 W1 => W0 ==Word W1 ~> #push ... </k>

    syntax BinStackOp ::= "SLT" | "SGT"
 // -----------------------------------
    rule <k> SLT W0 W1 => W0 s<Word W1 ~> #push ... </k>
    rule <k> SGT W0 W1 => W1 s<Word W0 ~> #push ... </k>

    syntax BinStackOp ::= "SHA3"
 // ----------------------------
    rule <k> SHA3 MEMSTART MEMWIDTH => keccak(#range(LM, MEMSTART, MEMWIDTH)) ~> #push ... </k>
         <localMem> LM </localMem>
```

### Local State

These operators make queries about the current execution state.

```k
    syntax NullStackOp ::= "PC" | "GAS" | "GASPRICE" | "GASLIMIT" | "BASEFEE" | "BLOBBASEFEE"
 // -----------------------------------------------------------------------------------------
    rule <k> PC          => PCOUNT                      ~> #push ... </k> <pc> PCOUNT </pc>
    rule <k> GAS         => gas2Int(GAVAIL)             ~> #push ... </k> <gas> GAVAIL </gas>
    rule <k> GASPRICE    => GPRICE                      ~> #push ... </k> <gasPrice> GPRICE </gasPrice>
    rule <k> GASLIMIT    => GLIMIT                      ~> #push ... </k> <gasLimit> GLIMIT </gasLimit>
    rule <k> BASEFEE     => BFEE                        ~> #push ... </k> <baseFee> BFEE </baseFee>
    rule <k> BLOBBASEFEE => #baseFeePerBlobGas(BLOBGAS) ~> #push ... </k> <excessBlobGas> BLOBGAS </excessBlobGas>  requires notBool #rangeNegUInt64(BLOBGAS)

    syntax NullStackOp ::= "COINBASE" | "TIMESTAMP" | "NUMBER" | "DIFFICULTY" | "PREVRANDAO"
 // ----------------------------------------------------------------------------------------
    rule <k> COINBASE   => CB   ~> #push ... </k> <coinbase> CB </coinbase>
    rule <k> TIMESTAMP  => TS   ~> #push ... </k> <timestamp> TS </timestamp>
    rule <k> NUMBER     => NUMB ~> #push ... </k> <number> NUMB </number>
    rule <k> DIFFICULTY => DIFF ~> #push ... </k> <difficulty> DIFF </difficulty>
    rule <k> PREVRANDAO => RDAO ~> #push ... </k> <mixHash> RDAO </mixHash>

    syntax NullStackOp ::= "ADDRESS" | "ORIGIN" | "CALLER" | "CALLVALUE" | "CHAINID" | "SELFBALANCE"
 // ------------------------------------------------------------------------------------------------
    rule <k> ADDRESS     => ACCT ~> #push ... </k> <id> ACCT </id>
    rule <k> ORIGIN      => ORG  ~> #push ... </k> <origin> ORG </origin>
    rule <k> CALLER      => CL   ~> #push ... </k> <caller> CL </caller>
    rule <k> CALLVALUE   => CV   ~> #push ... </k> <callValue> CV </callValue>
    rule <k> CHAINID     => CID  ~> #push ... </k> <chainID> CID </chainID>
    rule <k> SELFBALANCE => BAL  ~> #push ... </k>
         <id> ACCT </id>
         <account>
            <acctID> ACCT </acctID>
            <balance> BAL </balance>
            ...
         </account>

    syntax NullStackOp ::= "MSIZE" | "CODESIZE"
 // -------------------------------------------
    rule <k> MSIZE    => 32 *Word MU         ~> #push ... </k> <memoryUsed> MU </memoryUsed>
    rule <k> CODESIZE => lengthBytes(PGM) ~> #push ... </k> <program> PGM </program>

    syntax TernStackOp ::= "CODECOPY"
 // ---------------------------------
    rule <k> CODECOPY MEMSTART PGMSTART WIDTH => .K ... </k>
         <program> PGM </program>
         <localMem> LM =>  LM [ MEMSTART := #range(PGM, PGMSTART, WIDTH) ] </localMem>

    syntax UnStackOp ::= "BLOCKHASH"
 // --------------------------------
```

The blockhash is calculated here using the "shortcut" formula used for running tests.

```k
    rule <k> BLOCKHASH N => #blockhash(HASHES, N, HI -Int 1, 0) ~> #push ... </k>
         <number>      HI     </number>
         <blockhashes> HASHES </blockhashes>

    syntax Int ::= #blockhash ( List , Int , Int , Int ) [symbol(#blockhash), function]
 // -----------------------------------------------------------------------------------
    rule #blockhash(_, N, HI, _) => 0 requires N >Int HI
    rule #blockhash(_, _, _, 256) => 0
    rule #blockhash(ListItem(0) _, _, _, _) => 0
    rule #blockhash(ListItem(H) _, N, N, _) => H
    rule #blockhash(ListItem(_) L, N, HI, A) => #blockhash(L, N, HI -Int 1, A +Int 1) [owise]
```

```k
    syntax UnStackOp ::= "BLOBHASH"
 // -------------------------------

    rule <k> BLOBHASH INDEX => 0 ~> #push ... </k>
         <versionedHashes> HASHES </versionedHashes>
       requires INDEX >=Int size(HASHES)

    rule <k> BLOBHASH INDEX => #asWord( {HASHES[INDEX]}:>Bytes ) ~> #push ... </k>
         <versionedHashes> HASHES </versionedHashes>
       requires INDEX <Int size(HASHES)
```

EVM OpCodes
-----------

### EVM Control Flow

The `JUMP*` family of operations affect the current program counter.

```k
    syntax NullStackOp ::= "JUMPDEST"
 // ---------------------------------
    rule <k> JUMPDEST => .K ... </k>

    syntax UnStackOp ::= "JUMP"
 // ---------------------------
    rule [jump]:
         <k> JUMP DEST => #endBasicBlock ... </k>
         <pc> _ => DEST </pc>
         <jumpDests> DESTS </jumpDests>
      requires DEST <Int lengthBytes(DESTS) andBool DESTS[DEST] ==Int 1

    rule <k> JUMP _ => #end EVMC_BAD_JUMP_DESTINATION ... </k> [owise]

    syntax BinStackOp ::= "JUMPI"
 // -----------------------------
    rule [jumpi.false]: <k> JUMPI _DEST I => .K        ... </k> requires I  ==Int 0
    rule [jumpi.true]:  <k> JUMPI  DEST I => JUMP DEST ... </k> requires I =/=Int 0

    syntax InternalOp ::= "#endBasicBlock"
 // --------------------------------------
    rule                    <k> #endBasicBlock ~> (_:OpCode => .K) ... </k>
    rule [end-basic-block]: <k> (#endBasicBlock => .K) ~> #execute ... </k>
```

### `STOP`, `REVERT`, and `RETURN`

```k
    syntax NullStackOp ::= "STOP"
 // -----------------------------
    rule <k> STOP => #end EVMC_SUCCESS ... </k>
         <output> _ => .Bytes </output>

    syntax BinStackOp ::= "RETURN"
 // ------------------------------
    rule <k> RETURN RETSTART RETWIDTH => #end EVMC_SUCCESS ... </k>
         <output> _ => #range(LM, RETSTART, RETWIDTH) </output>
         <localMem> LM </localMem>

    syntax BinStackOp ::= "REVERT"
 // ------------------------------
    rule <k> REVERT RETSTART RETWIDTH => #end EVMC_REVERT ... </k>
         <output> _ => #range(LM, RETSTART, RETWIDTH) </output>
         <localMem> LM </localMem>
```

### Call Data

These operators query about the current `CALL*` state.

```k
    syntax NullStackOp ::= "CALLDATASIZE"
 // -------------------------------------
    rule <k> CALLDATASIZE => lengthBytes(CD) ~> #push ... </k>
         <callData> CD </callData>

    syntax UnStackOp ::= "CALLDATALOAD"
 // -----------------------------------
    rule <k> CALLDATALOAD DATASTART => #asWord(#range(CD, DATASTART, 32)) ~> #push ... </k>
         <callData> CD </callData>

    syntax TernStackOp ::= "CALLDATACOPY"
 // -------------------------------------
    rule <k> CALLDATACOPY MEMSTART DATASTART DATAWIDTH => .K ... </k>
         <localMem> LM => LM [ MEMSTART := #range(CD, DATASTART, DATAWIDTH) ] </localMem>
         <callData> CD </callData>
```

### Return Data

These operators query about the current return data buffer.

```k
    syntax NullStackOp ::= "RETURNDATASIZE"
 // ---------------------------------------
    rule <k> RETURNDATASIZE => lengthBytes(RD) ~> #push ... </k>
         <output> RD </output>

    syntax TernStackOp ::= "RETURNDATACOPY"
 // ---------------------------------------
    rule <k> RETURNDATACOPY MEMSTART DATASTART DATAWIDTH => .K ... </k>
         <localMem> LM => LM [ MEMSTART := #range(RD, DATASTART, DATAWIDTH) ] </localMem>
         <output> RD </output>
      requires DATASTART +Int DATAWIDTH <=Int lengthBytes(RD)

    rule <k> RETURNDATACOPY _MEMSTART DATASTART DATAWIDTH => #end EVMC_INVALID_MEMORY_ACCESS ... </k>
         <output> RD </output>
      requires DATASTART +Int DATAWIDTH >Int lengthBytes(RD)
```

### Log Operations

```k
    syntax BinStackOp ::= LogOp
    syntax LogOp ::= LOG ( Int ) [symbol(LOG)]
 // ------------------------------------------
    rule <k> LOG(N) MEMSTART MEMWIDTH => .K ... </k>
         <id> ACCT </id>
         <wordStack> WS => #drop(N, WS) </wordStack>
         <localMem> LM </localMem>
         <log> L => L ListItem({ ACCT | WordStack2List(#take(N, WS)) | #range(LM, MEMSTART, MEMWIDTH) }) </log>
      requires #sizeWordStack(WS) >=Int N
```

Ethereum Network OpCodes
------------------------

Operators that require access to the rest of the Ethereum network world-state can be taken as a first draft of a "blockchain generic" language.

### Account Queries

```k
    syntax UnStackOp ::= "BALANCE"
 // ------------------------------
    rule [balance.true]:
         <k> BALANCE ACCT => #accessAccounts ACCT ~> BAL ~> #push ... </k>
         <account>
           <acctID> ACCT </acctID>
           <balance> BAL </balance>
           ...
         </account>

    rule [balance.false]: <k> BALANCE ACCT => #accessAccounts ACCT ~> 0 ~> #push ... </k> [owise]

    syntax UnStackOp ::= "EXTCODESIZE"
 // ----------------------------------
    rule [extcodesize.true]:
         <k> EXTCODESIZE ACCT => #accessAccounts ACCT ~> lengthBytes(CODE) ~> #push ... </k>
         <account>
           <acctID> ACCT </acctID>
           <code> CODE </code>
           ...
         </account>

    rule [extcodesize.false]: <k> EXTCODESIZE ACCT => #accessAccounts ACCT ~> 0 ~> #push ... </k> [owise]

    syntax UnStackOp ::= "EXTCODEHASH"
 // ----------------------------------
    rule [extcodehash.true]:
         <k> EXTCODEHASH ACCT => #accessAccounts ACCT ~> keccak(CODE) ~> #push ... </k>
         <account>
           <acctID> ACCT </acctID>
           <code> CODE:Bytes </code>
           <nonce> NONCE </nonce>
           <balance> BAL </balance>
           ...
         </account>
      requires notBool #accountEmpty(CODE, NONCE, BAL)

    rule [extcodehash.false]: <k> EXTCODEHASH ACCT => #accessAccounts ACCT ~> 0 ~> #push ... </k> [owise]

    syntax QuadStackOp ::= "EXTCODECOPY"
 // ------------------------------------
    rule [extcodecopy.true]:
         <k> EXTCODECOPY ACCT MEMSTART PGMSTART WIDTH => #accessAccounts ACCT ... </k>
         <localMem> LM => LM [ MEMSTART := #range(PGM, PGMSTART, WIDTH) ] </localMem>
         <account>
           <acctID> ACCT </acctID>
           <code> PGM </code>
           ...
         </account>

    rule [extcodecopy.false]:
         <k> EXTCODECOPY ACCT MEMSTART _ WIDTH => #accessAccounts ACCT ... </k>
         <localMem> LM => LM [ MEMSTART := #padToWidth(WIDTH, .Bytes) ] </localMem> [owise]
```

### Account Storage Operations

These rules reach into the network state and load/store from account storage:

```k
    syntax UnStackOp ::= "SLOAD"
 // ----------------------------
    rule [sload]:
         <k> SLOAD INDEX => #lookup(STORAGE, INDEX) ~> #push ... </k>
         <id> ACCT </id>
         <account>
           <acctID> ACCT </acctID>
           <storage> STORAGE </storage>
           ...
         </account>

    syntax BinStackOp ::= "SSTORE"
 // ------------------------------
    rule [sstore]:
         <k> SSTORE INDEX NEW => .K ... </k>
         <id> ACCT </id>
         <account>
           <acctID> ACCT </acctID>
           <storage> STORAGE => STORAGE [ INDEX <- NEW ] </storage>
           ...
         </account>
      [preserves-definedness]

    syntax UnStackOp ::= "TLOAD"
 // ----------------------------
    rule [tload]:
         <k> TLOAD INDEX => #lookup(TSTORAGE, INDEX) ~> #push ... </k>
         <id> ACCT </id>
         <account>
           <acctID> ACCT </acctID>
           <transientStorage> TSTORAGE </transientStorage>
           ...
         </account>

    syntax BinStackOp ::= "TSTORE"
 // ------------------------------
    rule [tstore]:
         <k> TSTORE INDEX NEW => .K ... </k>
         <id> ACCT </id>
         <account>
           <acctID> ACCT </acctID>
           <transientStorage> TSTORAGE => TSTORAGE [ INDEX <- NEW ] </transientStorage>
           ...
         </account>
      [preserves-definedness]
```

### Call Operations

The various `CALL*` (and other inter-contract control flow) operations will be desugared into these `InternalOp`s.

-   `#checkCall` takes the calling account and the value of the call and triggers several checks before executing the call.
-   `#checkBalanceUnderflow` takes the calling account and the value of the call and checks if the call value is greater than the account balance.
-   `#checkDepthExceeded` checks if the current call depth is greater than or equal to `1024`.
-   `#checkNonceExceeded` takes the calling account and checks if the nonce is less than `maxUInt64` (`18446744073709551615`).
-   `#call` takes the calling account, the account to execute as, the account whose code should execute, the gas limit, the amount to transfer, the arguments, and the static flag.
-   `#callWithCode` takes the calling account, the account to execute as, the code to execute (as a `Bytes`), the gas limit, the amount to transfer, the arguments, and the static flag.
-   `#return` is a placeholder for the calling program, specifying where to place the returned data in memory.

```k
    syntax InternalOp ::= "#checkCall"             Int Int
                        | "#checkBalanceUnderflow" Int Int
                        | "#checkNonceExceeded"    Int
                        | "#checkDepthExceeded"
                        | "#call"                  Int Int Int Int Int Bytes Bool
                        | "#callWithCode"          Int Int Int Bytes Int Int Bytes Bool [symbol(callwithcode_check_fork)]
                        | "#mkCall"                Int Int Int Bytes     Int Bytes Bool
 // -----------------------------------------------------------------------------------
     rule <k> #checkBalanceUnderflow ACCT VALUE => #refund GCALL ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALANCE_UNDERFLOW ... </k>
         <output> _ => .Bytes </output>
         <callGas> GCALL </callGas>
         <account>
           <acctID> ACCT </acctID>
           <balance> BAL </balance>
           ...
         </account>
      requires VALUE >Int BAL

    rule <k> #checkBalanceUnderflow ACCT VALUE => .K ... </k>
         <account>
           <acctID> ACCT </acctID>
           <balance> BAL </balance>
           ...
         </account>
      requires VALUE <=Int BAL

    rule <k> #checkDepthExceeded => #refund GCALL ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_CALL_DEPTH_EXCEEDED ... </k>
         <output> _ => .Bytes </output>
         <callGas> GCALL </callGas>
         <callDepth> CD </callDepth>
      requires CD >=Int 1024

    rule <k> #checkDepthExceeded => .K ... </k>
         <callDepth> CD </callDepth>
      requires CD <Int 1024

    rule <k> #checkNonceExceeded ACCT => #refund GCALL ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_NONCE_EXCEEDED ... </k>
         <output> _ => .Bytes </output>
         <callGas> GCALL </callGas>
         <account>
           <acctID> ACCT </acctID>
           <nonce> NONCE </nonce>
           ...
         </account>
      requires notBool #rangeNonce(NONCE)

    rule <k> #checkNonceExceeded ACCT => .K ... </k>
         <account>
           <acctID> ACCT </acctID>
           <nonce> NONCE </nonce>
           ...
         </account>
      requires #rangeNonce(NONCE)

    rule <k> #checkCall ACCT VALUE => #checkBalanceUnderflow ACCT VALUE ~> #checkDepthExceeded ... </k>

    rule [call.true]:
         <k> #call ACCTFROM ACCTTO ACCTCODE VALUE APPVALUE ARGS STATIC
          => #callWithCode ACCTFROM ACCTTO ACCTCODE CODE VALUE APPVALUE ARGS STATIC
         ...
         </k>
         <account>
           <acctID> ACCTCODE </acctID>
           <code> CODE </code>
           ...
         </account>

    rule [call.false]:
         <k> #call ACCTFROM ACCTTO ACCTCODE VALUE APPVALUE ARGS STATIC
          => #callWithCode ACCTFROM ACCTTO ACCTCODE .Bytes VALUE APPVALUE ARGS STATIC
         ...
         </k> [owise]

    rule <k> #callWithCode ACCTFROM ACCTTO ACCTCODE BYTES VALUE APPVALUE ARGS STATIC
          => #pushCallStack ~> #pushWorldState
          ~> #transferFunds ACCTFROM ACCTTO VALUE
          ~> #mkCall ACCTFROM ACCTTO ACCTCODE BYTES APPVALUE ARGS STATIC
         ...
         </k>

    rule <k> #mkCall ACCTFROM ACCTTO ACCTCODE BYTES APPVALUE ARGS STATIC:Bool
          => #touchAccounts ACCTFROM ACCTTO ~> #accessAccounts ACCTFROM ACCTTO ~> #loadProgram BYTES ~> #initVM ~> #precompiled?(ACCTCODE, SCHED) ~> #execute
         ...
         </k>
         <useGas> USEGAS:Bool </useGas>
         <callDepth> CD => CD +Int 1 </callDepth>
         <callData> _ => ARGS </callData>
         <callValue> _ => APPVALUE </callValue>
         <id> _ => ACCTTO </id>
         <gas> GAVAIL:Gas => #if USEGAS #then GCALL:Gas #else GAVAIL:Gas #fi </gas>
         <callGas> GCALL:Gas => #if USEGAS #then 0:Gas #else GCALL:Gas #fi </callGas>
         <caller> _ => ACCTFROM </caller>
         <static> OLDSTATIC:Bool => OLDSTATIC orBool STATIC </static>
         <schedule> SCHED </schedule>

    syntax InternalOp ::= "#precompiled?" "(" Int "," Schedule ")"
 // --------------------------------------------------------------
    rule [precompile.true]:  <k> #precompiled?(ACCTCODE, SCHED) => #next [ #precompiled(ACCTCODE) ] ... </k> requires         #isPrecompiledAccount(ACCTCODE, SCHED) [preserves-definedness]
    rule [precompile.false]: <k> #precompiled?(ACCTCODE, SCHED) => .K                               ... </k> requires notBool #isPrecompiledAccount(ACCTCODE, SCHED)

    syntax Bool ::= #isPrecompiledAccount ( Int , Schedule ) [symbol(isPrecompiledAccount), function, total, smtlib(isPrecompiledAccount)]
 // --------------------------------------------------------------------------------------------------------------------------------------
    rule [isPrecompiledAccount]:  #isPrecompiledAccount(ACCTCODE, SCHED) => 0 <Int ACCTCODE andBool ACCTCODE <=Int #precompiledAccountsUB(SCHED)

    syntax KItem ::= "#initVM"
 // --------------------------
    rule <k> #initVM      => .K ...      </k>
         <pc>           _ => 0          </pc>
         <memoryUsed>   _ => 0          </memoryUsed>
         <output>       _ => .Bytes     </output>
         <wordStack>    _ => .WordStack </wordStack>
         <localMem>     _ => .Bytes     </localMem>

    syntax KItem ::= "#loadProgram" Bytes [symbol(loadProgram)]
 // -----------------------------------------------------------
    rule [program.load]:
         <k> #loadProgram BYTES => .K ... </k>
         <program> _ => BYTES </program>
         <jumpDests> _ => #computeValidJumpDests(BYTES) </jumpDests>

    syntax KItem ::= "#touchAccounts" Account | "#touchAccounts" Account Account
 // ----------------------------------------------------------------------------
    rule <k> #touchAccounts ADDR1 ADDR2 => #touchAccounts ADDR1 ~> #touchAccounts ADDR2 ... </k>

    rule <k> #touchAccounts ADDR => .K ... </k>
         <touchedAccounts> TOUCHED_ACCOUNTS => TOUCHED_ACCOUNTS |Set SetItem(ADDR) </touchedAccounts>

    syntax KItem ::= "#accessStorage" Account Int
 // ---------------------------------------------
    rule <k> #accessStorage ACCT INDEX => .K ... </k>
         <accessedStorage> ... ACCT |-> (TS:Set => TS |Set SetItem(INDEX)) ... </accessedStorage>
         <schedule> SCHED </schedule>
         requires Ghasaccesslist << SCHED >>
         [preserves-definedness]

    rule <k> #accessStorage ACCT INDEX => .K ... </k>
         <accessedStorage> TS => TS[ACCT <- SetItem(INDEX)] </accessedStorage>
         <schedule> SCHED </schedule>
      requires Ghasaccesslist << SCHED >> andBool notBool ACCT in_keys(TS)

    rule <k> #accessStorage _ _ => .K ... </k>
         <schedule> SCHED </schedule>
      requires notBool Ghasaccesslist << SCHED >>

    syntax KItem ::= "#accessAccounts" Account
                   | "#accessAccounts" Set
                   | "#accessAccounts" Account Account
                   | "#accessAccounts" Account Account Set
 // ------------------------------------------------------
    rule <k> #accessAccounts ADDR1:Account ADDR2:Account ADDRSET:Set => #accessAccounts ADDR1 ~> #accessAccounts ADDR2 ~> #accessAccounts ADDRSET ... </k>

    rule <k> #accessAccounts ADDR1:Account ADDR2:Account => #accessAccounts ADDR1 ~> #accessAccounts ADDR2 ... </k>

    rule <k> #accessAccounts ADDR:Account => .K ... </k>
         <accessedAccounts> TOUCHED_ACCOUNTS => TOUCHED_ACCOUNTS |Set SetItem(ADDR) </accessedAccounts>

    rule <k> #accessAccounts ADDRSET:Set => .K ... </k>
         <accessedAccounts> TOUCHED_ACCOUNTS => TOUCHED_ACCOUNTS |Set ADDRSET </accessedAccounts>

    syntax Bytes ::= #computeValidJumpDests(Bytes)             [symbol(computeValidJumpDests),    function, memo, total]
                   | #computeValidJumpDests(Bytes, Int, Bytes) [symbol(computeValidJumpDestsAux), function             ]
 // --------------------------------------------------------------------------------------------------------------------
    rule #computeValidJumpDests(PGM) => #computeValidJumpDests(PGM, 0, padRightBytes(.Bytes, lengthBytes(PGM), 0))

    syntax Bytes ::= #computeValidJumpDestsWithinBound(Bytes, Int, Bytes) [symbol(computeValidJumpDestsWithinBound), function]
 // --------------------------------------------------------------------------------------------------------------------------
    rule #computeValidJumpDests(PGM, I, RESULT) => RESULT requires I >=Int lengthBytes(PGM)
    rule #computeValidJumpDests(PGM, I, RESULT) => #computeValidJumpDestsWithinBound(PGM, I, RESULT) requires I <Int lengthBytes(PGM)

    rule #computeValidJumpDestsWithinBound(PGM, I, RESULT) => #computeValidJumpDests(PGM, I +Int 1, RESULT[I <- 1]) requires PGM [ I ] ==Int 91
    rule #computeValidJumpDestsWithinBound(PGM, I, RESULT) => #computeValidJumpDests(PGM, I +Int #widthOpCode(PGM [ I ]), RESULT) requires notBool PGM [ I ] ==Int 91
```

```k
    syntax Int ::= #widthOpCode(Int) [symbol(#widthOpCode), function]
 // -----------------------------------------------------------------
    rule #widthOpCode(W) => W -Int 94 requires W >=Int 96 andBool W <=Int 127
    rule #widthOpCode(_) => 1 [owise]

    syntax KItem ::= "#return" Int Int
 // ----------------------------------
    rule [return.exception]:
         <statusCode> _:ExceptionalStatusCode </statusCode>
         <k> #halt ~> #return _ _
          => #popCallStack ~> #popWorldState ~> 0 ~> #push
         ...
         </k>
         <output> _ => .Bytes </output>

    rule [return.revert]:
         <statusCode> EVMC_REVERT </statusCode>
         <k> #halt ~> #return RETSTART RETWIDTH
          => #popCallStack ~> #popWorldState
          ~> 0 ~> #push ~> #refund GAVAIL ~> #setLocalMem RETSTART RETWIDTH OUT
         ...
         </k>
         <output> OUT </output>
         <gas> GAVAIL </gas>

    rule [return.success]:
         <statusCode> EVMC_SUCCESS </statusCode>
         <k> #halt ~> #return RETSTART RETWIDTH
          => #popCallStack ~> #dropWorldState
          ~> 1 ~> #push ~> #refund GAVAIL ~> #setLocalMem RETSTART RETWIDTH OUT
         ...
         </k>
         <output> OUT </output>
         <gas> GAVAIL </gas>

    syntax InternalOp ::= "#refund" Gas
                        | "#setLocalMem" Int Int Bytes
 // --------------------------------------------------
    rule [refund]: <k> #refund G:Gas => .K ... </k> <gas> GAVAIL => GAVAIL +Gas G </gas> <useGas> true </useGas>
    rule [refund.noGas]: <k> #refund _ => .K ... </k> <useGas> false </useGas>


    rule <k> #setLocalMem START WIDTH WS => .K ... </k>
         <localMem> LM => LM [ START := #range(WS, 0, minInt(WIDTH, lengthBytes(WS))) ] </localMem>
```

Ethereum Network OpCodes
------------------------

### Call Operations

For each `CALL*` operation, we make a corresponding call to `#call` and a state-change to setup the custom parts of the calling environment.

```k
    syntax CallOp ::= "CALL"
 // ------------------------
    rule [call]:
         <k> CALL _GCAP ACCTTO VALUE ARGSTART ARGWIDTH RETSTART RETWIDTH
          => #accessAccounts ACCTTO
          ~> #checkCall ACCTFROM VALUE
          ~> #call ACCTFROM ACCTTO ACCTTO VALUE VALUE #range(LM, ARGSTART, ARGWIDTH) false
          ~> #return RETSTART RETWIDTH
         ...
         </k>
         <id> ACCTFROM </id>
         <localMem> LM </localMem>

    syntax CallOp ::= "CALLCODE"
 // ----------------------------
    rule [callcode]:
         <k> CALLCODE _GCAP ACCTTO VALUE ARGSTART ARGWIDTH RETSTART RETWIDTH
          => #accessAccounts ACCTTO
          ~> #checkCall ACCTFROM VALUE
          ~> #call ACCTFROM ACCTFROM ACCTTO VALUE VALUE #range(LM, ARGSTART, ARGWIDTH) false
          ~> #return RETSTART RETWIDTH
         ...
         </k>
         <id> ACCTFROM </id>
         <localMem> LM </localMem>

    syntax CallSixOp ::= "DELEGATECALL"
 // -----------------------------------
    rule [delegatecall]:
         <k> DELEGATECALL _GCAP ACCTTO ARGSTART ARGWIDTH RETSTART RETWIDTH
          => #accessAccounts ACCTTO
          ~> #checkCall ACCTFROM 0
          ~> #call ACCTAPPFROM ACCTFROM ACCTTO 0 VALUE #range(LM, ARGSTART, ARGWIDTH) false
          ~> #return RETSTART RETWIDTH
         ...
         </k>
         <id> ACCTFROM </id>
         <caller> ACCTAPPFROM </caller>
         <callValue> VALUE </callValue>
         <localMem> LM </localMem>

    syntax CallSixOp ::= "STATICCALL"
 // ---------------------------------
    rule [staticcall]:
         <k> STATICCALL _GCAP ACCTTO ARGSTART ARGWIDTH RETSTART RETWIDTH
          => #accessAccounts ACCTTO
          ~> #checkCall ACCTFROM 0
          ~> #call ACCTFROM ACCTTO ACCTTO 0 0 #range(LM, ARGSTART, ARGWIDTH) true
          ~> #return RETSTART RETWIDTH
         ...
         </k>
         <id> ACCTFROM </id>
         <localMem> LM </localMem>
```

### Account Creation/Deletion

-   `#create____` transfers the endowment to the new account and triggers the execution of the initialization code.
-   `#codeDeposit_` checks the result of initialization code and whether the code deposit can be paid, indicating an error if not.
-   `#isValidCode_` checks if the code returned by the execution of the initialization code begins with a reserved byte. [EIP-3541]
-   `#hasValidInitCode` checks the length of the transaction data in a create transaction. [EIP-3860]

```k
    syntax InternalOp ::= "#create"   Int Int Int Bytes
                        | "#mkCreate" Int Int Int Bytes
                        | "#incrementNonce" Int
                        | "#checkCreate" Int Int
 // --------------------------------------------
    rule <k> #create ACCTFROM ACCTTO VALUE INITCODE
          => #incrementNonce ACCTFROM
          ~> #pushCallStack ~> #pushWorldState
          ~> #newAccount ACCTTO
          ~> #transferFunds ACCTFROM ACCTTO VALUE
          ~> #mkCreate ACCTFROM ACCTTO VALUE INITCODE
         ...
         </k>

    rule <k> #mkCreate ACCTFROM ACCTTO VALUE INITCODE
          => #touchAccounts ACCTFROM ACCTTO ~> #accessAccounts ACCTFROM ACCTTO ~> #loadProgram INITCODE ~> #initVM ~> #execute
         ...
         </k>
         <useGas> USEGAS </useGas>
         <schedule> SCHED </schedule>
         <id> _ => ACCTTO </id>
         <gas> GAVAIL => #if USEGAS #then GCALL #else GAVAIL #fi </gas>
         <callGas> GCALL => #if USEGAS #then 0 #else GCALL #fi </callGas>
         <caller> _ => ACCTFROM </caller>
         <callDepth> CD => CD +Int 1 </callDepth>
         <callData> _ => .Bytes </callData>
         <callValue> _ => VALUE </callValue>
         <account>
           <acctID> ACCTTO </acctID>
           <nonce> NONCE => #if Gemptyisnonexistent << SCHED >> #then NONCE +Int 1 #else NONCE #fi </nonce>
           ...
         </account>
         <createdAccounts> ACCTS => ACCTS |Set SetItem(ACCTTO) </createdAccounts>

    rule <k> #incrementNonce ACCT => .K ... </k>
         <account>
           <acctID> ACCT </acctID>
           <nonce> NONCE => NONCE +Int 1 </nonce>
           ...
         </account>

    syntax Bool ::= #hasValidInitCode ( Int , Schedule ) [symbol(#hasValidInitCode), function]
 // ------------------------------------------------------------------------------------------
    rule #hasValidInitCode(INITCODELEN, SCHED) => notBool Ghasmaxinitcodesize << SCHED >> orBool INITCODELEN <=Int maxInitCodeSize < SCHED >

    syntax Bool ::= #isValidCode ( Bytes , Schedule ) [symbol(#isValidCode), function]
 // ----------------------------------------------------------------------------------
    rule #isValidCode( OUT ,  SCHED) => Ghasrejectedfirstbyte << SCHED >> impliesBool OUT[0] =/=Int 239 requires lengthBytes(OUT) >Int 0
    rule #isValidCode(_OUT , _SCHED) => true                                                            [owise]

    syntax KItem ::= "#codeDeposit" Int
                   | "#mkCodeDeposit" Int
                   | "#finishCodeDeposit" Int Bytes
 // -----------------------------------------------
    rule <statusCode> _:ExceptionalStatusCode </statusCode>
         <k> #halt ~> #codeDeposit _ => #popCallStack ~> #popWorldState ~> 0 ~> #push ... </k> <output> _ => .Bytes </output>

    rule <statusCode> EVMC_REVERT </statusCode>
         <k> #halt ~> #codeDeposit _ => #popCallStack ~> #popWorldState ~> #refund GAVAIL ~> 0 ~> #push ... </k>
         <gas> GAVAIL </gas>

    rule <statusCode> EVMC_SUCCESS </statusCode>
         <k> #halt ~> #codeDeposit ACCT => #mkCodeDeposit ACCT ... </k>

    rule <k> #mkCodeDeposit ACCT
          => Gcodedeposit < SCHED > *Int lengthBytes(OUT) ~> #deductGas
          ~> #finishCodeDeposit ACCT OUT
         ...
         </k>
         <schedule> SCHED </schedule>
         <output> OUT => .Bytes </output>
      requires lengthBytes(OUT) <=Int maxCodeSize < SCHED > andBool #isValidCode(OUT, SCHED)

    rule <k> #mkCodeDeposit _ACCT => #popCallStack ~> #popWorldState ~> 0 ~> #push ... </k>
         <schedule> SCHED </schedule>
         <output> OUT => .Bytes </output>
      requires notBool ( lengthBytes(OUT) <=Int maxCodeSize < SCHED > andBool #isValidCode(OUT, SCHED) )

    rule <k> #finishCodeDeposit ACCT OUT
          => #popCallStack ~> #dropWorldState
          ~> #refund GAVAIL ~> ACCT ~> #push
         ...
         </k>
         <gas> GAVAIL </gas>
         <account>
           <acctID> ACCT </acctID>
           <code> _ => OUT </code>
           ...
         </account>

    rule <statusCode> _:ExceptionalStatusCode </statusCode>
         <k> #halt ~> #finishCodeDeposit ACCT _
          => #popCallStack ~> #dropWorldState
          ~> #refund GAVAIL ~> ACCT ~> #push
         ...
         </k>
         <gas> GAVAIL </gas>
         <schedule> FRONTIER </schedule>

    rule <statusCode> _:ExceptionalStatusCode </statusCode>
         <k> #halt ~> #finishCodeDeposit _ _ => #popCallStack ~> #popWorldState ~> 0 ~> #push ... </k>
         <schedule> SCHED </schedule>
      requires SCHED =/=K FRONTIER

    rule <k> #checkCreate ACCT VALUE => #checkBalanceUnderflow ACCT VALUE ~> #checkDepthExceeded ~> #checkNonceExceeded ACCT ... </k>
```

`CREATE` will attempt to `#create` the account using the initialization code and cleans up the result with `#codeDeposit`.

```k
    syntax TernStackOp ::= "CREATE"
 // -------------------------------
    rule [create-valid]:
         <k> CREATE VALUE MEMSTART MEMWIDTH
          => #accessAccounts #newAddr(ACCT, NONCE)
          ~> #checkCreate ACCT VALUE
          ~> #create ACCT #newAddr(ACCT, NONCE) VALUE #range(LM, MEMSTART, MEMWIDTH)
          ~> #codeDeposit #newAddr(ACCT, NONCE)
         ...
         </k>
         <id> ACCT </id>
         <localMem> LM </localMem>
         <account>
           <acctID> ACCT </acctID>
           <nonce> NONCE </nonce>
           ...
         </account>
         <schedule> SCHED </schedule>
      requires #hasValidInitCode(MEMWIDTH, SCHED)
      [preserves-definedness]

    rule [create-invalid]:
         <k> CREATE _ _ _ => #end EVMC_OUT_OF_GAS ... </k> [owise]
```

`CREATE2` will attempt to `#create` the account, but with the new scheme for choosing the account address.

```k
    syntax QuadStackOp ::= "CREATE2"
 // --------------------------------
    rule [create2-valid]:
         <k> CREATE2 VALUE MEMSTART MEMWIDTH SALT
          => #accessAccounts #newAddr(ACCT, SALT, #range(LM, MEMSTART, MEMWIDTH))
          ~> #checkCreate ACCT VALUE
          ~> #create ACCT #newAddr(ACCT, SALT, #range(LM, MEMSTART, MEMWIDTH)) VALUE #range(LM, MEMSTART, MEMWIDTH)
          ~> #codeDeposit #newAddr(ACCT, SALT, #range(LM, MEMSTART, MEMWIDTH))
         ...
         </k>
         <id> ACCT </id>
         <localMem> LM </localMem>
         <schedule> SCHED </schedule>
      requires #hasValidInitCode(MEMWIDTH, SCHED)

    rule [create2-invalid]:
         <k> CREATE2 _ _ _ _ => #end EVMC_OUT_OF_GAS ... </k> [owise]
```

`SELFDESTRUCT` marks the current account for deletion and transfers funds out of the current account.
Self destructing to yourself, unlike a regular transfer, destroys the balance in the account, irreparably losing it.

```k
    syntax UnStackOp ::= "SELFDESTRUCT"
 // -----------------------------------
    rule <k> SELFDESTRUCT ACCTTO => #touchAccounts ACCT ACCTTO ~> #accessAccounts ACCTTO ~> #transferFunds ACCT ACCTTO BALFROM ~> #end EVMC_SUCCESS ... </k>
         <schedule> SCHED </schedule>
         <id> ACCT </id>
         <selfDestruct> SDS => SDS |Set SetItem(ACCT) </selfDestruct>
         <account>
           <acctID> ACCT </acctID>
           <balance> BALFROM </balance>
           ...
         </account>
         <output> _ => .Bytes </output>
         <createdAccounts> CA </createdAccounts>
      requires ((notBool Ghaseip6780 << SCHED >>) orBool ACCT in CA)
       andBool ACCT =/=Int ACCTTO

    rule <k> SELFDESTRUCT ACCT => #touchAccounts ACCT ~> #accessAccounts ACCT ~> #end EVMC_SUCCESS ... </k>
         <schedule> SCHED </schedule>
         <id> ACCT </id>
         <selfDestruct> SDS => SDS |Set SetItem(ACCT) </selfDestruct>
         <account>
           <acctID> ACCT </acctID>
           <balance> _ => 0 </balance>
           ...
         </account>
         <output> _ => .Bytes </output>
         <createdAccounts> CA </createdAccounts>
      requires ((notBool Ghaseip6780 << SCHED >>) orBool ACCT in CA)

    rule <k> SELFDESTRUCT ACCTTO => #touchAccounts ACCT ACCTTO ~> #accessAccounts ACCTTO ~> #transferFunds ACCT ACCTTO BALFROM ~> #end EVMC_SUCCESS ... </k>
         <schedule> SCHED </schedule>
         <id> ACCT </id>
         <account>
           <acctID> ACCT </acctID>
           <balance> BALFROM </balance>
           ...
         </account>
         <output> _ => .Bytes </output>
         <createdAccounts> CA </createdAccounts>
      requires Ghaseip6780 << SCHED >> andBool (notBool ACCT in CA)
       andBool ACCT =/=Int ACCTTO

    rule <k> SELFDESTRUCT ACCT => #touchAccounts ACCT ~> #accessAccounts ACCT ~> #end EVMC_SUCCESS ... </k>
         <schedule> SCHED </schedule>
         <id> ACCT </id>
         <output> _ => .Bytes </output>
         <createdAccounts> CA </createdAccounts>
      requires Ghaseip6780 << SCHED >> andBool (notBool ACCT in CA)
```

Precompiled Contracts
---------------------

-   `#precompiled` is a placeholder for the pre-compiled contracts of a given schedule. These contracts are located at contiguous addresses starting from 1.
-   `#precompiledAccountsUB`  returns the highest address (upper bound) of the precompiled contract accounts
-   `#precompiledAccountsSet` returns the set of addresses of the precompiled contract accounts

```k
    syntax NullStackOp   ::= PrecompiledOp
    syntax PrecompiledOp ::= #precompiled ( Int ) [symbol(#precompiled), function]
 // ------------------------------------------------------------------------------
    rule #precompiled(1) => ECREC
    rule #precompiled(2) => SHA256
    rule #precompiled(3) => RIP160
    rule #precompiled(4) => ID
    rule #precompiled(5) => MODEXP
    rule #precompiled(6) => ECADD
    rule #precompiled(7) => ECMUL
    rule #precompiled(8) => ECPAIRING
    rule #precompiled(9) => BLAKE2F

    syntax Int ::= #precompiledAccountsUB ( Schedule ) [symbol(#precompiledAccountsUB), function, total]
 // ----------------------------------------------------------------------------------------------------
    rule #precompiledAccountsUB(DEFAULT)           => 4
    rule #precompiledAccountsUB(FRONTIER)          => #precompiledAccountsUB(DEFAULT)
    rule #precompiledAccountsUB(HOMESTEAD)         => #precompiledAccountsUB(FRONTIER)
    rule #precompiledAccountsUB(TANGERINE_WHISTLE) => #precompiledAccountsUB(HOMESTEAD)
    rule #precompiledAccountsUB(SPURIOUS_DRAGON)   => #precompiledAccountsUB(TANGERINE_WHISTLE)
    rule #precompiledAccountsUB(BYZANTIUM)         => 8
    rule #precompiledAccountsUB(CONSTANTINOPLE)    => #precompiledAccountsUB(BYZANTIUM)
    rule #precompiledAccountsUB(PETERSBURG)        => #precompiledAccountsUB(CONSTANTINOPLE)
    rule #precompiledAccountsUB(ISTANBUL)          => 9
    rule #precompiledAccountsUB(BERLIN)            => #precompiledAccountsUB(ISTANBUL)
    rule #precompiledAccountsUB(LONDON)            => #precompiledAccountsUB(BERLIN)
    rule #precompiledAccountsUB(MERGE)             => #precompiledAccountsUB(LONDON)
    rule #precompiledAccountsUB(SHANGHAI)          => #precompiledAccountsUB(MERGE)
    rule #precompiledAccountsUB(CANCUN)            => #precompiledAccountsUB(SHANGHAI)


    syntax Set ::= #precompiledAccountsSet    ( Schedule ) [symbol(#precompiledAccountsSet),    function, total]
    syntax Set ::= #precompiledAccountsSetAux ( Int      ) [symbol(#precompiledAccountsSetAux), function, total]
 // ------------------------------------------------------------------------------------------------------------
    rule #precompiledAccountsSet(SCHED) => #precompiledAccountsSetAux(#precompiledAccountsUB(SCHED))

    rule #precompiledAccountsSetAux(N)  => .Set requires N <=Int 0
    rule #precompiledAccountsSetAux(N)  => SetItem(N) #precompiledAccountsSetAux(N -Int 1) [owise, preserves-definedness]
```

-   `ECREC` performs ECDSA public key recovery.
-   `SHA256` performs the SHA2-256 hash function.
-   `RIP160` performs the RIPEMD-160 hash function.
-   `ID` is the identity function (copies input to output).
-   `MODEXP` performs arbitrary-precision modular exponentiation.
-   `ECADD`  performs point addition on the elliptic curve alt_bn128.
-   `ECMUL` performs scalar multiplication on the elliptic curve alt_bn128.
-   `ECPAIRING` performs an optimal ate pairing check on the elliptic curve alt_bn128.
-   `BLAKE2F` performs the compression function F used in the BLAKE2 hashing algorithm.

```k
    syntax PrecompiledOp ::= "ECREC"
 // --------------------------------
    rule <k> ECREC => #end EVMC_SUCCESS ... </k>
         <callData> DATA </callData>
         <output> _ => #ecrec(#range(DATA, 0, 32), #range(DATA, 32, 32), #range(DATA, 64, 32), #range(DATA, 96, 32)) </output>

    syntax Bytes ::= #ecrec ( Bytes , Bytes , Bytes , Bytes ) [symbol(#ecrec),    function, total, smtlib(ecrec)]
                   | #ecrec ( Account )                       [symbol(#ecrecAux), function, total               ]
 // -------------------------------------------------------------------------------------------------------------
    rule [ecrec]: #ecrec(HASH, SIGV, SIGR, SIGS) => #ecrec(#sender(HASH, #asWord(SIGV), SIGR, SIGS)) [concrete]

    rule #ecrec(.Account) => .Bytes
    rule #ecrec(N:Int)    => #padToWidth(32, #asByteStack(N))

    syntax PrecompiledOp ::= "SHA256"
 // ---------------------------------
    rule <k> SHA256 => #end EVMC_SUCCESS ... </k>
         <callData> DATA </callData>
         <output> _ => #parseHexBytes(Sha256(DATA)) </output>

    syntax PrecompiledOp ::= "RIP160"
 // ---------------------------------
    rule <k> RIP160 => #end EVMC_SUCCESS ... </k>
         <callData> DATA </callData>
         <output> _ => #padToWidth(32, #parseHexBytes(RipEmd160(DATA))) </output>

    syntax PrecompiledOp ::= "ID"
 // -----------------------------
    rule <k> ID => #end EVMC_SUCCESS ... </k>
         <callData> DATA </callData>
         <output> _ => DATA </output>

    syntax PrecompiledOp ::= "MODEXP"
 // ---------------------------------
    rule <k> MODEXP => #end EVMC_SUCCESS ... </k>
         <callData> DATA </callData>
         <output> _ => #modexp1(#asWord(#range(DATA, 0, 32)), #asWord(#range(DATA, 32, 32)), #asWord(#range(DATA, 64, 32)), #range(DATA, 96, maxInt(0, lengthBytes(DATA) -Int 96))) </output>

    syntax Bytes ::= #modexp1 ( Int , Int , Int , Bytes ) [symbol(#modexp1), function]
                   | #modexp2 ( Int , Int , Int , Bytes ) [symbol(#modexp2), function]
                   | #modexp3 ( Int , Int , Int , Bytes ) [symbol(#modexp3), function]
                   | #modexp4 ( Int , Int , Int )         [symbol(#modexp4), function]
 // ----------------------------------------------------------------------------------
    rule #modexp1(BASELEN, EXPLEN,   MODLEN, DATA) => #modexp2(#asInteger(#range(DATA, 0, BASELEN)), EXPLEN, MODLEN, #range(DATA, BASELEN, maxInt(0, lengthBytes(DATA) -Int BASELEN))) requires MODLEN =/=Int 0
    rule #modexp1(_,       _,        0,      _)    => .Bytes
    rule #modexp2(BASE,    EXPLEN,   MODLEN, DATA) => #modexp3(BASE, #asInteger(#range(DATA, 0, EXPLEN)), MODLEN, #range(DATA, EXPLEN, maxInt(0, lengthBytes(DATA) -Int EXPLEN)))
    rule #modexp3(BASE,    EXPONENT, MODLEN, DATA) => #padToWidth(MODLEN, #modexp4(BASE, EXPONENT, #asInteger(#range(DATA, 0, MODLEN))))
    rule #modexp4(BASE,    EXPONENT, MODULUS)      => #asByteStack(powmod(BASE, EXPONENT, MODULUS))

    syntax PrecompiledOp ::= "ECADD"
 // --------------------------------
    rule <k> ECADD => #ecadd((#asWord(#range(DATA, 0, 32)), #asWord(#range(DATA, 32, 32))), (#asWord(#range(DATA, 64, 32)), #asWord(#range(DATA, 96, 32)))) ... </k>
         <callData> DATA </callData>

    syntax InternalOp ::= #ecadd(G1Point, G1Point) [symbol(#ecadd)]
 // ---------------------------------------------------------------
    rule <k> #ecadd(P1, P2) => #end EVMC_PRECOMPILE_FAILURE ... </k>
      requires notBool isValidPointWrapper(P1) orBool notBool isValidPointWrapper(P2)
    rule <k> #ecadd(P1, P2) => #end EVMC_SUCCESS ... </k> <output> _ => #point(BN128Add(P1, P2)) </output>
      requires isValidPointWrapper(P1) andBool isValidPointWrapper(P2)

    syntax PrecompiledOp ::= "ECMUL"
 // --------------------------------
    rule <k> ECMUL => #ecmul((#asWord(#range(DATA, 0, 32)), #asWord(#range(DATA, 32, 32))), #asWord(#range(DATA, 64, 32))) ... </k>
         <callData> DATA </callData>

    syntax InternalOp ::= #ecmul(G1Point, Int) [symbol(#ecmul)]
 // -----------------------------------------------------------
    rule <k> #ecmul(P, _S) => #end EVMC_PRECOMPILE_FAILURE ... </k>
      requires notBool isValidPointWrapper(P)
    rule <k> #ecmul(P,  S) => #end EVMC_SUCCESS ... </k> <output> _ => #point(BN128Mul(P, S)) </output>
      requires isValidPointWrapper(P)

    syntax Bytes ::= #point ( G1Point ) [symbol(#point), function]
 // --------------------------------------------------------------
    rule #point((X, Y)) => #padToWidth(32, #asByteStack(X)) +Bytes #padToWidth(32, #asByteStack(Y))

    syntax PrecompiledOp ::= "ECPAIRING"
 // ------------------------------------
    rule <k> ECPAIRING => #ecpairing(.List, .List, 0, DATA, lengthBytes(DATA)) ... </k>
         <callData> DATA </callData>
      requires lengthBytes(DATA) modInt 192 ==Int 0
    rule <k> ECPAIRING => #end EVMC_PRECOMPILE_FAILURE ... </k>
         <callData> DATA </callData>
      requires lengthBytes(DATA) modInt 192 =/=Int 0

    syntax InternalOp ::= #ecpairing(List, List, Int, Bytes, Int) [symbol(#ecpairing)]
 // ----------------------------------------------------------------------------------
    rule <k> (.K => #checkPoint) ~> #ecpairing((.List => ListItem((#asWord(#range(DATA, I, 32)), #asWord(#range(DATA, I +Int 32, 32))))) _, (.List => ListItem((#asWord(#range(DATA, I +Int 96, 32)) x #asWord(#range(DATA, I +Int 64, 32)) , #asWord(#range(DATA, I +Int 160, 32)) x #asWord(#range(DATA, I +Int 128, 32))))) _, I => I +Int 192, DATA, LEN) ... </k>
      requires I =/=Int LEN
    rule <k> #ecpairing(A, B, LEN, _, LEN) => #end EVMC_SUCCESS ... </k>
         <output> _ => #padToWidth(32, #asByteStack(bool2Word(BN128AtePairing(A, B)))) </output>

    syntax InternalOp ::= "#checkPoint"
 // -----------------------------------
    rule <k> (#checkPoint => .K) ~> #ecpairing(ListItem(AK::G1Point) _, ListItem(BK::G2Point) _, _, _, _) ... </k>
      requires isValidPointWrapper(AK) andBool isValidPointWrapper(BK)
    rule <k> #checkPoint ~> #ecpairing(ListItem(AK::G1Point) _, ListItem(BK::G2Point) _, _, _, _) => #end EVMC_PRECOMPILE_FAILURE ... </k>
      requires notBool isValidPointWrapper(AK) orBool notBool isValidPointWrapper(BK)

    syntax PrecompiledOp ::= "BLAKE2F"
 // ----------------------------------
    rule <k> BLAKE2F => #end EVMC_SUCCESS ... </k>
         <output> _ => #parseByteStack( Blake2Compress( DATA ) ) </output>
         <callData> DATA </callData>
      requires lengthBytes( DATA ) ==Int 213
       andBool DATA[212] <=Int 1

    rule <k> BLAKE2F => #end EVMC_PRECOMPILE_FAILURE ... </k>
         <callData> DATA </callData>
      requires lengthBytes( DATA ) ==Int 213
       andBool DATA[212] >Int 1

    rule <k> BLAKE2F => #end EVMC_PRECOMPILE_FAILURE ... </k>
         <callData> DATA </callData>
      requires lengthBytes( DATA ) =/=Int 213
```


Ethereum Gas Calculation
========================

Overall Gas
-----------

-   `#gas` calculates how much gas this operation costs, and takes into account the memory consumed.
-   `#deductGas` is used to check that there won't be a gas underflow (throwing `EVMC_OUT_OF_GAS` if so), and deducts the gas if not.
-   `#deductMemory` checks that access to memory stay within sensible bounds (and deducts the correct amount of gas for it), throwing `EVMC_INVALID_MEMORY_ACCESS` if bad access happens.

```k
    syntax InternalOp ::= "#gas" "[" OpCode "," OpCode "]"
 // ------------------------------------------------------
    rule <k> #gas [ OP , AOP ]
          => #memory [ OP , AOP ]
          ~> #gas [ AOP ]
          ~> #access [ OP , AOP ]
         ...
        </k>
        <useGas> true </useGas>

    rule <k> #gas [ _ , _ ] => .K ...  </k> <useGas> false </useGas>

    rule <k> #gas [ OP ] => #gasExec(SCHED, OP) ~> #deductGas ... </k>
         <schedule> SCHED </schedule>

    rule <k> #memory [ OP , AOP ] => #memory(AOP, MU) ~> #deductMemory ... </k>
         <memoryUsed> MU </memoryUsed>
      requires #usesMemory(OP)

   rule <k> #memory [ _ , _ ] => .K ... </k> [owise]

    syntax InternalOp ::= "#gas"    "[" OpCode "]" | "#deductGas" | "#deductMemoryGas"
                        | "#memory" "[" OpCode "," OpCode "]" | "#deductMemory"
 // ---------------------------------------------------------------------------
    rule <k> MU':Int ~> #deductMemory => (Cmem(SCHED, MU') -Int Cmem(SCHED, MU)) ~> #deductMemoryGas ... </k>
         <memoryUsed> MU => MU' </memoryUsed> <schedule> SCHED </schedule>

    rule <k> _G:Gas ~> (#deductMemoryGas => #deductGas)   ... </k> //Required for verification
    rule <k>  G:Gas ~> #deductGas => #end EVMC_OUT_OF_GAS ... </k> <gas> GAVAIL:Gas                  </gas> <useGas> true </useGas> requires GAVAIL <Gas G
    rule <k>  G:Gas ~> #deductGas => .K                    ... </k> <gas> GAVAIL:Gas => GAVAIL -Gas G </gas> <useGas> true </useGas> requires G <=Gas GAVAIL
    rule <k>  _:Gas ~> #deductGas => .K                    ... </k> <useGas> false </useGas>

    syntax Bool ::= #inStorage     ( Map   , Account , Int ) [symbol(#inStorage), function, total]
                  | #inStorageAux1 ( KItem ,           Int ) [symbol(#inStorageAux1), function, total]
                  | #inStorageAux2 ( Set   ,           Int ) [symbol(#inStorageAux2), function, total]
 // --------------------------------------------------------------------------------------------------
    rule #inStorage(TS, ACCT, KEY) => #inStorageAux1(TS[ACCT], KEY) requires ACCT in_keys(TS)
    rule #inStorage(_, _, _)       => false                         [owise]

    rule #inStorageAux1(KEYS:Set, KEY) => #inStorageAux2(KEYS, KEY)
    rule #inStorageAux1(_, _)          => false                     [owise]

    rule #inStorageAux2(KEYS, KEY) => true  requires KEY in KEYS
    rule #inStorageAux2(_, _)      => false [owise]
```

Memory Consumption
------------------

Memory consumed is tracked to determine the appropriate amount of gas to charge for each operation.
In the YellowPaper, each opcode is defined to consume zero gas unless specified otherwise next to the semantics of the opcode (appendix H).

-   `#memory` computes the new memory size given the old size and next operator (with its arguments).
-   `#memoryUsageUpdate` is the function `M` in appendix H of the YellowPaper which helps track the memory used.

```k
    syntax Int ::= #memory ( OpCode , Int ) [symbol(#memory), function, total]
 // --------------------------------------------------------------------------
    rule #memory ( MLOAD INDEX        , MU ) => #memoryUsageUpdate(MU, INDEX, 32)
    rule #memory ( MSTORE INDEX _     , MU ) => #memoryUsageUpdate(MU, INDEX, 32)
    rule #memory ( MSTORE8 INDEX _    , MU ) => #memoryUsageUpdate(MU, INDEX, 1)
    rule #memory ( MCOPY DST SRC WIDTH, MU ) => #memoryUsageUpdate(MU, maxInt(DST, SRC), WIDTH)

    rule #memory ( SHA3 START WIDTH   , MU ) => #memoryUsageUpdate(MU, START, WIDTH)
    rule #memory ( LOG(_) START WIDTH , MU ) => #memoryUsageUpdate(MU, START, WIDTH)

    rule #memory ( CODECOPY START _ WIDTH       , MU ) => #memoryUsageUpdate(MU, START, WIDTH)
    rule #memory ( EXTCODECOPY _ START _ WIDTH  , MU ) => #memoryUsageUpdate(MU, START, WIDTH)
    rule #memory ( CALLDATACOPY START _ WIDTH   , MU ) => #memoryUsageUpdate(MU, START, WIDTH)
    rule #memory ( RETURNDATACOPY START _ WIDTH , MU ) => #memoryUsageUpdate(MU, START, WIDTH)

    rule #memory ( CREATE  _ START WIDTH   , MU ) => #memoryUsageUpdate(MU, START, WIDTH)
    rule #memory ( CREATE2 _ START WIDTH _ , MU ) => #memoryUsageUpdate(MU, START, WIDTH)
    rule #memory ( RETURN START WIDTH      , MU ) => #memoryUsageUpdate(MU, START, WIDTH)
    rule #memory ( REVERT START WIDTH      , MU ) => #memoryUsageUpdate(MU, START, WIDTH)

    rule #memory ( _COP:CallOp     _ _ _ ARGSTART ARGWIDTH RETSTART RETWIDTH , MU ) => #memoryUsageUpdate(#memoryUsageUpdate(MU, ARGSTART, ARGWIDTH), RETSTART, RETWIDTH)
    rule #memory ( _CSOP:CallSixOp _ _   ARGSTART ARGWIDTH RETSTART RETWIDTH , MU ) => #memoryUsageUpdate(#memoryUsageUpdate(MU, ARGSTART, ARGWIDTH), RETSTART, RETWIDTH)

    rule #memory ( _ , MU ) => MU [owise]

    syntax Bool ::= #usesMemory ( OpCode ) [symbol(#usesMemory), function, total]
 // -----------------------------------------------------------------------------
    rule #usesMemory(_:LogOp)        => true
    rule #usesMemory(_:CallOp)       => true
    rule #usesMemory(_:CallSixOp)    => true
    rule #usesMemory(MLOAD)          => true
    rule #usesMemory(MSTORE)         => true
    rule #usesMemory(MSTORE8)        => true
    rule #usesMemory(SHA3)           => true
    rule #usesMemory(CODECOPY)       => true
    rule #usesMemory(EXTCODECOPY)    => true
    rule #usesMemory(CALLDATACOPY)   => true
    rule #usesMemory(RETURNDATACOPY) => true
    rule #usesMemory(CREATE)         => true
    rule #usesMemory(CREATE2)        => true
    rule #usesMemory(RETURN)         => true
    rule #usesMemory(REVERT)         => true
    rule #usesMemory(MCOPY)          => true
    rule #usesMemory(_)              => false [owise]

    syntax Int ::= #memoryUsageUpdate ( Int , Int , Int ) [symbol(#memoryUsageUpdate), function, total]
 // ---------------------------------------------------------------------------------------------------
    rule #memoryUsageUpdate(MU,     _, WIDTH) => MU                                       requires notBool 0 <Int WIDTH [concrete]
    rule #memoryUsageUpdate(MU, START, WIDTH) => maxInt(MU, (START +Int WIDTH) up/Int 32) requires         0 <Int WIDTH [concrete]
```

Access List Gas
---------------

```k
    syntax Bool ::= #usesAccessList ( OpCode ) [symbol(#usesAccessList), function, total]
 // -------------------------------------------------------------------------------------
    rule #usesAccessList(OP)     => true  requires isAddr1Op(OP)
    rule #usesAccessList(OP)     => true  requires isAddr2Op(OP)
    rule #usesAccessList(SLOAD)  => true
    rule #usesAccessList(SSTORE) => true
    rule #usesAccessList(_)      => false [owise]

    syntax InternalOp ::= "#access" "[" OpCode "," OpCode "]"
 // ---------------------------------------------------------
    rule <k> #access [ OP , AOP ] => #gasAccess(SCHED, AOP) ~> #deductGas ... </k>
         <schedule> SCHED </schedule>
      requires Ghasaccesslist << SCHED >> andBool #usesAccessList(OP)

    rule <k> #access [ _ , _ ] => .K ... </k> <schedule> _ </schedule> [owise]

    syntax InternalOp ::= #gasAccess ( Schedule, OpCode ) [symbol(#gasAccess)]
 // --------------------------------------------------------------------------
    rule <k> #gasAccess(SCHED, EXTCODESIZE ACCT)       => Caddraccess(SCHED, ACCT in ACCTS)                                                                   ... </k> <accessedAccounts> ACCTS </accessedAccounts>
    rule <k> #gasAccess(SCHED, EXTCODECOPY ACCT _ _ _) => Caddraccess(SCHED, ACCT in ACCTS)                                                                   ... </k> <accessedAccounts> ACCTS </accessedAccounts>
    rule <k> #gasAccess(SCHED, EXTCODEHASH ACCT)       => Caddraccess(SCHED, ACCT in ACCTS)                                                                   ... </k> <accessedAccounts> ACCTS </accessedAccounts>
    rule <k> #gasAccess(SCHED, BALANCE ACCT)           => Caddraccess(SCHED, ACCT in ACCTS)                                                                   ... </k> <accessedAccounts> ACCTS </accessedAccounts>
    rule <k> #gasAccess(SCHED, SELFDESTRUCT ACCT)      => #if ACCT in ACCTS #then 0 #else Gcoldaccountaccess < SCHED > #fi                                    ... </k> <accessedAccounts> ACCTS </accessedAccounts>
    rule <k> #gasAccess(_    , SLOAD INDEX )           => #accessStorage ACCT INDEX ~> 0                                                                      ... </k> <id> ACCT </id>
    rule <k> #gasAccess(SCHED, SSTORE INDEX _)         => #accessStorage ACCT INDEX ~> #if #inStorage(TS, ACCT, INDEX) #then 0 #else Gcoldsload < SCHED > #fi ... </k> <id> ACCT </id> <accessedStorage> TS </accessedStorage>
    rule <k> #gasAccess(_    , _ )                     => 0                                                                                                   ... </k> [owise]

```

Execution Gas
-------------

The intrinsic gas calculation mirrors the style of the YellowPaper (appendix H).

-   `#gasExec` loads all the relevant surrounding state and uses that to compute the intrinsic execution gas of each opcode.

-   Gas cost for `TSTORE` is the same as a warm `SSTORE` of a dirty slot (i.e. original value is not new value, original is not current value, currently 100 gas).
-   Gas cost of `TLOAD` is the same as a hot `SLOAD` (value has been read before, currently 100 gas).
-   Gas cost cannot be on par with memory access due to transient storage’s interactions with reverts.
```k
    syntax InternalOp ::= #gasExec ( Schedule , OpCode ) [symbol(#gasExec)]
 // -----------------------------------------------------------------------
    rule <k> #gasExec(SCHED, TLOAD _   ) => Gwarmstorageread < SCHED > ... </k>
    rule <k> #gasExec(SCHED, TSTORE _ _) => Gwarmstoragedirtystore < SCHED > ... </k>

    rule <k> #gasExec(SCHED, SSTORE INDEX NEW) => Csstore(SCHED, NEW, #lookup(STORAGE, INDEX), #lookup(ORIGSTORAGE, INDEX)) ... </k>
         <id> ACCT </id>
         <gas> GAVAIL </gas>
         <account>
           <acctID> ACCT </acctID>
           <storage> STORAGE </storage>
           <origStorage> ORIGSTORAGE </origStorage>
           ...
         </account>
         <refund> R => R +Int Rsstore(SCHED, NEW, #lookup(STORAGE, INDEX), #lookup(ORIGSTORAGE, INDEX)) </refund>
      requires notBool Ghassstorestipend << SCHED >>
        orBool notBool GAVAIL <=Gas Gcallstipend < SCHED >

    rule <k> #gasExec(SCHED, SSTORE _ _ ) => #end EVMC_OUT_OF_GAS ... </k>
         <gas> GAVAIL </gas>
      requires Ghassstorestipend << SCHED >>
       andBool GAVAIL <=Gas Gcallstipend < SCHED >

    rule <k> #gasExec(SCHED, EXP _ W1) => Gexp < SCHED > ... </k>                                                         requires W1 <=Int 0
    rule <k> #gasExec(SCHED, EXP _ W1) => Gexp < SCHED > +Int (Gexpbyte < SCHED > *Int (1 +Int (log256Int(W1)))) ... </k> requires 0 <Int W1 [preserves-definedness]

    rule <k> #gasExec(SCHED, CALLDATACOPY    _ _ WIDTH) => Gverylow < SCHED > +Int (Gcopy < SCHED > *Int (WIDTH up/Int 32)) ... </k>
    rule <k> #gasExec(SCHED, RETURNDATACOPY  _ _ WIDTH) => Gverylow < SCHED > +Int (Gcopy < SCHED > *Int (WIDTH up/Int 32)) ... </k>
    rule <k> #gasExec(SCHED, CODECOPY        _ _ WIDTH) => Gverylow < SCHED > +Int (Gcopy < SCHED > *Int (WIDTH up/Int 32)) ... </k>
    rule <k> #gasExec(SCHED, MCOPY           _ _ WIDTH) => Gverylow < SCHED > +Int (Gcopy < SCHED > *Int (WIDTH up/Int 32)) ... </k>

    rule <k> #gasExec(SCHED, LOG(N) _ WIDTH) => (Glog < SCHED > +Int (Glogdata < SCHED > *Int WIDTH) +Int (N *Int Glogtopic < SCHED >)) ... </k>

    rule <k> #gasExec(SCHED, CALL GCAP ACCTTO VALUE _ _ _ _)
          => Ccallgas(SCHED, #accountNonexistent(ACCTTO), GCAP, GAVAIL, VALUE, ACCTTO in ACCTS) ~> #allocateCallGas
          ~> Ccall(SCHED, #accountNonexistent(ACCTTO), GCAP, GAVAIL, VALUE, ACCTTO in ACCTS)
         ...
         </k>
         <gas> GAVAIL </gas>
         <accessedAccounts> ACCTS </accessedAccounts>

    rule <k> #gasExec(SCHED, CALLCODE GCAP ACCTTO VALUE _ _ _ _)
          => Ccallgas(SCHED, #accountNonexistent(ACCTFROM), GCAP, GAVAIL, VALUE, ACCTTO in ACCTS) ~> #allocateCallGas
          ~> Ccall(SCHED, #accountNonexistent(ACCTFROM), GCAP, GAVAIL, VALUE, ACCTTO in ACCTS)
         ...
         </k>
         <id> ACCTFROM </id>
         <gas> GAVAIL </gas>
         <accessedAccounts> ACCTS </accessedAccounts>

    rule <k> #gasExec(SCHED, DELEGATECALL GCAP ACCTTO _ _ _ _)
          => Ccallgas(SCHED, #accountNonexistent(ACCTFROM), GCAP, GAVAIL, 0, ACCTTO in ACCTS) ~> #allocateCallGas
          ~> Ccall(SCHED, #accountNonexistent(ACCTFROM), GCAP, GAVAIL, 0, ACCTTO in ACCTS)
         ...
         </k>
         <id> ACCTFROM </id>
         <gas> GAVAIL </gas>
         <accessedAccounts> ACCTS </accessedAccounts>

    rule <k> #gasExec(SCHED, STATICCALL GCAP ACCTTO _ _ _ _)
          => Ccallgas(SCHED, #accountNonexistent(ACCTTO), GCAP, GAVAIL, 0, ACCTTO in ACCTS) ~> #allocateCallGas
          ~> Ccall(SCHED, #accountNonexistent(ACCTTO), GCAP, GAVAIL, 0, ACCTTO in ACCTS)
         ...
         </k>
         <gas> GAVAIL </gas>
         <accessedAccounts> ACCTS </accessedAccounts>

    rule <k> #gasExec(SCHED, SELFDESTRUCT ACCTTO) => Cselfdestruct(SCHED, #accountNonexistent(ACCTTO), BAL) ... </k>
         <id> ACCTFROM </id>
         <selfDestruct> SDS </selfDestruct>
         <refund> RF => #if ACCTFROM in SDS #then RF #else RF +Word Rselfdestruct < SCHED > #fi </refund>
         <account>
           <acctID> ACCTFROM </acctID>
           <balance> BAL </balance>
           ...
         </account>

    rule <k> #gasExec(SCHED, CREATE _ _ WIDTH)
          => Gcreate < SCHED > +Int Cinitcode(SCHED, WIDTH) ~> #deductGas
          ~> #allocateCreateGas ~> 0
         ...
         </k>

    rule <k> #gasExec(SCHED, CREATE2 _ _ WIDTH _)
          => Gcreate < SCHED > +Int Gsha3word < SCHED > *Int (WIDTH up/Int 32) +Int Cinitcode(SCHED, WIDTH) ~> #deductGas
          ~> #allocateCreateGas ~> 0
         ...
         </k>

    rule <k> #gasExec(SCHED, SHA3 _ WIDTH) => Gsha3 < SCHED > +Int (Gsha3word < SCHED > *Int (WIDTH up/Int 32)) ... </k>

    rule <k> #gasExec(SCHED, JUMPDEST)    => Gjumpdest < SCHED >                        ... </k>
    rule <k> #gasExec(SCHED, SLOAD INDEX) => Csload(SCHED, #inStorage(TS, ACCT, INDEX)) ... </k>
         <id> ACCT </id>
         <accessedStorage> TS </accessedStorage>

    // Wzero
    rule <k> #gasExec(SCHED, STOP)       => Gzero < SCHED > ... </k>
    rule <k> #gasExec(SCHED, RETURN _ _) => Gzero < SCHED > ... </k>
    rule <k> #gasExec(SCHED, REVERT _ _) => Gzero < SCHED > ... </k>

    // Wbase
    rule <k> #gasExec(SCHED, ADDRESS)        => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, ORIGIN)         => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, CALLER)         => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, CALLVALUE)      => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, CALLDATASIZE)   => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, RETURNDATASIZE) => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, CODESIZE)       => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, GASPRICE)       => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, COINBASE)       => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, TIMESTAMP)      => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, NUMBER)         => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, DIFFICULTY)     => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, PREVRANDAO)     => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, GASLIMIT)       => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, BASEFEE)        => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, BLOBBASEFEE)    => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, POP _)          => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, PC)             => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, PUSHZERO)       => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, MSIZE)          => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, GAS)            => Gbase < SCHED > ... </k>
    rule <k> #gasExec(SCHED, CHAINID)        => Gbase < SCHED > ... </k>

    // Wverylow
    rule <k> #gasExec(SCHED, ADD _ _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SUB _ _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, NOT _)          => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, LT _ _)         => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, GT _ _)         => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SLT _ _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SGT _ _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, EQ _ _)         => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, ISZERO _)       => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, AND _ _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, EVMOR _ _)      => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, XOR _ _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, BYTE _ _)       => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SHL _ _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SHR _ _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SAR _ _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, CALLDATALOAD _) => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, MLOAD _)        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, MSTORE _ _)     => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, MSTORE8 _ _)    => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, PUSH(_))        => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, DUP(_) _)       => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SWAP(_) _)      => Gverylow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, BLOBHASH _)     => Gverylow < SCHED > ... </k>

    // Wlow
    rule <k> #gasExec(SCHED, MUL _ _)        => Glow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, DIV _ _)        => Glow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SDIV _ _)       => Glow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, MOD _ _)        => Glow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SMOD _ _)       => Glow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SIGNEXTEND _ _) => Glow < SCHED > ... </k>
    rule <k> #gasExec(SCHED, SELFBALANCE)    => Glow < SCHED > ... </k>

    // Wmid
    rule <k> #gasExec(SCHED, ADDMOD _ _ _) => Gmid < SCHED > ... </k>
    rule <k> #gasExec(SCHED, MULMOD _ _ _) => Gmid < SCHED > ... </k>
    rule <k> #gasExec(SCHED, JUMP _) => Gmid < SCHED > ... </k>

    // Whigh
    rule <k> #gasExec(SCHED, JUMPI _ _) => Ghigh < SCHED > ... </k>

    rule <k> #gasExec(SCHED, EXTCODECOPY _ _ _ WIDTH) => Cextcodecopy(SCHED, WIDTH) ... </k>
    rule <k> #gasExec(SCHED, EXTCODESIZE _)           => Cextcodesize(SCHED)        ... </k>
    rule <k> #gasExec(SCHED, BALANCE _)               => Cbalance(SCHED)            ... </k>
    rule <k> #gasExec(SCHED, EXTCODEHASH _)           => Cextcodehash(SCHED)        ... </k>
    rule <k> #gasExec(SCHED, BLOCKHASH _)             => Gblockhash < SCHED >       ... </k>

    // Precompiled
    rule <k> #gasExec(_, ECREC)  => 3000 ... </k>
    rule <k> #gasExec(_, SHA256) =>  60 +Int  12 *Int (lengthBytes(DATA) up/Int 32) ... </k> <callData> DATA </callData>
    rule <k> #gasExec(_, RIP160) => 600 +Int 120 *Int (lengthBytes(DATA) up/Int 32) ... </k> <callData> DATA </callData>
    rule <k> #gasExec(_, ID)     =>  15 +Int   3 *Int (lengthBytes(DATA) up/Int 32) ... </k> <callData> DATA </callData>

    rule <k> #gasExec(SCHED, MODEXP) => Cmodexp(SCHED, DATA, #asWord(#range(DATA, 0, 32) ), #asWord(#range(DATA, 32, 32)), #asWord(#range(DATA, 64, 32))) ... </k>
         <callData> DATA </callData>

    rule <k> #gasExec(SCHED, ECADD)     => Gecadd < SCHED>  ... </k>
    rule <k> #gasExec(SCHED, ECMUL)     => Gecmul < SCHED > ... </k>
    rule <k> #gasExec(SCHED, ECPAIRING) => Gecpairconst < SCHED > +Int (lengthBytes(DATA) /Int 192) *Int Gecpaircoeff < SCHED > ... </k> <callData> DATA </callData>
    rule <k> #gasExec(SCHED, BLAKE2F)   => Gfround < SCHED > *Int #asWord(#range(DATA, 0, 4) ) ... </k> <callData> DATA </callData>

    syntax InternalOp ::= "#allocateCallGas"
 // ----------------------------------------
    rule <k> GCALL:Gas ~> #allocateCallGas => .K ... </k>
         <callGas> _ => GCALL </callGas>

    syntax InternalOp ::= "#allocateCreateGas"
 // ------------------------------------------
    rule <schedule> SCHED </schedule>
         <k> #allocateCreateGas => .K ... </k>
         <gas>     GAVAIL => #if Gstaticcalldepth << SCHED >> #then 0      #else GAVAIL /Gas 64      #fi </gas>
         <callGas> _      => #if Gstaticcalldepth << SCHED >> #then GAVAIL #else #allBut64th(GAVAIL) #fi </callGas>
      [preserves-definedness]
```

There are several helpers for calculating gas (most of them also specified in the YellowPaper).

```k
    syntax Exp     ::= Int | Gas
    syntax KResult ::= Int
    syntax Exp ::= Ccall         ( Schedule , BExp , Gas , Gas , Int , Bool ) [symbol(Ccall), strict(2)]
                 | Ccallgas      ( Schedule , BExp , Gas , Gas , Int , Bool ) [symbol(Ccallgas), strict(2)]
                 | Cselfdestruct ( Schedule , BExp , Int )                    [symbol(Cselfdestruct), strict(2)]
 // ------------------------------------------------------------------------------------------------------------
    rule <k> Ccall(SCHED, ISEMPTY:Bool, GCAP, GAVAIL, VALUE, ISWARM)
          => Cextra(SCHED, ISEMPTY, VALUE, ISWARM) +Gas Cgascap(SCHED, GCAP, GAVAIL, Cextra(SCHED, ISEMPTY, VALUE, ISWARM)) ... </k>

    rule <k> Ccallgas(SCHED, ISEMPTY:Bool, GCAP, GAVAIL, VALUE, ISWARM)
          => Cgascap(SCHED, GCAP, GAVAIL, Cextra(SCHED, ISEMPTY, VALUE, ISWARM)) +Gas #if VALUE ==Int 0 #then 0 #else Gcallstipend < SCHED > #fi ... </k>

    rule <k> Cselfdestruct(SCHED, ISEMPTY:Bool, BAL)
          => Gselfdestruct < SCHED > +Int Cnew(SCHED, ISEMPTY andBool Gselfdestructnewaccount << SCHED >>, BAL) ... </k>

    syntax BExp    ::= Bool
    syntax KResult ::= Bool
    syntax BExp ::= #accountNonexistent ( Int ) [symbol(#accountNonexistent)]
 // -------------------------------------------------------------------------
    rule <k> #accountNonexistent(ACCT) => #accountEmpty(CODE, NONCE, BAL) andBool Gemptyisnonexistent << SCHED >> ... </k>
         <schedule> SCHED </schedule>
         <account>
           <acctID>  ACCT  </acctID>
           <balance> BAL   </balance>
           <nonce>   NONCE </nonce>
           <code>    CODE  </code>
           ...
         </account>

   rule <k> #accountNonexistent(_) => true ... </k> [owise]
```

EVM Program Representations
===========================

EVM programs are represented algebraically in K, but programs can load and manipulate program data directly.
The opcodes `CODECOPY` and `EXTCODECOPY` rely on the assembled form of the programs being present.
The opcode `CREATE` relies on being able to interpret EVM data as a program.

This is a program representation dependence, which we might want to avoid.
Perhaps the only program representation dependence we should have is the hash of the program; doing so achieves:

-   Program representation independence (different analysis tools on the language don't have to ensure they have a common representation of programs, just a common interpretation of the data-files holding programs).
-   Programming language independence (we wouldn't even have to commit to a particular language or interpretation of the data-file).
-   Only depending on the hash allows us to know that we have *exactly* the correct data-file (program), and nothing more.

Disassembler
------------

After interpreting the strings representing programs as a `WordStack`, it should be changed into an `OpCodes` for use by the EVM semantics.

-   `#dasmOpCode` interprets a `Int` as an `OpCode`.

```k
    syntax OpCode ::= #dasmOpCode ( Int , Schedule ) [symbol(#dasmOpCode), function, memo, total]
 // ---------------------------------------------------------------------------------------------
    rule #dasmOpCode(   0,     _ ) => STOP
    rule #dasmOpCode(   1,     _ ) => ADD
    rule #dasmOpCode(   2,     _ ) => MUL
    rule #dasmOpCode(   3,     _ ) => SUB
    rule #dasmOpCode(   4,     _ ) => DIV
    rule #dasmOpCode(   5,     _ ) => SDIV
    rule #dasmOpCode(   6,     _ ) => MOD
    rule #dasmOpCode(   7,     _ ) => SMOD
    rule #dasmOpCode(   8,     _ ) => ADDMOD
    rule #dasmOpCode(   9,     _ ) => MULMOD
    rule #dasmOpCode(  10,     _ ) => EXP
    rule #dasmOpCode(  11,     _ ) => SIGNEXTEND
    rule #dasmOpCode(  16,     _ ) => LT
    rule #dasmOpCode(  17,     _ ) => GT
    rule #dasmOpCode(  18,     _ ) => SLT
    rule #dasmOpCode(  19,     _ ) => SGT
    rule #dasmOpCode(  20,     _ ) => EQ
    rule #dasmOpCode(  21,     _ ) => ISZERO
    rule #dasmOpCode(  22,     _ ) => AND
    rule #dasmOpCode(  23,     _ ) => EVMOR
    rule #dasmOpCode(  24,     _ ) => XOR
    rule #dasmOpCode(  25,     _ ) => NOT
    rule #dasmOpCode(  26,     _ ) => BYTE
    rule #dasmOpCode(  27, SCHED ) => SHL requires Ghasshift << SCHED >>
    rule #dasmOpCode(  28, SCHED ) => SHR requires Ghasshift << SCHED >>
    rule #dasmOpCode(  29, SCHED ) => SAR requires Ghasshift << SCHED >>
    rule #dasmOpCode(  32,     _ ) => SHA3
    rule #dasmOpCode(  48,     _ ) => ADDRESS
    rule #dasmOpCode(  49,     _ ) => BALANCE
    rule #dasmOpCode(  50,     _ ) => ORIGIN
    rule #dasmOpCode(  51,     _ ) => CALLER
    rule #dasmOpCode(  52,     _ ) => CALLVALUE
    rule #dasmOpCode(  53,     _ ) => CALLDATALOAD
    rule #dasmOpCode(  54,     _ ) => CALLDATASIZE
    rule #dasmOpCode(  55,     _ ) => CALLDATACOPY
    rule #dasmOpCode(  56,     _ ) => CODESIZE
    rule #dasmOpCode(  57,     _ ) => CODECOPY
    rule #dasmOpCode(  58,     _ ) => GASPRICE
    rule #dasmOpCode(  59,     _ ) => EXTCODESIZE
    rule #dasmOpCode(  60,     _ ) => EXTCODECOPY
    rule #dasmOpCode(  61, SCHED ) => RETURNDATASIZE requires Ghasreturndata  << SCHED >>
    rule #dasmOpCode(  62, SCHED ) => RETURNDATACOPY requires Ghasreturndata  << SCHED >>
    rule #dasmOpCode(  63, SCHED ) => EXTCODEHASH    requires Ghasextcodehash << SCHED >>
    rule #dasmOpCode(  64,     _ ) => BLOCKHASH
    rule #dasmOpCode(  65,     _ ) => COINBASE
    rule #dasmOpCode(  66,     _ ) => TIMESTAMP
    rule #dasmOpCode(  67,     _ ) => NUMBER
    rule #dasmOpCode(  68, SCHED ) => PREVRANDAO  requires         Ghasprevrandao << SCHED >>
    rule #dasmOpCode(  68, SCHED ) => DIFFICULTY  requires notBool Ghasprevrandao << SCHED >>
    rule #dasmOpCode(  69,     _ ) => GASLIMIT
    rule #dasmOpCode(  70, SCHED ) => CHAINID     requires Ghaschainid     << SCHED >>
    rule #dasmOpCode(  71, SCHED ) => SELFBALANCE requires Ghasselfbalance << SCHED >>
    rule #dasmOpCode(  72, SCHED ) => BASEFEE     requires Ghasbasefee     << SCHED >>
    rule #dasmOpCode(  73, SCHED ) => BLOBHASH    requires Ghasblobhash    << SCHED >>
    rule #dasmOpCode(  74, SCHED ) => BLOBBASEFEE requires Ghasblobbasefee << SCHED >>
    rule #dasmOpCode(  80,     _ ) => POP
    rule #dasmOpCode(  81,     _ ) => MLOAD
    rule #dasmOpCode(  82,     _ ) => MSTORE
    rule #dasmOpCode(  83,     _ ) => MSTORE8
    rule #dasmOpCode(  84,     _ ) => SLOAD
    rule #dasmOpCode(  85,     _ ) => SSTORE
    rule #dasmOpCode(  86,     _ ) => JUMP
    rule #dasmOpCode(  87,     _ ) => JUMPI
    rule #dasmOpCode(  88,     _ ) => PC
    rule #dasmOpCode(  89,     _ ) => MSIZE
    rule #dasmOpCode(  90,     _ ) => GAS
    rule #dasmOpCode(  91,     _ ) => JUMPDEST
    rule #dasmOpCode(  92, SCHED ) => TLOAD    requires Ghastransient << SCHED >>
    rule #dasmOpCode(  93, SCHED ) => TSTORE   requires Ghastransient << SCHED >>
    rule #dasmOpCode(  94, SCHED ) => MCOPY    requires Ghasmcopy     << SCHED >>
    rule #dasmOpCode(  95, SCHED ) => PUSHZERO requires Ghaspushzero  << SCHED >>
    rule #dasmOpCode(  96,     _ ) => PUSH(1)
    rule #dasmOpCode(  97,     _ ) => PUSH(2)
    rule #dasmOpCode(  98,     _ ) => PUSH(3)
    rule #dasmOpCode(  99,     _ ) => PUSH(4)
    rule #dasmOpCode( 100,     _ ) => PUSH(5)
    rule #dasmOpCode( 101,     _ ) => PUSH(6)
    rule #dasmOpCode( 102,     _ ) => PUSH(7)
    rule #dasmOpCode( 103,     _ ) => PUSH(8)
    rule #dasmOpCode( 104,     _ ) => PUSH(9)
    rule #dasmOpCode( 105,     _ ) => PUSH(10)
    rule #dasmOpCode( 106,     _ ) => PUSH(11)
    rule #dasmOpCode( 107,     _ ) => PUSH(12)
    rule #dasmOpCode( 108,     _ ) => PUSH(13)
    rule #dasmOpCode( 109,     _ ) => PUSH(14)
    rule #dasmOpCode( 110,     _ ) => PUSH(15)
    rule #dasmOpCode( 111,     _ ) => PUSH(16)
    rule #dasmOpCode( 112,     _ ) => PUSH(17)
    rule #dasmOpCode( 113,     _ ) => PUSH(18)
    rule #dasmOpCode( 114,     _ ) => PUSH(19)
    rule #dasmOpCode( 115,     _ ) => PUSH(20)
    rule #dasmOpCode( 116,     _ ) => PUSH(21)
    rule #dasmOpCode( 117,     _ ) => PUSH(22)
    rule #dasmOpCode( 118,     _ ) => PUSH(23)
    rule #dasmOpCode( 119,     _ ) => PUSH(24)
    rule #dasmOpCode( 120,     _ ) => PUSH(25)
    rule #dasmOpCode( 121,     _ ) => PUSH(26)
    rule #dasmOpCode( 122,     _ ) => PUSH(27)
    rule #dasmOpCode( 123,     _ ) => PUSH(28)
    rule #dasmOpCode( 124,     _ ) => PUSH(29)
    rule #dasmOpCode( 125,     _ ) => PUSH(30)
    rule #dasmOpCode( 126,     _ ) => PUSH(31)
    rule #dasmOpCode( 127,     _ ) => PUSH(32)
    rule #dasmOpCode( 128,     _ ) => DUP(1)
    rule #dasmOpCode( 129,     _ ) => DUP(2)
    rule #dasmOpCode( 130,     _ ) => DUP(3)
    rule #dasmOpCode( 131,     _ ) => DUP(4)
    rule #dasmOpCode( 132,     _ ) => DUP(5)
    rule #dasmOpCode( 133,     _ ) => DUP(6)
    rule #dasmOpCode( 134,     _ ) => DUP(7)
    rule #dasmOpCode( 135,     _ ) => DUP(8)
    rule #dasmOpCode( 136,     _ ) => DUP(9)
    rule #dasmOpCode( 137,     _ ) => DUP(10)
    rule #dasmOpCode( 138,     _ ) => DUP(11)
    rule #dasmOpCode( 139,     _ ) => DUP(12)
    rule #dasmOpCode( 140,     _ ) => DUP(13)
    rule #dasmOpCode( 141,     _ ) => DUP(14)
    rule #dasmOpCode( 142,     _ ) => DUP(15)
    rule #dasmOpCode( 143,     _ ) => DUP(16)
    rule #dasmOpCode( 144,     _ ) => SWAP(1)
    rule #dasmOpCode( 145,     _ ) => SWAP(2)
    rule #dasmOpCode( 146,     _ ) => SWAP(3)
    rule #dasmOpCode( 147,     _ ) => SWAP(4)
    rule #dasmOpCode( 148,     _ ) => SWAP(5)
    rule #dasmOpCode( 149,     _ ) => SWAP(6)
    rule #dasmOpCode( 150,     _ ) => SWAP(7)
    rule #dasmOpCode( 151,     _ ) => SWAP(8)
    rule #dasmOpCode( 152,     _ ) => SWAP(9)
    rule #dasmOpCode( 153,     _ ) => SWAP(10)
    rule #dasmOpCode( 154,     _ ) => SWAP(11)
    rule #dasmOpCode( 155,     _ ) => SWAP(12)
    rule #dasmOpCode( 156,     _ ) => SWAP(13)
    rule #dasmOpCode( 157,     _ ) => SWAP(14)
    rule #dasmOpCode( 158,     _ ) => SWAP(15)
    rule #dasmOpCode( 159,     _ ) => SWAP(16)
    rule #dasmOpCode( 160,     _ ) => LOG(0)
    rule #dasmOpCode( 161,     _ ) => LOG(1)
    rule #dasmOpCode( 162,     _ ) => LOG(2)
    rule #dasmOpCode( 163,     _ ) => LOG(3)
    rule #dasmOpCode( 164,     _ ) => LOG(4)
    rule #dasmOpCode( 240,     _ ) => CREATE
    rule #dasmOpCode( 241,     _ ) => CALL
    rule #dasmOpCode( 242,     _ ) => CALLCODE
    rule #dasmOpCode( 243,     _ ) => RETURN
    rule #dasmOpCode( 244, SCHED ) => DELEGATECALL requires SCHED =/=K FRONTIER
    rule #dasmOpCode( 245, SCHED ) => CREATE2      requires Ghascreate2    << SCHED >>
    rule #dasmOpCode( 250, SCHED ) => STATICCALL   requires Ghasstaticcall << SCHED >>
    rule #dasmOpCode( 253, SCHED ) => REVERT       requires Ghasrevert     << SCHED >>
    rule #dasmOpCode( 254,     _ ) => INVALID
    rule #dasmOpCode( 255,     _ ) => SELFDESTRUCT
    rule #dasmOpCode(   W,     _ ) => UNDEFINED(W) [owise]
endmodule
```
