
┌─ 1 (root, split, init)
│   k: #next [ TLOAD ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 31
┃  │   k: #next [ TLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 6
┃  │   k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 7 (leaf, pending)
┃  ┃      k: #lookup ( TSTORAGE:Map , _W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 8
┃     │   k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 12 (leaf, pending)
┃     ┃      k: #lookup ( TSTORAGE0:Map , _W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 13
┃        │   k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  └─ 17 (leaf, pending)
┃        ┃      k: #lookup ( TSTORAGE1:Map , _W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
┃        ┃      pc: _PC_CELL:Int
┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 18
┃           │   k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  └─ 21 (leaf, pending)
┃           ┃      k: #lookup ( TSTORAGE2:Map , _W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
┃           ┃      pc: _PC_CELL:Int
┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              ├─ 22
┃              │   k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃              │   pc: _PC_CELL:Int
┃              │   callDepth: _CALLDEPTH_CELL:Int
┃              │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┃ (1 step)
┃              ┣━━┓
┃              ┃  │
┃              ┃  └─ 26 (leaf, pending)
┃              ┃      k: #lookup ( TSTORAGE3:Map , _W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
┃              ┃      pc: _PC_CELL:Int
┃              ┃      callDepth: _CALLDEPTH_CELL:Int
┃              ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┗━━┓
┃                 │
┃                 └─ 27 (leaf, pending)
┃                     k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃                     pc: _PC_CELL:Int
┃                     callDepth: _CALLDEPTH_CELL:Int
┃                     statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Gwarmstorageread < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 34
┃  │   k: #next [ TLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (9 steps)
┃  ├─ 14
┃  │   k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 15 (leaf, pending)
┃  ┃      k: #lookup ( TSTORAGE:Map , _W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 16
┃     │   k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 19 (leaf, pending)
┃     ┃      k: #lookup ( TSTORAGE0:Map , _W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 20
┃        │   k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  └─ 24 (leaf, pending)
┃        ┃      k: #lookup ( TSTORAGE1:Map , _W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
┃        ┃      pc: _PC_CELL:Int
┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 25
┃           │   k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  └─ 28 (leaf, pending)
┃           ┃      k: #lookup ( TSTORAGE2:Map , _W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
┃           ┃      pc: _PC_CELL:Int
┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              └─ 29 (leaf, pending)
┃                  k: TLOAD _W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
┃                  pc: _PC_CELL:Int
┃                  callDepth: _CALLDEPTH_CELL:Int
┃                  statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     _GAS_CELL:Gas <Gas Gwarmstorageread < _SCHEDULE_CELL:Schedule >
   │
   ├─ 35
   │   k: #next [ TLOAD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (12 steps)
   └─ 23 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_OUT_OF_GAS


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-TLOAD-1-SPEC
    
    
    rule [BASIC-BLOCK-31-TO-6]: <kevm>
           <k>
             ( #next [ TLOAD ] ~> .K => TLOAD _W0:Int
             ~> #pc [ TLOAD ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
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
      [priority(20), label(BASIC-BLOCK-31-TO-6)]
    
    rule [BASIC-BLOCK-34-TO-14]: <kevm>
           <k>
             ( #next [ TLOAD ] ~> .K => TLOAD _W0:Int
             ~> #pc [ TLOAD ] )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Gwarmstorageread < _SCHEDULE_CELL:Schedule > )
                 </gas>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( Gwarmstorageread < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               ))
      [priority(20), label(BASIC-BLOCK-34-TO-14)]
    
    rule [BASIC-BLOCK-35-TO-23]: <kevm>
           <k>
             ( #next [ TLOAD ] => #halt )
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
                   ( ( __W0 : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( _GAS_CELL:Gas <Gas Gwarmstorageread < _SCHEDULE_CELL:Schedule >
               ))
      [priority(20), label(BASIC-BLOCK-35-TO-23)]

endmodule
