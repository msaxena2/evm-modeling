
┌─ 1 (root, init)
│   k: #next [ UNDEFINED ( _W:Int ) ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
│
│  (6 steps)
└─ 3 (leaf, terminal)
    k: #halt ~> _K_CELL:K
    pc: _PC_CELL:Int
    callDepth: _CALLDEPTH_CELL:Int
    statusCode: EVMC_UNDEFINED_INSTRUCTION


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-UNDEFINED(-0-SPEC
    
    
    rule [BASIC-BLOCK-1-TO-3]: <kevm>
           <k>
             ( #next [ UNDEFINED ( __W ) ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_UNDEFINED_INSTRUCTION )
               </statusCode>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      [priority(20), label(BASIC-BLOCK-1-TO-3)]

endmodule
