
┌─ 1 (root, split, init)
│   k: #next [ CALLCODE ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 20
┃  │   k: #next [ CALLCODE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 6
┃  │   k: CALLCODE _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:I ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 7
┃  ┃  │   k: #accessAccounts ( _W1:Int modInt pow160 ) ~> #checkCall ACCTFROM:Int _W2:Int ~>  ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (2 steps)
┃  ┃  ├─ 12
┃  ┃  │   k: #checkBalanceUnderflow ACCTFROM:Int _W2:Int ~> #checkDepthExceeded ~> #call ACCT ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (1 step)
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  └─ 13 (leaf, pending)
┃  ┃  ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  └─ 14 (leaf, pending)
┃  ┃  ┃      k: #checkDepthExceeded ~> #call ACCTFROM:Int ACCTFROM:Int ( _W1:Int modInt pow160 ) ...
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓
┃  ┃     │
┃  ┃     └─ 15 (leaf, pending)
┃  ┃         k: #checkBalanceUnderflow ACCTFROM:Int _W2:Int ~> #checkDepthExceeded ~> #call ACCT ...
┃  ┃         pc: _PC_CELL:Int
┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 8 (stuck, leaf)
┃         k: CALLCODE _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:I ...
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 23
┃  │   k: #next [ CALLCODE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (9 steps)
┃  ├─ 16
┃  │   k: #gasExec ( _SCHEDULE_CELL:Schedule , CALLCODE _W0:Int ( _W1:Int modInt pow160 )  ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 17 (leaf, pending)
┃  ┃      k: Ccallgas ( _SCHEDULE_CELL:Schedule , #accountNonexistent ( ACCTFROM:Int ) , _W0: ...
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 18 (leaf, pending)
┃         k: #gasExec ( _SCHEDULE_CELL:Schedule , CALLCODE _W0:Int ( _W1:Int modInt pow160 )  ...
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
   │
   ├─ 24
   │   k: #next [ CALLCODE ] ~> _K_CELL:K
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



module SUMMARY-CALLCODE-7-SPEC
    
    
    rule [BASIC-BLOCK-7-TO-12]: <kevm>
           <k>
             ( #accessAccounts ( _W1:Int modInt pow160 )
             ~> #checkCall ACCTFROM:Int _W2:Int => #checkBalanceUnderflow ACCTFROM:Int _W2:Int
             ~> #checkDepthExceeded )
             ~> #call ACCTFROM:Int ACCTFROM:Int ( _W1:Int modInt pow160 ) _W2:Int _W2:Int #range ( _LOCALMEM_CELL:Bytes , __W3 , __W4 ) false
             ~> #return __W5 __W6
             ~> #pc [ CALLCODE ]
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
       andBool ( ( notBool __USEGAS_CELL )
               ))
      [priority(20), label(BASIC-BLOCK-7-TO-12)]
    
    rule [BASIC-BLOCK-20-TO-6]: <kevm>
           <k>
             ( #next [ CALLCODE ] ~> .K => CALLCODE _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int
             ~> #pc [ CALLCODE ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) => _WS:WordStack )
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
      [priority(20), label(BASIC-BLOCK-20-TO-6)]
    
    rule [BASIC-BLOCK-23-TO-16]: <kevm>
           <k>
             ( #next [ CALLCODE ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , CALLCODE _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int )
             ~> #deductGas
             ~> #access [ CALLCODE , CALLCODE _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int ]
             ~> CALLCODE _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int
             ~> #pc [ CALLCODE ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) )
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
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               ))
      [priority(20), label(BASIC-BLOCK-23-TO-16)]
    
    rule [BASIC-BLOCK-24-TO-11]: <kevm>
           <k>
             ( #next [ CALLCODE ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ CALLCODE _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int ]
             ~> #access [ CALLCODE , CALLCODE _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int ]
             ~> CALLCODE _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int
             ~> #pc [ CALLCODE ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) )
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
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))
      [priority(20), label(BASIC-BLOCK-24-TO-11)]

endmodule
