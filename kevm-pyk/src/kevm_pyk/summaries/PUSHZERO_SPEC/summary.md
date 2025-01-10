
┌─ 1 (root, split, init)
│   k: #next [ PUSHZERO ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023
┃  ┃     #if _USEGAS_CELL:Bool #then Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi
┃  │
┃  └─ 3 (leaf, pending)
┃      k: #next [ PUSHZERO ] ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0
┃  │
┃  ├─ 4
┃  │   k: #next [ PUSHZERO ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 7
┃  ┃  │   k: _K_CELL:K
┃  ┃  │   pc: ( _PC_CELL:Int +Int 1 )
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  ┊  constraint: true
┃  ┃  ┊  subst: ...
┃  ┃  └─ 2 (leaf, target)
┃  ┃      k: _K_CELL:K
┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 8
┃     │   k: #end EVMC_STACK_UNDERFLOW ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     │
┃     │  (1 step)
┃     └─ 15 (leaf, terminal)
┃         k: #halt ~> _K_CELL:K
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: EVMC_STACK_UNDERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024
┃  │
┃  ├─ 5
┃  │   k: #next [ PUSHZERO ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 11 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0 )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
   │
   ├─ 6
   │   k: #next [ PUSHZERO ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9
   ┃  │   k: _K_CELL:K
   ┃  │   pc: ( _PC_CELL:Int +Int 1 )
   ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  │
   ┃  ┊  constraint: true
   ┃  ┊  subst: ...
   ┃  └─ 2 (leaf, target)
   ┃      k: _K_CELL:K
   ┃      pc: ?_FINAL_PC_CELL:Int
   ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
   ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #addr [ PUSHZERO ] ~> #exec [ PUSHZERO ] ~> #pc [ PUSHZERO ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      │
      │  (6 steps)
      ├─ 12
      │   k: Gbase < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ PUSHZERO , PUSHZERO ...
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  └─ 13 (leaf, pending)
      ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ PUSHZERO , PUSHZERO ] ~> PUSHZERO ~> #pc [ PUS ...
      ┃      pc: _PC_CELL:Int
      ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         └─ 14 (stuck, leaf)
             k: Gbase < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ PUSHZERO , PUSHZERO ...
             pc: _PC_CELL:Int
             callDepth: _CALLDEPTH_CELL:Int
             statusCode: _STATUSCODE_CELL:StatusCode




module SUMMARY-PUSHZERO-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-11]: <kevm>
           <k>
             ( #next [ PUSHZERO ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-5-TO-11)]
    
    rule [BASIC-BLOCK-10-TO-12]: <kevm>
           <k>
             ( #addr [ PUSHZERO ]
             ~> #exec [ PUSHZERO ] => Gbase < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ PUSHZERO , PUSHZERO ]
             ~> PUSHZERO )
             ~> #pc [ PUSHZERO ]
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
      requires ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool #if _USEGAS_CELL:Bool #then Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) )
               )))
       ensures ( _USEGAS_CELL:Bool
       andBool ( ( notBool ( Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas andBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 ) )
               ))
      [priority(20), label(BASIC-BLOCK-10-TO-12)]
    
    rule [BASIC-BLOCK-8-TO-15]: <kevm>
           <k>
             ( #end EVMC_STACK_UNDERFLOW => #halt )
             ~> __K_CELL
           </k>
           <schedule>
             _SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STACK_UNDERFLOW )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool #if _USEGAS_CELL:Bool #then Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) )
               ))
      [priority(20), label(BASIC-BLOCK-8-TO-15)]

endmodule
