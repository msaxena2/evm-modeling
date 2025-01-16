
┌─ 1 (root, split, init)
│   k: #next [ SELFBALANCE ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     1023 <Int #sizeWordStack ( WS:WordStack , 0 )
┃  │
┃  ├─ 3
┃  │   k: #next [ SELFBALANCE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 5 (leaf, terminal)
┃      k: #halt ~> K_CELL:K
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
   ┃     ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
   │
   ├─ 4
   │   k: #next [ SELFBALANCE ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   │
   │  (7 steps)
   ├─ 6
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




module SUMMARY-SELFBALANCE-0-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-5]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] => #halt )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <statusCode>
                 ( _STATUSCODE_CELL => EVMC_STACK_OVERFLOW )
               </statusCode>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
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
      requires ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( 1023 <Int #sizeWordStack ( WS:WordStack , 0 )
               ))
      [priority(20), label(BASIC-BLOCK-3-TO-5)]
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             ( #next [ SELFBALANCE ] ~> .K => .K )
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
                   ( WS:WordStack => ( BALANCE_CELL:Int : WS:WordStack ) )
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
                   <balance>
                     BALANCE_CELL:Int
                   </balance>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
               )))
       ensures #sizeWordStack ( WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-4-TO-6)]

endmodule
