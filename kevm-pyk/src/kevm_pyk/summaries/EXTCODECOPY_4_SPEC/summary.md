
┌─ 1 (root, split, init)
│   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 33
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (3 steps)
┃  └─ 5 (leaf, pending)
┃      k: #gas [ EXTCODECOPY , EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:I ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 47
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 15 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int )
┃  │
┃  ├─ 61
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (15 steps)
┃  └─ 21 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int )
┃  │
┃  ├─ 86
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 19 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 87
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 20 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int )
┃  │
┃  ├─ 94
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 25 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 95
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 26 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int )
┃  │
┃  ├─ 102
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 30 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 103
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 31 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 104
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (11 steps)
┃  └─ 27 (leaf, pending)
┃      k: #access [ EXTCODECOPY , EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
   ┃     Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
   │
   ├─ 105
   │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (11 steps)
   └─ 28 (leaf, pending)
       k: #access [ EXTCODECOPY , EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W ...
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-EXTCODECOPY-4-SPEC
    
    
    rule [BASIC-BLOCK-33-TO-5]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #gas [ EXTCODECOPY , EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int ]
             ~> EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int
             ~> #pc [ EXTCODECOPY ] )
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( notBool _USEGAS_CELL:Bool )
      [priority(20), label(BASIC-BLOCK-33-TO-5)]
    
    rule [BASIC-BLOCK-47-TO-15]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] => #halt )
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
                   ( ( __W0 : ( _W1:Int : ( __W2 : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
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
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))
      [priority(20), label(BASIC-BLOCK-47-TO-15)]
    
    rule [BASIC-BLOCK-61-TO-21]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] => #halt )
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
                   ( ( __W0 : ( _W1:Int : ( __W2 : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
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
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int )
               )))
      [priority(20), label(BASIC-BLOCK-61-TO-21)]
    
    rule [BASIC-BLOCK-86-TO-19]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int
             ~> #pc [ EXTCODECOPY ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int )
               )))))
      [priority(20), label(BASIC-BLOCK-86-TO-19)]
    
    rule [BASIC-BLOCK-87-TO-20]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int
             ~> #pc [ EXTCODECOPY ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               )))))
      [priority(20), label(BASIC-BLOCK-87-TO-20)]
    
    rule [BASIC-BLOCK-94-TO-25]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int
             ~> #pc [ EXTCODECOPY ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int )
               )))))
      [priority(20), label(BASIC-BLOCK-94-TO-25)]
    
    rule [BASIC-BLOCK-95-TO-26]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int
             ~> #pc [ EXTCODECOPY ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               )))))
      [priority(20), label(BASIC-BLOCK-95-TO-26)]
    
    rule [BASIC-BLOCK-102-TO-30]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int
             ~> #pc [ EXTCODECOPY ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int )
               )))))
      [priority(20), label(BASIC-BLOCK-102-TO-30)]
    
    rule [BASIC-BLOCK-103-TO-31]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int
             ~> #pc [ EXTCODECOPY ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
                 </memoryUsed>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               )))))
      [priority(20), label(BASIC-BLOCK-103-TO-31)]
    
    rule [BASIC-BLOCK-104-TO-27]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #access [ EXTCODECOPY , EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int ]
             ~> EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int
             ~> #pc [ EXTCODECOPY ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
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
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))
      [priority(20), label(BASIC-BLOCK-104-TO-27)]
    
    rule [BASIC-BLOCK-105-TO-28]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #access [ EXTCODECOPY , EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int ]
             ~> EXTCODECOPY ( _W0:Int modInt pow160 ) _W1:Int _W2:Int _W3:Int
             ~> #pc [ EXTCODECOPY ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : _WS:WordStack ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) )
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
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextcodecopy ( _SCHEDULE_CELL:Schedule , _W3:Int ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W1:Int , _W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))
      [priority(20), label(BASIC-BLOCK-105-TO-28)]

endmodule
