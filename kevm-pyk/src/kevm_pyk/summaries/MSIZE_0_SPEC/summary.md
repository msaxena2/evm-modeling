
┌─ 1 (root, split, init)
│   k: #next [ MSIZE ] ~> K_CELL:K
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
┃  │   k: #next [ MSIZE ] ~> K_CELL:K
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
   │   k: #next [ MSIZE ] ~> K_CELL:K
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
   ┊  constraint: true
   ┊  subst: ...
   └─ 2 (leaf, target)
       k: K_CELL:K
       pc: FINAL_PC_CELL:Int
       callDepth: FINAL_CALLDEPTH_CELL:Int
       statusCode: FINAL_STATUSCODE_CELL:StatusCode




module SUMMARY-MSIZE-0-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-5]: <kevm>
           <k>
             ( #next [ MSIZE ] => #halt )
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
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires 1023 <Int #sizeWordStack ( WS:WordStack , 0 )
      [priority(20), label(BASIC-BLOCK-3-TO-5)]
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             ( #next [ MSIZE ] ~> .K => .K )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( WS:WordStack => ( chop ( ( 32 *Int MEMORYUSED_CELL:Int ) ) : WS:WordStack ) )
                 </wordStack>
                 <pc>
                   ( PC_CELL:Int => ( PC_CELL:Int +Int 1 ) )
                 </pc>
                 <memoryUsed>
                   MEMORYUSED_CELL:Int
                 </memoryUsed>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
               ))
       ensures #sizeWordStack ( WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-4-TO-6)]

endmodule
