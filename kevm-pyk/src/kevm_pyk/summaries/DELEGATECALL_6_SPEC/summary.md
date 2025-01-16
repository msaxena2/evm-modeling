
┌─ 1 (root, split, init)
│   k: #next [ DELEGATECALL ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 25
┃  │   k: #next [ DELEGATECALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 6
┃  │   k: DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ~ ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 7
┃  ┃  │   k: #accessAccounts ( _W1:Int modInt pow160 ) ~> #checkCall ACCTFROM:Int 0 ~> #call  ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (2 steps)
┃  ┃  ├─ 14
┃  ┃  │   k: #checkBalanceUnderflow ACCTFROM:Int 0 ~> #checkDepthExceeded ~> #call ACCTAPPFRO ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (1 step)
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  └─ 15 (leaf, pending)
┃  ┃  ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  └─ 16 (leaf, pending)
┃  ┃  ┃      k: #checkDepthExceeded ~> #call ACCTAPPFROM:Int ACCTFROM:Int ( _W1:Int modInt pow16 ...
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓
┃  ┃     │
┃  ┃     └─ 17 (leaf, pending)
┃  ┃         k: #checkBalanceUnderflow ACCTFROM:Int 0 ~> #checkDepthExceeded ~> #call ACCTAPPFRO ...
┃  ┃         pc: _PC_CELL:Int
┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 8
┃     │   k: DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ~ ...
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  ├─ 12
┃     ┃  │   k: #accessAccounts ( _W1:Int modInt pow160 ) ~> #checkCall ACCTFROM0:Int 0 ~> #call ...
┃     ┃  │   pc: _PC_CELL:Int
┃     ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  │
┃     ┃  │  (2 steps)
┃     ┃  └─ 23 (leaf, pending)
┃     ┃      k: #checkBalanceUnderflow ACCTFROM0:Int 0 ~> #checkDepthExceeded ~> #call ACCTAPPFR ...
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 13
┃        │   k: DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ~ ...
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  └─ 19 (leaf, pending)
┃        ┃      k: #accessAccounts ( _W1:Int modInt pow160 ) ~> #checkCall ACCTFROM1:Int 0 ~> #call ...
┃        ┃      pc: _PC_CELL:Int
┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           └─ 20 (leaf, pending)
┃               k: DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ~ ...
┃               pc: _PC_CELL:Int
┃               callDepth: _CALLDEPTH_CELL:Int
┃               statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 28
┃  │   k: #next [ DELEGATECALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (9 steps)
┃  ├─ 18
┃  │   k: #gasExec ( _SCHEDULE_CELL:Schedule , DELEGATECALL _W0:Int ( _W1:Int modInt pow16 ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 21 (leaf, pending)
┃  ┃      k: Ccallgas ( _SCHEDULE_CELL:Schedule , #accountNonexistent ( ACCTFROM:Int ) , _W0: ...
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 22 (leaf, pending)
┃         k: #gasExec ( _SCHEDULE_CELL:Schedule , DELEGATECALL _W0:Int ( _W1:Int modInt pow16 ...
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
   │
   ├─ 29
   │   k: #next [ DELEGATECALL ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (7 steps)
   └─ 11 (leaf, pending)
       k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _ME ...
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-DELEGATECALL-6-SPEC
    
    
    rule [BASIC-BLOCK-7-TO-14]: <kevm>
           <k>
             ( #accessAccounts ( _W1:Int modInt pow160 )
             ~> #checkCall ACCTFROM:Int 0 => #checkBalanceUnderflow ACCTFROM:Int 0
             ~> #checkDepthExceeded )
             ~> #call ACCTAPPFROM:Int ACCTFROM:Int ( _W1:Int modInt pow160 ) 0 _CALLVALUE_CELL:Int #range ( _LOCALMEM_CELL:Bytes , __W2 , __W3 ) false
             ~> #return __W4 __W5
             ~> #pc [ DELEGATECALL ]
             ~> __K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ACCTFROM:Int
                 </id>
                 <caller>
                   ACCTAPPFROM:Int
                 </caller>
                 <callValue>
                   _CALLVALUE_CELL:Int
                 </callValue>
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( _ACCESSEDACCOUNTS_CELL:Set => _ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( _W1:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __ID_CELL ==K ACCTFROM:Int
       andBool ( __CALLER_CELL ==K ACCTAPPFROM:Int
       andBool ( ( notBool __USEGAS_CELL )
               )))
      [priority(20), label(BASIC-BLOCK-7-TO-14)]
    
    rule [BASIC-BLOCK-12-TO-23]: <kevm>
           <k>
             ( #accessAccounts ( _W1:Int modInt pow160 )
             ~> #checkCall ACCTFROM0:Int 0 => #checkBalanceUnderflow ACCTFROM0:Int 0
             ~> #checkDepthExceeded )
             ~> #call ACCTAPPFROM:Int ACCTFROM0:Int ( _W1:Int modInt pow160 ) 0 _CALLVALUE_CELL:Int #range ( _LOCALMEM_CELL:Bytes , __W2 , __W3 ) false
             ~> #return __W4 __W5
             ~> #pc [ DELEGATECALL ]
             ~> __K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ACCTFROM0:Int
                 </id>
                 <caller>
                   ACCTAPPFROM:Int
                 </caller>
                 <callValue>
                   _CALLVALUE_CELL:Int
                 </callValue>
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( _ACCESSEDACCOUNTS_CELL:Set => _ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( _W1:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __ID_CELL ==K ACCTFROM0:Int
       andBool ( __CALLER_CELL ==K ACCTAPPFROM:Int
       andBool ( ( notBool __USEGAS_CELL )
       andBool ( _ACCTFROM =/=Int ACCTFROM0:Int
               ))))
      [priority(20), label(BASIC-BLOCK-12-TO-23)]
    
    rule [BASIC-BLOCK-25-TO-6]: <kevm>
           <k>
             ( #next [ DELEGATECALL ] ~> .K => DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int
             ~> #pc [ DELEGATECALL ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : _WS:WordStack ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( notBool _USEGAS_CELL:Bool )
      [priority(20), label(BASIC-BLOCK-25-TO-6)]
    
    rule [BASIC-BLOCK-28-TO-18]: <kevm>
           <k>
             ( #next [ DELEGATECALL ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int )
             ~> #deductGas
             ~> #access [ DELEGATECALL , DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ]
             ~> DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int
             ~> #pc [ DELEGATECALL ] )
             ~> __K_CELL
           </k>
           <schedule>
             _SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             ( _USEGAS_CELL:Bool => true )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : _WS:WordStack ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               ))
      [priority(20), label(BASIC-BLOCK-28-TO-18)]
    
    rule [BASIC-BLOCK-29-TO-11]: <kevm>
           <k>
             ( #next [ DELEGATECALL ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ]
             ~> #access [ DELEGATECALL , DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ]
             ~> DELEGATECALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int
             ~> #pc [ DELEGATECALL ] )
             ~> __K_CELL
           </k>
           <schedule>
             _SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             ( _USEGAS_CELL:Bool => true )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : _WS:WordStack ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))
      [priority(20), label(BASIC-BLOCK-29-TO-11)]

endmodule
