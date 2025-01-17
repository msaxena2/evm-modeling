
┌─ 1 (root, split, init)
│   k: #next [ LOG ( 0 ) ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     STATIC_CELL:Bool
┃  │
┃  ├─ 4
┃  │   k: #next [ LOG ( 0 ) ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 8 (leaf, terminal)
┃      k: #halt ~> K_CELL:K
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STATIC_MODE_VIOLATION
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  ┃     ( notBool USEGAS_CELL:Bool )
┃  │
┃  ├─ 20
┃  │   k: #next [ LOG ( 0 ) ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (6 steps)
┃  ├─ 17
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
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  ┃     GAS_CELL:Gas <Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 26
┃  │   k: #next [ LOG ( 0 ) ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 15 (leaf, terminal)
┃      k: #halt ~> K_CELL:K
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     USEGAS_CELL:Bool
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  ┃     ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) <=Gas GAS_CELL:Gas
┃  ┃     ( Glog < SCHEDULE_CELL:Schedule > +Int ( Glogdata < SCHEDULE_CELL:Schedule > *Int W1:Int ) ) <=Gas GAS_CELL:Gas -Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 29
┃  │   k: #next [ LOG ( 0 ) ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (14 steps)
┃  ├─ 18
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
   ┃     ( notBool STATIC_CELL:Bool )
   ┃     ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) <=Gas GAS_CELL:Gas
   ┃     GAS_CELL:Gas -Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) <Gas ( Glog < SCHEDULE_CELL:Schedule > +Int ( Glogdata < SCHEDULE_CELL:Schedule > *Int W1:Int ) )
   │
   ├─ 30
   │   k: #next [ LOG ( 0 ) ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   │
   │  (15 steps)
   └─ 16 (leaf, terminal)
       k: #halt ~> K_CELL:K
       pc: PC_CELL:Int
       callDepth: CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS




module SUMMARY-LOG-2-SPEC
    
    
    rule [BASIC-BLOCK-4-TO-8]: <kevm>
           <k>
             ( #next [ LOG ( 0 ) ] => #halt )
             ~> _K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( _STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
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
             ...
           </ethereum>
           ...
         </kevm>
      requires STATIC_CELL:Bool
      [priority(20), label(BASIC-BLOCK-4-TO-8)]
    
    rule [BASIC-BLOCK-20-TO-17]: <kevm>
           <k>
             ( #next [ LOG ( 0 ) ] ~> .K => .K )
             ~> _K_CELL
           </k>
           <useGas>
             ( USEGAS_CELL:Bool => false )
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
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <pc>
                   ( PC_CELL:Int => ( PC_CELL:Int +Int 1 ) )
                 </pc>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               <substate>
                 <log>
                   ( LOG_CELL:List => LOG_CELL:List ListItem ( { ID_CELL:Int | .List | #range ( LOCALMEM_CELL:Bytes , W0:Int , W1:Int ) } ) )
                 </log>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool STATIC_CELL:Bool )
       andBool ( ( notBool USEGAS_CELL:Bool )
               ))
      [priority(20), label(BASIC-BLOCK-20-TO-17)]
    
    rule [BASIC-BLOCK-26-TO-15]: <kevm>
           <k>
             ( #next [ LOG ( 0 ) ] => #halt )
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
                   ( ( W0:Int : ( W1:Int : WS:WordStack ) ) => WS:WordStack )
                 </wordStack>
                 <gas>
                   GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( MEMORYUSED_CELL:Int => #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) )
                 </memoryUsed>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( USEGAS_CELL:Bool
       andBool ( ( notBool STATIC_CELL:Bool )
       andBool ( GAS_CELL:Gas <Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) )
               )))
      [priority(20), label(BASIC-BLOCK-26-TO-15)]
    
    rule [BASIC-BLOCK-29-TO-18]: <kevm>
           <k>
             ( #next [ LOG ( 0 ) ] ~> .K => .K )
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : WS:WordStack ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <pc>
                   ( PC_CELL:Int => ( PC_CELL:Int +Int 1 ) )
                 </pc>
                 <gas>
                   ( GAS_CELL:Gas => GAS_CELL:Gas -Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) -Gas ( Glog < SCHEDULE_CELL:Schedule > +Int ( Glogdata < SCHEDULE_CELL:Schedule > *Int W1:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( MEMORYUSED_CELL:Int => #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) )
                 </memoryUsed>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               <substate>
                 <log>
                   ( LOG_CELL:List => LOG_CELL:List ListItem ( { ID_CELL:Int | .List | #range ( LOCALMEM_CELL:Bytes , W0:Int , W1:Int ) } ) )
                 </log>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( USEGAS_CELL:Bool
       andBool ( ( notBool STATIC_CELL:Bool )
       andBool ( ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) <=Gas GAS_CELL:Gas
       andBool ( ( Glog < SCHEDULE_CELL:Schedule > +Int ( Glogdata < SCHEDULE_CELL:Schedule > *Int W1:Int ) ) <=Gas GAS_CELL:Gas -Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) )
               ))))
      [priority(20), label(BASIC-BLOCK-29-TO-18)]
    
    rule [BASIC-BLOCK-30-TO-16]: <kevm>
           <k>
             ( #next [ LOG ( 0 ) ] => #halt )
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
                   ( ( W0:Int : ( W1:Int : WS:WordStack ) ) => WS:WordStack )
                 </wordStack>
                 <gas>
                   ( GAS_CELL:Gas => GAS_CELL:Gas -Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( MEMORYUSED_CELL:Int => #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) )
                 </memoryUsed>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( USEGAS_CELL:Bool
       andBool ( ( notBool STATIC_CELL:Bool )
       andBool ( ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) <=Gas GAS_CELL:Gas
       andBool ( GAS_CELL:Gas -Gas ( Cmem ( SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( SCHEDULE_CELL:Schedule , MEMORYUSED_CELL:Int ) ) <Gas ( Glog < SCHEDULE_CELL:Schedule > +Int ( Glogdata < SCHEDULE_CELL:Schedule > *Int W1:Int ) )
               ))))
      [priority(20), label(BASIC-BLOCK-30-TO-16)]

endmodule
