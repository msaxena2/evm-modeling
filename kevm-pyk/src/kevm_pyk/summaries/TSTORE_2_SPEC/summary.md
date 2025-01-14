
┌─ 1 (root, split, init)
│   k: #next [ TSTORE ] ~> _K_CELL:K
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
┃  │   k: #next [ TSTORE ] ~> _K_CELL:K
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
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 34
┃  │   k: #next [ TSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 9
┃  │   k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 10 (leaf, pending)
┃  ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 11
┃     │   k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 15 (leaf, pending)
┃     ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 16
┃        │   k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  └─ 20 (leaf, pending)
┃        ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃        ┃      pc: _PC_CELL:Int
┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 21
┃           │   k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  └─ 24 (leaf, pending)
┃           ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃           ┃      pc: _PC_CELL:Int
┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              ├─ 25
┃              │   k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃              │   pc: _PC_CELL:Int
┃              │   callDepth: _CALLDEPTH_CELL:Int
┃              │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┃ (1 step)
┃              ┣━━┓
┃              ┃  │
┃              ┃  └─ 29 (leaf, pending)
┃              ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃              ┃      pc: _PC_CELL:Int
┃              ┃      callDepth: _CALLDEPTH_CELL:Int
┃              ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┗━━┓
┃                 │
┃                 └─ 30 (leaf, pending)
┃                     k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃                     pc: _PC_CELL:Int
┃                     callDepth: _CALLDEPTH_CELL:Int
┃                     statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 37
┃  │   k: #next [ TSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (9 steps)
┃  ├─ 17
┃  │   k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 18 (leaf, pending)
┃  ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 19
┃     │   k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 22 (leaf, pending)
┃     ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 23
┃        │   k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  └─ 27 (leaf, pending)
┃        ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃        ┃      pc: _PC_CELL:Int
┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 28
┃           │   k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  └─ 31 (leaf, pending)
┃           ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃           ┃      pc: _PC_CELL:Int
┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              └─ 32 (leaf, pending)
┃                  k: TSTORE _W0:Int _W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃                  pc: _PC_CELL:Int
┃                  callDepth: _CALLDEPTH_CELL:Int
┃                  statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     ( notBool _STATIC_CELL:Bool )
   ┃     _GAS_CELL:Gas <Gas Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule >
   │
   ├─ 38
   │   k: #next [ TSTORE ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (12 steps)
   └─ 26 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-TSTORE-2-SPEC
    
    
    rule [BASIC-BLOCK-4-TO-8]: <kevm>
           <k>
             ( #next [ TSTORE ] => #halt )
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
    
    rule [BASIC-BLOCK-34-TO-9]: <kevm>
           <k>
             ( #next [ TSTORE ] ~> .K => TSTORE _W0:Int _W1:Int
             ~> #pc [ TSTORE ] )
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
      [priority(20), label(BASIC-BLOCK-34-TO-9)]
    
    rule [BASIC-BLOCK-37-TO-17]: <kevm>
           <k>
             ( #next [ TSTORE ] ~> .K => TSTORE _W0:Int _W1:Int
             ~> #pc [ TSTORE ] )
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
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule > )
                 </gas>
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
       andBool ( Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               )))
      [priority(20), label(BASIC-BLOCK-37-TO-17)]
    
    rule [BASIC-BLOCK-38-TO-26]: <kevm>
           <k>
             ( #next [ TSTORE ] => #halt )
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
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_OUT_OF_GAS )
               </statusCode>
               <callState>
                 <wordStack>
                   ( ( __W0 : ( __W1 : _WS:WordStack ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
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
       andBool ( _GAS_CELL:Gas <Gas Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule >
               )))
      [priority(20), label(BASIC-BLOCK-38-TO-26)]

endmodule
