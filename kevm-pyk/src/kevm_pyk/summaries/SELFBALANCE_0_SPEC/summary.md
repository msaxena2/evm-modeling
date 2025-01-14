
┌─ 1 (root, split, init)
│   k: #next [ SELFBALANCE ] ~> _K_CELL:K
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
┃  │   k: #next [ SELFBALANCE ] ~> _K_CELL:K
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
┃  ├─ 34
┃  │   k: #next [ SELFBALANCE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 9
┃  │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 10 (leaf, pending)
┃  ┃      k: BAL:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 11
┃     │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 15 (leaf, pending)
┃     ┃      k: BAL0:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 16
┃        │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  └─ 20 (leaf, pending)
┃        ┃      k: BAL1:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃        ┃      pc: _PC_CELL:Int
┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 21
┃           │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  └─ 24 (leaf, pending)
┃           ┃      k: BAL2:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃           ┃      pc: _PC_CELL:Int
┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              ├─ 25
┃              │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃              │   pc: _PC_CELL:Int
┃              │   callDepth: _CALLDEPTH_CELL:Int
┃              │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┃ (1 step)
┃              ┣━━┓
┃              ┃  │
┃              ┃  └─ 29 (leaf, pending)
┃              ┃      k: BAL3:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃              ┃      pc: _PC_CELL:Int
┃              ┃      callDepth: _CALLDEPTH_CELL:Int
┃              ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┗━━┓
┃                 │
┃                 └─ 30 (leaf, pending)
┃                     k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃                     pc: _PC_CELL:Int
┃                     callDepth: _CALLDEPTH_CELL:Int
┃                     statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
┃  ┃     Glow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 37
┃  │   k: #next [ SELFBALANCE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (9 steps)
┃  ├─ 17
┃  │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 18 (leaf, pending)
┃  ┃      k: BAL:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 19
┃     │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 22 (leaf, pending)
┃     ┃      k: BAL0:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 23
┃        │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  └─ 27 (leaf, pending)
┃        ┃      k: BAL1:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃        ┃      pc: _PC_CELL:Int
┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 28
┃           │   k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  └─ 31 (leaf, pending)
┃           ┃      k: BAL2:Int ~> #push ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃           ┃      pc: _PC_CELL:Int
┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              └─ 32 (leaf, pending)
┃                  k: SELFBALANCE ~> #pc [ SELFBALANCE ] ~> _K_CELL:K
┃                  pc: _PC_CELL:Int
┃                  callDepth: _CALLDEPTH_CELL:Int
┃                  statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     ( notBool #sizeWordStack ( _WS:WordStack , 0 ) <Int 0 )
   ┃     ( notBool 1023 <Int #sizeWordStack ( _WS:WordStack , 0 ) )
   ┃     _GAS_CELL:Gas <Gas Glow < _SCHEDULE_CELL:Schedule >
   │
   ├─ 38
   │   k: #next [ SELFBALANCE ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (12 steps)
   └─ 26 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SELFBALANCE-0-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] => #halt )
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
    
    rule [BASIC-BLOCK-34-TO-9]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] ~> .K => SELFBALANCE
             ~> #pc [ SELFBALANCE ] )
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
      [priority(20), label(BASIC-BLOCK-34-TO-9)]
    
    rule [BASIC-BLOCK-37-TO-17]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] ~> .K => SELFBALANCE
             ~> #pc [ SELFBALANCE ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Glow < _SCHEDULE_CELL:Schedule > )
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
       andBool ( Glow < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               ))))
       ensures #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-37-TO-17)]
    
    rule [BASIC-BLOCK-38-TO-26]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] => #halt )
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
       andBool ( _GAS_CELL:Gas <Gas Glow < _SCHEDULE_CELL:Schedule >
               ))))
       ensures #sizeWordStack ( _WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-38-TO-26)]

endmodule
