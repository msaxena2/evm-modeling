
┌─ 1 (root, split, init)
│   k: #next [ GASPRICE ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     1023 <Int #sizeWordStack ( _WS:WordStack , 0 )
┃  │
┃  ├─ 3
┃  │   k: #next [ GASPRICE ] ~> _K_CELL:K
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
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  ┃     ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
┃  │
┃  ├─ 16
┃  │   k: #next [ GASPRICE ] ~> _K_CELL:K
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
┃  ┃     ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
┃  ┃     Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 19
┃  │   k: #next [ GASPRICE ] ~> _K_CELL:K
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
   ┃     ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
   ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
   ┃     _GAS_CELL:Gas <Gas Gbase < _SCHEDULE_CELL:Schedule >
   │
   ├─ 20
   │   k: #next [ GASPRICE ] ~> _K_CELL:K
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




module SUMMARY-GASPRICE-0-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ GASPRICE ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STACK_OVERFLOW )
               </statusCode>
               <callState>
                 <wordStack>
                   _WS:WordStack
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires 1023 <Int #sizeWordStack ( _WS:WordStack , 0 )
      [priority(20), label(BASIC-BLOCK-3-TO-8)]
    
    rule [BASIC-BLOCK-16-TO-13]: <kevm>
           <k>
             ( #next [ GASPRICE ] ~> .K => .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( _WS:WordStack => ( _GASPRICE_CELL:Int : _WS:WordStack ) )
                 </wordStack>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 ...
               </callState>
               <gasPrice>
                 _GASPRICE_CELL:Int
               </gasPrice>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
               )))
       ensures #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-16-TO-13)]
    
    rule [BASIC-BLOCK-19-TO-14]: <kevm>
           <k>
             ( #next [ GASPRICE ] ~> .K => .K )
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
                   ( _WS:WordStack => ( _GASPRICE_CELL:Int : _WS:WordStack ) )
                 </wordStack>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Gbase < _SCHEDULE_CELL:Schedule > )
                 </gas>
                 ...
               </callState>
               <gasPrice>
                 _GASPRICE_CELL:Int
               </gasPrice>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
       andBool ( Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               ))))
       ensures #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-19-TO-14)]
    
    rule [BASIC-BLOCK-20-TO-12]: <kevm>
           <k>
             ( #next [ GASPRICE ] => #halt )
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
                   _WS:WordStack
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
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
       andBool ( _GAS_CELL:Gas <Gas Gbase < _SCHEDULE_CELL:Schedule >
               ))))
       ensures #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-20-TO-12)]

endmodule
