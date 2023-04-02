State Manager
-------------

```k
requires "evm.md"
requires "asm.md"

module STATE-UTILS
    imports EVM
    imports EVM-ASSEMBLY

    syntax JSON ::= Bytes | OpCodes | Map | SubstateLogEntry | Account
 // ------------------------------------------------------------------

```

### Clearing State

-   `clear` clears all the execution state of the machine.
-   `clearX` clears the substate `X`, for `TX`, `BLOCK`, and `NETWORK`.

```k
    syntax EthereumCommand ::= "clear"
 // ----------------------------------
    rule <k> clear => clearTX ~> clearBLOCK ~> clearNETWORK ... </k>

    syntax EthereumCommand ::= "clearTX"
 // ------------------------------------
    rule <k> clearTX => . ... </k>
         <output>           _ => .Bytes     </output>
         <memoryUsed>       _ => 0          </memoryUsed>
         <callDepth>        _ => 0          </callDepth>
         <callStack>        _ => .List      </callStack>
         <program>          _ => .Bytes     </program>
         <jumpDests>        _ => .Set       </jumpDests>
         <id>               _ => .Account   </id>
         <caller>           _ => .Account   </caller>
         <callData>         _ => .Bytes     </callData>
         <callValue>        _ => 0          </callValue>
         <wordStack>        _ => .WordStack </wordStack>
         <localMem>         _ => .Bytes     </localMem>
         <pc>               _ => 0          </pc>
         <gas>              _ => 0          </gas>
         <callGas>          _ => 0          </callGas>
         <selfDestruct>     _ => .Set       </selfDestruct>
         <log>              _ => .List      </log>
         <refund>           _ => 0          </refund>
         <gasPrice>         _ => 0          </gasPrice>
         <origin>           _ => .Account   </origin>
         <touchedAccounts>  _ => .Set       </touchedAccounts>
         <accessedAccounts> _ => .Set       </accessedAccounts>

    syntax EthereumCommand ::= "clearBLOCK"
 // ---------------------------------------
    rule <k> clearBLOCK => . ... </k>
         <previousHash>      _ => 0          </previousHash>
         <ommersHash>        _ => 0          </ommersHash>
         <coinbase>          _ => 0          </coinbase>
         <stateRoot>         _ => 0          </stateRoot>
         <transactionsRoot>  _ => 0          </transactionsRoot>
         <receiptsRoot>      _ => 0          </receiptsRoot>
         <logsBloom>         _ => .Bytes     </logsBloom>
         <difficulty>        _ => 0          </difficulty>
         <number>            _ => 0          </number>
         <gasLimit>          _ => 0          </gasLimit>
         <gasUsed>           _ => 0          </gasUsed>
         <timestamp>         _ => 0          </timestamp>
         <extraData>         _ => .Bytes     </extraData>
         <mixHash>           _ => 0          </mixHash>
         <blockNonce>        _ => 0          </blockNonce>
         <ommerBlockHeaders> _ => [ .JSONs ] </ommerBlockHeaders>
         <blockhashes>       _ => .List      </blockhashes>
         <baseFee>           _ => 0          </baseFee>

    syntax EthereumCommand ::= "clearNETWORK"
 // -----------------------------------------
    rule <k> clearNETWORK => . ... </k>
         <statusCode>     _ => .StatusCode </statusCode>
         <accounts>       _ => .Bag        </accounts>
         <messages>       _ => .Bag        </messages>
         <schedule>       _ => DEFAULT     </schedule>
```

### Loading State

