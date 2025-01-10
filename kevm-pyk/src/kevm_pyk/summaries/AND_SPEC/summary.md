
┌─ 1 (root, split, init)
│   k: #next [ AND ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( WS:WordStack , 0 ) <=Int 1023
┃  ┃     _WORDSTACK_CELL:WordStack ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
┃  ┃     #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi
┃  │
┃  └─ 3 (leaf, pending)
┃      k: #next [ AND ] ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2
┃  │
┃  ├─ 4
┃  │   k: #next [ AND ] ~> _K_CELL:K
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
┃  ├─ 5
┃  │   k: #next [ AND ] ~> _K_CELL:K
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
   ├─ 6
   │   k: #next [ AND ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 7
   │   k: #exec [ AND ] ~> #pc [ AND ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 10 (split)
   ┃  │   k: #gas [ AND , AND W0:Int W1:Int ] ~> AND W0:Int W1:Int ~> #pc [ AND ] ~> _K_CELL: ...
   ┃  │   pc: _PC_CELL:Int
   ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┃ (branch)
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     _USEGAS_CELL:Bool
   ┃  ┃  │
   ┃  ┃  ├─ 12
   ┃  ┃  │   k: #gas [ AND , AND W0:Int W1:Int ] ~> AND W0:Int W1:Int ~> #pc [ AND ] ~> _K_CELL: ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 20
   ┃  ┃  │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ AND , AND W0:Int ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 21 (leaf, pending)
   ┃  ┃  ┃      k: #access [ AND , AND W0:Int W1:Int ] ~> AND W0:Int W1:Int ~> #pc [ AND ] ~> _K_CE ...
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 22
   ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ AND , AND W0:Int W1:Int ] ~> AND W0:Int W1:Int ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  │  (4 steps)
   ┃  ┃  ┃  └─ 29 (leaf, terminal)
   ┃  ┃  ┃      k: #halt ~> _K_CELL:K
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 23 (stuck, leaf)
   ┃  ┃         k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ AND , AND W0:Int ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     └─ 13 (leaf, pending)
   ┃         k: #gas [ AND , AND W0:Int W1:Int ] ~> AND W0:Int W1:Int ~> #pc [ AND ] ~> _K_CELL: ...
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 11
      │   k: #exec [ AND ] ~> #pc [ AND ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 14 (split)
      ┃  │   k: #gas [ AND , AND W0:Int W2:Int ] ~> AND W0:Int W2:Int ~> #pc [ AND ] ~> _K_CELL: ...
      ┃  │   pc: _PC_CELL:Int
      ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┃ (branch)
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     _USEGAS_CELL:Bool
      ┃  ┃  │
      ┃  ┃  ├─ 16
      ┃  ┃  │   k: #gas [ AND , AND W0:Int W2:Int ] ~> AND W0:Int W2:Int ~> #pc [ AND ] ~> _K_CELL: ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (4 steps)
      ┃  ┃  ├─ 28
      ┃  ┃  │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ AND , AND W0:Int ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  └─ 33 (leaf, pending)
      ┃  ┃  ┃      k: #access [ AND , AND W0:Int W2:Int ] ~> AND W0:Int W2:Int ~> #pc [ AND ] ~> _K_CE ...
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  └─ 34 (leaf, pending)
      ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ AND , AND W0:Int W2:Int ] ~> AND W0:Int W2:Int ...
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 35 (leaf, pending)
      ┃  ┃         k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ AND , AND W0:Int ...
      ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     └─ 17 (leaf, pending)
      ┃         k: #gas [ AND , AND W0:Int W2:Int ] ~> AND W0:Int W2:Int ~> #pc [ AND ] ~> _K_CELL: ...
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 15
         │   k: #exec [ AND ] ~> #pc [ AND ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 18 (split)
         ┃  │   k: #gas [ AND , AND W0:Int W3:Int ] ~> AND W0:Int W3:Int ~> #pc [ AND ] ~> _K_CELL: ...
         ┃  │   pc: _PC_CELL:Int
         ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┃ (branch)
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     _USEGAS_CELL:Bool
         ┃  ┃  │
         ┃  ┃  ├─ 24
         ┃  ┃  │   k: #gas [ AND , AND W0:Int W3:Int ] ~> AND W0:Int W3:Int ~> #pc [ AND ] ~> _K_CELL: ...
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  │
         ┃  ┃  │  (4 steps)
         ┃  ┃  ├─ 30
         ┃  ┃  │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ AND , AND W0:Int ...
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┃ (1 step)
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 36 (leaf, pending)
         ┃  ┃  ┃      k: #access [ AND , AND W0:Int W3:Int ] ~> AND W0:Int W3:Int ~> #pc [ AND ] ~> _K_CE ...
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 37 (leaf, pending)
         ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ AND , AND W0:Int W3:Int ] ~> AND W0:Int W3:Int ...
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┗━━┓
         ┃  ┃     │
         ┃  ┃     └─ 38 (leaf, pending)
         ┃  ┃         k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ AND , AND W0:Int ...
         ┃  ┃         pc: _PC_CELL:Int
         ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     └─ 25 (leaf, pending)
         ┃         k: #gas [ AND , AND W0:Int W3:Int ] ~> AND W0:Int W3:Int ~> #pc [ AND ] ~> _K_CELL: ...
         ┃         pc: _PC_CELL:Int
         ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 19
            │   k: #exec [ AND ] ~> #pc [ AND ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  ├─ 26 (split)
            ┃  │   k: #gas [ AND , AND W0:Int W4:Int ] ~> AND W0:Int W4:Int ~> #pc [ AND ] ~> _K_CELL: ...
            ┃  │   pc: _PC_CELL:Int
            ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┃ (branch)
            ┃  ┣━━┓ subst: .Subst
            ┃  ┃  ┃ constraint:
            ┃  ┃  ┃     _USEGAS_CELL:Bool
            ┃  ┃  │
            ┃  ┃  └─ 31 (leaf, pending)
            ┃  ┃      k: #gas [ AND , AND W0:Int W4:Int ] ~> AND W0:Int W4:Int ~> #pc [ AND ] ~> _K_CELL: ...
            ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┗━━┓ subst: .Subst
            ┃     ┃ constraint:
            ┃     ┃     ( notBool _USEGAS_CELL:Bool )
            ┃     │
            ┃     └─ 32 (leaf, pending)
            ┃         k: #gas [ AND , AND W0:Int W4:Int ] ~> AND W0:Int W4:Int ~> #pc [ AND ] ~> _K_CELL: ...
            ┃         pc: _PC_CELL:Int
            ┃         callDepth: _CALLDEPTH_CELL:Int
            ┃         statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               └─ 27 (leaf, pending)
                   k: #exec [ AND ] ~> #pc [ AND ] ~> _K_CELL:K
                   pc: _PC_CELL:Int
                   callDepth: _CALLDEPTH_CELL:Int
                   statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-AND-SPEC
    
    
    rule [BASIC-BLOCK-6-TO-7]: <kevm>
           <k>
             ( #next [ AND ] ~> .K => #exec [ AND ]
             ~> #pc [ AND ] )
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
      [priority(20), label(BASIC-BLOCK-6-TO-7)]
    
    rule [BASIC-BLOCK-5-TO-8]: <kevm>
           <k>
             ( #next [ AND ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-5-TO-8)]
    
    rule [BASIC-BLOCK-4-TO-9]: <kevm>
           <k>
             ( #next [ AND ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-4-TO-9)]
    
    rule [BASIC-BLOCK-12-TO-20]: <kevm>
           <k>
             ( #gas [ AND , AND W0:Int W1:Int ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ AND , AND W0:Int W1:Int ] )
             ~> AND W0:Int W1:Int
             ~> #pc [ AND ]
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
      [priority(20), label(BASIC-BLOCK-12-TO-20)]
    
    rule [BASIC-BLOCK-16-TO-28]: <kevm>
           <k>
             ( #gas [ AND , AND W0:Int W2:Int ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ AND , AND W0:Int W2:Int ] )
             ~> AND W0:Int W2:Int
             ~> #pc [ AND ]
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
      [priority(20), label(BASIC-BLOCK-16-TO-28)]
    
    rule [BASIC-BLOCK-22-TO-29]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ AND , AND W0:Int W1:Int ]
             ~> AND W0:Int W1:Int
             ~> #pc [ AND ] => #halt ~> .K )
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
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_OUT_OF_GAS )
               </statusCode>
               <callState>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-22-TO-29)]
    
    rule [BASIC-BLOCK-24-TO-30]: <kevm>
           <k>
             ( #gas [ AND , AND W0:Int W3:Int ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ AND , AND W0:Int W3:Int ] )
             ~> AND W0:Int W3:Int
             ~> #pc [ AND ]
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
                   WS1:WordStack
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
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W3:Int : WS1:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS1:WordStack , 2 ) +Int -1 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W3:Int andBool _WS ==K WS1:WordStack ) )
       andBool ( ( notBool ( _W2 ==Int W3:Int andBool _WS0 ==K WS1:WordStack ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-24-TO-30)]

endmodule
