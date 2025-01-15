
┌─ 1 (root, split, init)
│   k: #next [ LOG ( 3 ) ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WS:WordStack , 3 ) <Int 5
┃  │
┃  ├─ 3
┃  │   k: #next [ LOG ( 3 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 10 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_UNDERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _STATIC_CELL:Bool
┃  ┃     5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
┃  │
┃  ├─ 5
┃  │   k: #next [ LOG ( 3 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 9 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STATIC_MODE_VIOLATION
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  ┃     5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
┃  │
┃  ├─ 28
┃  │   k: #next [ LOG ( 3 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 11
┃  │   k: LOG ( 3 ) _W0:Int _W1:Int ~> #pc [ LOG ( 3 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 12
┃  ┃  │   k: #pc [ LOG ( 3 ) ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (1 step)
┃  ┃  ├─ 25
┃  ┃  │   k: _K_CELL:K
┃  ┃  │   pc: ( _PC_CELL:Int +Int 1 )
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  ┊  constraint: true
┃  ┃  ┊  subst: ...
┃  ┃  └─ 2 (leaf, target)
┃  ┃      k: _K_CELL:K
┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 13 (stuck, leaf)
┃         k: LOG ( 3 ) _W0:Int _W1:Int ~> #pc [ LOG ( 3 ) ] ~> _K_CELL:K
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
┃  ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 34
┃  │   k: #next [ LOG ( 3 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 23 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int _W1:Int ) ) +Int ( 3 *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 37
┃  │   k: #next [ LOG ( 3 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (12 steps)
┃  ├─ 20
┃  │   k: LOG ( 3 ) _W0:Int _W1:Int ~> #pc [ LOG ( 3 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 21
┃  ┃  │   k: #pc [ LOG ( 3 ) ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (1 step)
┃  ┃  ├─ 26
┃  ┃  │   k: _K_CELL:K
┃  ┃  │   pc: ( _PC_CELL:Int +Int 1 )
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  ┊  constraint: true
┃  ┃  ┊  subst: ...
┃  ┃  └─ 2 (leaf, target)
┃  ┃      k: _K_CELL:K
┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 22 (stuck, leaf)
┃         k: LOG ( 3 ) _W0:Int _W1:Int ~> #pc [ LOG ( 3 ) ] ~> _K_CELL:K
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     ( notBool _STATIC_CELL:Bool )
   ┃     5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
   ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
   ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int _W1:Int ) ) +Int ( 3 *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
   │
   ├─ 38
   │   k: #next [ LOG ( 3 ) ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (15 steps)
   └─ 24 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS




module SUMMARY-LOG-3-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-9]: <kevm>
           <k>
             ( #next [ LOG ( 3 ) ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
                 <wordStack>
                   ( __W0 : ( __W1 : ( __W2 : _WS:WordStack ) ) )
                 </wordStack>
                 <static>
                   ( _STATIC_CELL:Bool => true )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _STATIC_CELL:Bool
       andBool ( 5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-9)]
    
    rule [BASIC-BLOCK-3-TO-10]: <kevm>
           <k>
             ( #next [ LOG ( 3 ) ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STACK_UNDERFLOW )
               </statusCode>
               <callState>
                 <wordStack>
                   ( __W0 : ( __W1 : ( __W2 : _WS:WordStack ) ) )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires #sizeWordStack ( _WS:WordStack , 3 ) <Int 5
      [priority(20), label(BASIC-BLOCK-3-TO-10)]
    
    rule [BASIC-BLOCK-12-TO-25]: <kevm>
           <k>
             ( #pc [ LOG ( 3 ) ] ~> .K => .K )
             ~> __K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ACCT:Int
                 </id>
                 <wordStack>
                   #drop ( 1 , #drop ( 1 , _WS:WordStack ) )
                 </wordStack>
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               <substate>
                 <log>
                   __LOG_CELL ListItem ( { ACCT:Int | ListItem ( __W2 ) WordStack2List ( #take ( 2 , _WS:WordStack ) ) | #range ( _LOCALMEM_CELL:Bytes , __W0 , __W1 ) } )
                 </log>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __ID_CELL ==K ACCT:Int
       andBool ( ( notBool __STATIC_CELL )
       andBool ( ( notBool __USEGAS_CELL )
       andBool ( 3 <=Int #sizeWordStack ( _WS:WordStack , 1 )
       andBool ( 5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
               )))))
      [priority(20), label(BASIC-BLOCK-12-TO-25)]
    
    rule [BASIC-BLOCK-21-TO-26]: <kevm>
           <k>
             ( #pc [ LOG ( 3 ) ] ~> .K => .K )
             ~> __K_CELL
           </k>
           <schedule>
             _SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             true
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ACCT:Int
                 </id>
                 <wordStack>
                   #drop ( 1 , #drop ( 1 , _WS:WordStack ) )
                 </wordStack>
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int _W1:Int ) ) +Int ( 3 *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int )
                 </memoryUsed>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               <substate>
                 <log>
                   __LOG_CELL ListItem ( { ACCT:Int | ListItem ( __W2 ) WordStack2List ( #take ( 2 , _WS:WordStack ) ) | #range ( _LOCALMEM_CELL:Bytes , _W0:Int , _W1:Int ) } )
                 </log>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( __ID_CELL ==K ACCT:Int
       andBool ( ( notBool __STATIC_CELL )
       andBool ( 3 <=Int #sizeWordStack ( _WS:WordStack , 1 )
       andBool ( 5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int _W1:Int ) ) +Int ( 3 *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))))))
      [priority(20), label(BASIC-BLOCK-21-TO-26)]
    
    rule [BASIC-BLOCK-28-TO-11]: <kevm>
           <k>
             ( #next [ LOG ( 3 ) ] ~> .K => LOG ( 3 ) _W0:Int _W1:Int
             ~> #pc [ LOG ( 3 ) ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int => _W2:Int ) : ( ( _W1:Int : ( _W2:Int : _WS:WordStack ) ) => _WS:WordStack ) )
                 </wordStack>
                 <static>
                   ( _STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _STATIC_CELL:Bool )
       andBool ( ( notBool _USEGAS_CELL:Bool )
       andBool ( 5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
               )))
      [priority(20), label(BASIC-BLOCK-28-TO-11)]
    
    rule [BASIC-BLOCK-34-TO-23]: <kevm>
           <k>
             ( #next [ LOG ( 3 ) ] => #halt )
             ~> __K_CELL
           </k>
           <schedule>
             _SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             ( _USEGAS_CELL:Bool => true )
           </useGas>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_OUT_OF_GAS )
               </statusCode>
               <callState>
                 <wordStack>
                   ( ( _W0:Int => _W2:Int ) : ( ( _W1:Int : ( _W2:Int : _WS:WordStack ) ) => _WS:WordStack ) )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) )
                 </memoryUsed>
                 <static>
                   ( _STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( notBool _STATIC_CELL:Bool )
       andBool ( 5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))
      [priority(20), label(BASIC-BLOCK-34-TO-23)]
    
    rule [BASIC-BLOCK-37-TO-20]: <kevm>
           <k>
             ( #next [ LOG ( 3 ) ] ~> .K => LOG ( 3 ) _W0:Int _W1:Int
             ~> #pc [ LOG ( 3 ) ] )
             ~> __K_CELL
           </k>
           <schedule>
             _SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             ( _USEGAS_CELL:Bool => true )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int => _W2:Int ) : ( ( _W1:Int : ( _W2:Int : _WS:WordStack ) ) => _WS:WordStack ) )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int _W1:Int ) ) +Int ( 3 *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) )
                 </memoryUsed>
                 <static>
                   ( _STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( notBool _STATIC_CELL:Bool )
       andBool ( 5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int _W1:Int ) ) +Int ( 3 *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))))
      [priority(20), label(BASIC-BLOCK-37-TO-20)]
    
    rule [BASIC-BLOCK-38-TO-24]: <kevm>
           <k>
             ( #next [ LOG ( 3 ) ] => #halt )
             ~> __K_CELL
           </k>
           <schedule>
             _SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             ( _USEGAS_CELL:Bool => true )
           </useGas>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_OUT_OF_GAS )
               </statusCode>
               <callState>
                 <wordStack>
                   ( ( _W0:Int => _W2:Int ) : ( ( _W1:Int : ( _W2:Int : _WS:WordStack ) ) => _WS:WordStack ) )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) )
                 </memoryUsed>
                 <static>
                   ( _STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( notBool _STATIC_CELL:Bool )
       andBool ( 5 <=Int #sizeWordStack ( _WS:WordStack , 3 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , _W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int _W1:Int ) ) +Int ( 3 *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
               )))))
      [priority(20), label(BASIC-BLOCK-38-TO-24)]

endmodule
