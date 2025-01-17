
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
┃  │  (6 steps)
┃  ├─ 6
┃  │   k: K_CELL:K
┃  │   pc: ( PC_CELL:Int +Int 1 )
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  ┊  constraint:
┃  ┊      ( notBool <acctID>
  ID_CELL:Int
</acctID> in_keys ( DotAccountVar:AccountCellMap ) )
┃  ┊  subst: ...
┃  └─ 2 (leaf, target)
┃      k: K_CELL:K
┃      pc: FINAL_PC_CELL:Int
┃      callDepth: FINAL_CALLDEPTH_CELL:Int
┃      statusCode: FINAL_STATUSCODE_CELL:StatusCode
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
   └─ 5 (leaf, terminal)
       k: #halt ~> K_CELL:K
       pc: PC_CELL:Int
       callDepth: CALLDEPTH_CELL:Int
       statusCode: EVMC_STATIC_MODE_VIOLATION




module SUMMARY-SSTORE-2-SPEC
    
    
    rule [BASIC-BLOCK-4-TO-5]: <kevm>
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
                 <id>
                   ID_CELL:Int
                 </id>
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
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( STATIC_CELL:Bool
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
               ))
      [priority(20), label(BASIC-BLOCK-4-TO-5)]
    
    rule [BASIC-BLOCK-3-TO-6]: <kevm>
           <k>
             ( #next [ SSTORE ] ~> .K => .K )
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
                   ( ( W0:Int : ( W1:Int : WS:WordStack ) ) => WS:WordStack )
                 </wordStack>
                 <pc>
                   ( PC_CELL:Int => ( PC_CELL:Int +Int 1 ) )
                 </pc>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
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
                     ( STORAGE_CELL:Map => STORAGE_CELL:Map [ W0:Int <- W1:Int ] )
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
      requires ( ( notBool STATIC_CELL:Bool )
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
               ))
      [priority(20), label(BASIC-BLOCK-3-TO-6)]

endmodule
