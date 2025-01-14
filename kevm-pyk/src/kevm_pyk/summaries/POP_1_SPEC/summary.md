
┌─ 1 (root, split, init)
│   k: #next [ POP ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 11
┃  │   k: #next [ POP ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (3 steps)
┃  └─ 5 (leaf, pending)
┃      k: #gas [ POP , POP _W0:Int ] ~> POP _W0:Int ~> #pc [ POP ] ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 14
┃  │   k: #next [ POP ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  └─ 7 (leaf, pending)
┃      k: Gbase < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ POP , POP _W0:Int ] ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     _GAS_CELL:Gas <Gas Gbase < _SCHEDULE_CELL:Schedule >
   │
   ├─ 15
   │   k: #next [ POP ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (12 steps)
   └─ 9 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-POP-1-SPEC
    
    
    rule [BASIC-BLOCK-11-TO-5]: <kevm>
           <k>
             ( #next [ POP ] ~> .K => #gas [ POP , POP _W0:Int ]
             ~> POP _W0:Int
             ~> #pc [ POP ] )
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( notBool _USEGAS_CELL:Bool )
      [priority(20), label(BASIC-BLOCK-11-TO-5)]
    
    rule [BASIC-BLOCK-14-TO-7]: <kevm>
           <k>
             ( #next [ POP ] ~> .K => Gbase < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ POP , POP _W0:Int ]
             ~> POP _W0:Int
             ~> #pc [ POP ] )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( Gbase < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               ))
      [priority(20), label(BASIC-BLOCK-14-TO-7)]
    
    rule [BASIC-BLOCK-15-TO-9]: <kevm>
           <k>
             ( #next [ POP ] => #halt )
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
                   ( ( __W0 : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( _GAS_CELL:Gas <Gas Gbase < _SCHEDULE_CELL:Schedule >
               ))
      [priority(20), label(BASIC-BLOCK-15-TO-9)]

endmodule
