
┌─ 1 (root, split, init)
│   k: #next [ CALL ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     STATIC_CELL:Bool
┃  ┃     #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) )
┃  │
┃  ├─ 4
┃  │   k: #next [ CALL ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 6 (leaf, terminal)
┃      k: #halt ~> K_CELL:K
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STATIC_MODE_VIOLATION
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     USEGAS_CELL:Bool
┃  ┃     ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) <=Gas GAS_CELL:Gas
┃  ┃     ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
┃  │
┃  ├─ 34
┃  │   k: #next [ CALL ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (11 steps)
┃  ├─ 19 (split)
┃  │   k: #accountNonexistent ( ( W1:Int modInt pow160 ) ) ~> #freezerCcallgas1_ ( SCHEDUL ...
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (branch)
┃  ┣━━┓ subst: .Subst
┃  ┃  ┃ constraint:
┃  ┃  ┃     ID_CELL:Int ==Int ( W1:Int modInt pow160 )
┃  ┃  ┃     ( notBool <acctID>
  ( W1:Int modInt pow160 )
</acctID> in_keys ( DotAccountVar:AccountCellMap ) )
┃  ┃  │
┃  ┃  └─ 23 (leaf, pending)
┃  ┃      k: #accountNonexistent ( ( W1:Int modInt pow160 ) ) ~> #freezerCcallgas1_ ( SCHEDUL ...
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓ subst: .Subst
┃  ┃  ┃ constraint:
┃  ┃  ┃     ( notBool <acctID>
  ID_CELL:Int
</acctID> in_keys ( AC1_1:AccountCellMap ) )
┃  ┃  ┃     ( notBool ID_CELL:Int ==Int ( W1:Int modInt pow160 ) )
┃  ┃  ┃     ( notBool <acctID>
  ( W1:Int modInt pow160 )
</acctID> in_keys ( AC1_1:AccountCellMap ) )
┃  ┃  ┃     DotAccountVar:AccountCellMap ==K ( <account>
  <acctID>
    ( W1:Int modInt pow160 )
  </acctID>
  <balance>
    BAL:Int
  </balance>
  <code>
    CODE:AccountCode
  </code>
  _Gen0:StorageCell
  _Gen1:OrigStorageCell
  _Gen2:TransientStorageCell
  <nonce>
    NONCE:Int
  </nonce>
</account>
AC1_1:AccountCellMap )
┃  ┃  │
┃  ┃  └─ 24 (leaf, pending)
┃  ┃      k: #accountNonexistent ( ( W1:Int modInt pow160 ) ) ~> #freezerCcallgas1_ ( SCHEDUL ...
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓ subst: .Subst
┃     ┃ constraint: true
┃     │
┃     └─ 25 (leaf, pending)
┃         k: #accountNonexistent ( ( W1:Int modInt pow160 ) ) ~> #freezerCcallgas1_ ( SCHEDUL ...
┃         pc: PC_CELL:Int
┃         callDepth: CALLDEPTH_CELL:Int
┃         statusCode: STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     USEGAS_CELL:Bool
┃  ┃     GAS_CELL:Gas <Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) )
┃  ┃     ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
┃  │
┃  ├─ 35
┃  │   k: #next [ CALL ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  └─ 14 (leaf, pending)
┃      k: ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( MEMO ...
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool USEGAS_CELL:Bool )
┃  ┃     BALANCE_CELL:Int <Int W2:Int
┃  ┃     ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
┃  │
┃  ├─ 36
┃  │   k: #next [ CALL ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  └─ 10 (leaf, pending)
┃      k: #checkBalanceUnderflow ID_CELL:Int W2:Int ~> #checkDepthExceeded ~> #call ID_CEL ...
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool USEGAS_CELL:Bool )
┃  ┃     W2:Int <=Int BALANCE_CELL:Int
┃  ┃     CALLDEPTH_CELL:Int <Int 1024
┃  ┃     ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
┃  │
┃  ├─ 40
┃  │   k: #next [ CALL ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (9 steps)
┃  ├─ 18 (split)
┃  │   k: #call ID_CELL:Int ( W1:Int modInt pow160 ) ( W1:Int modInt pow160 ) W2:Int W2:In ...
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (branch)
┃  ┣━━┓ subst: .Subst
┃  ┃  ┃ constraint:
┃  ┃  ┃     CODE_CELL:AccountCode ==K CODE:Bytes
┃  ┃  ┃     ID_CELL:Int ==Int ( W1:Int modInt pow160 )
┃  ┃  ┃     ( notBool <acctID>
  ( W1:Int modInt pow160 )
</acctID> in_keys ( DotAccountVar:AccountCellMap ) )
┃  ┃  │
┃  ┃  └─ 20 (leaf, pending)
┃  ┃      k: #call ID_CELL:Int ( W1:Int modInt pow160 ) ( W1:Int modInt pow160 ) W2:Int W2:In ...
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓ subst: .Subst
┃  ┃  ┃ constraint:
┃  ┃  ┃     ( notBool <acctID>
  ID_CELL:Int
</acctID> in_keys ( AC1_1:AccountCellMap ) )
┃  ┃  ┃     ( notBool ID_CELL:Int ==Int ( W1:Int modInt pow160 ) )
┃  ┃  ┃     ( notBool <acctID>
  ( W1:Int modInt pow160 )
</acctID> in_keys ( AC1_1:AccountCellMap ) )
┃  ┃  ┃     DotAccountVar:AccountCellMap ==K ( <account>
  <acctID>
    ( W1:Int modInt pow160 )
  </acctID>
  _Gen0:BalanceCell
  <code>
    CODE:Bytes
  </code>
  _Gen1:StorageCell
  _Gen2:OrigStorageCell
  _Gen3:TransientStorageCell
  _Gen4:NonceCell
</account>
AC1_1:AccountCellMap )
┃  ┃  │
┃  ┃  └─ 21 (leaf, pending)
┃  ┃      k: #call ID_CELL:Int ( W1:Int modInt pow160 ) ( W1:Int modInt pow160 ) W2:Int W2:In ...
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓ subst: .Subst
┃     ┃ constraint: true
┃     │
┃     └─ 22 (leaf, pending)
┃         k: #call ID_CELL:Int ( W1:Int modInt pow160 ) ( W1:Int modInt pow160 ) W2:Int W2:In ...
┃         pc: PC_CELL:Int
┃         callDepth: CALLDEPTH_CELL:Int
┃         statusCode: STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool USEGAS_CELL:Bool )
   ┃     W2:Int <=Int BALANCE_CELL:Int
   ┃     1024 <=Int CALLDEPTH_CELL:Int
   ┃     ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
   │
   ├─ 41
   │   k: #next [ CALL ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   │
   │  (8 steps)
   └─ 17 (leaf, pending)
       k: #checkDepthExceeded ~> #call ID_CELL:Int ( W1:Int modInt pow160 ) ( W1:Int modIn ...
       pc: PC_CELL:Int
       callDepth: CALLDEPTH_CELL:Int
       statusCode: STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: K_CELL:K
