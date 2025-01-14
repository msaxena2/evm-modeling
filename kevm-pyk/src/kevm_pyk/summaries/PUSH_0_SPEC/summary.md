
┌─ 1 (root, split, init)
│   k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
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
┃  │   k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
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
┃  ├─ 14
┃  │   k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (3 steps)
┃  └─ 7 (leaf, pending)
┃      k: #gas [ PUSH ( _N:Int ) , PUSH ( _N:Int ) ] ~> PUSH ( _N:Int ) ~> #pc [ PUSH ( _N ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
┃  ┃     Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 17
┃  │   k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  └─ 10 (leaf, pending)
┃      k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ PUSH ( _N:Int )  ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
   ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
   ┃     _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
   │
   ├─ 18
   │   k: #next [ PUSH ( _N:Int ) ] ~> _K_CELL:K
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


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-PUSH-0-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ PUSH ( __N ) ] => #halt )
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
    
    rule [BASIC-BLOCK-14-TO-7]: <kevm>
           <k>
             ( #next [ PUSH ( _N:Int ) ] ~> .K => #gas [ PUSH ( _N:Int ) , PUSH ( _N:Int ) ]
             ~> PUSH ( _N:Int )
             ~> #pc [ PUSH ( _N:Int ) ] )
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
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
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
               )))
       ensures #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-14-TO-7)]
    
    rule [BASIC-BLOCK-17-TO-10]: <kevm>
           <k>
             ( #next [ PUSH ( _N:Int ) ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ PUSH ( _N:Int ) , PUSH ( _N:Int ) ]
             ~> PUSH ( _N:Int )
             ~> #pc [ PUSH ( _N:Int ) ] )
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
       andBool ( Gverylow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               ))))
       ensures #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-17-TO-10)]
    
    rule [BASIC-BLOCK-18-TO-12]: <kevm>
           <k>
             ( #next [ PUSH ( __N ) ] => #halt )
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
       andBool ( _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
               ))))
       ensures #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-18-TO-12)]

endmodule
