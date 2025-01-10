
┌─ 1 (root, split, init)
│   k: #next [ EXP ] ~> _K_CELL:K
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
┃  │   k: #next [ EXP ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 8 (leaf, terminal)
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
┃  │   k: #next [ EXP ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 7 (leaf, terminal)
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
   │   k: #next [ EXP ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 6
   │   k: #exec [ EXP ] ~> #pc [ EXP ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9 (split)
   ┃  │   k: #gas [ EXP , EXP W0:Int W1:Int ] ~> EXP W0:Int W1:Int ~> #pc [ EXP ] ~> _K_CELL: ...
   ┃  │   pc: _PC_CELL:Int
   ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┃ (branch)
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
   ┃  ┃  │
   ┃  ┃  └─ 12 (leaf, pending)
   ┃  ┃      k: #gas [ EXP , EXP W0:Int W1:Int ] ~> EXP W0:Int W1:Int ~> #pc [ EXP ] ~> _K_CELL: ...
   ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     _USEGAS_CELL:Bool
   ┃  ┃  ┃     W1:Int <=Int 0
   ┃  ┃  │
   ┃  ┃  ├─ 37
   ┃  ┃  │   k: #gas [ EXP , EXP W0:Int W1:Int ] ~> EXP W0:Int W1:Int ~> #pc [ EXP ] ~> _K_CELL: ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 27
   ┃  ┃  │   k: Gexp < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ EXP , EXP W0:Int W1: ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 31 (leaf, pending)
   ┃  ┃  ┃      k: #access [ EXP , EXP W0:Int W1:Int ] ~> EXP W0:Int W1:Int ~> #pc [ EXP ] ~> _K_CE ...
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 32 (leaf, pending)
   ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ EXP , EXP W0:Int W1:Int ] ~> EXP W0:Int W1:Int ...
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 33 (leaf, pending)
   ┃  ┃         k: Gexp < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ EXP , EXP W0:Int W1: ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     _USEGAS_CELL:Bool
   ┃     ┃     0 <Int W1:Int
   ┃     │
   ┃     ├─ 38
   ┃     │   k: #gas [ EXP , EXP W0:Int W1:Int ] ~> EXP W0:Int W1:Int ~> #pc [ EXP ] ~> _K_CELL: ...
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     │
   ┃     │  (4 steps)
   ┃     ├─ 28
   ┃     │   k: ( Gexp < _SCHEDULE_CELL:Schedule > +Int ( Gexpbyte < _SCHEDULE_CELL:Schedule > * ...
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     ┃
   ┃     ┃ (1 step)
   ┃     ┣━━┓
   ┃     ┃  │
   ┃     ┃  └─ 34 (leaf, pending)
   ┃     ┃      k: #access [ EXP , EXP W0:Int W1:Int ] ~> EXP W0:Int W1:Int ~> #pc [ EXP ] ~> _K_CE ...
   ┃     ┃      pc: _PC_CELL:Int
   ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃     ┃
   ┃     ┣━━┓
   ┃     ┃  │
   ┃     ┃  └─ 35 (leaf, pending)
   ┃     ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ EXP , EXP W0:Int W1:Int ] ~> EXP W0:Int W1:Int ...
   ┃     ┃      pc: _PC_CELL:Int
   ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃     ┃
   ┃     ┗━━┓
   ┃        │
   ┃        └─ 36 (leaf, pending)
   ┃            k: ( Gexp < _SCHEDULE_CELL:Schedule > +Int ( Gexpbyte < _SCHEDULE_CELL:Schedule > * ...
   ┃            pc: _PC_CELL:Int
   ┃            callDepth: _CALLDEPTH_CELL:Int
   ┃            statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #exec [ EXP ] ~> #pc [ EXP ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13 (split)
      ┃  │   k: #gas [ EXP , EXP W0:Int W2:Int ] ~> EXP W0:Int W2:Int ~> #pc [ EXP ] ~> _K_CELL: ...
      ┃  │   pc: _PC_CELL:Int
      ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┃ (branch)
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
      ┃  ┃  │
      ┃  ┃  └─ 16 (leaf, pending)
      ┃  ┃      k: #gas [ EXP , EXP W0:Int W2:Int ] ~> EXP W0:Int W2:Int ~> #pc [ EXP ] ~> _K_CELL: ...
      ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     _USEGAS_CELL:Bool
      ┃  ┃  ┃     W2:Int <=Int 0
      ┃  ┃  │
      ┃  ┃  ├─ 39
      ┃  ┃  │   k: #gas [ EXP , EXP W0:Int W2:Int ] ~> EXP W0:Int W2:Int ~> #pc [ EXP ] ~> _K_CELL: ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (3 steps)
      ┃  ┃  └─ 29 (leaf, pending)
      ┃  ┃      k: #gasExec ( _SCHEDULE_CELL:Schedule , EXP W0:Int W2:Int ) ~> #deductGas ~> #acces ...
      ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     _USEGAS_CELL:Bool
      ┃     ┃     0 <Int W2:Int
      ┃     │
      ┃     ├─ 40
      ┃     │   k: #gas [ EXP , EXP W0:Int W2:Int ] ~> EXP W0:Int W2:Int ~> #pc [ EXP ] ~> _K_CELL: ...
      ┃     │   pc: _PC_CELL:Int
      ┃     │   callDepth: _CALLDEPTH_CELL:Int
      ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃     │
      ┃     │  (3 steps)
      ┃     └─ 30 (leaf, pending)
      ┃         k: #gasExec ( _SCHEDULE_CELL:Schedule , EXP W0:Int W2:Int ) ~> #deductGas ~> #acces ...
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 14
         │   k: #exec [ EXP ] ~> #pc [ EXP ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 20 (split)
         ┃  │   k: #gas [ EXP , EXP W0:Int W3:Int ] ~> EXP W0:Int W3:Int ~> #pc [ EXP ] ~> _K_CELL: ...
         ┃  │   pc: _PC_CELL:Int
         ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┃ (branch)
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     _USEGAS_CELL:Bool
         ┃  ┃  │
         ┃  ┃  └─ 22 (leaf, pending)
         ┃  ┃      k: #gas [ EXP , EXP W0:Int W3:Int ] ~> EXP W0:Int W3:Int ~> #pc [ EXP ] ~> _K_CELL: ...
         ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     └─ 23 (leaf, pending)
         ┃         k: #gas [ EXP , EXP W0:Int W3:Int ] ~> EXP W0:Int W3:Int ~> #pc [ EXP ] ~> _K_CELL: ...
         ┃         pc: _PC_CELL:Int
         ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 21
            │   k: #exec [ EXP ] ~> #pc [ EXP ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  └─ 25 (leaf, pending)
            ┃      k: #gas [ EXP , EXP W0:Int W4:Int ] ~> EXP W0:Int W4:Int ~> #pc [ EXP ] ~> _K_CELL: ...
            ┃      pc: _PC_CELL:Int
            ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               └─ 26 (leaf, pending)
                   k: #exec [ EXP ] ~> #pc [ EXP ] ~> _K_CELL:K
                   pc: _PC_CELL:Int
                   callDepth: _CALLDEPTH_CELL:Int
                   statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-EXP-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ EXP ] ~> .K => #exec [ EXP ]
             ~> #pc [ EXP ] )
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
    
    rule [BASIC-BLOCK-4-TO-7]: <kevm>
           <k>
             ( #next [ EXP ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-4-TO-7)]
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ EXP ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-3-TO-8)]
    
    rule [BASIC-BLOCK-39-TO-29]: <kevm>
           <k>
             ( #gas [ EXP , EXP W0:Int W2:Int ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , EXP W0:Int W2:Int )
             ~> #deductGas
             ~> #access [ EXP , EXP W0:Int W2:Int ] )
             ~> EXP W0:Int W2:Int
             ~> #pc [ EXP ]
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
       andBool ( W2:Int <=Int 0
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int -1 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-39-TO-29)]
    
    rule [BASIC-BLOCK-40-TO-30]: <kevm>
           <k>
             ( #gas [ EXP , EXP W0:Int W2:Int ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , EXP W0:Int W2:Int )
             ~> #deductGas
             ~> #access [ EXP , EXP W0:Int W2:Int ] )
             ~> EXP W0:Int W2:Int
             ~> #pc [ EXP ]
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
       andBool ( 0 <Int W2:Int
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int -1 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-40-TO-30)]
    
    rule [BASIC-BLOCK-37-TO-27]: <kevm>
           <k>
             ( #gas [ EXP , EXP W0:Int W1:Int ] ~> .K => Gexp < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ EXP , EXP W0:Int W1:Int ] )
             ~> EXP W0:Int W1:Int
             ~> #pc [ EXP ]
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
       andBool ( W1:Int <=Int 0
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-37-TO-27)]
    
    rule [BASIC-BLOCK-38-TO-28]: <kevm>
           <k>
             ( #gas [ EXP , EXP W0:Int W1:Int ] ~> .K => ( Gexp < _SCHEDULE_CELL:Schedule > +Int ( Gexpbyte < _SCHEDULE_CELL:Schedule > *Int ( ( log2Int ( W1:Int ) /Int 8 ) +Int 1 ) ) )
             ~> #deductGas
             ~> #access [ EXP , EXP W0:Int W1:Int ] )
             ~> EXP W0:Int W1:Int
             ~> #pc [ EXP ]
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
       andBool ( 0 <Int W1:Int
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-38-TO-28)]

endmodule
