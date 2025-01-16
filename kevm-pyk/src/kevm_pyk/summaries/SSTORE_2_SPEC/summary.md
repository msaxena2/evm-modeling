
┌─ 1 (root, split, init)
│   k: #next [ SSTORE ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  │
┃  ├─ 3
┃  │   k: #next [ SSTORE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 5
┃  │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 7 (leaf, pending)
┃  ┃      k: #pc [ SSTORE ] ~> K_CELL:K
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 8
┃     │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> K_CELL:K
┃     │   pc: PC_CELL:Int
┃     │   callDepth: CALLDEPTH_CELL:Int
┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 9 (leaf, pending)
┃     ┃      k: #pc [ SSTORE ] ~> K_CELL:K
┃     ┃      pc: PC_CELL:Int
┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 10
┃        │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> K_CELL:K
┃        │   pc: PC_CELL:Int
┃        │   callDepth: CALLDEPTH_CELL:Int
┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  └─ 11 (leaf, pending)
┃        ┃      k: #pc [ SSTORE ] ~> K_CELL:K
┃        ┃      pc: PC_CELL:Int
┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 12
┃           │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> K_CELL:K
┃           │   pc: PC_CELL:Int
┃           │   callDepth: CALLDEPTH_CELL:Int
┃           │   statusCode: STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  └─ 13 (leaf, pending)
┃           ┃      k: #pc [ SSTORE ] ~> K_CELL:K
┃           ┃      pc: PC_CELL:Int
┃           ┃      callDepth: CALLDEPTH_CELL:Int
┃           ┃      statusCode: STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              ├─ 14
┃              │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> K_CELL:K
┃              │   pc: PC_CELL:Int
┃              │   callDepth: CALLDEPTH_CELL:Int
┃              │   statusCode: STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┃ (1 step)
┃              ┣━━┓
┃              ┃  │
┃              ┃  └─ 15 (leaf, pending)
┃              ┃      k: #pc [ SSTORE ] ~> K_CELL:K
┃              ┃      pc: PC_CELL:Int
┃              ┃      callDepth: CALLDEPTH_CELL:Int
┃              ┃      statusCode: STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┗━━┓
┃                 │
┃                 ├─ 16
┃                 │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> K_CELL:K
┃                 │   pc: PC_CELL:Int
┃                 │   callDepth: CALLDEPTH_CELL:Int
┃                 │   statusCode: STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┃ (1 step)
┃                 ┣━━┓
┃                 ┃  │
┃                 ┃  └─ 17 (leaf, pending)
┃                 ┃      k: #pc [ SSTORE ] ~> K_CELL:K
┃                 ┃      pc: PC_CELL:Int
┃                 ┃      callDepth: CALLDEPTH_CELL:Int
┃                 ┃      statusCode: STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┗━━┓
┃                    │
┃                    ├─ 18
┃                    │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> K_CELL:K
┃                    │   pc: PC_CELL:Int
┃                    │   callDepth: CALLDEPTH_CELL:Int
┃                    │   statusCode: STATUSCODE_CELL:StatusCode
┃                    ┃
┃                    ┃ (1 step)
┃                    ┣━━┓
┃                    ┃  │
┃                    ┃  └─ 19 (leaf, pending)
┃                    ┃      k: #pc [ SSTORE ] ~> K_CELL:K
┃                    ┃      pc: PC_CELL:Int
┃                    ┃      callDepth: CALLDEPTH_CELL:Int
┃                    ┃      statusCode: STATUSCODE_CELL:StatusCode
┃                    ┃
┃                    ┗━━┓
┃                       │
┃                       ├─ 20
┃                       │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> K_CELL:K
┃                       │   pc: PC_CELL:Int
┃                       │   callDepth: CALLDEPTH_CELL:Int
┃                       │   statusCode: STATUSCODE_CELL:StatusCode
┃                       ┃
┃                       ┃ (1 step)
┃                       ┣━━┓
┃                       ┃  │
┃                       ┃  └─ 21 (leaf, pending)
┃                       ┃      k: #pc [ SSTORE ] ~> K_CELL:K
┃                       ┃      pc: PC_CELL:Int
┃                       ┃      callDepth: CALLDEPTH_CELL:Int
┃                       ┃      statusCode: STATUSCODE_CELL:StatusCode
┃                       ┃
┃                       ┗━━┓
┃                          │
┃                          └─ 22 (leaf, pending)
┃                              k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> K_CELL:K
┃                              pc: PC_CELL:Int
┃                              callDepth: CALLDEPTH_CELL:Int
┃                              statusCode: STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     STATIC_CELL:Bool
   │
   ├─ 4
   │   k: #next [ SSTORE ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   └─ 6 (leaf, terminal)
       k: #halt ~> K_CELL:K
       pc: PC_CELL:Int
       callDepth: CALLDEPTH_CELL:Int
       statusCode: EVMC_STATIC_MODE_VIOLATION


┌─ 2 (root, leaf, target)
│   k: K_CELL:K
│   pc: FINAL_PC_CELL:Int
│   callDepth: FINAL_CALLDEPTH_CELL:Int
│   statusCode: FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SSTORE-2-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-5]: <kevm>
           <k>
             ( #next [ SSTORE ] ~> .K => SSTORE W0:Int W1:Int
             ~> #pc [ SSTORE ] )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : WS:WordStack ) ) => WS:WordStack )
                 </wordStack>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( notBool STATIC_CELL:Bool )
      [priority(20), label(BASIC-BLOCK-3-TO-5)]
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             ( #next [ SSTORE ] => #halt )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <statusCode>
                 ( _STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
                 <wordStack>
                   ( _W0 : ( _W1 : _WS ) )
                 </wordStack>
                 <static>
                   ( STATIC_CELL:Bool => true )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires STATIC_CELL:Bool
      [priority(20), label(BASIC-BLOCK-4-TO-6)]

endmodule
