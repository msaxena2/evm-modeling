
┌─ 1 (root, split, init)
│   k: #next [ SLOAD ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 51
┃  │   k: #next [ SLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 6
┃  │   k: SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 7 (leaf, pending)
┃  ┃      k: #lookup ( STORAGE:Map , _W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 8
┃     │   k: SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 12 (leaf, pending)
┃     ┃      k: #lookup ( STORAGE0:Map , _W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 13
┃        │   k: SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  └─ 17 (leaf, pending)
┃        ┃      k: #lookup ( STORAGE1:Map , _W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
┃        ┃      pc: _PC_CELL:Int
┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 18
┃           │   k: SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  └─ 22 (leaf, pending)
┃           ┃      k: #lookup ( STORAGE2:Map , _W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
┃           ┃      pc: _PC_CELL:Int
┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              ├─ 23
┃              │   k: SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃              │   pc: _PC_CELL:Int
┃              │   callDepth: _CALLDEPTH_CELL:Int
┃              │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┃ (1 step)
┃              ┣━━┓
┃              ┃  │
┃              ┃  └─ 31 (leaf, pending)
┃              ┃      k: #lookup ( STORAGE3:Map , _W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
┃              ┃      pc: _PC_CELL:Int
┃              ┃      callDepth: _CALLDEPTH_CELL:Int
┃              ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┗━━┓
┃                 │
┃                 ├─ 32
┃                 │   k: SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃                 │   pc: _PC_CELL:Int
┃                 │   callDepth: _CALLDEPTH_CELL:Int
┃                 │   statusCode: _STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┃ (1 step)
┃                 ┣━━┓
┃                 ┃  │
┃                 ┃  └─ 45 (leaf, pending)
┃                 ┃      k: #lookup ( STORAGE4:Map , _W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
┃                 ┃      pc: _PC_CELL:Int
┃                 ┃      callDepth: _CALLDEPTH_CELL:Int
┃                 ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┗━━┓
┃                    │
┃                    └─ 46 (leaf, pending)
┃                        k: SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃                        pc: _PC_CELL:Int
┃                        callDepth: _CALLDEPTH_CELL:Int
┃                        statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     _GAS_CELL:Gas <Gas Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) )
┃  │
┃  ├─ 57
┃  │   k: #next [ SLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (12 steps)
┃  └─ 27 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 64
┃  │   k: #next [ SLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  ├─ 21
┃  │   k: #accessStorage _ID_CELL:Account _W0:Int ~> 0 ~> #deductGas ~> SLOAD _W0:Int ~> # ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 24 (split)
┃  ┃  │   k: 0 ~> #deductGas ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     0 <=Gas _GAS_CELL:Gas -Gas Gcoldsload < _SCHEDULE_CELL:Schedule >
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 33
┃  ┃  ┃  │   k: 0 ~> #deductGas ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  └─ 47 (leaf, pending)
┃  ┃  ┃      k: SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     _GAS_CELL:Gas -Gas Gcoldsload < _SCHEDULE_CELL:Schedule > <Gas 0
┃  ┃     │
┃  ┃     ├─ 34
┃  ┃     │   k: 0 ~> #deductGas ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     │
┃  ┃     │  (4 steps)
┃  ┃     └─ 49 (leaf, pending)
┃  ┃         k: #halt ~> _K_CELL:K
┃  ┃         pc: _PC_CELL:Int
┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃         statusCode: EVMC_OUT_OF_GAS
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 25 (split)
┃  ┃  │   k: 0 ~> #deductGas ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     0 <=Gas _GAS_CELL:Gas -Gas #if #inStorageAux2 ( TS:Set , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 35
┃  ┃  ┃  │   k: 0 ~> #deductGas ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  └─ 48 (leaf, pending)
┃  ┃  ┃      k: SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     _GAS_CELL:Gas -Gas #if #inStorageAux2 ( TS:Set , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi <Gas 0
┃  ┃     │
┃  ┃     └─ 36 (leaf, pending)
┃  ┃         k: 0 ~> #deductGas ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃         pc: _PC_CELL:Int
┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 26
┃     │   k: #accessStorage _ID_CELL:Account _W0:Int ~> 0 ~> #deductGas ~> SLOAD _W0:Int ~> # ...
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  └─ 37 (leaf, pending)
┃     ┃      k: 0 ~> #deductGas ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃     ┃      pc: _PC_CELL:Int
┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        └─ 38 (leaf, pending)
┃            k: #accessStorage _ID_CELL:Account _W0:Int ~> 0 ~> #deductGas ~> SLOAD _W0:Int ~> # ...
┃            pc: _PC_CELL:Int
┃            callDepth: _CALLDEPTH_CELL:Int
┃            statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 70
┃  │   k: #next [ SLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  ├─ 30
┃  │   k: #accessStorage _ID_CELL:Account _W0:Int ~> 0 ~> #deductGas ~> SLOAD _W0:Int ~> # ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 39 (leaf, pending)
┃  ┃      k: 0 ~> #deductGas ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 40 (leaf, pending)
┃  ┃      k: 0 ~> #deductGas ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 41 (leaf, pending)
┃         k: #accessStorage _ID_CELL:Account _W0:Int ~> 0 ~> #deductGas ~> SLOAD _W0:Int ~> # ...
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 76
┃  │   k: #next [ SLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 42 (leaf, pending)
┃      k: #accessStorage _ID_CELL:Account _W0:Int ~> 0 ~> #deductGas ~> SLOAD _W0:Int ~> # ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 78
┃  │   k: #next [ SLOAD ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (8 steps)
┃  └─ 43 (leaf, pending)
┃      k: #access [ SLOAD , SLOAD _W0:Int ] ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
   │
   ├─ 79
   │   k: #next [ SLOAD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (8 steps)
   └─ 44 (leaf, pending)
       k: #access [ SLOAD , SLOAD _W0:Int ] ~> SLOAD _W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SLOAD-1-SPEC
    
    
    rule [BASIC-BLOCK-33-TO-47]: <kevm>
           <k>
             ( 0
             ~> #deductGas => .K )
             ~> SLOAD _W0:Int
             ~> #pc [ SLOAD ]
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
                   _ID_CELL:Account
                 </id>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Gcoldsload < _SCHEDULE_CELL:Schedule > ) -Gas ( Gcoldsload < _SCHEDULE_CELL:Schedule > => 0 )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   ( ( _ID_CELL:Account |-> SetItem ( _W0:Int ) )
                   _ACCESSEDSTORAGE_CELL:Map )
                 </accessedStorage>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( notBool _ID_CELL:Account in_keys ( _ACCESSEDSTORAGE_CELL:Map ) )
       andBool ( Gcoldsload < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( 0 <=Gas _GAS_CELL:Gas -Gas Gcoldsload < _SCHEDULE_CELL:Schedule >
               )))))
      [priority(20), label(BASIC-BLOCK-33-TO-47)]
    
    rule [BASIC-BLOCK-35-TO-48]: <kevm>
           <k>
             ( 0
             ~> #deductGas => .K )
             ~> SLOAD _W0:Int
             ~> #pc [ SLOAD ]
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
                   _ID_CELL:Account
                 </id>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas #if #inStorageAux2 ( TS:Set , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi ) -Gas ( #if #inStorageAux2 ( TS:Set , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi => 0 )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   ( ( _ID_CELL:Account |-> TS:Set |Set SetItem ( _W0:Int ) )
                   _DotVar6:Map )
                 </accessedStorage>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( notBool _ID_CELL:Account in_keys ( _DotVar6:Map ) )
       andBool ( __ACCESSEDSTORAGE_CELL ==K ( ( _ID_CELL:Account |-> TS:Set )
        _DotVar6:Map )
       andBool ( #if #inStorageAux2 ( TS:Set , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas
       andBool ( 0 <=Gas _GAS_CELL:Gas -Gas #if #inStorageAux2 ( TS:Set , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi
               ))))))
      [priority(20), label(BASIC-BLOCK-35-TO-48)]
    
    rule [BASIC-BLOCK-34-TO-49]: <kevm>
           <k>
             ( 0
             ~> #deductGas
             ~> SLOAD _W0:Int
             ~> #pc [ SLOAD ] => #halt ~> .K )
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
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_OUT_OF_GAS )
               </statusCode>
               <callState>
                 <id>
                   _ID_CELL:Account
                 </id>
                 <gas>
                   _GAS_CELL:Gas -Gas Gcoldsload < _SCHEDULE_CELL:Schedule >
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   ( ( _ID_CELL:Account |-> SetItem ( _W0:Int ) )
                   _ACCESSEDSTORAGE_CELL:Map )
                 </accessedStorage>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( notBool _ID_CELL:Account in_keys ( _ACCESSEDSTORAGE_CELL:Map ) )
       andBool ( Gcoldsload < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas Gcoldsload < _SCHEDULE_CELL:Schedule > <Gas 0
               )))))
      [priority(20), label(BASIC-BLOCK-34-TO-49)]
    
    rule [BASIC-BLOCK-51-TO-6]: <kevm>
           <k>
             ( #next [ SLOAD ] ~> .K => SLOAD _W0:Int
             ~> #pc [ SLOAD ] )
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
      [priority(20), label(BASIC-BLOCK-51-TO-6)]
    
    rule [BASIC-BLOCK-57-TO-27]: <kevm>
           <k>
             ( #next [ SLOAD ] => #halt )
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( _GAS_CELL:Gas <Gas Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) )
               ))
      [priority(20), label(BASIC-BLOCK-57-TO-27)]
    
    rule [BASIC-BLOCK-64-TO-21]: <kevm>
           <k>
             ( #next [ SLOAD ] ~> .K => #accessStorage _ID_CELL:Account _W0:Int
             ~> 0
             ~> #deductGas
             ~> SLOAD _W0:Int
             ~> #pc [ SLOAD ] )
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
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
       andBool ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
               )))
       ensures #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-64-TO-21)]
    
    rule [BASIC-BLOCK-70-TO-30]: <kevm>
           <k>
             ( #next [ SLOAD ] ~> .K => #accessStorage _ID_CELL:Account _W0:Int
             ~> 0
             ~> #deductGas
             ~> SLOAD _W0:Int
             ~> #pc [ SLOAD ] )
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
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
       andBool ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
               )))
       ensures #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-70-TO-30)]
    
    rule [BASIC-BLOCK-76-TO-42]: <kevm>
           <k>
             ( #next [ SLOAD ] ~> .K => #accessStorage _ID_CELL:Account _W0:Int
             ~> 0
             ~> #deductGas
             ~> SLOAD _W0:Int
             ~> #pc [ SLOAD ] )
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
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
       andBool ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
               )))
       ensures #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-76-TO-42)]
    
    rule [BASIC-BLOCK-78-TO-43]: <kevm>
           <k>
             ( #next [ SLOAD ] ~> .K => #access [ SLOAD , SLOAD _W0:Int ]
             ~> SLOAD _W0:Int
             ~> #pc [ SLOAD ] )
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
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
       andBool ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
               )))
      [priority(20), label(BASIC-BLOCK-78-TO-43)]
    
    rule [BASIC-BLOCK-79-TO-44]: <kevm>
           <k>
             ( #next [ SLOAD ] ~> .K => #access [ SLOAD , SLOAD _W0:Int ]
             ~> SLOAD _W0:Int
             ~> #pc [ SLOAD ] )
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , _W0:Int ) ) <=Gas _GAS_CELL:Gas
               ))
      [priority(20), label(BASIC-BLOCK-79-TO-44)]

endmodule
