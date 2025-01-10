
┌─ 1 (root, split, init)
│   k: #next [ EXTCODESIZE ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1
┃  │
┃  ├─ 3
┃  │   k: #next [ EXTCODESIZE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 8 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_UNDERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ EXTCODESIZE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 7 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1 )
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024 )
   │
   ├─ 5
   │   k: #next [ EXTCODESIZE ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (1 step)
   ├─ 6
   │   k: #addr [ EXTCODESIZE ] ~> #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL ...
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9 (split)
   ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
   ┃  │   pc: _PC_CELL:Int
   ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┃ (branch)
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     _USEGAS_CELL:Bool
   ┃  ┃  │
   ┃  ┃  ├─ 77
   ┃  ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (5 steps)
   ┃  ┃  ├─ 21
   ┃  ┃  │   k: Cextcodesize ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODESIZE  ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 22 (split)
   ┃  ┃  ┃  │   k: #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃ (branch)
   ┃  ┃  ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃  ┃  ┃ constraint:
   ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ├─ 31
   ┃  ┃  ┃  ┃  │   k: #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  │  (2 steps)
   ┃  ┃  ┃  ┃  ├─ 41
   ┃  ┃  ┃  ┃  │   k: #if ( W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragerea ...
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃  ┃ (1 step)
   ┃  ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ┃  └─ 48 (leaf, pending)
   ┃  ┃  ┃  ┃  ┃      k: EXTCODESIZE ( W0:Int modInt pow160 ) ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ┃  ├─ 49
   ┃  ┃  ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> EXTCODESIZE ( W0:Int modInt pow160 ) ~> #pc [ EXTCODESIZ ...
   ┃  ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ┃  │  (3 steps)
   ┃  ┃  ┃  ┃  ┃  └─ 67 (leaf, pending)
   ┃  ┃  ┃  ┃  ┃      k: #halt ~> _K_CELL:K
   ┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
   ┃  ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃  ┗━━┓
   ┃  ┃  ┃  ┃     │
   ┃  ┃  ┃  ┃     └─ 50 (stuck, leaf)
   ┃  ┃  ┃  ┃         k: #if ( W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragerea ...
   ┃  ┃  ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃  ┃  ┃ constraint:
   ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ├─ 44
   ┃  ┃  ┃  ┃  │   k: #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  │  (2 steps)
   ┃  ┃  ┃  ┃  ├─ 58
   ┃  ┃  ┃  ┃  │   k: #if ( W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragerea ...
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃  ┃ (1 step)
   ┃  ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ┃  └─ 71 (leaf, pending)
   ┃  ┃  ┃  ┃  ┃      k: EXTCODESIZE ( W0:Int modInt pow160 ) ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ┃  └─ 72 (leaf, pending)
   ┃  ┃  ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> EXTCODESIZE ( W0:Int modInt pow160 ) ~> #pc [ EXTCODESIZ ...
   ┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃  ┗━━┓
   ┃  ┃  ┃  ┃     │
   ┃  ┃  ┃  ┃     └─ 73 (leaf, pending)
   ┃  ┃  ┃  ┃         k: #if ( W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragerea ...
   ┃  ┃  ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃  ┃  ┃ constraint:
   ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  └─ 60 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┗━━┓ subst: .Subst
   ┃  ┃  ┃     ┃ constraint: true
   ┃  ┃  ┃     │
   ┃  ┃  ┃     └─ 61 (leaf, pending)
   ┃  ┃  ┃         k: #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
   ┃  ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 23
   ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow1 ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  │  (4 steps)
   ┃  ┃  ┃  └─ 40 (leaf, terminal)
   ┃  ┃  ┃      k: #halt ~> _K_CELL:K
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 24 (stuck, leaf)
   ┃  ┃         k: Cextcodesize ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODESIZE  ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     ├─ 78
   ┃     │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     │
   ┃     │  (1 step)
   ┃     └─ 13 (leaf, pending)
   ┃         k: #gas [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ] ~> EXTCODESIZE ( W0: ...
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #addr [ EXTCODESIZE ] ~> #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL ...
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 14 (split)
      ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
      ┃  │   pc: _PC_CELL:Int
      ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┃ (branch)
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     _USEGAS_CELL:Bool
      ┃  ┃  │
      ┃  ┃  ├─ 79
      ┃  ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (5 steps)
      ┃  ┃  ├─ 30
      ┃  ┃  │   k: Cextcodesize ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODESIZE  ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 33 (split)
      ┃  ┃  ┃  │   k: #access [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┃ (branch)
      ┃  ┃  ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃  ┃  ┃ constraint:
      ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  ├─ 46
      ┃  ┃  ┃  ┃  │   k: #access [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
      ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  │  (2 steps)
      ┃  ┃  ┃  ┃  └─ 62 (leaf, pending)
      ┃  ┃  ┃  ┃      k: #if ( W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstoragerea ...
      ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃  ┃  ┃ constraint:
      ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  └─ 63 (leaf, pending)
      ┃  ┃  ┃  ┃      k: #access [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
      ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┗━━┓ subst: .Subst
      ┃  ┃  ┃     ┃ constraint: true
      ┃  ┃  ┃     │
      ┃  ┃  ┃     └─ 64 (leaf, pending)
      ┃  ┃  ┃         k: #access [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
      ┃  ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 34
      ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow1 ...
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  │
      ┃  ┃  ┃  │  (4 steps)
      ┃  ┃  ┃  └─ 57 (leaf, terminal)
      ┃  ┃  ┃      k: #halt ~> _K_CELL:K
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 35 (stuck, leaf)
      ┃  ┃         k: Cextcodesize ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODESIZE  ...
      ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     ├─ 80
      ┃     │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
      ┃     │   pc: _PC_CELL:Int
      ┃     │   callDepth: _CALLDEPTH_CELL:Int
      ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃     │
      ┃     │  (1 step)
      ┃     └─ 18 (leaf, pending)
      ┃         k: #gas [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow160 ) ] ~> EXTCODESIZE ( W1: ...
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 15
         │   k: #addr [ EXTCODESIZE ] ~> #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL ...
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 19 (split)
         ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
         ┃  │   pc: _PC_CELL:Int
         ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┃ (branch)
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     _USEGAS_CELL:Bool
         ┃  ┃  │
         ┃  ┃  ├─ 81
         ┃  ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  │
         ┃  ┃  │  (5 steps)
         ┃  ┃  ├─ 39
         ┃  ┃  │   k: Cextcodesize ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODESIZE  ...
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┃ (1 step)
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  ├─ 51 (split)
         ┃  ┃  ┃  │   k: #access [ EXTCODESIZE , EXTCODESIZE ( W2:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
         ┃  ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃  ┃
         ┃  ┃  ┃  ┃ (branch)
         ┃  ┃  ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃  ┃  ┃ constraint:
         ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
         ┃  ┃  ┃  ┃  │
         ┃  ┃  ┃  ┃  └─ 65 (leaf, pending)
         ┃  ┃  ┃  ┃      k: #access [ EXTCODESIZE , EXTCODESIZE ( W2:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
         ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃  ┃
         ┃  ┃  ┃  ┗━━┓ subst: .Subst
         ┃  ┃  ┃     ┃ constraint: true
         ┃  ┃  ┃     │
         ┃  ┃  ┃     └─ 66 (leaf, pending)
         ┃  ┃  ┃         k: #access [ EXTCODESIZE , EXTCODESIZE ( W2:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
         ┃  ┃  ┃         pc: _PC_CELL:Int
         ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 52 (leaf, pending)
         ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ EXTCODESIZE , EXTCODESIZE ( W2:Int modInt pow1 ...
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┗━━┓
         ┃  ┃     │
         ┃  ┃     └─ 53 (stuck, leaf)
         ┃  ┃         k: Cextcodesize ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODESIZE  ...
         ┃  ┃         pc: _PC_CELL:Int
         ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     ├─ 82
         ┃     │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
         ┃     │   pc: _PC_CELL:Int
         ┃     │   callDepth: _CALLDEPTH_CELL:Int
         ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃     │
         ┃     │  (1 step)
         ┃     └─ 27 (leaf, pending)
         ┃         k: #gas [ EXTCODESIZE , EXTCODESIZE ( W2:Int modInt pow160 ) ] ~> EXTCODESIZE ( W2: ...
         ┃         pc: _PC_CELL:Int
         ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 20
            │   k: #addr [ EXTCODESIZE ] ~> #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL ...
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  ├─ 28 (split)
            ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
            ┃  │   pc: _PC_CELL:Int
            ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┃ (branch)
            ┃  ┣━━┓ subst: .Subst
            ┃  ┃  ┃ constraint:
            ┃  ┃  ┃     _USEGAS_CELL:Bool
            ┃  ┃  │
            ┃  ┃  ├─ 83
            ┃  ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
            ┃  ┃  │   pc: _PC_CELL:Int
            ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  │
            ┃  ┃  │  (5 steps)
            ┃  ┃  ├─ 59
            ┃  ┃  │   k: Cextcodesize ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODESIZE  ...
            ┃  ┃  │   pc: _PC_CELL:Int
            ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┃ (1 step)
            ┃  ┃  ┣━━┓
            ┃  ┃  ┃  │
            ┃  ┃  ┃  └─ 74 (leaf, pending)
            ┃  ┃  ┃      k: #access [ EXTCODESIZE , EXTCODESIZE ( W3:Int modInt pow160 ) ] ~> EXTCODESIZE (  ...
            ┃  ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┣━━┓
            ┃  ┃  ┃  │
            ┃  ┃  ┃  └─ 75 (leaf, pending)
            ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ EXTCODESIZE , EXTCODESIZE ( W3:Int modInt pow1 ...
            ┃  ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┗━━┓
            ┃  ┃     │
            ┃  ┃     └─ 76 (leaf, pending)
            ┃  ┃         k: Cextcodesize ( _SCHEDULE_CELL:Schedule ) ~> #deductGas ~> #access [ EXTCODESIZE  ...
            ┃  ┃         pc: _PC_CELL:Int
            ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┗━━┓ subst: .Subst
            ┃     ┃ constraint:
            ┃     ┃     ( notBool _USEGAS_CELL:Bool )
            ┃     │
            ┃     ├─ 84
            ┃     │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
            ┃     │   pc: _PC_CELL:Int
            ┃     │   callDepth: _CALLDEPTH_CELL:Int
            ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃     │
            ┃     │  (1 step)
            ┃     └─ 43 (leaf, pending)
            ┃         k: #gas [ EXTCODESIZE , EXTCODESIZE ( W3:Int modInt pow160 ) ] ~> EXTCODESIZE ( W3: ...
            ┃         pc: _PC_CELL:Int
            ┃         callDepth: _CALLDEPTH_CELL:Int
            ┃         statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               ├─ 29
               │   k: #addr [ EXTCODESIZE ] ~> #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL ...
               │   pc: _PC_CELL:Int
               │   callDepth: _CALLDEPTH_CELL:Int
               │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┃ (1 step)
               ┣━━┓
               ┃  │
               ┃  ├─ 37 (split)
               ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
               ┃  │   pc: _PC_CELL:Int
               ┃  │   callDepth: _CALLDEPTH_CELL:Int
               ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┃ (branch)
               ┃  ┣━━┓ subst: .Subst
               ┃  ┃  ┃ constraint:
               ┃  ┃  ┃     _USEGAS_CELL:Bool
               ┃  ┃  │
               ┃  ┃  ├─ 85
               ┃  ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
               ┃  ┃  │   pc: _PC_CELL:Int
               ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
               ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃  │
               ┃  ┃  │  (1 step)
               ┃  ┃  └─ 68 (leaf, pending)
               ┃  ┃      k: #gas [ EXTCODESIZE , EXTCODESIZE ( W4:Int modInt pow160 ) ] ~> EXTCODESIZE ( W4: ...
               ┃  ┃      pc: _PC_CELL:Int
               ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
               ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┗━━┓ subst: .Subst
               ┃     ┃ constraint:
               ┃     ┃     ( notBool _USEGAS_CELL:Bool )
               ┃     │
               ┃     ├─ 86
               ┃     │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
               ┃     │   pc: _PC_CELL:Int
               ┃     │   callDepth: _CALLDEPTH_CELL:Int
               ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃     │
               ┃     │  (1 step)
               ┃     └─ 69 (leaf, pending)
               ┃         k: #gas [ EXTCODESIZE , EXTCODESIZE ( W4:Int modInt pow160 ) ] ~> EXTCODESIZE ( W4: ...
               ┃         pc: _PC_CELL:Int
               ┃         callDepth: _CALLDEPTH_CELL:Int
               ┃         statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┗━━┓
                  │
                  ├─ 38
                  │   k: #addr [ EXTCODESIZE ] ~> #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL ...
                  │   pc: _PC_CELL:Int
                  │   callDepth: _CALLDEPTH_CELL:Int
                  │   statusCode: _STATUSCODE_CELL:StatusCode
                  ┃
                  ┃ (1 step)
                  ┣━━┓
                  ┃  │
                  ┃  ├─ 55
                  ┃  │   k: #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL:K
                  ┃  │   pc: _PC_CELL:Int
                  ┃  │   callDepth: _CALLDEPTH_CELL:Int
                  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
                  ┃  │
                  ┃  │  (1 step)
                  ┃  └─ 70 (leaf, pending)
                  ┃      k: #gas [ EXTCODESIZE , EXTCODESIZE ( W5:Int modInt pow160 ) ] ~> EXTCODESIZE ( W5: ...
                  ┃      pc: _PC_CELL:Int
                  ┃      callDepth: _CALLDEPTH_CELL:Int
                  ┃      statusCode: _STATUSCODE_CELL:StatusCode
                  ┃
                  ┗━━┓
                     │
                     └─ 56 (leaf, pending)
                         k: #addr [ EXTCODESIZE ] ~> #exec [ EXTCODESIZE ] ~> #pc [ EXTCODESIZE ] ~> _K_CELL ...
                         pc: _PC_CELL:Int
                         callDepth: _CALLDEPTH_CELL:Int
                         statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-EXTCODESIZE-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ EXTCODESIZE ] ~> .K => #addr [ EXTCODESIZE ]
             ~> #exec [ EXTCODESIZE ]
             ~> #pc [ EXTCODESIZE ] )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   _WORDSTACK_CELL:WordStack
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024 )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-6)]
    
    rule [BASIC-BLOCK-4-TO-7]: <kevm>
           <k>
             ( #next [ EXTCODESIZE ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STACK_OVERFLOW )
               </statusCode>
               <callState>
                 <wordStack>
                   _WORDSTACK_CELL:WordStack
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-7)]
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ EXTCODESIZE ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STACK_UNDERFLOW )
               </statusCode>
               <callState>
                 <wordStack>
                   _WORDSTACK_CELL:WordStack
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1
      [priority(20), label(BASIC-BLOCK-3-TO-8)]
    
    rule [BASIC-BLOCK-23-TO-40]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W0:Int modInt pow160 )
             ~> #pc [ EXTCODESIZE ] => #halt ~> .K )
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
                 <wordStack>
                   _WS:WordStack
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
      requires ( __USEGAS_CELL
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( _GAS_CELL:Gas <Gas Cextcodesize ( _SCHEDULE_CELL:Schedule )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-23-TO-40)]
    
    rule [BASIC-BLOCK-31-TO-41]: <kevm>
           <k>
             ( #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ] ~> .K => #if ( W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas )
             ~> EXTCODESIZE ( W0:Int modInt pow160 )
             ~> #pc [ EXTCODESIZE ]
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
                 <wordStack>
                   _WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cextcodesize ( _SCHEDULE_CELL:Schedule ) => 0 )
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
      requires ( __USEGAS_CELL
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( Cextcodesize ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-31-TO-41)]
    
    rule [BASIC-BLOCK-34-TO-57]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W1:Int modInt pow160 )
             ~> #pc [ EXTCODESIZE ] => #halt ~> .K )
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
                 <wordStack>
                   _WS:WordStack
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
      requires ( __USEGAS_CELL
       andBool ( _W0 =/=Int W1:Int
       andBool ( __WORDSTACK_CELL ==K ( W1:Int : _WS:WordStack )
       andBool ( _GAS_CELL:Gas <Gas Cextcodesize ( _SCHEDULE_CELL:Schedule )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-34-TO-57)]
    
    rule [BASIC-BLOCK-44-TO-58]: <kevm>
           <k>
             ( #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ] ~> .K => #if ( W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas )
             ~> EXTCODESIZE ( W0:Int modInt pow160 )
             ~> #pc [ EXTCODESIZE ]
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
                 <wordStack>
                   _WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cextcodesize ( _SCHEDULE_CELL:Schedule ) => 0 )
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
      requires ( __USEGAS_CELL
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( Cextcodesize ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-44-TO-58)]
    
    rule [BASIC-BLOCK-46-TO-62]: <kevm>
           <k>
             ( #access [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow160 ) ] ~> .K => #if ( W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
             ~> #deductGas )
             ~> EXTCODESIZE ( W1:Int modInt pow160 )
             ~> #pc [ EXTCODESIZE ]
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
                 <wordStack>
                   _WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cextcodesize ( _SCHEDULE_CELL:Schedule ) => 0 )
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
      requires ( __USEGAS_CELL
       andBool ( _W0 =/=Int W1:Int
       andBool ( __WORDSTACK_CELL ==K ( W1:Int : _WS:WordStack )
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( Cextcodesize ( _SCHEDULE_CELL:Schedule ) <=Gas _GAS_CELL:Gas
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               )))))))
       ensures 0 <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-46-TO-62)]
    
    rule [BASIC-BLOCK-49-TO-67]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> EXTCODESIZE ( W0:Int modInt pow160 )
             ~> #pc [ EXTCODESIZE ] => #halt ~> .K )
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
                 <wordStack>
                   _WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas 0
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
      requires ( __USEGAS_CELL
       andBool ( 0 <=Gas _GAS_CELL:Gas
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
       andBool ( _GAS_CELL:Gas -Gas 0 <Gas #if ( W0:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldaccountaccess < _SCHEDULE_CELL:Schedule > #fi
               )))))))
      [priority(20), label(BASIC-BLOCK-49-TO-67)]
    
    rule [BASIC-BLOCK-55-TO-70]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => #gas [ EXTCODESIZE , EXTCODESIZE ( W5:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W5:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W5:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _W0 =/=Int W5:Int
       andBool ( _W1 =/=Int W5:Int
       andBool ( _W2 =/=Int W5:Int
       andBool ( _W3 =/=Int W5:Int
       andBool ( _W4 =/=Int W5:Int
       andBool ( __WORDSTACK_CELL ==K ( W5:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))))
      [priority(20), label(BASIC-BLOCK-55-TO-70)]
    
    rule [BASIC-BLOCK-78-TO-13]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => #gas [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W0:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W0:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-78-TO-13)]
    
    rule [BASIC-BLOCK-80-TO-18]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => #gas [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W1:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W1:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( _W0 =/=Int W1:Int
       andBool ( __WORDSTACK_CELL ==K ( W1:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-80-TO-18)]
    
    rule [BASIC-BLOCK-82-TO-27]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => #gas [ EXTCODESIZE , EXTCODESIZE ( W2:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W2:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W2:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( _W0 =/=Int W2:Int
       andBool ( _W1 =/=Int W2:Int
       andBool ( __WORDSTACK_CELL ==K ( W2:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-82-TO-27)]
    
    rule [BASIC-BLOCK-84-TO-43]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => #gas [ EXTCODESIZE , EXTCODESIZE ( W3:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W3:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W3:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( _W0 =/=Int W3:Int
       andBool ( _W1 =/=Int W3:Int
       andBool ( _W2 =/=Int W3:Int
       andBool ( __WORDSTACK_CELL ==K ( W3:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-84-TO-43)]
    
    rule [BASIC-BLOCK-85-TO-68]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => #gas [ EXTCODESIZE , EXTCODESIZE ( W4:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W4:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W4:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( _W0 =/=Int W4:Int
       andBool ( _W1 =/=Int W4:Int
       andBool ( _W2 =/=Int W4:Int
       andBool ( _W3 =/=Int W4:Int
       andBool ( __WORDSTACK_CELL ==K ( W4:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))))
      [priority(20), label(BASIC-BLOCK-85-TO-68)]
    
    rule [BASIC-BLOCK-86-TO-69]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => #gas [ EXTCODESIZE , EXTCODESIZE ( W4:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W4:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W4:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( _W0 =/=Int W4:Int
       andBool ( _W1 =/=Int W4:Int
       andBool ( _W2 =/=Int W4:Int
       andBool ( _W3 =/=Int W4:Int
       andBool ( __WORDSTACK_CELL ==K ( W4:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))))
      [priority(20), label(BASIC-BLOCK-86-TO-69)]
    
    rule [BASIC-BLOCK-77-TO-21]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => Cextcodesize ( _SCHEDULE_CELL:Schedule )
             ~> #deductGas
             ~> #access [ EXTCODESIZE , EXTCODESIZE ( W0:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W0:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
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
                   ( ( ( W0:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-77-TO-21)]
    
    rule [BASIC-BLOCK-79-TO-30]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => Cextcodesize ( _SCHEDULE_CELL:Schedule )
             ~> #deductGas
             ~> #access [ EXTCODESIZE , EXTCODESIZE ( W1:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W1:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
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
                   ( ( ( W1:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( _W0 =/=Int W1:Int
       andBool ( __WORDSTACK_CELL ==K ( W1:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-79-TO-30)]
    
    rule [BASIC-BLOCK-81-TO-39]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => Cextcodesize ( _SCHEDULE_CELL:Schedule )
             ~> #deductGas
             ~> #access [ EXTCODESIZE , EXTCODESIZE ( W2:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W2:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
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
                   ( ( ( W2:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( _W0 =/=Int W2:Int
       andBool ( _W1 =/=Int W2:Int
       andBool ( __WORDSTACK_CELL ==K ( W2:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-81-TO-39)]
    
    rule [BASIC-BLOCK-83-TO-59]: <kevm>
           <k>
             ( #exec [ EXTCODESIZE ] ~> .K => Cextcodesize ( _SCHEDULE_CELL:Schedule )
             ~> #deductGas
             ~> #access [ EXTCODESIZE , EXTCODESIZE ( W3:Int modInt pow160 ) ]
             ~> EXTCODESIZE ( W3:Int modInt pow160 ) )
             ~> #pc [ EXTCODESIZE ]
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
                   ( ( ( W3:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( _W0 =/=Int W3:Int
       andBool ( _W1 =/=Int W3:Int
       andBool ( _W2 =/=Int W3:Int
       andBool ( __WORDSTACK_CELL ==K ( W3:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-83-TO-59)]

endmodule
