
┌─ 1 (root, split, init)
│   k: #next [ REVERT ] ~> _K_CELL:K
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
┃  │   k: #next [ REVERT ] ~> _K_CELL:K
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
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ REVERT ] ~> _K_CELL:K
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
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024 )
   │
   ├─ 5
   │   k: #next [ REVERT ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 6
   │   k: #exec [ REVERT ] ~> #pc [ REVERT ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9 (split)
   ┃  │   k: #gas [ REVERT , REVERT W0:Int W1:Int ] ~> REVERT W0:Int W1:Int ~> #pc [ REVERT ] ...
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
   ┃  ┃  │   k: #gas [ REVERT , REVERT W0:Int W1:Int ] ~> REVERT W0:Int W1:Int ~> #pc [ REVERT ] ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 17
   ┃  ┃  │   k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 20
   ┃  ┃  ┃  │   k: #gas [ REVERT W0:Int W1:Int ] ~> #access [ REVERT , REVERT W0:Int W1:Int ] ~> RE ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  │  (2 steps)
   ┃  ┃  ┃  ├─ 28
   ┃  ┃  ┃  │   k: Gzero < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ REVERT , REVERT W0: ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃ (1 step)
   ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  └─ 33 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #access [ REVERT , REVERT W0:Int W1:Int ] ~> REVERT W0:Int W1:Int ~> #pc [ REVER ...
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  └─ 34 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ REVERT , REVERT W0:Int W1:Int ] ~> REVERT W0:I ...
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┗━━┓
   ┃  ┃  ┃     │
   ┃  ┃  ┃     └─ 35 (leaf, pending)
   ┃  ┃  ┃         k: Gzero < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ REVERT , REVERT W0: ...
   ┃  ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 21 (leaf, pending)
   ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #gas [ REVERT W0:Int W1:Int ] ~> #access [ REVERT , REVE ...
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 22 (stuck, leaf)
   ┃  ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     ├─ 12
   ┃     │   k: #gas [ REVERT , REVERT W0:Int W1:Int ] ~> REVERT W0:Int W1:Int ~> #pc [ REVERT ] ...
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     │
   ┃     │  (4 steps)
   ┃     └─ 23 (leaf, terminal)
   ┃         k: #halt ~> _K_CELL:K
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: EVMC_REVERT
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #exec [ REVERT ] ~> #pc [ REVERT ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13 (split)
      ┃  │   k: #gas [ REVERT , REVERT W0:Int W2:Int ] ~> REVERT W0:Int W2:Int ~> #pc [ REVERT ] ...
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
      ┃  ┃  │   k: #gas [ REVERT , REVERT W0:Int W2:Int ] ~> REVERT W0:Int W2:Int ~> #pc [ REVERT ] ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (4 steps)
      ┃  ┃  ├─ 29
      ┃  ┃  │   k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  └─ 30 (leaf, pending)
      ┃  ┃  ┃      k: #gas [ REVERT W0:Int W2:Int ] ~> #access [ REVERT , REVERT W0:Int W2:Int ] ~> RE ...
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  └─ 31 (leaf, pending)
      ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #gas [ REVERT W0:Int W2:Int ] ~> #access [ REVERT , REVE ...
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 32 (leaf, pending)
      ┃  ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
      ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     └─ 16 (leaf, pending)
      ┃         k: #gas [ REVERT , REVERT W0:Int W2:Int ] ~> REVERT W0:Int W2:Int ~> #pc [ REVERT ] ...
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 14
         │   k: #exec [ REVERT ] ~> #pc [ REVERT ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 18 (split)
         ┃  │   k: #gas [ REVERT , REVERT W0:Int W3:Int ] ~> REVERT W0:Int W3:Int ~> #pc [ REVERT ] ...
         ┃  │   pc: _PC_CELL:Int
         ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┃ (branch)
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     _USEGAS_CELL:Bool
         ┃  ┃  │
         ┃  ┃  └─ 24 (leaf, pending)
         ┃  ┃      k: #gas [ REVERT , REVERT W0:Int W3:Int ] ~> REVERT W0:Int W3:Int ~> #pc [ REVERT ] ...
         ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     └─ 25 (leaf, pending)
         ┃         k: #gas [ REVERT , REVERT W0:Int W3:Int ] ~> REVERT W0:Int W3:Int ~> #pc [ REVERT ] ...
         ┃         pc: _PC_CELL:Int
         ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 19
            │   k: #exec [ REVERT ] ~> #pc [ REVERT ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  └─ 26 (leaf, pending)
            ┃      k: #gas [ REVERT , REVERT W0:Int W4:Int ] ~> REVERT W0:Int W4:Int ~> #pc [ REVERT ] ...
            ┃      pc: _PC_CELL:Int
            ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               └─ 27 (leaf, pending)
                   k: #exec [ REVERT ] ~> #pc [ REVERT ] ~> _K_CELL:K
                   pc: _PC_CELL:Int
                   callDepth: _CALLDEPTH_CELL:Int
                   statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-REVERT-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ REVERT ] ~> .K => #exec [ REVERT ]
             ~> #pc [ REVERT ] )
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
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024 )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-6)]
    
    rule [BASIC-BLOCK-3-TO-7]: <kevm>
           <k>
             ( #next [ REVERT ] => #halt )
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
             ( #next [ REVERT ] => #halt )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-8)]
    
    rule [BASIC-BLOCK-11-TO-17]: <kevm>
           <k>
             ( #gas [ REVERT , REVERT W0:Int W1:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ REVERT W0:Int W1:Int ]
             ~> #access [ REVERT , REVERT W0:Int W1:Int ] )
             ~> REVERT W0:Int W1:Int
             ~> #pc [ REVERT ]
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
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) )
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -2 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-11-TO-17)]
    
    rule [BASIC-BLOCK-12-TO-23]: <kevm>
           <k>
             ( #gas [ REVERT , REVERT W0:Int W1:Int ]
             ~> REVERT W0:Int W1:Int
             ~> #pc [ REVERT ] => #halt ~> .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <output>
                 ( __OUTPUT_CELL => #range ( _LOCALMEM_CELL:Bytes , W0:Int , W1:Int ) )
               </output>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_REVERT )
               </statusCode>
               <callState>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -2 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-12-TO-23)]
    
    rule [BASIC-BLOCK-20-TO-28]: <kevm>
           <k>
             ( #gas [ REVERT W0:Int W1:Int ] ~> .K => Gzero < _SCHEDULE_CELL:Schedule >
             ~> #deductGas )
             ~> #access [ REVERT , REVERT W0:Int W1:Int ]
             ~> REVERT W0:Int W1:Int
             ~> #pc [ REVERT ]
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
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int )
                 </memoryUsed>
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
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -2 ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               )))))
      [priority(20), label(BASIC-BLOCK-20-TO-28)]
    
    rule [BASIC-BLOCK-15-TO-29]: <kevm>
           <k>
             ( #gas [ REVERT , REVERT W0:Int W2:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ REVERT W0:Int W2:Int ]
             ~> #access [ REVERT , REVERT W0:Int W2:Int ] )
             ~> REVERT W0:Int W2:Int
             ~> #pc [ REVERT ]
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
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) )
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
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int -2 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
               )))))
      [priority(20), label(BASIC-BLOCK-15-TO-29)]

endmodule
