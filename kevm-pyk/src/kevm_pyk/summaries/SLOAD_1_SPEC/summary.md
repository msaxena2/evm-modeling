
┌─ 1 (root, init)
│   k: #next [ SLOAD ] ~> K_CELL:K
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
┊  constraint:
┊      ( notBool <acctID>
  ID_CELL:Int
</acctID> in_keys ( DotAccountVar:AccountCellMap ) )
┊  subst: ...
└─ 2 (leaf, target)
    k: K_CELL:K
    pc: FINAL_PC_CELL:Int
    callDepth: FINAL_CALLDEPTH_CELL:Int
    statusCode: FINAL_STATUSCODE_CELL:StatusCode




module SUMMARY-SLOAD-1-SPEC
    
    
    rule [BASIC-BLOCK-1-TO-3]: <kevm>
           <k>
             ( #next [ SLOAD ] ~> .K => .K )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int => #lookup ( STORAGE_CELL:Map , W0:Int ) ) : _WS )
                 </wordStack>
                 <pc>
                   ( PC_CELL:Int => ( PC_CELL:Int +Int 1 ) )
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <storage>
                     STORAGE_CELL:Map
                   </storage>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( notBool <acctID>
        ID_CELL:Int
      </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
      [priority(20), label(BASIC-BLOCK-1-TO-3)]

endmodule
