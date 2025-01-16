
┌─ 1 (root, init)
│   k: #next [ POP ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
│
│  (6 steps)
├─ 3
│   k: K_CELL:K
│   pc: ( PC_CELL:Int +Int 1 )
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
│
┊  constraint: true
┊  subst: ...
└─ 2 (leaf, target)
    k: K_CELL:K
    pc: FINAL_PC_CELL:Int
    callDepth: FINAL_CALLDEPTH_CELL:Int
    statusCode: FINAL_STATUSCODE_CELL:StatusCode




module SUMMARY-POP-1-SPEC
    
    
    rule [BASIC-BLOCK-1-TO-3]: <kevm>
           <k>
             ( #next [ POP ] ~> .K => .K )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0 : WS:WordStack ) => WS:WordStack )
                 </wordStack>
                 <pc>
                   ( PC_CELL:Int => ( PC_CELL:Int +Int 1 ) )
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      [priority(20), label(BASIC-BLOCK-1-TO-3)]

endmodule
