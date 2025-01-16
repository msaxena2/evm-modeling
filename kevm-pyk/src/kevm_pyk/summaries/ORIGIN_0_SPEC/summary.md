
┌─ 1 (root, split, init)
│   k: #next [ ORIGIN ] ~> K_CELL:K
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
┃  │   k: #next [ ORIGIN ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 8 (leaf, terminal)
┃      k: #halt ~> K_CELL:K
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool USEGAS_CELL:Bool )
┃  ┃     ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
┃  │
┃  ├─ 16
┃  │   k: #next [ ORIGIN ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 13
┃  │   k: K_CELL:K
┃  │   pc: ( PC_CELL:Int +Int 1 )
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  ┊  constraint: true
┃  ┊  subst: ...
┃  └─ 2 (leaf, target)
┃      k: K_CELL:K
┃      pc: FINAL_PC_CELL:Int
┃      callDepth: FINAL_CALLDEPTH_CELL:Int
┃      statusCode: FINAL_STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     USEGAS_CELL:Bool
┃  ┃     ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
┃  ┃     Gbase < SCHEDULE_CELL:Schedule > <=Gas GAS_CELL:Gas
┃  │
┃  ├─ 19
┃  │   k: #next [ ORIGIN ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (12 steps)
┃  ├─ 14
┃  │   k: K_CELL:K
┃  │   pc: ( PC_CELL:Int +Int 1 )
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  ┊  constraint: true
┃  ┊  subst: ...
┃  └─ 2 (leaf, target)
┃      k: K_CELL:K
┃      pc: FINAL_PC_CELL:Int
┃      callDepth: FINAL_CALLDEPTH_CELL:Int
┃      statusCode: FINAL_STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     USEGAS_CELL:Bool
   ┃     ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
   ┃     ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
   ┃     GAS_CELL:Gas <Gas Gbase < SCHEDULE_CELL:Schedule >
   │
   ├─ 20
   │   k: #next [ ORIGIN ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   │
   │  (12 steps)
   └─ 12 (leaf, terminal)
       k: #halt ~> K_CELL:K
       pc: PC_CELL:Int
       callDepth: CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS




module SUMMARY-ORIGIN-0-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ ORIGIN ] => #halt )
             ~> _K_CELL
           </k>
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
      [priority(20), label(BASIC-BLOCK-3-TO-8)]
    
    rule [BASIC-BLOCK-16-TO-13]: <kevm>
           <k>
             ( #next [ ORIGIN ] ~> .K => .K )
             ~> _K_CELL
           </k>
           <useGas>
             ( USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( WS:WordStack => ( ORIGIN_CELL:Int : WS:WordStack ) )
                 </wordStack>
                 <pc>
                   ( PC_CELL:Int => ( PC_CELL:Int +Int 1 ) )
                 </pc>
                 ...
               </callState>
               <origin>
                 ORIGIN_CELL:Int
               </origin>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool USEGAS_CELL:Bool )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
               )))
       ensures #sizeWordStack ( WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-16-TO-13)]
    
    rule [BASIC-BLOCK-19-TO-14]: <kevm>
           <k>
             ( #next [ ORIGIN ] ~> .K => .K )
             ~> _K_CELL
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             ( USEGAS_CELL:Bool => true )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( WS:WordStack => ( ORIGIN_CELL:Int : WS:WordStack ) )
                 </wordStack>
                 <pc>
                   ( PC_CELL:Int => ( PC_CELL:Int +Int 1 ) )
                 </pc>
                 <gas>
                   ( GAS_CELL:Gas => GAS_CELL:Gas -Gas Gbase < SCHEDULE_CELL:Schedule > )
                 </gas>
                 ...
               </callState>
               <origin>
                 ORIGIN_CELL:Int
               </origin>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( USEGAS_CELL:Bool
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
       andBool ( Gbase < SCHEDULE_CELL:Schedule > <=Gas GAS_CELL:Gas
               ))))
       ensures #sizeWordStack ( WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-19-TO-14)]
    
    rule [BASIC-BLOCK-20-TO-12]: <kevm>
           <k>
             ( #next [ ORIGIN ] => #halt )
             ~> _K_CELL
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             ( USEGAS_CELL:Bool => true )
           </useGas>
           <ethereum>
             <evm>
               <statusCode>
                 ( _STATUSCODE_CELL => EVMC_OUT_OF_GAS )
               </statusCode>
               <callState>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <gas>
                   GAS_CELL:Gas
                 </gas>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( USEGAS_CELL:Bool
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
       andBool ( GAS_CELL:Gas <Gas Gbase < SCHEDULE_CELL:Schedule >
               ))))
       ensures #sizeWordStack ( WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-20-TO-12)]

endmodule
