
┌─ 1 (root, split, init)
│   k: #next [ CALLER ] ~> K_CELL:K
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
┃  │   k: #next [ CALLER ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 6 (leaf, terminal)
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
┃  ├─ 14
┃  │   k: #next [ CALLER ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (3 steps)
┃  └─ 8 (leaf, pending)
┃      k: #gas [ CALLER , CALLER ] ~> CALLER ~> #pc [ CALLER ] ~> K_CELL:K
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     USEGAS_CELL:Bool
┃  ┃     ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
┃  ┃     ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
┃  ┃     Gbase < SCHEDULE_CELL:Schedule > <=Gas GAS_CELL:Gas
┃  │
┃  ├─ 17
┃  │   k: #next [ CALLER ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  └─ 10 (leaf, pending)
┃      k: Gbase < SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ CALLER , CALLER ] ~> ...
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     USEGAS_CELL:Bool
   ┃     ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
   ┃     ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
   ┃     GAS_CELL:Gas <Gas Gbase < SCHEDULE_CELL:Schedule >
   │
   ├─ 18
   │   k: #next [ CALLER ] ~> K_CELL:K
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


┌─ 2 (root, leaf, target)
│   k: K_CELL:K
│   pc: FINAL_PC_CELL:Int
│   callDepth: FINAL_CALLDEPTH_CELL:Int
│   statusCode: FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-CALLER-0-SPEC
    
    
    rule [BASIC-BLOCK-3-TO-6]: <kevm>
           <k>
             ( #next [ CALLER ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-3-TO-6)]
    
    rule [BASIC-BLOCK-14-TO-8]: <kevm>
           <k>
             ( #next [ CALLER ] ~> .K => #gas [ CALLER , CALLER ]
             ~> CALLER
             ~> #pc [ CALLER ] )
             ~> _K_CELL
           </k>
           <useGas>
             USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
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
      requires ( ( notBool USEGAS_CELL:Bool )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 0 ) <Int 0 )
       andBool ( ( notBool 1023 <Int #sizeWordStack ( WS:WordStack , 0 ) )
               )))
       ensures #sizeWordStack ( WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-14-TO-8)]
    
    rule [BASIC-BLOCK-17-TO-10]: <kevm>
           <k>
             ( #next [ CALLER ] ~> .K => Gbase < SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ CALLER , CALLER ]
             ~> CALLER
             ~> #pc [ CALLER ] )
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
       andBool ( Gbase < SCHEDULE_CELL:Schedule > <=Gas GAS_CELL:Gas
               ))))
       ensures #sizeWordStack ( WS:WordStack , 0 ) <=Int 1023
      [priority(20), label(BASIC-BLOCK-17-TO-10)]
    
    rule [BASIC-BLOCK-18-TO-12]: <kevm>
           <k>
             ( #next [ CALLER ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-18-TO-12)]

endmodule
