
┌─ 1 (root, init)
│   k: #next [ EXTCODECOPY ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
│
│  (7 steps)
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




module SUMMARY-EXTCODECOPY-4-SPEC
    
    
    rule [BASIC-BLOCK-1-TO-3]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => .K )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( _W2 : ( W3:Int : WS:WordStack ) ) ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   ( LOCALMEM_CELL:Bytes => LOCALMEM_CELL:Bytes [ W1:Int := #padToWidth ( W3:Int , b"" ) ] )
                 </localMem>
                 <pc>
                   ( PC_CELL:Int => ( PC_CELL:Int +Int 1 ) )
                 </pc>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( ACCESSEDACCOUNTS_CELL:Set => ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( W0:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      [priority(20), label(BASIC-BLOCK-1-TO-3)]

endmodule
