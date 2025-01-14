
┌─ 1 (root, split, init)
│   k: #next [ SELFDESTRUCT ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _STATIC_CELL:Bool
┃  │
┃  ├─ 4
┃  │   k: #next [ SELFDESTRUCT ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 6 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STATIC_MODE_VIOLATION
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  │
┃  ├─ 22
┃  │   k: #next [ SELFDESTRUCT ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (6 steps)
┃  ├─ 9
┃  │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( _W0:Int modInt pow160 ) ) ~> ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 10
┃  ┃  │   k: Cselfdestruct ( _SCHEDULE_CELL:Schedule , #accountNonexistent ( ( _W0:Int modInt ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (1 step)
┃  ┃  └─ 18 (leaf, pending)
┃  ┃      k: #accountNonexistent ( ( _W0:Int modInt pow160 ) ) ~> #freezerCselfdestruct1_ ( _ ...
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 11
┃     │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( _W0:Int modInt pow160 ) ) ~> ...
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 16 (leaf, pending)
┃     ┃      k: Cselfdestruct ( _SCHEDULE_CELL:Schedule , #accountNonexistent ( ( _W0:Int modInt ...
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        └─ 17 (leaf, pending)
┃            k: #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( _W0:Int modInt pow160 ) ) ~> ...
┃            pc: _PC_CELL:Int
┃            callDepth: _CALLDEPTH_CELL:Int
┃            statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool _STATIC_CELL:Bool )
   ┃     ( notBool _USEGAS_CELL:Bool )
   │
   ├─ 23
   │   k: #next [ SELFDESTRUCT ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (4 steps)
   ├─ 12
   │   k: SELFDESTRUCT ( _W0:Int modInt pow160 ) ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  └─ 13 (leaf, pending)
   ┃      k: #touchAccounts ACCT:Int ( _W0:Int modInt pow160 ) ~> #accessAccounts ( _W0:Int m ...
   ┃      pc: _PC_CELL:Int
   ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┣━━┓
   ┃  │
   ┃  └─ 14 (leaf, pending)
   ┃      k: #touchAccounts ( _W0:Int modInt pow160 ) ~> #accessAccounts ( _W0:Int modInt pow ...
   ┃      pc: _PC_CELL:Int
   ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 15
      │   k: SELFDESTRUCT ( _W0:Int modInt pow160 ) ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  └─ 19 (leaf, pending)
      ┃      k: #touchAccounts ACCT0:Int ( _W0:Int modInt pow160 ) ~> #accessAccounts ( _W0:Int  ...
      ┃      pc: _PC_CELL:Int
      ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┣━━┓
      ┃  │
      ┃  └─ 20 (leaf, pending)
      ┃      k: #touchAccounts ( _W0:Int modInt pow160 ) ~> #accessAccounts ( _W0:Int modInt pow ...
      ┃      pc: _PC_CELL:Int
      ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         └─ 21 (leaf, pending)
             k: SELFDESTRUCT ( _W0:Int modInt pow160 ) ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
             pc: _PC_CELL:Int
             callDepth: _CALLDEPTH_CELL:Int
             statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SELFDESTRUCT-1-SPEC
    
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             ( #next [ SELFDESTRUCT ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
                 <wordStack>
                   ( __W0 : __WS )
                 </wordStack>
                 <static>
                   ( _STATIC_CELL:Bool => true )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires _STATIC_CELL:Bool
      [priority(20), label(BASIC-BLOCK-4-TO-6)]
    
    rule [BASIC-BLOCK-10-TO-18]: <kevm>
           <k>
             ( Cselfdestruct ( _SCHEDULE_CELL:Schedule , #accountNonexistent ( ( _W0:Int modInt pow160 ) ) , BAL:Int ) ~> .K => #accountNonexistent ( ( _W0:Int modInt pow160 ) )
             ~> #freezerCselfdestruct1_ ( _SCHEDULE_CELL:Schedule ~> .K , BAL:Int ~> .K ) )
             ~> #deductGas
             ~> #access [ SELFDESTRUCT , SELFDESTRUCT ( _W0:Int modInt pow160 ) ]
             ~> SELFDESTRUCT ( _W0:Int modInt pow160 )
             ~> #pc [ SELFDESTRUCT ]
             ~> __K_CELL
           </k>
           <schedule>
             _SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             true
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ACCTFROM:Int
                 </id>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               <substate>
                 <selfDestruct>
                   _SELFDESTRUCT_CELL:Set
                 </selfDestruct>
                 <refund>
                   #if ACCTFROM:Int in _SELFDESTRUCT_CELL:Set #then _REFUND_CELL:Int #else chop ( ( _REFUND_CELL:Int +Int Rselfdestruct < _SCHEDULE_CELL:Schedule > ) ) #fi
                 </refund>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ACCTFROM:Int
                   </acctID>
                   <balance>
                     BAL:Int
                   </balance>
                   _Gen25:CodeCell
                   _Gen26:StorageCell
                   _Gen27:OrigStorageCell
                   _Gen28:TransientStorageCell
                   _Gen29:NonceCell
                 </account>
                 _DotVar8:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( __ID_CELL ==K ACCTFROM:Int
       andBool ( ( notBool __STATIC_CELL )
       andBool ( ( notBool <acctID>
          ACCTFROM:Int
        </acctID> in_keys ( _DotVar8:AccountCellMap ) )
       andBool ( __ACCOUNTS_CELL ==K ( <account>
          <acctID>
            ACCTFROM:Int
          </acctID>
          <balance>
            BAL:Int
          </balance>
          _Gen25:CodeCell
          _Gen26:StorageCell
          _Gen27:OrigStorageCell
          _Gen28:TransientStorageCell
          _Gen29:NonceCell
        </account>
        _DotVar8:AccountCellMap )
               )))))
      [priority(20), label(BASIC-BLOCK-10-TO-18)]
    
    rule [BASIC-BLOCK-22-TO-9]: <kevm>
           <k>
             ( #next [ SELFDESTRUCT ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( _W0:Int modInt pow160 ) )
             ~> #deductGas
             ~> #access [ SELFDESTRUCT , SELFDESTRUCT ( _W0:Int modInt pow160 ) ]
             ~> SELFDESTRUCT ( _W0:Int modInt pow160 )
             ~> #pc [ SELFDESTRUCT ] )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <static>
                   ( _STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( notBool _STATIC_CELL:Bool )
               ))
      [priority(20), label(BASIC-BLOCK-22-TO-9)]
    
    rule [BASIC-BLOCK-23-TO-12]: <kevm>
           <k>
             ( #next [ SELFDESTRUCT ] ~> .K => SELFDESTRUCT ( _W0:Int modInt pow160 )
             ~> #pc [ SELFDESTRUCT ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <static>
                   ( _STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _STATIC_CELL:Bool )
       andBool ( ( notBool _USEGAS_CELL:Bool )
               ))
      [priority(20), label(BASIC-BLOCK-23-TO-12)]

endmodule
