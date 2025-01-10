
┌─ 1 (root, split, init)
│   k: #next [ TSTORE ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2
┃  │
┃  ├─ 3
┃  │   k: #next [ TSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 9 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_UNDERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024
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
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
┃  ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
┃  │
┃  ├─ 5
┃  │   k: #next [ TSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  ├─ 7
┃  │   k: #exec [ TSTORE ] ~> #pc [ TSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 11 (split)
┃  ┃  │   k: #gas [ TSTORE , TSTORE W0:Int W1:Int ] ~> TSTORE W0:Int W1:Int ~> #pc [ TSTORE ] ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     _USEGAS_CELL:Bool
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 13
┃  ┃  ┃  │   k: #gas [ TSTORE , TSTORE W0:Int W1:Int ] ~> TSTORE W0:Int W1:Int ~> #pc [ TSTORE ] ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (4 steps)
┃  ┃  ┃  ├─ 24
┃  ┃  ┃  │   k: Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TS ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 25
┃  ┃  ┃  ┃  │   k: #access [ TSTORE , TSTORE W0:Int W1:Int ] ~> TSTORE W0:Int W1:Int ~> #pc [ TSTOR ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  └─ 36 (leaf, pending)
┃  ┃  ┃  ┃      k: TSTORE W0:Int W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  └─ 26 (leaf, pending)
┃  ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ TSTORE , TSTORE W0:Int W1:Int ] ~> TSTORE W0:I ...
┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓
┃  ┃  ┃     │
┃  ┃  ┃     └─ 27 (stuck, leaf)
┃  ┃  ┃         k: Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TS ...
┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃  ┃     │
┃  ┃     ├─ 14
┃  ┃     │   k: #gas [ TSTORE , TSTORE W0:Int W1:Int ] ~> TSTORE W0:Int W1:Int ~> #pc [ TSTORE ] ...
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     │
┃  ┃     │  (1 step)
┃  ┃     ├─ 19
┃  ┃     │   k: TSTORE W0:Int W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┃ (1 step)
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  └─ 22 (leaf, pending)
┃  ┃     ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┗━━┓
┃  ┃        │
┃  ┃        ├─ 23
┃  ┃        │   k: TSTORE W0:Int W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃  ┃        │   pc: _PC_CELL:Int
┃  ┃        │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┃ (1 step)
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  └─ 30 (leaf, pending)
┃  ┃        ┃      k: #pc [ TSTORE ] ~> _K_CELL:K
┃  ┃        ┃      pc: _PC_CELL:Int
┃  ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┗━━┓
┃  ┃           │
┃  ┃           └─ 31 (leaf, pending)
┃  ┃               k: TSTORE W0:Int W1:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃  ┃               pc: _PC_CELL:Int
┃  ┃               callDepth: _CALLDEPTH_CELL:Int
┃  ┃               statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 12
┃     │   k: #exec [ TSTORE ] ~> #pc [ TSTORE ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  ├─ 15 (split)
┃     ┃  │   k: #gas [ TSTORE , TSTORE W0:Int W2:Int ] ~> TSTORE W0:Int W2:Int ~> #pc [ TSTORE ] ...
┃     ┃  │   pc: _PC_CELL:Int
┃     ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┃ (branch)
┃     ┃  ┣━━┓ subst: .Subst
┃     ┃  ┃  ┃ constraint:
┃     ┃  ┃  ┃     _USEGAS_CELL:Bool
┃     ┃  ┃  │
┃     ┃  ┃  ├─ 17
┃     ┃  ┃  │   k: #gas [ TSTORE , TSTORE W0:Int W2:Int ] ~> TSTORE W0:Int W2:Int ~> #pc [ TSTORE ] ...
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  │
┃     ┃  ┃  │  (4 steps)
┃     ┃  ┃  └─ 35 (leaf, pending)
┃     ┃  ┃      k: Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TS ...
┃     ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┗━━┓ subst: .Subst
┃     ┃     ┃ constraint:
┃     ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃     ┃     │
┃     ┃     ├─ 18
┃     ┃     │   k: #gas [ TSTORE , TSTORE W0:Int W2:Int ] ~> TSTORE W0:Int W2:Int ~> #pc [ TSTORE ] ...
┃     ┃     │   pc: _PC_CELL:Int
┃     ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     │
┃     ┃     │  (1 step)
┃     ┃     └─ 34 (leaf, pending)
┃     ┃         k: TSTORE W0:Int W2:Int ~> #pc [ TSTORE ] ~> _K_CELL:K
┃     ┃         pc: _PC_CELL:Int
┃     ┃         callDepth: _CALLDEPTH_CELL:Int
┃     ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 16
┃        │   k: #exec [ TSTORE ] ~> #pc [ TSTORE ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  ├─ 20 (split)
┃        ┃  │   k: #gas [ TSTORE , TSTORE W0:Int W3:Int ] ~> TSTORE W0:Int W3:Int ~> #pc [ TSTORE ] ...
┃        ┃  │   pc: _PC_CELL:Int
┃        ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┃ (branch)
┃        ┃  ┣━━┓ subst: .Subst
┃        ┃  ┃  ┃ constraint:
┃        ┃  ┃  ┃     _USEGAS_CELL:Bool
┃        ┃  ┃  │
┃        ┃  ┃  └─ 28 (leaf, pending)
┃        ┃  ┃      k: #gas [ TSTORE , TSTORE W0:Int W3:Int ] ~> TSTORE W0:Int W3:Int ~> #pc [ TSTORE ] ...
┃        ┃  ┃      pc: _PC_CELL:Int
┃        ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┗━━┓ subst: .Subst
┃        ┃     ┃ constraint:
┃        ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃        ┃     │
┃        ┃     └─ 29 (leaf, pending)
┃        ┃         k: #gas [ TSTORE , TSTORE W0:Int W3:Int ] ~> TSTORE W0:Int W3:Int ~> #pc [ TSTORE ] ...
┃        ┃         pc: _PC_CELL:Int
┃        ┃         callDepth: _CALLDEPTH_CELL:Int
┃        ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 21
┃           │   k: #exec [ TSTORE ] ~> #pc [ TSTORE ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  └─ 32 (leaf, pending)
┃           ┃      k: #gas [ TSTORE , TSTORE W0:Int W4:Int ] ~> TSTORE W0:Int W4:Int ~> #pc [ TSTORE ] ...
┃           ┃      pc: _PC_CELL:Int
┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              └─ 33 (leaf, pending)
┃                  k: #exec [ TSTORE ] ~> #pc [ TSTORE ] ~> _K_CELL:K
┃                  pc: _PC_CELL:Int
┃                  callDepth: _CALLDEPTH_CELL:Int
┃                  statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _STATIC_CELL:Bool
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
   │
   ├─ 6
   │   k: #next [ TSTORE ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   └─ 10 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_STATIC_MODE_VIOLATION


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-TSTORE-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-7]: <kevm>
           <k>
             ( #next [ TSTORE ] ~> .K => #exec [ TSTORE ]
             ~> #pc [ TSTORE ] )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   _WORDSTACK_CELL:WordStack
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-5-TO-7)]
    
    rule [BASIC-BLOCK-4-TO-8]: <kevm>
           <k>
             ( #next [ TSTORE ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STACK_OVERFLOW )
               </statusCode>
               <callState>
                 <wordStack>
                   _WORDSTACK_CELL:WordStack
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-8)]
    
    rule [BASIC-BLOCK-3-TO-9]: <kevm>
           <k>
             ( #next [ TSTORE ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STACK_UNDERFLOW )
               </statusCode>
               <callState>
                 <wordStack>
                   _WORDSTACK_CELL:WordStack
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2
      [priority(20), label(BASIC-BLOCK-3-TO-9)]
    
    rule [BASIC-BLOCK-6-TO-10]: <kevm>
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
                   _WORDSTACK_CELL:WordStack
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
      requires ( _STATIC_CELL:Bool
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-6-TO-10)]
    
    rule [BASIC-BLOCK-14-TO-19]: <kevm>
           <k>
             ( #gas [ TSTORE , TSTORE W0:Int W1:Int ] ~> .K => .K )
             ~> TSTORE W0:Int W1:Int
             ~> #pc [ TSTORE ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool __STATIC_CELL )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-14-TO-19)]
    
    rule [BASIC-BLOCK-13-TO-24]: <kevm>
           <k>
             ( #gas [ TSTORE , TSTORE W0:Int W1:Int ] ~> .K => Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ TSTORE , TSTORE W0:Int W1:Int ] )
             ~> TSTORE W0:Int W1:Int
             ~> #pc [ TSTORE ]
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
                   WS:WordStack
                 </wordStack>
                 <static>
                   false
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
       andBool ( ( notBool __STATIC_CELL )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-13-TO-24)]
    
    rule [BASIC-BLOCK-18-TO-34]: <kevm>
           <k>
             ( #gas [ TSTORE , TSTORE W0:Int W2:Int ] ~> .K => .K )
             ~> TSTORE W0:Int W2:Int
             ~> #pc [ TSTORE ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   WS0:WordStack
                 </wordStack>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool __STATIC_CELL )
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int -1 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-18-TO-34)]
    
    rule [BASIC-BLOCK-17-TO-35]: <kevm>
           <k>
             ( #gas [ TSTORE , TSTORE W0:Int W2:Int ] ~> .K => Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ TSTORE , TSTORE W0:Int W2:Int ] )
             ~> TSTORE W0:Int W2:Int
             ~> #pc [ TSTORE ]
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
                   WS0:WordStack
                 </wordStack>
                 <static>
                   false
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
       andBool ( ( notBool __STATIC_CELL )
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int -1 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-17-TO-35)]
    
    rule [BASIC-BLOCK-25-TO-36]: <kevm>
           <k>
             ( #access [ TSTORE , TSTORE W0:Int W1:Int ] ~> .K => .K )
             ~> TSTORE W0:Int W1:Int
             ~> #pc [ TSTORE ]
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
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule >
                 </gas>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool __STATIC_CELL )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( Gwarmstoragedirtystore < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-25-TO-36)]

endmodule
