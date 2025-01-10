
┌─ 1 (root, split, init)
│   k: #next [ SELFBALANCE ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0
┃  │
┃  ├─ 3
┃  │   k: #next [ SELFBALANCE ] ~> _K_CELL:K
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
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ SELFBALANCE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 10 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0 )
┃  ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
┃  │
┃  ├─ 36
┃  │   k: #next [ SELFBALANCE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 14
┃  │   k: Glow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ SELFBALANCE , SELFBA ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 15
┃  ┃  │   k: #access [ SELFBALANCE , SELFBALANCE ] ~> SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _ ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (1 step)
┃  ┃  ├─ 20
┃  ┃  │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (1 step)
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  └─ 21 (leaf, pending)
┃  ┃  ┃      k: BAL:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓
┃  ┃     │
┃  ┃     ├─ 22
┃  ┃     │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┃ (1 step)
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  └─ 26 (leaf, pending)
┃  ┃     ┃      k: BAL0:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┗━━┓
┃  ┃        │
┃  ┃        ├─ 27
┃  ┃        │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃        │   pc: _PC_CELL:Int
┃  ┃        │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┃ (1 step)
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  └─ 30 (leaf, pending)
┃  ┃        ┃      k: BAL1:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃        ┃      pc: _PC_CELL:Int
┃  ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┗━━┓
┃  ┃           │
┃  ┃           ├─ 31
┃  ┃           │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃           │   pc: _PC_CELL:Int
┃  ┃           │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┃ (1 step)
┃  ┃           ┣━━┓
┃  ┃           ┃  │
┃  ┃           ┃  └─ 34 (leaf, pending)
┃  ┃           ┃      k: BAL2:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃           ┃      pc: _PC_CELL:Int
┃  ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┗━━┓
┃  ┃              │
┃  ┃              └─ 35 (leaf, pending)
┃  ┃                  k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃                  pc: _PC_CELL:Int
┃  ┃                  callDepth: _CALLDEPTH_CELL:Int
┃  ┃                  statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 16
┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ SELFBALANCE , SELFBALANCE ] ~> SELFBALANCE ~>  ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (4 steps)
┃  ┃  └─ 25 (leaf, terminal)
┃  ┃      k: #halt ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: EVMC_OUT_OF_GAS
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 17 (stuck, leaf)
┃         k: Glow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ SELFBALANCE , SELFBA ...
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0 )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
   │
   ├─ 37
   │   k: #next [ SELFBALANCE ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (4 steps)
   ├─ 11
   │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  └─ 12 (leaf, pending)
   ┃      k: BAL:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
   ┃      pc: _PC_CELL:Int
   ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 13
      │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  └─ 18 (leaf, pending)
      ┃      k: BAL0:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
      ┃      pc: _PC_CELL:Int
      ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 19
         │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  └─ 23 (leaf, pending)
         ┃      k: BAL1:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
         ┃      pc: _PC_CELL:Int
         ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 24
            │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  └─ 28 (leaf, pending)
            ┃      k: BAL2:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
            ┃      pc: _PC_CELL:Int
            ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               ├─ 29
               │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
               │   pc: _PC_CELL:Int
               │   callDepth: _CALLDEPTH_CELL:Int
               │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┃ (1 step)
               ┣━━┓
               ┃  │
               ┃  └─ 32 (leaf, pending)
               ┃      k: BAL3:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
               ┃      pc: _PC_CELL:Int
               ┃      callDepth: _CALLDEPTH_CELL:Int
               ┃      statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┗━━┓
                  │
                  └─ 33 (leaf, pending)
                      k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
                      pc: _PC_CELL:Int
                      callDepth: _CALLDEPTH_CELL:Int
                      statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SELFBALANCE-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-7]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] => #halt )
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
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0
      [priority(20), label(BASIC-BLOCK-3-TO-7)]
    
    rule [BASIC-BLOCK-4-TO-10]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] => #halt )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-10)]
    
    rule [BASIC-BLOCK-15-TO-20]: <kevm>
           <k>
             ( #access [ SELFBALANCE , SELFBALANCE ] ~> .K => .K )
             ~> SELFBALANCE
             ~> #pc [ SELFBALANCE ]
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
                   _WORDSTACK_CELL:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas Glow < _SCHEDULE_CELL:Schedule >
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0 )
       andBool ( Glow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-15-TO-20)]
    
    rule [BASIC-BLOCK-16-TO-25]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ SELFBALANCE , SELFBALANCE ]
             ~> SELFBALANCE
             ~> #pc [ SELFBALANCE ] => #halt ~> .K )
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
                   _WORDSTACK_CELL:WordStack
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0 )
       andBool ( _GAS_CELL:Gas <Gas Glow < _SCHEDULE_CELL:Schedule >
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-16-TO-25)]
    
    rule [BASIC-BLOCK-36-TO-14]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] ~> .K => Glow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ SELFBALANCE , SELFBALANCE ]
             ~> SELFBALANCE
             ~> #pc [ SELFBALANCE ] )
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
      requires ( _USEGAS_CELL:Bool
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-36-TO-14)]
    
    rule [BASIC-BLOCK-37-TO-11]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] ~> .K => SELFBALANCE
             ~> #pc [ SELFBALANCE ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
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
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-37-TO-11)]

endmodule
