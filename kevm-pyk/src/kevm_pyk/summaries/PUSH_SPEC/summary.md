
┌─ 1 (root, split, init)
│   k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023
┃  ┃     #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi
┃  │
┃  └─ 3 (leaf, pending)
┃      k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 0
┃  │
┃  ├─ 4
┃  │   k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 7
┃  ┃  │   k: _K_CELL:K
┃  ┃  │   pc: ( ( _PC_CELL:Int +Int _N:Int ) +Int 1 )
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
┃  │   k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
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
   │   k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9
   ┃  │   k: _K_CELL:K
   ┃  │   pc: ( ( _PC_CELL:Int +Int _N:Int ) +Int 1 )
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
      │   k: #addr [ PUSH ( _N:Int ) ] ~> #exec [ PUSH ( _N:Int ) ] ~> #pc [ PUSH ( _N:Int )  ...
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      │
      │  (6 steps)
      ├─ 12
      │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ PUSH ( _N:Int )  ...
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13
      ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ PUSH ( _N:Int ) , PUSH ( _N:Int ) ] ~> PUSH (  ...
      ┃  │   pc: _PC_CELL:Int
      ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  │
      ┃  │  (4 steps)
      ┃  └─ 16 (leaf, terminal)
      ┃      k: #halt ~> _K_CELL:K
      ┃      pc: _PC_CELL:Int
      ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃      statusCode: EVMC_OUT_OF_GAS
      ┃
      ┗━━┓
         │
         └─ 14 (stuck, leaf)
             k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ PUSH ( _N:Int )  ...
             pc: _PC_CELL:Int
             callDepth: _CALLDEPTH_CELL:Int
             statusCode: _STATUSCODE_CELL:StatusCode




module SUMMARY-PUSH-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-11]: <kevm>
           <k>
             ( #next [ PUSH ( __N ) ] => #halt )
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
                 ( __STATUSCODE_CELL => EVMC_STACK_OVERFLOW )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024
       ensures ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) )
      [priority(20), label(BASIC-BLOCK-5-TO-11)]
    
    rule [BASIC-BLOCK-10-TO-12]: <kevm>
           <k>
             ( #addr [ PUSH ( _N:Int ) ]
             ~> #exec [ PUSH ( _N:Int ) ] => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ PUSH ( _N:Int ) , PUSH ( _N:Int ) ]
             ~> PUSH ( _N:Int ) )
             ~> #pc [ PUSH ( _N:Int ) ]
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
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) )
               )))
       ensures ( _USEGAS_CELL:Bool
       andBool ( ( notBool ( Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas andBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 ) )
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
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) )
               ))
      [priority(20), label(BASIC-BLOCK-8-TO-15)]
    
    rule [BASIC-BLOCK-13-TO-16]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ PUSH ( _N:Int ) , PUSH ( _N:Int ) ]
             ~> PUSH ( _N:Int )
             ~> #pc [ PUSH ( _N:Int ) ] => #halt ~> .K )
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
       andBool ( _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int 1 ) >Int 1024 )
       andBool ( ( notBool ( Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas andBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 ) )
               )))))
      [priority(20), label(BASIC-BLOCK-13-TO-16)]

endmodule
