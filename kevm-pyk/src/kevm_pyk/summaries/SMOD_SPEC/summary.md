
┌─ 1 (root, split, init)
│   k: #next [ SMOD ] ~> _K_CELL:K
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
┃  │   k: #next [ SMOD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 7 (leaf, terminal)
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
┃  │   k: #next [ SMOD ] ~> _K_CELL:K
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
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
   │
   ├─ 5
   │   k: #next [ SMOD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 6
   │   k: #exec [ SMOD ] ~> #pc [ SMOD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9 (split)
   ┃  │   k: #gas [ SMOD , SMOD W0:Int W1:Int ] ~> SMOD W0:Int W1:Int ~> #pc [ SMOD ] ~> _K_C ...
   ┃  │   pc: _PC_CELL:Int
   ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┃ (branch)
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     _USEGAS_CELL:Bool
   ┃  ┃  │
   ┃  ┃  ├─ 11
   ┃  ┃  │   k: #gas [ SMOD , SMOD W0:Int W1:Int ] ~> SMOD W0:Int W1:Int ~> #pc [ SMOD ] ~> _K_C ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 19
   ┃  ┃  │   k: Glow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ SMOD , SMOD W0:Int W ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 20 (leaf, pending)
   ┃  ┃  ┃      k: #access [ SMOD , SMOD W0:Int W1:Int ] ~> SMOD W0:Int W1:Int ~> #pc [ SMOD ] ~> _ ...
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 21 (leaf, pending)
   ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ SMOD , SMOD W0:Int W1:Int ] ~> SMOD W0:Int W1: ...
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 22 (stuck, leaf)
   ┃  ┃         k: Glow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ SMOD , SMOD W0:Int W ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     └─ 12 (leaf, pending)
   ┃         k: #gas [ SMOD , SMOD W0:Int W1:Int ] ~> SMOD W0:Int W1:Int ~> #pc [ SMOD ] ~> _K_C ...
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #exec [ SMOD ] ~> #pc [ SMOD ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13 (split)
      ┃  │   k: #gas [ SMOD , SMOD W0:Int W2:Int ] ~> SMOD W0:Int W2:Int ~> #pc [ SMOD ] ~> _K_C ...
      ┃  │   pc: _PC_CELL:Int
      ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┃ (branch)
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     _USEGAS_CELL:Bool
      ┃  ┃  │
      ┃  ┃  ├─ 15
      ┃  ┃  │   k: #gas [ SMOD , SMOD W0:Int W2:Int ] ~> SMOD W0:Int W2:Int ~> #pc [ SMOD ] ~> _K_C ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (4 steps)
      ┃  ┃  └─ 27 (leaf, pending)
      ┃  ┃      k: Glow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ SMOD , SMOD W0:Int W ...
      ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     └─ 16 (leaf, pending)
      ┃         k: #gas [ SMOD , SMOD W0:Int W2:Int ] ~> SMOD W0:Int W2:Int ~> #pc [ SMOD ] ~> _K_C ...
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 14
         │   k: #exec [ SMOD ] ~> #pc [ SMOD ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 17 (split)
         ┃  │   k: #gas [ SMOD , SMOD W0:Int W3:Int ] ~> SMOD W0:Int W3:Int ~> #pc [ SMOD ] ~> _K_C ...
         ┃  │   pc: _PC_CELL:Int
         ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┃ (branch)
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     _USEGAS_CELL:Bool
         ┃  ┃  │
         ┃  ┃  └─ 23 (leaf, pending)
         ┃  ┃      k: #gas [ SMOD , SMOD W0:Int W3:Int ] ~> SMOD W0:Int W3:Int ~> #pc [ SMOD ] ~> _K_C ...
         ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     └─ 24 (leaf, pending)
         ┃         k: #gas [ SMOD , SMOD W0:Int W3:Int ] ~> SMOD W0:Int W3:Int ~> #pc [ SMOD ] ~> _K_C ...
         ┃         pc: _PC_CELL:Int
         ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 18
            │   k: #exec [ SMOD ] ~> #pc [ SMOD ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  └─ 25 (leaf, pending)
            ┃      k: #gas [ SMOD , SMOD W0:Int W4:Int ] ~> SMOD W0:Int W4:Int ~> #pc [ SMOD ] ~> _K_C ...
            ┃      pc: _PC_CELL:Int
            ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               └─ 26 (leaf, pending)
                   k: #exec [ SMOD ] ~> #pc [ SMOD ] ~> _K_CELL:K
                   pc: _PC_CELL:Int
                   callDepth: _CALLDEPTH_CELL:Int
                   statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SMOD-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ SMOD ] ~> .K => #exec [ SMOD ]
             ~> #pc [ SMOD ] )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
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
      requires ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-6)]
    
    rule [BASIC-BLOCK-3-TO-7]: <kevm>
           <k>
             ( #next [ SMOD ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-3-TO-7)]
    
    rule [BASIC-BLOCK-4-TO-8]: <kevm>
           <k>
             ( #next [ SMOD ] => #halt )
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
    
    rule [BASIC-BLOCK-11-TO-19]: <kevm>
           <k>
             ( #gas [ SMOD , SMOD W0:Int W1:Int ] ~> .K => Glow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ SMOD , SMOD W0:Int W1:Int ] )
             ~> SMOD W0:Int W1:Int
             ~> #pc [ SMOD ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-11-TO-19)]
    
    rule [BASIC-BLOCK-15-TO-27]: <kevm>
           <k>
             ( #gas [ SMOD , SMOD W0:Int W2:Int ] ~> .K => Glow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ SMOD , SMOD W0:Int W2:Int ] )
             ~> SMOD W0:Int W2:Int
             ~> #pc [ SMOD ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int -1 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
               )))))
      [priority(20), label(BASIC-BLOCK-15-TO-27)]

endmodule
