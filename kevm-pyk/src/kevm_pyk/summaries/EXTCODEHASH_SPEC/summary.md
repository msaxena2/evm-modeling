
┌─ 1 (root, split, init)
│   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1
┃  │
┃  ├─ 3
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
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
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
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
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1 )
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024 )
   │
   ├─ 5
   │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (1 step)
   ├─ 6
   │   k: #addr [ EXTCODEHASH ] ~> #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL ...
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9 (split)
   ┃  │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
   ┃  │   pc: _PC_CELL:Int
   ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┃ (branch)
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     _USEGAS_CELL:Bool
   ┃  ┃  │
   ┃  ┃  ├─ 37
   ┃  ┃  │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (5 steps)
   ┃  ┃  ├─ 21
   ┃  ┃  │   k: Cextcodehash ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODEHASH  ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 22 (split)
   ┃  ┃  ┃  │   k: #access [ EXTCODEHASH , EXTCODEHASH ( W0:Int modInt pow160 ) ] ~> EXTCODEHASH (  ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃ (branch)
   ┃  ┃  ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃  ┃  ┃ constraint:
   ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  └─ 31 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #access [ EXTCODEHASH , EXTCODEHASH ( W0:Int modInt pow160 ) ] ~> EXTCODEHASH (  ...
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┗━━┓ subst: .Subst
   ┃  ┃  ┃     ┃ constraint: true
   ┃  ┃  ┃     │
   ┃  ┃  ┃     └─ 32 (leaf, pending)
   ┃  ┃  ┃         k: #access [ EXTCODEHASH , EXTCODEHASH ( W0:Int modInt pow160 ) ] ~> EXTCODEHASH (  ...
   ┃  ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 23 (leaf, pending)
   ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ EXTCODEHASH , EXTCODEHASH ( W0:Int modInt pow1 ...
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 24 (stuck, leaf)
   ┃  ┃         k: Cextcodehash ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODEHASH  ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     ├─ 38
   ┃     │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     │
   ┃     │  (1 step)
   ┃     └─ 15 (leaf, pending)
   ┃         k: #gas [ EXTCODEHASH , EXTCODEHASH ( W0:Int modInt pow160 ) ] ~> EXTCODEHASH ( W0: ...
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #addr [ EXTCODEHASH ] ~> #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL ...
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 12 (split)
      ┃  │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
      ┃  │   pc: _PC_CELL:Int
      ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┃ (branch)
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     _USEGAS_CELL:Bool
      ┃  ┃  │
      ┃  ┃  ├─ 39
      ┃  ┃  │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (5 steps)
      ┃  ┃  ├─ 30
      ┃  ┃  │   k: Cextcodehash ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODEHASH  ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  └─ 33 (leaf, pending)
      ┃  ┃  ┃      k: #access [ EXTCODEHASH , EXTCODEHASH ( W1:Int modInt pow160 ) ] ~> EXTCODEHASH (  ...
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  └─ 34 (leaf, pending)
      ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ EXTCODEHASH , EXTCODEHASH ( W1:Int modInt pow1 ...
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 35 (leaf, pending)
      ┃  ┃         k: Cextcodehash ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODEHASH  ...
      ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     ├─ 40
      ┃     │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
      ┃     │   pc: _PC_CELL:Int
      ┃     │   callDepth: _CALLDEPTH_CELL:Int
      ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃     │
      ┃     │  (1 step)
      ┃     └─ 18 (leaf, pending)
      ┃         k: #gas [ EXTCODEHASH , EXTCODEHASH ( W1:Int modInt pow160 ) ] ~> EXTCODEHASH ( W1: ...
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 13
         │   k: #addr [ EXTCODEHASH ] ~> #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL ...
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 19 (split)
         ┃  │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
         ┃  │   pc: _PC_CELL:Int
         ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┃ (branch)
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     _USEGAS_CELL:Bool
         ┃  ┃  │
         ┃  ┃  ├─ 41
         ┃  ┃  │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  │
         ┃  ┃  │  (1 step)
         ┃  ┃  └─ 28 (leaf, pending)
         ┃  ┃      k: #gas [ EXTCODEHASH , EXTCODEHASH ( W2:Int modInt pow160 ) ] ~> EXTCODEHASH ( W2: ...
         ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     ├─ 42
         ┃     │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
         ┃     │   pc: _PC_CELL:Int
         ┃     │   callDepth: _CALLDEPTH_CELL:Int
         ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃     │
         ┃     │  (1 step)
         ┃     └─ 29 (leaf, pending)
         ┃         k: #gas [ EXTCODEHASH , EXTCODEHASH ( W2:Int modInt pow160 ) ] ~> EXTCODEHASH ( W2: ...
         ┃         pc: _PC_CELL:Int
         ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 20
            │   k: #addr [ EXTCODEHASH ] ~> #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL ...
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  ├─ 26
            ┃  │   k: #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL:K
            ┃  │   pc: _PC_CELL:Int
            ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  │
            ┃  │  (1 step)
            ┃  └─ 36 (leaf, pending)
            ┃      k: #gas [ EXTCODEHASH , EXTCODEHASH ( W3:Int modInt pow160 ) ] ~> EXTCODEHASH ( W3: ...
            ┃      pc: _PC_CELL:Int
            ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               └─ 27 (leaf, pending)
                   k: #addr [ EXTCODEHASH ] ~> #exec [ EXTCODEHASH ] ~> #pc [ EXTCODEHASH ] ~> _K_CELL ...
                   pc: _PC_CELL:Int
                   callDepth: _CALLDEPTH_CELL:Int
                   statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-EXTCODEHASH-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #addr [ EXTCODEHASH ]
             ~> #exec [ EXTCODEHASH ]
             ~> #pc [ EXTCODEHASH ] )
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
      requires ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024 )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-6)]
    
    rule [BASIC-BLOCK-4-TO-7]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-7)]
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1
      [priority(20), label(BASIC-BLOCK-3-TO-8)]
    
    rule [BASIC-BLOCK-26-TO-36]: <kevm>
           <k>
             ( #exec [ EXTCODEHASH ] ~> .K => #gas [ EXTCODEHASH , EXTCODEHASH ( W3:Int modInt pow160 ) ]
             ~> EXTCODEHASH ( W3:Int modInt pow160 ) )
             ~> #pc [ EXTCODEHASH ]
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W3:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _W0 =/=Int W3:Int
       andBool ( _W1 =/=Int W3:Int
       andBool ( _W2 =/=Int W3:Int
       andBool ( __WORDSTACK_CELL ==K ( W3:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-26-TO-36)]
    
    rule [BASIC-BLOCK-38-TO-15]: <kevm>
           <k>
             ( #exec [ EXTCODEHASH ] ~> .K => #gas [ EXTCODEHASH , EXTCODEHASH ( W0:Int modInt pow160 ) ]
             ~> EXTCODEHASH ( W0:Int modInt pow160 ) )
             ~> #pc [ EXTCODEHASH ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W0:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-38-TO-15)]
    
    rule [BASIC-BLOCK-40-TO-18]: <kevm>
           <k>
             ( #exec [ EXTCODEHASH ] ~> .K => #gas [ EXTCODEHASH , EXTCODEHASH ( W1:Int modInt pow160 ) ]
             ~> EXTCODEHASH ( W1:Int modInt pow160 ) )
             ~> #pc [ EXTCODEHASH ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W1:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( _W0 =/=Int W1:Int
       andBool ( __WORDSTACK_CELL ==K ( W1:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-40-TO-18)]
    
    rule [BASIC-BLOCK-41-TO-28]: <kevm>
           <k>
             ( #exec [ EXTCODEHASH ] ~> .K => #gas [ EXTCODEHASH , EXTCODEHASH ( W2:Int modInt pow160 ) ]
             ~> EXTCODEHASH ( W2:Int modInt pow160 ) )
             ~> #pc [ EXTCODEHASH ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W2:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( _W0 =/=Int W2:Int
       andBool ( _W1 =/=Int W2:Int
       andBool ( __WORDSTACK_CELL ==K ( W2:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-41-TO-28)]
    
    rule [BASIC-BLOCK-42-TO-29]: <kevm>
           <k>
             ( #exec [ EXTCODEHASH ] ~> .K => #gas [ EXTCODEHASH , EXTCODEHASH ( W2:Int modInt pow160 ) ]
             ~> EXTCODEHASH ( W2:Int modInt pow160 ) )
             ~> #pc [ EXTCODEHASH ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W2:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( _W0 =/=Int W2:Int
       andBool ( _W1 =/=Int W2:Int
       andBool ( __WORDSTACK_CELL ==K ( W2:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-42-TO-29)]
    
    rule [BASIC-BLOCK-37-TO-21]: <kevm>
           <k>
             ( #exec [ EXTCODEHASH ] ~> .K => Cextcodehash ( _SCHEDULE_CELL:Schedule )
             ~> #deductGas
             ~> #access [ EXTCODEHASH , EXTCODEHASH ( W0:Int modInt pow160 ) ]
             ~> EXTCODEHASH ( W0:Int modInt pow160 ) )
             ~> #pc [ EXTCODEHASH ]
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
                   ( ( ( W0:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-37-TO-21)]
    
    rule [BASIC-BLOCK-39-TO-30]: <kevm>
           <k>
             ( #exec [ EXTCODEHASH ] ~> .K => Cextcodehash ( _SCHEDULE_CELL:Schedule )
             ~> #deductGas
             ~> #access [ EXTCODEHASH , EXTCODEHASH ( W1:Int modInt pow160 ) ]
             ~> EXTCODEHASH ( W1:Int modInt pow160 ) )
             ~> #pc [ EXTCODEHASH ]
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
                   ( ( ( W1:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( _W0 =/=Int W1:Int
       andBool ( __WORDSTACK_CELL ==K ( W1:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-39-TO-30)]

endmodule
