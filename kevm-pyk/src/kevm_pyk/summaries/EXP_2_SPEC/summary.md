
┌─ 1 (root, split, init)
│   k: #next [ EXP ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 22
┃  │   k: #next [ EXP ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 18
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
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     0 <Int _W1:Int
┃  │
┃  ├─ 28
┃  │   k: #next [ EXP ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 10
┃  │   k: ( Gexp < _SCHEDULE_CELL:Schedule > +Int ( Gexpbyte < _SCHEDULE_CELL:Schedule > * ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 13
┃  ┃  │   k: #access [ EXP , EXP _W0:Int _W1:Int ] ~> EXP _W0:Int _W1:Int ~> #pc [ EXP ] ~> _ ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (4 steps)
┃  ┃  ├─ 20
┃  ┃  │   k: _K_CELL:K
┃  ┃  │   pc: ( _PC_CELL:Int +Int 1 )
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  ┊  constraint:
┃  ┃  ┊      Ceil_f22a2e60
┃  ┃  ┊  subst: ...
┃  ┃  └─ 2 (leaf, target)
┃  ┃      k: _K_CELL:K
┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 14
┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ EXP , EXP _W0:Int _W1:Int ] ~> EXP _W0:Int _W1 ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (4 steps)
┃  ┃  └─ 16 (leaf, terminal)
┃  ┃      k: #halt ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: EVMC_OUT_OF_GAS
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 15 (stuck, leaf)
┃         k: ( Gexp < _SCHEDULE_CELL:Schedule > +Int ( Gexpbyte < _SCHEDULE_CELL:Schedule > * ...
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     _W1:Int <=Int 0
┃  ┃     Gexp < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 31
┃  │   k: #next [ EXP ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (12 steps)
┃  ├─ 19
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
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     _W1:Int <=Int 0
   ┃     _GAS_CELL:Gas <Gas Gexp < _SCHEDULE_CELL:Schedule >
   │
   ├─ 32
   │   k: #next [ EXP ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (12 steps)
   └─ 17 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS




module SUMMARY-EXP-2-SPEC
    
    
    rule [BASIC-BLOCK-14-TO-16]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ EXP , EXP _W0:Int _W1:Int ]
             ~> EXP _W0:Int _W1:Int
             ~> #pc [ EXP ] => #halt ~> .K )
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
       andBool ( 0 <Int _W1:Int
       andBool ( _GAS_CELL:Gas <Gas ( Gexp < _SCHEDULE_CELL:Schedule > +Int ( Gexpbyte < _SCHEDULE_CELL:Schedule > *Int ( ( log2Int ( _W1:Int ) /Int 8 ) +Int 1 ) ) )
               )))
      [priority(20), label(BASIC-BLOCK-14-TO-16)]
    
    rule [BASIC-BLOCK-13-TO-20]: <kevm>
           <k>
             ( #access [ EXP , EXP _W0:Int _W1:Int ]
             ~> EXP _W0:Int _W1:Int
             ~> #pc [ EXP ] => .K )
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
                   ( _WS:WordStack => ( powmod ( _W0:Int , _W1:Int , pow256 ) : _WS:WordStack ) )
                 </wordStack>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Gexp < _SCHEDULE_CELL:Schedule > +Int ( Gexpbyte < _SCHEDULE_CELL:Schedule > *Int ( ( log2Int ( _W1:Int ) /Int 8 ) +Int 1 ) ) )
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
       andBool ( 0 <Int _W1:Int
       andBool ( ( Gexp < _SCHEDULE_CELL:Schedule > +Int ( Gexpbyte < _SCHEDULE_CELL:Schedule > *Int ( ( log2Int ( _W1:Int ) /Int 8 ) +Int 1 ) ) ) <=Gas _GAS_CELL:Gas
               )))
      [priority(20), label(BASIC-BLOCK-13-TO-20)]
    
    rule [BASIC-BLOCK-22-TO-18]: <kevm>
           <k>
             ( #next [ EXP ] ~> .K => .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int => powmod ( _W0:Int , _W1:Int , pow256 ) ) : ( ( _W1:Int : _WS:WordStack ) => _WS:WordStack ) )
                 </wordStack>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( notBool _USEGAS_CELL:Bool )
      [priority(20), label(BASIC-BLOCK-22-TO-18)]
    
    rule [BASIC-BLOCK-28-TO-10]: <kevm>
           <k>
             ( #next [ EXP ] ~> .K => ( Gexp < _SCHEDULE_CELL:Schedule > +Int ( Gexpbyte < _SCHEDULE_CELL:Schedule > *Int ( ( log2Int ( _W1:Int ) /Int 8 ) +Int 1 ) ) )
             ~> #deductGas
             ~> #access [ EXP , EXP _W0:Int _W1:Int ]
             ~> EXP _W0:Int _W1:Int
             ~> #pc [ EXP ] )
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
                   ( ( _W0:Int : ( _W1:Int : _WS:WordStack ) ) => _WS:WordStack )
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
       andBool ( 0 <Int _W1:Int
               ))
      [priority(20), label(BASIC-BLOCK-28-TO-10)]
    
    rule [BASIC-BLOCK-31-TO-19]: <kevm>
           <k>
             ( #next [ EXP ] ~> .K => .K )
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
                   ( ( _W0:Int => powmod ( _W0:Int , _W1:Int , pow256 ) ) : ( ( _W1:Int : _WS:WordStack ) => _WS:WordStack ) )
                 </wordStack>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Gexp < _SCHEDULE_CELL:Schedule > )
                 </gas>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( _W1:Int <=Int 0
       andBool ( Gexp < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               )))
      [priority(20), label(BASIC-BLOCK-31-TO-19)]
    
    rule [BASIC-BLOCK-32-TO-17]: <kevm>
           <k>
             ( #next [ EXP ] => #halt )
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
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_OUT_OF_GAS )
               </statusCode>
               <callState>
                 <wordStack>
                   ( ( __W0 : ( _W1:Int : _WS:WordStack ) ) => _WS:WordStack )
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
      requires ( _USEGAS_CELL:Bool
       andBool ( _W1:Int <=Int 0
       andBool ( _GAS_CELL:Gas <Gas Gexp < _SCHEDULE_CELL:Schedule >
               )))
      [priority(20), label(BASIC-BLOCK-32-TO-17)]

endmodule
