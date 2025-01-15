
┌─ 1 (root, split, init)
│   k: #next [ DUP ( 14 ) ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     1023 <Int #sizeWordStack ( _WS:WordStack , 14 )
┃  │
┃  ├─ 3
┃  │   k: #next [ DUP ( 14 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 6 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  ┃     ( notBool #sizeWordStack ( _WS:WordStack , 14 ) <Int 14 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 14 ) )
┃  │
┃  ├─ 16
┃  │   k: #next [ DUP ( 14 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 13
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
┃  ┃     ( notBool #sizeWordStack ( _WS:WordStack , 14 ) <Int 14 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 14 ) )
┃  ┃     Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 19
┃  │   k: #next [ DUP ( 14 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (12 steps)
┃  ├─ 14
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
   ┃     ( notBool #sizeWordStack ( _WS:WordStack , 14 ) <Int 14 )
   ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 14 ) )
   ┃     _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
   │
   ├─ 20
   │   k: #next [ DUP ( 14 ) ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (12 steps)
   └─ 12 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS




module SUMMARY-DUP-14-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-6]: <kevm>
           <k>
             ( #next [ DUP ( 14 ) ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STACK_OVERFLOW )
               </statusCode>
               <callState>
                 <wordStack>
                   ( __W0 : ( __W1 : ( __W2 : ( __W3 : ( __W4 : ( __W5 : ( __W6 : ( __W7 : ( __W8 : ( __W9 : ( __W10 : ( __W11 : ( __W12 : ( __W13 : _WS:WordStack ) ) ) ) ) ) ) ) ) ) ) ) ) )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires 1023 <Int #sizeWordStack ( _WS:WordStack , 14 )
      [priority(20), label(BASIC-BLOCK-3-TO-6)]
    
    rule [BASIC-BLOCK-16-TO-13]: <kevm>
           <k>
             ( #next [ DUP ( 14 ) ] ~> .K => .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int => _W13:Int ) : ( ( _W1:Int => _W0:Int ) : ( ( _W2:Int => _W1:Int ) : ( ( _W3:Int => _W2:Int ) : ( ( _W4:Int => _W3:Int ) : ( ( _W5:Int => _W4:Int ) : ( ( _W6:Int => _W5:Int ) : ( ( _W7:Int => _W6:Int ) : ( ( _W8:Int => _W7:Int ) : ( ( _W9:Int => _W8:Int ) : ( ( _W10:Int => _W9:Int ) : ( ( _W11:Int => _W10:Int ) : ( ( _W12:Int => _W11:Int ) : ( ( _W13:Int => _W12:Int ) : ( _WS:WordStack => ( _W13:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
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
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 14 ) <Int 14 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 14 ) )
               )))
       ensures #sizeWordStack ( _WS:WordStack , 14 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-16-TO-13)]
    
    rule [BASIC-BLOCK-19-TO-14]: <kevm>
           <k>
             ( #next [ DUP ( 14 ) ] ~> .K => .K )
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
                   ( ( _W0:Int => _W13:Int ) : ( ( _W1:Int => _W0:Int ) : ( ( _W2:Int => _W1:Int ) : ( ( _W3:Int => _W2:Int ) : ( ( _W4:Int => _W3:Int ) : ( ( _W5:Int => _W4:Int ) : ( ( _W6:Int => _W5:Int ) : ( ( _W7:Int => _W6:Int ) : ( ( _W8:Int => _W7:Int ) : ( ( _W9:Int => _W8:Int ) : ( ( _W10:Int => _W9:Int ) : ( ( _W11:Int => _W10:Int ) : ( ( _W12:Int => _W11:Int ) : ( ( _W13:Int => _W12:Int ) : ( _WS:WordStack => ( _W13:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
                 </wordStack>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Gverylow < _SCHEDULE_CELL:Schedule > )
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
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 14 ) <Int 14 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 14 ) )
       andBool ( Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               ))))
       ensures #sizeWordStack ( _WS:WordStack , 14 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-19-TO-14)]
    
    rule [BASIC-BLOCK-20-TO-12]: <kevm>
           <k>
             ( #next [ DUP ( 14 ) ] => #halt )
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
                   ( __W0 : ( __W1 : ( __W2 : ( __W3 : ( __W4 : ( __W5 : ( __W6 : ( __W7 : ( __W8 : ( __W9 : ( __W10 : ( __W11 : ( __W12 : ( __W13 : _WS:WordStack ) ) ) ) ) ) ) ) ) ) ) ) ) )
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
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 14 ) <Int 14 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 14 ) )
       andBool ( _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
               ))))
       ensures #sizeWordStack ( _WS:WordStack , 14 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-20-TO-12)]

endmodule
