
┌─ 1 (root, split, init)
│   k: #next [ SSTORE ] ~> _K_CELL:K
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
┃  │   k: #next [ SSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 8 (leaf, terminal)
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
┃  │   k: #next [ SSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (6 steps)
┃  ├─ 12
┃  │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE _W0:Int _W1:Int ) ~> #deductGas ~> # ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 13 (split)
┃  ┃  │   k: Csstore ( _SCHEDULE_CELL:Schedule , _W1:Int , #lookup ( STORAGE:Map , _W0:Int )  ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     Csstore ( _SCHEDULE_CELL:Schedule , _W1:Int , #lookup ( STORAGE:Map , _W0:Int ) , #lookup ( ORIGSTORAGE:Map , _W0:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃  ┃  │
┃  ┃  ┃  └─ 20 (leaf, pending)
┃  ┃  ┃      k: Csstore ( _SCHEDULE_CELL:Schedule , _W1:Int , #lookup ( STORAGE:Map , _W0:Int )  ...
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     _GAS_CELL:Gas <Gas Csstore ( _SCHEDULE_CELL:Schedule , _W1:Int , #lookup ( STORAGE:Map , _W0:Int ) , #lookup ( ORIGSTORAGE:Map , _W0:Int ) )
┃  ┃     │
┃  ┃     └─ 21 (leaf, pending)
┃  ┃         k: Csstore ( _SCHEDULE_CELL:Schedule , _W1:Int , #lookup ( STORAGE:Map , _W0:Int )  ...
┃  ┃         pc: _PC_CELL:Int
┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 14 (leaf, pending)
┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #deductGas ~> #access [ SSTORE , SSTORE _W0:Int _W1:Int  ...
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 15
┃     │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE _W0:Int _W1:Int ) ~> #deductGas ~> # ...
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 18 (leaf, pending)
┃     ┃      k: Csstore ( _SCHEDULE_CELL:Schedule , _W1:Int , #lookup ( STORAGE0:Map , _W0:Int ) ...
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        └─ 19 (leaf, pending)
┃            k: #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE _W0:Int _W1:Int ) ~> #deductGas ~> # ...
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
   │   k: #next [ SSTORE ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (4 steps)
   ├─ 9
   │   k: SSTORE _W0:Int _W1:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  └─ 10 (leaf, pending)
   ┃      k: #pc [ SSTORE ] ~> _K_CELL:K
   ┃      pc: _PC_CELL:Int
   ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 11
      │   k: SSTORE _W0:Int _W1:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  └─ 16 (leaf, pending)
      ┃      k: #pc [ SSTORE ] ~> _K_CELL:K
      ┃      pc: _PC_CELL:Int
      ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         └─ 17 (leaf, pending)
             k: SSTORE _W0:Int _W1:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
             pc: _PC_CELL:Int
             callDepth: _CALLDEPTH_CELL:Int
             statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SSTORE-2-SPEC
    
    
    rule [BASIC-BLOCK-4-TO-8]: <kevm>
           <k>
             ( #next [ SSTORE ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
                 <wordStack>
                   ( __W0 : ( __W1 : __WS ) )
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
      [priority(20), label(BASIC-BLOCK-4-TO-8)]
    
    rule [BASIC-BLOCK-22-TO-12]: <kevm>
           <k>
             ( #next [ SSTORE ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE _W0:Int _W1:Int )
             ~> #deductGas
             ~> #access [ SSTORE , SSTORE _W0:Int _W1:Int ]
             ~> SSTORE _W0:Int _W1:Int
             ~> #pc [ SSTORE ] )
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
                   ( ( _W0:Int : ( _W1:Int : _WS:WordStack ) ) => _WS:WordStack )
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
      [priority(20), label(BASIC-BLOCK-22-TO-12)]
    
    rule [BASIC-BLOCK-23-TO-9]: <kevm>
           <k>
             ( #next [ SSTORE ] ~> .K => SSTORE _W0:Int _W1:Int
             ~> #pc [ SSTORE ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : ( _W1:Int : _WS:WordStack ) ) => _WS:WordStack )
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
      [priority(20), label(BASIC-BLOCK-23-TO-9)]

endmodule