│   pc: FINAL_PC_CELL:Int
│   callDepth: FINAL_CALLDEPTH_CELL:Int
│   statusCode: FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-CALL-7-SPEC
    
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             ( #next [ CALL ] => #halt )
             ~> _K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( _STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) )
                 </wordStack>
                 <static>
                   ( STATIC_CELL:Bool => true )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( STATIC_CELL:Bool
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) )
               )))
      [priority(20), label(BASIC-BLOCK-4-TO-6)]
    
    rule [BASIC-BLOCK-36-TO-10]: <kevm>
           <k>
             ( #next [ CALL ] ~> .K => #checkBalanceUnderflow ID_CELL:Int W2:Int
             ~> #checkDepthExceeded
             ~> #call ID_CELL:Int ( W1:Int modInt pow160 ) ( W1:Int modInt pow160 ) W2:Int W2:Int #range ( LOCALMEM_CELL:Bytes , W3:Int , W4:Int ) false
             ~> #return W5:Int W6:Int
             ~> #pc [ CALL ] )
             ~> _K_CELL
           </k>
           <useGas>
             ( USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   STATIC_CELL:Bool
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( ACCESSEDACCOUNTS_CELL:Set => ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( W1:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <balance>
                     BALANCE_CELL:Int
                   </balance>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool USEGAS_CELL:Bool )
       andBool ( BALANCE_CELL:Int <Int W2:Int
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
               ))))
      [priority(20), label(BASIC-BLOCK-36-TO-10)]
    
    rule [BASIC-BLOCK-34-TO-19]: <kevm>
           <k>
             ( #next [ CALL ] ~> .K => #accountNonexistent ( ( W1:Int modInt pow160 ) )
             ~> #freezerCcallgas1_ ( SCHEDULE_CELL:Schedule ~> .K , W0:Int ~> .K , GAS_CELL:Gas -Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) ~> .K , W2:Int ~> .K , ( W1:Int modInt pow160 ) in ACCESSEDACCOUNTS_CELL:Set ~> .K )
             ~> #allocateCallGas
             ~> Ccall ( SCHEDULE_CELL:Schedule , #accountNonexistent ( ( W1:Int modInt pow160 ) ) , W0:Int , GAS_CELL:Gas -Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) , W2:Int , ( W1:Int modInt pow160 ) in ACCESSEDACCOUNTS_CELL:Set )
             ~> #deductGas
             ~> #access [ CALL , CALL W0:Int ( W1:Int modInt pow160 ) W2:Int W3:Int W4:Int W5:Int W6:Int ]
             ~> CALL W0:Int ( W1:Int modInt pow160 ) W2:Int W3:Int W4:Int W5:Int W6:Int
             ~> #pc [ CALL ] )
             ~> _K_CELL
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             ( USEGAS_CELL:Bool => true )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) => WS:WordStack )
                 </wordStack>
                 <gas>
                   ( GAS_CELL:Gas => GAS_CELL:Gas -Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) )
                 </memoryUsed>
                 <static>
                   STATIC_CELL:Bool
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( USEGAS_CELL:Bool
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) <=Gas GAS_CELL:Gas
       andBool ( ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
               ))))
      [priority(20), label(BASIC-BLOCK-34-TO-19)]
    
    rule [BASIC-BLOCK-35-TO-14]: <kevm>
           <k>
             ( #next [ CALL ] ~> .K => ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ CALL W0:Int ( W1:Int modInt pow160 ) W2:Int W3:Int W4:Int W5:Int W6:Int ]
             ~> #access [ CALL , CALL W0:Int ( W1:Int modInt pow160 ) W2:Int W3:Int W4:Int W5:Int W6:Int ]
             ~> CALL W0:Int ( W1:Int modInt pow160 ) W2:Int W3:Int W4:Int W5:Int W6:Int
             ~> #pc [ CALL ] )
             ~> _K_CELL
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             ( USEGAS_CELL:Bool => true )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) => WS:WordStack )
                 </wordStack>
                 <gas>
                   GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) )
                 </memoryUsed>
                 <static>
                   STATIC_CELL:Bool
                 </static>
                 ...
               </callState>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( USEGAS_CELL:Bool
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( GAS_CELL:Gas <Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W3:Int , W4:Int ) , W5:Int , W6:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) )
       andBool ( ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
               ))))
      [priority(20), label(BASIC-BLOCK-35-TO-14)]
    
    rule [BASIC-BLOCK-40-TO-18]: <kevm>
           <k>
             ( #next [ CALL ] ~> .K => #call ID_CELL:Int ( W1:Int modInt pow160 ) ( W1:Int modInt pow160 ) W2:Int W2:Int #range ( LOCALMEM_CELL:Bytes , W3:Int , W4:Int ) false
             ~> #return W5:Int W6:Int
             ~> #pc [ CALL ] )
             ~> _K_CELL
           </k>
           <useGas>
             ( USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   STATIC_CELL:Bool
                 </static>
                 <callDepth>
                   CALLDEPTH_CELL:Int
                 </callDepth>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( ACCESSEDACCOUNTS_CELL:Set => ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( W1:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <balance>
                     BALANCE_CELL:Int
                   </balance>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool USEGAS_CELL:Bool )
       andBool ( W2:Int <=Int BALANCE_CELL:Int
       andBool ( CALLDEPTH_CELL:Int <Int 1024
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
               )))))
      [priority(20), label(BASIC-BLOCK-40-TO-18)]
    
    rule [BASIC-BLOCK-41-TO-17]: <kevm>
           <k>
             ( #next [ CALL ] ~> .K => #checkDepthExceeded
             ~> #call ID_CELL:Int ( W1:Int modInt pow160 ) ( W1:Int modInt pow160 ) W2:Int W2:Int #range ( LOCALMEM_CELL:Bytes , W3:Int , W4:Int ) false
             ~> #return W5:Int W6:Int
             ~> #pc [ CALL ] )
             ~> _K_CELL
           </k>
           <useGas>
             ( USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   STATIC_CELL:Bool
                 </static>
                 <callDepth>
                   CALLDEPTH_CELL:Int
                 </callDepth>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( ACCESSEDACCOUNTS_CELL:Set => ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( W1:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <balance>
                     BALANCE_CELL:Int
                   </balance>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool USEGAS_CELL:Bool )
       andBool ( W2:Int <=Int BALANCE_CELL:Int
       andBool ( 1024 <=Int CALLDEPTH_CELL:Int
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( notBool ( STATIC_CELL:Bool andBool #changesState ( CALL , ( W0:Int : ( W1:Int : ( W2:Int : ( W3:Int : ( W4:Int : ( W5:Int : ( W6:Int : WS:WordStack ) ) ) ) ) ) ) ) ) )
               )))))
      [priority(20), label(BASIC-BLOCK-41-TO-17)]

endmodule
