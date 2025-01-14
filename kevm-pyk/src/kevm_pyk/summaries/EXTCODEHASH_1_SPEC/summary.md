
┌─ 1 (root, split, init)
│   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 65
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (8 steps)
┃  ├─ 57
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
┃  ┃     _GAS_CELL:Gas <Gas Cextcodehash ( _SCHEDULE_CELL:Schedule )
┃  │
┃  ├─ 87
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (12 steps)
┃  └─ 17 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
┃  │
┃  ├─ 108
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 15 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 109
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (14 steps)
┃  └─ 31 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
┃  │
┃  ├─ 124
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 21 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 125
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (14 steps)
┃  └─ 34 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
┃  │
┃  ├─ 136
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
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
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 137
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (14 steps)
┃  └─ 43 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
┃  │
┃  ├─ 148
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 35 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 149
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (14 steps)
┃  └─ 49 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
┃  │
┃  ├─ 160
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 41 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 161
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (14 steps)
┃  └─ 53 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
┃  │
┃  ├─ 172
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 47 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 173
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (14 steps)
┃  └─ 56 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
┃  │
┃  ├─ 182
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 50 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 183
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (14 steps)
┃  └─ 58 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
┃  │
┃  ├─ 188
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 59 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
┃  │
┃  ├─ 189
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 60 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 190
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (10 steps)
┃  └─ 61 (leaf, pending)
┃      k: #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragere ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
┃  │
┃  ├─ 192
┃  │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (8 steps)
┃  └─ 62 (leaf, pending)
┃      k: #access [ EXTCODEHASH , EXTCODEHASH ( _W0:Int modInt pow160 ) ] ~> EXTCODEHASH ( ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
   │
   ├─ 193
   │   k: #next [ EXTCODEHASH ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (8 steps)
   └─ 63 (leaf, pending)
       k: #access [ EXTCODEHASH , EXTCODEHASH ( _W0:Int modInt pow160 ) ] ~> EXTCODEHASH ( ...
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: _STATUSCODE_CELL:StatusCode




module SUMMARY-EXTCODEHASH-1-SPEC
    
    
    rule [BASIC-BLOCK-65-TO-57]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int => 0 ) : __WS )
                 </wordStack>
                 <pc>
                   ( _PC_CELL:Int => ( _PC_CELL:Int +Int 1 ) )
                 </pc>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( _ACCESSEDACCOUNTS_CELL:Set => _ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( _W0:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( notBool _USEGAS_CELL:Bool )
      [priority(20), label(BASIC-BLOCK-65-TO-57)]
    
    rule [BASIC-BLOCK-87-TO-17]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
       andBool ( _GAS_CELL:Gas <Gas Cextcodehash ( _SCHEDULE_CELL:Schedule )
               ))
      [priority(20), label(BASIC-BLOCK-87-TO-17)]
    
    rule [BASIC-BLOCK-108-TO-15]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-108-TO-15)]
    
    rule [BASIC-BLOCK-109-TO-31]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-109-TO-31)]
    
    rule [BASIC-BLOCK-124-TO-21]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-124-TO-21)]
    
    rule [BASIC-BLOCK-125-TO-34]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-125-TO-34)]
    
    rule [BASIC-BLOCK-136-TO-26]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-136-TO-26)]
    
    rule [BASIC-BLOCK-137-TO-43]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-137-TO-43)]
    
    rule [BASIC-BLOCK-148-TO-35]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-148-TO-35)]
    
    rule [BASIC-BLOCK-149-TO-49]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-149-TO-49)]
    
    rule [BASIC-BLOCK-160-TO-41]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-160-TO-41)]
    
    rule [BASIC-BLOCK-161-TO-53]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-161-TO-53)]
    
    rule [BASIC-BLOCK-172-TO-47]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-172-TO-47)]
    
    rule [BASIC-BLOCK-173-TO-56]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-173-TO-56)]
    
    rule [BASIC-BLOCK-182-TO-50]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-182-TO-50)]
    
    rule [BASIC-BLOCK-183-TO-58]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] => #halt )
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
                   ( ( _W0:Int : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-183-TO-58)]
    
    rule [BASIC-BLOCK-188-TO-59]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas -Gas 0
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-188-TO-59)]
    
    rule [BASIC-BLOCK-189-TO-60]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas 0 <Gas #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               ))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-189-TO-60)]
    
    rule [BASIC-BLOCK-190-TO-61]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #if ( _W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas 0 )
                 </gas>
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
               )))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-190-TO-61)]
    
    rule [BASIC-BLOCK-192-TO-62]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #access [ EXTCODEHASH , EXTCODEHASH ( _W0:Int modInt pow160 ) ]
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Cextcodehash ( _SCHEDULE_CELL:Schedule ) )
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
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
               )))
      [priority(20), label(BASIC-BLOCK-192-TO-62)]
    
    rule [BASIC-BLOCK-193-TO-63]: <kevm>
           <k>
             ( #next [ EXTCODEHASH ] ~> .K => #access [ EXTCODEHASH , EXTCODEHASH ( _W0:Int modInt pow160 ) ]
             ~> EXTCODEHASH ( _W0:Int modInt pow160 )
             ~> #pc [ EXTCODEHASH ] )
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
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas Cextcodehash ( _SCHEDULE_CELL:Schedule ) )
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
       andBool ( Cextcodehash ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
               ))
      [priority(20), label(BASIC-BLOCK-193-TO-63)]

endmodule
