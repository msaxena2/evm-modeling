
┌─ 1 (root, split, init)
│   k: #next [ ORIGIN ] ~> _K_CELL:K
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
┃  │   k: #next [ ORIGIN ] ~> _K_CELL:K
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
┃  ├─ 22
┃  │   k: #next [ ORIGIN ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (5 steps)
┃  ├─ 9
┃  │   k: _ORIGIN_CELL:Account ~> #push ~> #pc [ ORIGIN ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 10
┃  ┃  │   k: #pc [ ORIGIN ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (1 step)
┃  ┃  ├─ 19
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
┃     └─ 11 (stuck, leaf)
┃         k: _ORIGIN_CELL:Account ~> #push ~> #pc [ ORIGIN ] ~> _K_CELL:K
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
┃  ┃     Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 25
┃  │   k: #next [ ORIGIN ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  ├─ 15
┃  │   k: _ORIGIN_CELL:Account ~> #push ~> #pc [ ORIGIN ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 16
┃  ┃  │   k: #pc [ ORIGIN ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (1 step)
┃  ┃  ├─ 20
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
┃     └─ 17 (stuck, leaf)
┃         k: _ORIGIN_CELL:Account ~> #push ~> #pc [ ORIGIN ] ~> _K_CELL:K
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
   ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
   ┃     _GAS_CELL:Gas <Gas Gbase < _SCHEDULE_CELL:Schedule >
   │
   ├─ 26
   │   k: #next [ ORIGIN ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (12 steps)
   └─ 18 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS




module SUMMARY-ORIGIN-0-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ ORIGIN ] => #halt )
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
    
    rule [BASIC-BLOCK-10-TO-19]: <kevm>
           <k>
             ( #pc [ ORIGIN ] ~> .K => .K )
             ~> __K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( W0:Int : _WS:WordStack )
                 </wordStack>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 ...
               </callState>
               <origin>
                 W0:Int
               </origin>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __ORIGIN_CELL ==K W0:Int
       andBool ( ( notBool __USEGAS_CELL )
       andBool ( #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
               )))
      [priority(20), label(BASIC-BLOCK-10-TO-19)]
    
    rule [BASIC-BLOCK-16-TO-20]: <kevm>
           <k>
             ( #pc [ ORIGIN ] ~> .K => .K )
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
                   ( W0:Int : _WS:WordStack )
                 </wordStack>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 <gas>
                   _GAS_CELL:Gas -Gas Gbase < _SCHEDULE_CELL:Schedule >
                 </gas>
                 ...
               </callState>
               <origin>
                 W0:Int
               </origin>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( __ORIGIN_CELL ==K W0:Int
       andBool ( #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
       andBool ( Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               ))))
      [priority(20), label(BASIC-BLOCK-16-TO-20)]
    
    rule [BASIC-BLOCK-22-TO-9]: <kevm>
           <k>
             ( #next [ ORIGIN ] ~> .K => _ORIGIN_CELL:Account
             ~> #push
             ~> #pc [ ORIGIN ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   _WS:WordStack
                 </wordStack>
                 ...
               </callState>
               <origin>
                 _ORIGIN_CELL:Account
               </origin>
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
      [priority(20), label(BASIC-BLOCK-22-TO-9)]
    
    rule [BASIC-BLOCK-25-TO-15]: <kevm>
           <k>
             ( #next [ ORIGIN ] ~> .K => _ORIGIN_CELL:Account
             ~> #push
             ~> #pc [ ORIGIN ] )
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
                   _WS:WordStack
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Gbase < _SCHEDULE_CELL:Schedule > )
                 </gas>
                 ...
               </callState>
               <origin>
                 _ORIGIN_CELL:Account
               </origin>
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
      [priority(20), label(BASIC-BLOCK-25-TO-15)]
    
    rule [BASIC-BLOCK-26-TO-18]: <kevm>
           <k>
             ( #next [ ORIGIN ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-26-TO-18)]

endmodule