-   `mkAcct_` creates an account with the supplied ID (assuming it's already been chopped to 160 bits).

```k
    syntax EthereumCommand ::= "mkAcct" Int
 // ---------------------------------------
    rule <k> mkAcct ACCT => #newAccount ACCT ... </k>
```

-   `load` loads an account or transaction into the world state.

```k
    syntax EthereumCommand ::= "load" JSON
 // --------------------------------------
    rule <k> load _DATA : { .JSONs }             => .                                                   ... </k>
    rule <k> load  DATA : { KEY : VALUE , REST } => load DATA : { KEY : VALUE } ~> load DATA : { REST } ... </k>
      requires REST =/=K .JSONs andBool DATA =/=String "transaction"

    rule <k> load _DATA : [ .JSONs ]          => .                                            ... </k>
    rule <k> load  DATA : [ { TEST } , REST ] => load DATA : { TEST } ~> load DATA : [ REST ] ... </k>
```

Here we perform pre-proccesing on account data which allows "pretty" specification of input.

```k
    rule <k> load "pre" : { (ACCTID:String) : ACCT } => mkAcct #parseAddr(ACCTID) ~> loadAccount #parseAddr(ACCTID) ACCT ... </k>

    syntax EthereumCommand ::= "loadAccount" Int JSON
 // -------------------------------------------------
    rule <k> loadAccount _ { .JSONs } => . ... </k>

    rule <k> loadAccount ACCT { "balance" : (BAL:Int), REST => REST } ... </k>
         <account> <acctID> ACCT </acctID> <balance> _ => BAL </balance> ... </account>

    rule <k> loadAccount ACCT { "code" : (CODE:Bytes), REST => REST } ... </k>
         <account> <acctID> ACCT </acctID> <code> _ => CODE </code> ... </account>

    rule <k> loadAccount ACCT { "nonce" : (NONCE:Int), REST => REST } ... </k>
         <account> <acctID> ACCT </acctID> <nonce> _ => NONCE </nonce> ... </account>

    rule <k> loadAccount ACCT { "storage" : (STORAGE:Map), REST => REST } ... </k>
         <account> <acctID> ACCT </acctID> <origStorage> _ => STORAGE </origStorage> <storage> _ => STORAGE </storage> ... </account>
```

Here we load the environmental information.

```k
    rule <k> load "env" : { KEY : ((VAL:String) => #parseWord(VAL)) } ... </k>
      requires KEY in (SetItem("currentTimestamp") SetItem("currentGasLimit") SetItem("currentNumber") SetItem("currentDifficulty") SetItem("currentBaseFee"))
    rule <k> load "env" : { KEY : ((VAL:String) => #parseHexWord(VAL)) } ... </k>
      requires KEY in (SetItem("currentCoinbase") SetItem("previousHash"))
 // ----------------------------------------------------------------------
    rule <k> load "env" : { "currentCoinbase"   : (CB:Int)     } => . ... </k> <coinbase>     _ => CB     </coinbase>
    rule <k> load "env" : { "currentDifficulty" : (DIFF:Int)   } => . ... </k> <difficulty>   _ => DIFF   </difficulty>
    rule <k> load "env" : { "currentGasLimit"   : (GLIMIT:Int) } => . ... </k> <gasLimit>     _ => GLIMIT </gasLimit>
    rule <k> load "env" : { "currentNumber"     : (NUM:Int)    } => . ... </k> <number>       _ => NUM    </number>
    rule <k> load "env" : { "previousHash"      : (HASH:Int)   } => . ... </k> <previousHash> _ => HASH   </previousHash>
    rule <k> load "env" : { "currentTimestamp"  : (TS:Int)     } => . ... </k> <timestamp>    _ => TS     </timestamp>
    rule <k> load "env" : { "currentBaseFee"    : (BF:Int)     } => . ... </k> <baseFee>      _ => BF     </baseFee>

    syntax KItem ::= "loadCallState" JSON
 // -------------------------------------
    rule <k> loadCallState { "data" : ( DATA:String => #parseByteStack( DATA ) ), _REST } ... </k>

    rule <k> loadCallState { "code" : CODE:Bytes, REST } => #loadProgram CODE ~> loadCallState { REST } ... </k>

    rule <k> loadCallState { "gas"      : GLIMIT:Int, REST => REST } ... </k> <gas>       _ => GLIMIT </gas>
    rule <k> loadCallState { "gasPrice" : GPRICE:Int, REST => REST } ... </k> <gasPrice>  _ => GPRICE </gasPrice>
    rule <k> loadCallState { "value"    : VALUE:Int , REST => REST } ... </k> <callValue> _ => VALUE  </callValue>
    rule <k> loadCallState { "data"     : DATA:Bytes, REST => REST } ... </k> <callData>  _ => DATA   </callData>

    rule <k> loadCallState { .JSONs } => . ... </k>
```

The `"network"` key allows setting the fee schedule inside the test.

```k
    rule <k> load "network" : SCHEDSTRING => . ... </k>
         <schedule> _ => #asScheduleString(SCHEDSTRING) </schedule>

    syntax Schedule ::= #asScheduleString ( String ) [function]
 // -----------------------------------------------------------
    rule #asScheduleString("Frontier")          => FRONTIER
    rule #asScheduleString("Homestead")         => HOMESTEAD
    rule #asScheduleString("EIP150")            => TANGERINE_WHISTLE
    rule #asScheduleString("EIP158")            => SPURIOUS_DRAGON
    rule #asScheduleString("Byzantium")         => BYZANTIUM
    rule #asScheduleString("Constantinople")    => CONSTANTINOPLE
    rule #asScheduleString("ConstantinopleFix") => PETERSBURG
    rule #asScheduleString("Istanbul")          => ISTANBUL
    rule #asScheduleString("Berlin")            => BERLIN
    rule #asScheduleString("London")            => LONDON
    rule #asScheduleString("Merge")             => MERGE
```

The `"rlp"` key loads the block information.

```k
    rule <k> load "rlp"        : (VAL:String => #rlpDecode(#unparseByteStack(#parseByteStack(VAL)))) ... </k>
    rule <k> load "genesisRLP" : (VAL:String => #rlpDecode(#unparseByteStack(#parseByteStack(VAL)))) ... </k>
 // ---------------------------------------------------------------------------------------------------------
    rule <k> load "rlp" : [ [ HP , HO , HC , HR , HT , HE , HB , HD , HI , HL , HG , HS , HX , HM , HN , .JSONs ] , BT , BU , .JSONs ]
          => load "transaction" : BT
         ...
         </k>
         <previousHash>      _ => #asWord(#parseByteStackRaw(HP)) </previousHash>
         <ommersHash>        _ => #asWord(#parseByteStackRaw(HO)) </ommersHash>
         <coinbase>          _ => #asWord(#parseByteStackRaw(HC)) </coinbase>
         <stateRoot>         _ => #asWord(#parseByteStackRaw(HR)) </stateRoot>
         <transactionsRoot>  _ => #asWord(#parseByteStackRaw(HT)) </transactionsRoot>
         <receiptsRoot>      _ => #asWord(#parseByteStackRaw(HE)) </receiptsRoot>
         <logsBloom>         _ => #parseByteStackRaw(HB)          </logsBloom>
         <difficulty>        _ => #asWord(#parseByteStackRaw(HD)) </difficulty>
         <number>            _ => #asWord(#parseByteStackRaw(HI)) </number>
         <gasLimit>          _ => #asWord(#parseByteStackRaw(HL)) </gasLimit>
         <gasUsed>           _ => #asWord(#parseByteStackRaw(HG)) </gasUsed>
         <timestamp>         _ => #asWord(#parseByteStackRaw(HS)) </timestamp>
         <extraData>         _ => #parseByteStackRaw(HX)          </extraData>
         <mixHash>           _ => #asWord(#parseByteStackRaw(HM)) </mixHash>
         <blockNonce>        _ => #asWord(#parseByteStackRaw(HN)) </blockNonce>
         <ommerBlockHeaders> _ => BU                              </ommerBlockHeaders>

    rule <k> load "rlp" : [ [ HP , HO , HC , HR , HT , HE , HB , HD , HI , HL , HG , HS , HX , HM , HN , HF , .JSONs ] , BT , BU , .JSONs ]
          => load "transaction" : BT
         ...
         </k>
         <previousHash>      _ => #asWord(#parseByteStackRaw(HP)) </previousHash>
         <ommersHash>        _ => #asWord(#parseByteStackRaw(HO)) </ommersHash>
         <coinbase>          _ => #asWord(#parseByteStackRaw(HC)) </coinbase>
         <stateRoot>         _ => #asWord(#parseByteStackRaw(HR)) </stateRoot>
         <transactionsRoot>  _ => #asWord(#parseByteStackRaw(HT)) </transactionsRoot>
         <receiptsRoot>      _ => #asWord(#parseByteStackRaw(HE)) </receiptsRoot>
         <logsBloom>         _ => #parseByteStackRaw(HB)          </logsBloom>
         <difficulty>        _ => #asWord(#parseByteStackRaw(HD)) </difficulty>
         <number>            _ => #asWord(#parseByteStackRaw(HI)) </number>
         <gasLimit>          _ => #asWord(#parseByteStackRaw(HL)) </gasLimit>
         <gasUsed>           _ => #asWord(#parseByteStackRaw(HG)) </gasUsed>
         <timestamp>         _ => #asWord(#parseByteStackRaw(HS)) </timestamp>
         <extraData>         _ => #parseByteStackRaw(HX)          </extraData>
         <mixHash>           _ => #asWord(#parseByteStackRaw(HM)) </mixHash>
         <blockNonce>        _ => #asWord(#parseByteStackRaw(HN)) </blockNonce>
         <baseFee>           _ => #asWord(#parseByteStackRaw(HF)) </baseFee>
         <ommerBlockHeaders> _ => BU                              </ommerBlockHeaders>

    rule <k> load "genesisRLP": [ [ HP, HO, HC, HR, HT, HE:String, HB, HD, HI, HL, HG, HS, HX, HM, HN, .JSONs ], _, _, .JSONs ] => .K ... </k>
         <blockhashes> .List => ListItem(#blockHeaderHash(HP, HO, HC, HR, HT, HE, HB, HD, HI, HL, HG, HS, HX, HM, HN)) ListItem(#asWord(#parseByteStackRaw(HP))) ... </blockhashes>

    rule <k> load "genesisRLP": [ [ HP, HO, HC, HR, HT, HE:String, HB, HD, HI, HL, HG, HS, HX, HM, HN, HF, .JSONs ], _, _, .JSONs ] => .K ... </k>
         <blockhashes> .List => ListItem(#blockHeaderHash(HP, HO, HC, HR, HT, HE, HB, HD, HI, HL, HG, HS, HX, HM, HN, HF)) ListItem(#asWord(#parseByteStackRaw(HP))) ... </blockhashes>

    syntax EthereumCommand ::= "mkTX" Int
 // -------------------------------------
    rule <k> mkTX TXID => . ... </k>
         <chainID> CID </chainID>
         <txOrder>   ... (.List => ListItem(TXID)) </txOrder>
         <txPending> ... (.List => ListItem(TXID)) </txPending>
         <messages>
            ( .Bag
           => <message>
                <msgID>      TXID:Int </msgID>
                <txGasPrice> 20000000000   </txGasPrice>
                <txGasLimit> 90000         </txGasLimit>
                <txChainID>  CID           </txChainID>
                ...
              </message>
            )
          ...
          </messages>

    rule <k> load "transaction" : [ (T => [#rlpDecodeTransaction(#parseByteStackRaw(T))]) , _ ] ... </k>

    rule <k> load "transaction" : [ [ TN , TP , TG , TT , TV , TI , TW , TR , TS ] , REST ]
          => mkTX !ID:Int
          ~> loadTransaction !ID { "data"  : TI   ,   "gasLimit" : TG   ,   "gasPrice"             : TP
                                 , "nonce" : TN   ,   "r"        : TR   ,   "s"                    : TS
                                 , "to"    : TT   ,   "v"        : TW   ,   "value"                : TV
                                 , "type"  : #dasmTxPrefix(Legacy)      ,   "maxPriorityFeePerGas" : TP
                                 , "maxFeePerGas": TP                   , .JSONs
                                 }
          ~> load "transaction" : [ REST ]
          ...
          </k>

    rule <k> load "transaction" : [ [TYPE , [TC, TN, TP, TG, TT, TV, TI, TA, TY , TR, TS ]] , REST ]
          => mkTX !ID:Int
          ~> loadTransaction !ID { "data"       : TI   ,   "gasLimit" : TG   ,   "gasPrice"  : TP
                                 , "nonce"      : TN   ,   "r"        : TR   ,   "s"         : TS
                                 , "to"         : TT   ,   "v"        : TY   ,   "value"     : TV
                                 , "accessList" : TA   ,   "type"     : TYPE ,   "chainID"   : TC
                                 , "maxPriorityFeePerGas" : TP               , "maxFeePerGas": TP
                                 , .JSONs
                                 }
          ~> load "transaction" : [ REST ]
          ...
         </k>
    requires #asWord(#parseByteStackRaw(TYPE)) ==Int #dasmTxPrefix(AccessList)


    rule <k> load "transaction" : [ [TYPE , [TC, TN, TP, TF, TG, TT, TV, TI, TA, TY , TR, TS ]] , REST ]
          => mkTX !ID:Int
          ~> loadTransaction !ID { "data"         : TI   ,   "gasLimit" : TG   ,   "maxPriorityFeePerGas" : TP
                                 , "nonce"        : TN   ,   "r"        : TR   ,   "s"                    : TS
                                 , "to"           : TT   ,   "v"        : TY   ,   "value"                : TV
                                 , "accessList"   : TA   ,   "type"     : TYPE ,   "chainID"              : TC
                                 , "maxFeePerGas" : TF   , .JSONs
                                 }
          ~> load "transaction" : [ REST ]
          ...
         </k>
    requires #asWord(#parseByteStackRaw(TYPE)) ==Int #dasmTxPrefix(DynamicFee)

    syntax EthereumCommand ::= "loadTransaction" Int JSON
 // -----------------------------------------------------
    rule <k> loadTransaction _ { .JSONs } => . ... </k>

    rule <k> loadTransaction TXID { GLIMIT : TG:Int, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <txGasLimit> _ => TG </txGasLimit> ... </message>
      requires GLIMIT in (SetItem("gas") SetItem("gasLimit"))

    rule <k> loadTransaction TXID { "gasPrice" : TP:Int, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <txGasPrice> _ => TP </txGasPrice> ... </message>

    rule <k> loadTransaction TXID { "nonce" : TN:Int, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <txNonce> _ => TN </txNonce> ... </message>

    rule <k> loadTransaction TXID { "value" : TV:Int, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <value> _ => TV </value> ... </message>

    rule <k> loadTransaction TXID { "to" : TT:Account, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <to> _ => TT </to> ... </message>

    rule <k> loadTransaction TXID { "data" : TI:Bytes, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <data> _ => TI </data> ... </message>

    rule <k> loadTransaction TXID { "v" : TW:Int, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <sigV> _ => TW </sigV> ... </message>

    rule <k> loadTransaction TXID { "r" : TR:Bytes, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <sigR> _ => TR </sigR> ... </message>

    rule <k> loadTransaction TXID { "s" : TS:Bytes, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <sigS> _ => TS </sigS> ... </message>

    rule <k> loadTransaction TXID { "type" : T:Int, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <txType> _ => #asmTxPrefix(T) </txType> ... </message>

    rule <k> loadTransaction TXID { "chainID" : TC:Int, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <txChainID> _ => TC </txChainID> ... </message>

    rule <k> loadTransaction TXID { "accessList" : [TA:JSONs], REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <txAccess> _ => [TA] </txAccess> ... </message>

    rule <k> loadTransaction TXID { "maxPriorityFeePerGas" : TP:Int, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <txPriorityFee> _ => TP </txPriorityFee> ... </message>

    rule <k> loadTransaction TXID { "maxFeePerGas" : TF:Int, REST => REST } ... </k>
         <message> <msgID> TXID </msgID> <txMaxFee> _ => TF </txMaxFee> ... </message>
```

### Getting State

- `#getTxData` will pull the parameters of TXID into an appropriate `TxData` symbol
- `#effectiveGasPrice` will compute the gas price for TXID, as specified by EIP-1559

```k
    syntax TxData ::= #getTxData( Int ) [function]
 // ----------------------------------------------
    rule [[ #getTxData( TXID ) => LegacyTxData(TN, TP, TG, TT, TV, DATA) ]]
         <message>
           <msgID>      TXID </msgID>
           <txNonce>    TN   </txNonce>
           <txGasPrice> TP   </txGasPrice>
           <txGasLimit> TG   </txGasLimit>
           <to>         TT   </to>
           <value>      TV   </value>
           <sigV>       TW   </sigV>
           <data>       DATA </data>
           <txType> Legacy </txType>
           ...
         </message>
      requires TW ==Int 0 orBool TW ==Int 1 orBool TW ==Int 27 orBool TW ==Int 28

    rule [[ #getTxData( TXID ) => LegacyProtectedTxData(TN, TP, TG, TT, TV, DATA, CID) ]]
         <message>
           <msgID>      TXID </msgID>
           <txNonce>    TN   </txNonce>
           <txGasPrice> TP   </txGasPrice>
           <txGasLimit> TG   </txGasLimit>
           <to>         TT   </to>
           <value>      TV   </value>
           <sigV>       TW   </sigV>
           <data>       DATA </data>
           <txChainID>  CID  </txChainID>
           <txType> Legacy </txType>
           ...
         </message>
      requires notBool (TW ==Int 0 orBool TW ==Int 1 orBool TW ==Int 27 orBool TW ==Int 28)

    rule [[ #getTxData( TXID ) => AccessListTxData(TN, TP, TG, TT, TV, DATA, CID, TA) ]]
         <message>
           <msgID>      TXID </msgID>
           <txNonce>    TN   </txNonce>
           <txGasPrice> TP   </txGasPrice>
           <txGasLimit> TG   </txGasLimit>
           <to>         TT   </to>
           <value>      TV   </value>
           <data>       DATA </data>
           <txChainID>  CID  </txChainID>
           <txAccess>   TA   </txAccess>
           <txType> AccessList </txType>
           ...
         </message>

    rule [[ #getTxData( TXID ) => DynamicFeeTxData(TN, TPF, TM, TG, TT, TV, DATA, CID, TA) ]]
         <message>
           <msgID>         TXID </msgID>
           <txNonce>       TN   </txNonce>
           <txGasLimit>    TG   </txGasLimit>
           <to>            TT   </to>
           <value>         TV   </value>
           <data>          DATA </data>
           <txChainID>     CID  </txChainID>
           <txAccess>      TA   </txAccess>
           <txPriorityFee> TPF  </txPriorityFee>
           <txMaxFee>      TM   </txMaxFee>
           <txType> DynamicFee </txType>
           ...
         </message>

    syntax Int ::= #effectiveGasPrice( Int ) [function]
 // ---------------------------------------------------
    rule [[ #effectiveGasPrice( TXID )
         => #if ( notBool Ghasbasefee << SCHED >> )
                orBool TXTYPE ==K Legacy
                orBool TXTYPE ==K AccessList
              #then GPRICE
              #else BFEE +Int minInt(TPF, TM -Int BFEE)
            #fi
         ]]
         <schedule> SCHED </schedule>
         <baseFee> BFEE </baseFee>
         <message>
           <msgID>         TXID   </msgID>
           <txGasPrice>    GPRICE </txGasPrice>
           <txType>        TXTYPE </txType>
           <txPriorityFee> TPF    </txPriorityFee>
           <txMaxFee>      TM     </txMaxFee>
           ...
         </message>
```

### Block Identifiers

```k
    syntax BlockIdentifier ::= Int
                             | "LATEST"
                             | "PENDING"
                             | "EARLIEST"
 // -------------------------------------

    syntax BlockIdentifier ::= #parseBlockIdentifier ( JSON ) [function]
 // --------------------------------------------------------------------
    rule #parseBlockIdentifier(BLOCKNUM:Int) => BLOCKNUM
    rule #parseBlockIdentifier("pending")    => PENDING
    rule #parseBlockIdentifier("latest")     => LATEST
    rule #parseBlockIdentifier("earliest")   => EARLIEST
    rule #parseBlockIdentifier(BLOCKNUM)     => #parseWord(BLOCKNUM) [owise]
```
```k
endmodule
```
