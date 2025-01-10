
┌─ 1 (root, split, init)
│   k: #next [ JUMPI ] ~> _K_CELL:K
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
┃  │   k: #next [ JUMPI ] ~> _K_CELL:K
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
┃  │   k: #next [ JUMPI ] ~> _K_CELL:K
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
   │   k: #next [ JUMPI ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 6
   │   k: #exec [ JUMPI ] ~> #pc [ JUMPI ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9 (split)
   ┃  │   k: #gas [ JUMPI , JUMPI W0:Int W1:Int ] ~> JUMPI W0:Int W1:Int ~> #pc [ JUMPI ] ~>  ...
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
   ┃  ┃  │   k: #gas [ JUMPI , JUMPI W0:Int W1:Int ] ~> JUMPI W0:Int W1:Int ~> #pc [ JUMPI ] ~>  ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 22
   ┃  ┃  │   k: Ghigh < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ JUMPI , JUMPI W0:In ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 23 (leaf, pending)
   ┃  ┃  ┃      k: #access [ JUMPI , JUMPI W0:Int W1:Int ] ~> JUMPI W0:Int W1:Int ~> #pc [ JUMPI ]  ...
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 24 (leaf, pending)
   ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ JUMPI , JUMPI W0:Int W1:Int ] ~> JUMPI W0:Int  ...
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 25 (leaf, pending)
   ┃  ┃         k: Ghigh < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ JUMPI , JUMPI W0:In ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
   ┃  ┃  ┃     ( notBool W1:Int ==Int 0 )
   ┃  ┃  │
   ┃  ┃  ├─ 26
   ┃  ┃  │   k: #gas [ JUMPI , JUMPI W0:Int W1:Int ] ~> JUMPI W0:Int W1:Int ~> #pc [ JUMPI ] ~>  ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (1 step)
   ┃  ┃  └─ 20 (leaf, pending)
   ┃  ┃      k: JUMPI W0:Int W1:Int ~> #pc [ JUMPI ] ~> _K_CELL:K
   ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     W1:Int ==Int 0
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     ┃     _WORDSTACK_CELL:WordStack ==K ( W0:Int : ( 0 : WS:WordStack ) )
   ┃     │
   ┃     ├─ 27
   ┃     │   k: #gas [ JUMPI , JUMPI W0:Int W1:Int ] ~> JUMPI W0:Int W1:Int ~> #pc [ JUMPI ] ~>  ...
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     │
   ┃     │  (1 step)
   ┃     └─ 21 (leaf, pending)
   ┃         k: JUMPI W0:Int W1:Int ~> #pc [ JUMPI ] ~> _K_CELL:K
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #exec [ JUMPI ] ~> #pc [ JUMPI ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13 (split)
      ┃  │   k: #gas [ JUMPI , JUMPI W0:Int W2:Int ] ~> JUMPI W0:Int W2:Int ~> #pc [ JUMPI ] ~>  ...
      ┃  │   pc: _PC_CELL:Int
      ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┃ (branch)
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     _USEGAS_CELL:Bool
      ┃  ┃  │
      ┃  ┃  └─ 15 (leaf, pending)
      ┃  ┃      k: #gas [ JUMPI , JUMPI W0:Int W2:Int ] ~> JUMPI W0:Int W2:Int ~> #pc [ JUMPI ] ~>  ...
      ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     └─ 16 (leaf, pending)
      ┃         k: #gas [ JUMPI , JUMPI W0:Int W2:Int ] ~> JUMPI W0:Int W2:Int ~> #pc [ JUMPI ] ~>  ...
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 14
         │   k: #exec [ JUMPI ] ~> #pc [ JUMPI ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  └─ 18 (leaf, pending)
         ┃      k: #gas [ JUMPI , JUMPI W0:Int W3:Int ] ~> JUMPI W0:Int W3:Int ~> #pc [ JUMPI ] ~>  ...
         ┃      pc: _PC_CELL:Int
         ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            └─ 19 (leaf, pending)
                k: #exec [ JUMPI ] ~> #pc [ JUMPI ] ~> _K_CELL:K
                pc: _PC_CELL:Int
                callDepth: _CALLDEPTH_CELL:Int
                statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-JUMPI-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ JUMPI ] ~> .K => #exec [ JUMPI ]
             ~> #pc [ JUMPI ] )
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
             ( #next [ JUMPI ] => #halt )
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
             ( #next [ JUMPI ] => #halt )
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
    
    rule [BASIC-BLOCK-11-TO-22]: <kevm>
           <k>
             ( #gas [ JUMPI , JUMPI W0:Int W1:Int ] ~> .K => Ghigh < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ JUMPI , JUMPI W0:Int W1:Int ] )
             ~> JUMPI W0:Int W1:Int
             ~> #pc [ JUMPI ]
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
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -2 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-11-TO-22)]
    
    rule [BASIC-BLOCK-26-TO-20]: <kevm>
           <k>
             ( #gas [ JUMPI , JUMPI W0:Int W1:Int ] ~> .K => .K )
             ~> JUMPI W0:Int W1:Int
             ~> #pc [ JUMPI ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( W1:Int =/=Int 0
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -2 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-26-TO-20)]
    
    rule [BASIC-BLOCK-27-TO-21]: <kevm>
           <k>
             ( #gas [ JUMPI , JUMPI W0:Int W1:Int ] ~> .K => .K )
             ~> JUMPI W0:Int W1:Int
             ~> #pc [ JUMPI ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( W1:Int ==Int 0
       andBool ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( _WORDSTACK_CELL:WordStack ==K ( W0:Int : ( 0 : WS:WordStack ) )
       andBool ( _WORDSTACK_CELL:WordStack ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -2 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-27-TO-21)]

endmodule
