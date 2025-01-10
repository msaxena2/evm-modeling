
┌─ 1 (root, split, init)
│   k: #next [ DUP ( _N:Int ) ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023
┃  ┃     _N:Int <=Int #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 )
┃  ┃     #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi
┃  │
┃  └─ 3 (leaf, pending)
┃      k: #next [ DUP ( _N:Int ) ] ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int _N:Int
┃  │
┃  ├─ 4
┃  │   k: #next [ DUP ( _N:Int ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 7
┃  ┃  │   k: #end EVMC_STACK_UNDERFLOW ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (1 step)
┃  ┃  └─ 16 (leaf, terminal)
┃  ┃      k: #halt ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: EVMC_STACK_UNDERFLOW
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 8
┃     │   k: #end EVMC_STACK_OVERFLOW ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     │
┃     │  (1 step)
┃     └─ 18 (leaf, terminal)
┃         k: #halt ~> _K_CELL:K
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: EVMC_STACK_OVERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( ( _N:Int +Int 1 ) -Int _N:Int ) ) >Int 1024
┃  │
┃  ├─ 5
┃  │   k: #next [ DUP ( _N:Int ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 9
┃  ┃  │   k: #end EVMC_STACK_UNDERFLOW ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (1 step)
┃  ┃  └─ 17 (leaf, terminal)
┃  ┃      k: #halt ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: EVMC_STACK_UNDERFLOW
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 10
┃     │   k: #end EVMC_STACK_OVERFLOW ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     │
┃     │  (1 step)
┃     └─ 19 (leaf, terminal)
┃         k: #halt ~> _K_CELL:K
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: EVMC_STACK_OVERFLOW
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int _N:Int )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( ( _N:Int +Int 1 ) -Int _N:Int ) ) >Int 1024 )
   │
   ├─ 6
   │   k: #next [ DUP ( _N:Int ) ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 11
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
      ├─ 12
      │   k: #addr [ DUP ( _N:Int ) ] ~> #exec [ DUP ( _N:Int ) ] ~> #pc [ DUP ( _N:Int ) ] ~ ...
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      │
      │  (6 steps)
      ├─ 13
      │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ DUP ( _N:Int ) , ...
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 14
      ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ DUP ( _N:Int ) , DUP ( _N:Int ) _WORDSTACK_CEL ...
      ┃  │   pc: _PC_CELL:Int
      ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  │
      ┃  │  (4 steps)
      ┃  └─ 20 (leaf, terminal)
      ┃      k: #halt ~> _K_CELL:K
      ┃      pc: _PC_CELL:Int
      ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃      statusCode: EVMC_OUT_OF_GAS
      ┃
      ┗━━┓
         │
         └─ 15 (stuck, leaf)
             k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ DUP ( _N:Int ) , ...
             pc: _PC_CELL:Int
             callDepth: _CALLDEPTH_CELL:Int
             statusCode: _STATUSCODE_CELL:StatusCode




module SUMMARY-DUP-SPEC
    
    
    rule [BASIC-BLOCK-12-TO-13]: <kevm>
           <k>
             ( #addr [ DUP ( _N:Int ) ]
             ~> #exec [ DUP ( _N:Int ) ] => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ DUP ( _N:Int ) , DUP ( _N:Int ) _WORDSTACK_CELL:WordStack ]
             ~> DUP ( _N:Int ) _WORDSTACK_CELL:WordStack )
             ~> #pc [ DUP ( _N:Int ) ]
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
      requires ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int _N:Int )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( ( _N:Int +Int 1 ) -Int _N:Int ) ) >Int 1024 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool ( _N:Int <=Int #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) andBool #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) ) )
               )))
       ensures ( _USEGAS_CELL:Bool
       andBool ( ( notBool ( Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas andBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool _N:Int <=Int #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) ) ) )
               ))
      [priority(20), label(BASIC-BLOCK-12-TO-13)]
    
    rule [BASIC-BLOCK-7-TO-16]: <kevm>
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int _N:Int
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool ( _N:Int <=Int #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) andBool #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) ) )
               ))
      [priority(20), label(BASIC-BLOCK-7-TO-16)]
    
    rule [BASIC-BLOCK-9-TO-17]: <kevm>
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int _N:Int
       andBool ( ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( ( _N:Int +Int 1 ) -Int _N:Int ) ) >Int 1024
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool ( _N:Int <=Int #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) andBool #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) ) )
               )))
      [priority(20), label(BASIC-BLOCK-9-TO-17)]
    
    rule [BASIC-BLOCK-8-TO-18]: <kevm>
           <k>
             ( #end EVMC_STACK_OVERFLOW => #halt )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int _N:Int
       andBool ( ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( ( _N:Int +Int 1 ) -Int _N:Int ) ) >Int 1024
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool ( _N:Int <=Int #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) andBool #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) ) )
               )))
      [priority(20), label(BASIC-BLOCK-8-TO-18)]
    
    rule [BASIC-BLOCK-10-TO-19]: <kevm>
           <k>
             ( #end EVMC_STACK_OVERFLOW => #halt )
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
      requires ( ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( ( _N:Int +Int 1 ) -Int _N:Int ) ) >Int 1024
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool ( _N:Int <=Int #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) andBool #if _USEGAS_CELL:Bool #then Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas #else true #fi ) ) )
               ))
      [priority(20), label(BASIC-BLOCK-10-TO-19)]
    
    rule [BASIC-BLOCK-14-TO-20]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ DUP ( _N:Int ) , DUP ( _N:Int ) _WORDSTACK_CELL:WordStack ]
             ~> DUP ( _N:Int ) _WORDSTACK_CELL:WordStack
             ~> #pc [ DUP ( _N:Int ) ] => #halt ~> .K )
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int _N:Int )
       andBool ( _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( ( _N:Int +Int 1 ) -Int _N:Int ) ) >Int 1024 )
       andBool ( ( notBool ( Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas andBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <=Int 1023 andBool _N:Int <=Int #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) ) ) )
               )))))
      [priority(20), label(BASIC-BLOCK-14-TO-20)]

endmodule
