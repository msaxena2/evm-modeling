
┌─ 1 (root, split, init)
│   k: #next [ MCOPY ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 17
┃  │   k: #next [ MCOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (6 steps)
┃  ├─ 14
┃  │   k: _K_CELL:K
┃  │   pc: ( _PC_CELL:Int +Int 1 )
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  ┊  constraint: true
┃  ┊  subst: ...
┃  └─ 2 (leaf, target)
┃      k: _K_CELL:K
┃      pc: ?_FINAL_PC_CELL:Int
┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 23
┃  │   k: #next [ MCOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 12 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     ( Gverylow < _SCHEDULE_CELL:Schedule > +Int ( Gcopy < _SCHEDULE_CELL:Schedule > *Int ( _W2:Int up/Int 32 ) ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 26
┃  │   k: #next [ MCOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (14 steps)
┃  ├─ 15
┃  │   k: _K_CELL:K
┃  │   pc: ( _PC_CELL:Int +Int 1 )
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  ┊  constraint: true
┃  ┊  subst: ...
┃  └─ 2 (leaf, target)
┃      k: _K_CELL:K
┃      pc: ?_FINAL_PC_CELL:Int
┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
   ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas ( Gverylow < _SCHEDULE_CELL:Schedule > +Int ( Gcopy < _SCHEDULE_CELL:Schedule > *Int ( _W2:Int up/Int 32 ) ) )
   │
   ├─ 27
   │   k: #next [ MCOPY ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (15 steps)
   └─ 13 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS




module SUMMARY-MCOPY-3-SPEC
    
    
    rule [BASIC-BLOCK-17-TO-14]: <kevm>
           <k>
             ( #next [ MCOPY ] ~> .K => .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : _WS:WordStack ) ) ) => _WS:WordStack )
                 </wordStack>
                 <localMem>
                   ( _LOCALMEM_CELL:Bytes => _LOCALMEM_CELL:Bytes [ _W0:Int := #range ( _LOCALMEM_CELL:Bytes , _W1:Int , _W2:Int ) ] )
                 </localMem>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( notBool _USEGAS_CELL:Bool )
      [priority(20), label(BASIC-BLOCK-17-TO-14)]
    
    rule [BASIC-BLOCK-23-TO-12]: <kevm>
           <k>
             ( #next [ MCOPY ] => #halt )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : _WS:WordStack ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))
      [priority(20), label(BASIC-BLOCK-23-TO-12)]
    
    rule [BASIC-BLOCK-26-TO-15]: <kevm>
           <k>
             ( #next [ MCOPY ] ~> .K => .K )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : _WS:WordStack ) ) ) => _WS:WordStack )
                 </wordStack>
                 <localMem>
                   ( _LOCALMEM_CELL:Bytes => _LOCALMEM_CELL:Bytes [ _W0:Int := #range ( _LOCALMEM_CELL:Bytes , _W1:Int , _W2:Int ) ] )
                 </localMem>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas ( Gverylow < _SCHEDULE_CELL:Schedule > +Int ( Gcopy < _SCHEDULE_CELL:Schedule > *Int ( _W2:Int up/Int 32 ) ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( Gverylow < _SCHEDULE_CELL:Schedule > +Int ( Gcopy < _SCHEDULE_CELL:Schedule > *Int ( _W2:Int up/Int 32 ) ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))
      [priority(20), label(BASIC-BLOCK-26-TO-15)]
    
    rule [BASIC-BLOCK-27-TO-13]: <kevm>
           <k>
             ( #next [ MCOPY ] => #halt )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : _WS:WordStack ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , maxInt ( _W0:Int , _W1:Int ) , _W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas ( Gverylow < _SCHEDULE_CELL:Schedule > +Int ( Gcopy < _SCHEDULE_CELL:Schedule > *Int ( _W2:Int up/Int 32 ) ) )
               )))
      [priority(20), label(BASIC-BLOCK-27-TO-13)]

endmodule
