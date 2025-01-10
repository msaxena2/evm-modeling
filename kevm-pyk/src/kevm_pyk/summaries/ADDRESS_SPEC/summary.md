
┌─ 1 (root, split, init)
│   k: #next [ ADDRESS ] ~> _K_CELL:K
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
┃  │   k: #next [ ADDRESS ] ~> _K_CELL:K
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
┃  │   k: #next [ ADDRESS ] ~> _K_CELL:K
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
┃  ├─ 22
┃  │   k: #next [ ADDRESS ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 14
┃  │   k: Gbase < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ ADDRESS , ADDRESS ] ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 15
┃  ┃  │   k: #access [ ADDRESS , ADDRESS ] ~> ADDRESS ~> #pc [ ADDRESS ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (2 steps)
┃  ┃  ├─ 18
┃  ┃  │   k: _ID_CELL:Account ~> #push ~> #pc [ ADDRESS ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (1 step)
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  └─ 19 (leaf, pending)
┃  ┃  ┃      k: #pc [ ADDRESS ] ~> _K_CELL:K
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓
┃  ┃     │
┃  ┃     └─ 20 (stuck, leaf)
┃  ┃         k: _ID_CELL:Account ~> #push ~> #pc [ ADDRESS ] ~> _K_CELL:K
┃  ┃         pc: _PC_CELL:Int
┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 16
┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ ADDRESS , ADDRESS ] ~> ADDRESS ~> #pc [ ADDRES ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (4 steps)
┃  ┃  └─ 21 (leaf, terminal)
┃  ┃      k: #halt ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: EVMC_OUT_OF_GAS
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 17 (stuck, leaf)
┃         k: Gbase < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ ADDRESS , ADDRESS ] ...
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
   ├─ 23
   │   k: #next [ ADDRESS ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (5 steps)
   ├─ 11
   │   k: _ID_CELL:Account ~> #push ~> #pc [ ADDRESS ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  └─ 12 (leaf, pending)
   ┃      k: #pc [ ADDRESS ] ~> _K_CELL:K
   ┃      pc: _PC_CELL:Int
   ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      └─ 13 (stuck, leaf)
          k: _ID_CELL:Account ~> #push ~> #pc [ ADDRESS ] ~> _K_CELL:K
          pc: _PC_CELL:Int
          callDepth: _CALLDEPTH_CELL:Int
          statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-ADDRESS-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-7]: <kevm>
           <k>
             ( #next [ ADDRESS ] => #halt )
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
             ( #next [ ADDRESS ] => #halt )
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
    
    rule [BASIC-BLOCK-15-TO-18]: <kevm>
           <k>
             ( #access [ ADDRESS , ADDRESS ]
             ~> ADDRESS => _ID_CELL:Account
             ~> #push )
             ~> #pc [ ADDRESS ]
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
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   _WORDSTACK_CELL:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas Gbase < _SCHEDULE_CELL:Schedule >
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
       andBool ( Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-15-TO-18)]
    
    rule [BASIC-BLOCK-16-TO-21]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ ADDRESS , ADDRESS ]
             ~> ADDRESS
             ~> #pc [ ADDRESS ] => #halt ~> .K )
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
       andBool ( _GAS_CELL:Gas <Gas Gbase < _SCHEDULE_CELL:Schedule >
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-16-TO-21)]
    
    rule [BASIC-BLOCK-22-TO-14]: <kevm>
           <k>
             ( #next [ ADDRESS ] ~> .K => Gbase < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ ADDRESS , ADDRESS ]
             ~> ADDRESS
             ~> #pc [ ADDRESS ] )
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
      [priority(20), label(BASIC-BLOCK-22-TO-14)]
    
    rule [BASIC-BLOCK-23-TO-11]: <kevm>
           <k>
             ( #next [ ADDRESS ] ~> .K => _ID_CELL:Account
             ~> #push
             ~> #pc [ ADDRESS ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   _ID_CELL:Account
                 </id>
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
      [priority(20), label(BASIC-BLOCK-23-TO-11)]

endmodule
