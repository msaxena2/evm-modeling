
┌─ 1 (root, init)
│   k: #next [ JUMPI ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
│
│  (5 steps)
├─ 3
│   k: JUMP W0:Int ~> #pc [ JUMPI ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
┃
┃ (1 step)
┣━━┓
┃  │
┃  ├─ 4
┃  │   k: #endBasicBlock ~> #pc [ JUMPI ] ~> K_CELL:K
┃  │   pc: W0:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (1 step)
┃  ├─ 6
┃  │   k: #endBasicBlock ~> K_CELL:K
┃  │   pc: W0:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  ┊  constraint: true
┃  ┊  subst: ...
┃  └─ 2 (leaf, target)
┃      k: #endBasicBlock ~> K_CELL:K
┃      pc: FINAL_PC_CELL:Int
┃      callDepth: FINAL_CALLDEPTH_CELL:Int
┃      statusCode: FINAL_STATUSCODE_CELL:StatusCode
┃
┗━━┓
   │
   ├─ 5
   │   k: #end EVMC_BAD_JUMP_DESTINATION ~> #pc [ JUMPI ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   └─ 7 (leaf, terminal)
       k: #halt ~> K_CELL:K
       pc: PC_CELL:Int
       callDepth: CALLDEPTH_CELL:Int
       statusCode: EVMC_BAD_JUMP_DESTINATION




module SUMMARY-JUMPI-TRUE-2-SPEC
    
    
    rule [BASIC-BLOCK-1-TO-3]: <kevm>
           <k>
             ( #next [ JUMPI ] ~> .K => JUMP W0:Int
             ~> #pc [ JUMPI ] )
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires W1:Int =/=Int 0
      [priority(20), label(BASIC-BLOCK-1-TO-3)]
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             #endBasicBlock
             ~> ( #pc [ JUMPI ] ~> .K => .K )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _W1 =/=Int 0
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))
      [priority(20), label(BASIC-BLOCK-4-TO-6)]
    
    rule [BASIC-BLOCK-5-TO-7]: <kevm>
           <k>
             ( #end EVMC_BAD_JUMP_DESTINATION
             ~> #pc [ JUMPI ] => #halt ~> .K )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <statusCode>
                 ( _STATUSCODE_CELL => EVMC_BAD_JUMP_DESTINATION )
               </statusCode>
               <callState>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _W1 =/=Int 0
       andBool ( ( notBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes ) andBool 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ] ) )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-7)]

endmodule
