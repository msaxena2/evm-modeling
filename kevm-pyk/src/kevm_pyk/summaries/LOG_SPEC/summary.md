
┌─ 1 (root, split, init)
│   k: #next [ LOG ( _N:Int ) ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int ( _N:Int +Int 2 )
┃  │
┃  ├─ 3
┃  │   k: #next [ LOG ( _N:Int ) ] ~> _K_CELL:K
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
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( -2 -Int _N:Int ) ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 9 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int ( _N:Int +Int 2 ) )
┃  ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
┃  │
┃  ├─ 5
┃  │   k: #next [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  ├─ 7
┃  │   k: #exec [ LOG ( _N:Int ) ] ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 11 (split)
┃  ┃  │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     _USEGAS_CELL:Bool
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 13
┃  ┃  ┃  │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (4 steps)
┃  ┃  ┃  ├─ 24
┃  ┃  ┃  │   k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 25
┃  ┃  ┃  ┃  │   k: #gas [ LOG ( _N:Int ) W0:Int W1:Int ] ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  │  (2 steps)
┃  ┃  ┃  ┃  ├─ 36
┃  ┃  ┃  ┃  │   k: ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ├─ 44
┃  ┃  ┃  ┃  ┃  │   k: #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ] ~> LOG ( _N:Int ) W0:I ...
┃  ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  ┃  ├─ 54
┃  ┃  ┃  ┃  ┃  │   k: LOG ( _N:Int ) W0:Int W1:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃  ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  └─ 67 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃      k: #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃  ┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃  ┃     └─ 68 (leaf, pending)
┃  ┃  ┃  ┃  ┃         k: LOG ( _N:Int ) W0:Int W1:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃  ┃  ┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ├─ 45
┃  ┃  ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int  ...
┃  ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  │  (4 steps)
┃  ┃  ┃  ┃  ┃  └─ 72 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #halt ~> _K_CELL:K
┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃     └─ 46 (stuck, leaf)
┃  ┃  ┃  ┃         k: ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > ...
┃  ┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 26
┃  ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #gas [ LOG ( _N:Int ) W0:Int W1:Int ] ~> #access [ LOG ( ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  │  (5 steps)
┃  ┃  ┃  ┃  └─ 43 (leaf, terminal)
┃  ┃  ┃  ┃      k: #halt ~> _K_CELL:K
┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓
┃  ┃  ┃     │
┃  ┃  ┃     └─ 27 (stuck, leaf)
┃  ┃  ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃  ┃     │
┃  ┃     ├─ 14
┃  ┃     │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     │
┃  ┃     │  (1 step)
┃  ┃     ├─ 19
┃  ┃     │   k: LOG ( _N:Int ) W0:Int W1:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┃ (1 step)
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  └─ 22 (leaf, pending)
┃  ┃     ┃      k: #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┗━━┓
┃  ┃        │
┃  ┃        └─ 23 (stuck, leaf)
┃  ┃            k: LOG ( _N:Int ) W0:Int W1:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃  ┃            pc: _PC_CELL:Int
┃  ┃            callDepth: _CALLDEPTH_CELL:Int
┃  ┃            statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 12
┃     │   k: #exec [ LOG ( _N:Int ) ] ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  ├─ 15 (split)
┃     ┃  │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃     ┃  │   pc: _PC_CELL:Int
┃     ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┃ (branch)
┃     ┃  ┣━━┓ subst: .Subst
┃     ┃  ┃  ┃ constraint:
┃     ┃  ┃  ┃     _USEGAS_CELL:Bool
┃     ┃  ┃  │
┃     ┃  ┃  ├─ 17
┃     ┃  ┃  │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  │
┃     ┃  ┃  │  (4 steps)
┃     ┃  ┃  ├─ 33
┃     ┃  ┃  │   k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┃ (1 step)
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ├─ 37
┃     ┃  ┃  ┃  │   k: #gas [ LOG ( _N:Int ) W0:Int W2:Int ] ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ...
┃     ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  │  (2 steps)
┃     ┃  ┃  ┃  ├─ 52
┃     ┃  ┃  ┃  │   k: ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > ...
┃     ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃
┃     ┃  ┃  ┃  ┃ (1 step)
┃     ┃  ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ┃  ├─ 60
┃     ┃  ┃  ┃  ┃  │   k: #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ] ~> LOG ( _N:Int ) W0:I ...
┃     ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ┃  │  (1 step)
┃     ┃  ┃  ┃  ┃  └─ 76 (leaf, pending)
┃     ┃  ┃  ┃  ┃      k: LOG ( _N:Int ) W0:Int W2:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃     ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃
┃     ┃  ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ┃  └─ 61 (leaf, pending)
┃     ┃  ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int  ...
┃     ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃
┃     ┃  ┃  ┃  ┗━━┓
┃     ┃  ┃  ┃     │
┃     ┃  ┃  ┃     └─ 62 (stuck, leaf)
┃     ┃  ┃  ┃         k: ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > ...
┃     ┃  ┃  ┃         pc: _PC_CELL:Int
┃     ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ├─ 38
┃     ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #gas [ LOG ( _N:Int ) W0:Int W2:Int ] ~> #access [ LOG ( ...
┃     ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  │  (5 steps)
┃     ┃  ┃  ┃  └─ 59 (leaf, terminal)
┃     ┃  ┃  ┃      k: #halt ~> _K_CELL:K
┃     ┃  ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
┃     ┃  ┃  ┃
┃     ┃  ┃  ┗━━┓
┃     ┃  ┃     │
┃     ┃  ┃     └─ 39 (stuck, leaf)
┃     ┃  ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
┃     ┃  ┃         pc: _PC_CELL:Int
┃     ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┗━━┓ subst: .Subst
┃     ┃     ┃ constraint:
┃     ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃     ┃     │
┃     ┃     ├─ 18
┃     ┃     │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃     ┃     │   pc: _PC_CELL:Int
┃     ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     │
┃     ┃     │  (1 step)
┃     ┃     ├─ 30
┃     ┃     │   k: LOG ( _N:Int ) W0:Int W2:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃     ┃     │   pc: _PC_CELL:Int
┃     ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     ┃
┃     ┃     ┃ (1 step)
┃     ┃     ┣━━┓
┃     ┃     ┃  │
┃     ┃     ┃  └─ 34 (leaf, pending)
┃     ┃     ┃      k: #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃     ┃     ┃      pc: _PC_CELL:Int
┃     ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     ┃
┃     ┃     ┗━━┓
┃     ┃        │
┃     ┃        └─ 35 (stuck, leaf)
┃     ┃            k: LOG ( _N:Int ) W0:Int W2:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃     ┃            pc: _PC_CELL:Int
┃     ┃            callDepth: _CALLDEPTH_CELL:Int
┃     ┃            statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 16
┃        │   k: #exec [ LOG ( _N:Int ) ] ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  ├─ 20 (split)
┃        ┃  │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W3:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃        ┃  │   pc: _PC_CELL:Int
┃        ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┃ (branch)
┃        ┃  ┣━━┓ subst: .Subst
┃        ┃  ┃  ┃ constraint:
┃        ┃  ┃  ┃     _USEGAS_CELL:Bool
┃        ┃  ┃  │
┃        ┃  ┃  ├─ 28
┃        ┃  ┃  │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W3:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃        ┃  ┃  │   pc: _PC_CELL:Int
┃        ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  │
┃        ┃  ┃  │  (4 steps)
┃        ┃  ┃  ├─ 47
┃        ┃  ┃  │   k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
┃        ┃  ┃  │   pc: _PC_CELL:Int
┃        ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┃ (1 step)
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  ├─ 56
┃        ┃  ┃  ┃  │   k: #gas [ LOG ( _N:Int ) W0:Int W3:Int ] ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ...
┃        ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃        ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  │  (2 steps)
┃        ┃  ┃  ┃  └─ 75 (leaf, pending)
┃        ┃  ┃  ┃      k: ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > ...
┃        ┃  ┃  ┃      pc: _PC_CELL:Int
┃        ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  └─ 57 (leaf, pending)
┃        ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #gas [ LOG ( _N:Int ) W0:Int W3:Int ] ~> #access [ LOG ( ...
┃        ┃  ┃  ┃      pc: _PC_CELL:Int
┃        ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┗━━┓
┃        ┃  ┃     │
┃        ┃  ┃     └─ 58 (stuck, leaf)
┃        ┃  ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
┃        ┃  ┃         pc: _PC_CELL:Int
┃        ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┗━━┓ subst: .Subst
┃        ┃     ┃ constraint:
┃        ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃        ┃     │
┃        ┃     ├─ 29
┃        ┃     │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W3:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃        ┃     │   pc: _PC_CELL:Int
┃        ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃     │
┃        ┃     │  (1 step)
┃        ┃     ├─ 42
┃        ┃     │   k: LOG ( _N:Int ) W0:Int W3:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃        ┃     │   pc: _PC_CELL:Int
┃        ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃     ┃
┃        ┃     ┃ (1 step)
┃        ┃     ┣━━┓
┃        ┃     ┃  │
┃        ┃     ┃  └─ 50 (leaf, pending)
┃        ┃     ┃      k: #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃        ┃     ┃      pc: _PC_CELL:Int
┃        ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃     ┃
┃        ┃     ┗━━┓
┃        ┃        │
┃        ┃        └─ 51 (stuck, leaf)
┃        ┃            k: LOG ( _N:Int ) W0:Int W3:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃        ┃            pc: _PC_CELL:Int
┃        ┃            callDepth: _CALLDEPTH_CELL:Int
┃        ┃            statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 21
┃           │   k: #exec [ LOG ( _N:Int ) ] ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  ├─ 31 (split)
┃           ┃  │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W4:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃           ┃  │   pc: _PC_CELL:Int
┃           ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┃ (branch)
┃           ┃  ┣━━┓ subst: .Subst
┃           ┃  ┃  ┃ constraint:
┃           ┃  ┃  ┃     _USEGAS_CELL:Bool
┃           ┃  ┃  │
┃           ┃  ┃  ├─ 40
┃           ┃  ┃  │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W4:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃           ┃  ┃  │   pc: _PC_CELL:Int
┃           ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃  │
┃           ┃  ┃  │  (4 steps)
┃           ┃  ┃  ├─ 55
┃           ┃  ┃  │   k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
┃           ┃  ┃  │   pc: _PC_CELL:Int
┃           ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃  ┃
┃           ┃  ┃  ┃ (1 step)
┃           ┃  ┃  ┣━━┓
┃           ┃  ┃  ┃  │
┃           ┃  ┃  ┃  └─ 69 (leaf, pending)
┃           ┃  ┃  ┃      k: #gas [ LOG ( _N:Int ) W0:Int W4:Int ] ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ...
┃           ┃  ┃  ┃      pc: _PC_CELL:Int
┃           ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃  ┃
┃           ┃  ┃  ┣━━┓
┃           ┃  ┃  ┃  │
┃           ┃  ┃  ┃  └─ 70 (leaf, pending)
┃           ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #gas [ LOG ( _N:Int ) W0:Int W4:Int ] ~> #access [ LOG ( ...
┃           ┃  ┃  ┃      pc: _PC_CELL:Int
┃           ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃  ┃
┃           ┃  ┃  ┗━━┓
┃           ┃  ┃     │
┃           ┃  ┃     └─ 71 (leaf, pending)
┃           ┃  ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
┃           ┃  ┃         pc: _PC_CELL:Int
┃           ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┗━━┓ subst: .Subst
┃           ┃     ┃ constraint:
┃           ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃           ┃     │
┃           ┃     ├─ 41
┃           ┃     │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W4:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃           ┃     │   pc: _PC_CELL:Int
┃           ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃     │
┃           ┃     │  (1 step)
┃           ┃     ├─ 53
┃           ┃     │   k: LOG ( _N:Int ) W0:Int W4:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃           ┃     │   pc: _PC_CELL:Int
┃           ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃     ┃
┃           ┃     ┃ (1 step)
┃           ┃     ┣━━┓
┃           ┃     ┃  │
┃           ┃     ┃  └─ 63 (leaf, pending)
┃           ┃     ┃      k: #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃           ┃     ┃      pc: _PC_CELL:Int
┃           ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃     ┃
┃           ┃     ┗━━┓
┃           ┃        │
┃           ┃        └─ 64 (leaf, pending)
┃           ┃            k: LOG ( _N:Int ) W0:Int W4:Int ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃           ┃            pc: _PC_CELL:Int
┃           ┃            callDepth: _CALLDEPTH_CELL:Int
┃           ┃            statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              ├─ 32
┃              │   k: #exec [ LOG ( _N:Int ) ] ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃              │   pc: _PC_CELL:Int
┃              │   callDepth: _CALLDEPTH_CELL:Int
┃              │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┃ (1 step)
┃              ┣━━┓
┃              ┃  │
┃              ┃  ├─ 48 (split)
┃              ┃  │   k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W5:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃              ┃  │   pc: _PC_CELL:Int
┃              ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃              ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃  ┃
┃              ┃  ┃ (branch)
┃              ┃  ┣━━┓ subst: .Subst
┃              ┃  ┃  ┃ constraint:
┃              ┃  ┃  ┃     _USEGAS_CELL:Bool
┃              ┃  ┃  │
┃              ┃  ┃  └─ 65 (leaf, pending)
┃              ┃  ┃      k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W5:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃              ┃  ┃      pc: _PC_CELL:Int
┃              ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃              ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃  ┃
┃              ┃  ┗━━┓ subst: .Subst
┃              ┃     ┃ constraint:
┃              ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃              ┃     │
┃              ┃     └─ 66 (leaf, pending)
┃              ┃         k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W5:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃              ┃         pc: _PC_CELL:Int
┃              ┃         callDepth: _CALLDEPTH_CELL:Int
┃              ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┗━━┓
┃                 │
┃                 ├─ 49
┃                 │   k: #exec [ LOG ( _N:Int ) ] ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃                 │   pc: _PC_CELL:Int
┃                 │   callDepth: _CALLDEPTH_CELL:Int
┃                 │   statusCode: _STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┃ (1 step)
┃                 ┣━━┓
┃                 ┃  │
┃                 ┃  └─ 73 (leaf, pending)
┃                 ┃      k: #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W6:Int ] ~> LOG ( _N:Int ) W0:Int  ...
┃                 ┃      pc: _PC_CELL:Int
┃                 ┃      callDepth: _CALLDEPTH_CELL:Int
┃                 ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┗━━┓
┃                    │
┃                    └─ 74 (leaf, pending)
┃                        k: #exec [ LOG ( _N:Int ) ] ~> #pc [ LOG ( _N:Int ) ] ~> _K_CELL:K
┃                        pc: _PC_CELL:Int
┃                        callDepth: _CALLDEPTH_CELL:Int
┃                        statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _STATIC_CELL:Bool
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int ( _N:Int +Int 2 ) )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
   │
   ├─ 6
   │   k: #next [ LOG ( _N:Int ) ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   └─ 10 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_STATIC_MODE_VIOLATION


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-LOG-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-7]: <kevm>
           <k>
             ( #next [ LOG ( _N:Int ) ] ~> .K => #exec [ LOG ( _N:Int ) ]
             ~> #pc [ LOG ( _N:Int ) ] )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   _WORDSTACK_CELL:WordStack
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-5-TO-7)]
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ LOG ( _N:Int ) ] => #halt )
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
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int ( _N:Int +Int 2 )
      [priority(20), label(BASIC-BLOCK-3-TO-8)]
    
    rule [BASIC-BLOCK-4-TO-9]: <kevm>
           <k>
             ( #next [ LOG ( _N:Int ) ] => #halt )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( -2 -Int _N:Int ) ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-9)]
    
    rule [BASIC-BLOCK-6-TO-10]: <kevm>
           <k>
             ( #next [ LOG ( _N:Int ) ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
                 <wordStack>
                   _WORDSTACK_CELL:WordStack
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-6-TO-10)]
    
    rule [BASIC-BLOCK-14-TO-19]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ] ~> .K => .K )
             ~> LOG ( _N:Int ) W0:Int W1:Int
             ~> #pc [ LOG ( _N:Int ) ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-14-TO-19)]
    
    rule [BASIC-BLOCK-13-TO-24]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ LOG ( _N:Int ) W0:Int W1:Int ]
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ] )
             ~> LOG ( _N:Int ) W0:Int W1:Int
             ~> #pc [ LOG ( _N:Int ) ]
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
                   WS:WordStack
                 </wordStack>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) )
                 </memoryUsed>
                 <static>
                   false
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
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-13-TO-24)]
    
    rule [BASIC-BLOCK-18-TO-30]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ] ~> .K => .K )
             ~> LOG ( _N:Int ) W0:Int W2:Int
             ~> #pc [ LOG ( _N:Int ) ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   WS0:WordStack
                 </wordStack>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-18-TO-30)]
    
    rule [BASIC-BLOCK-17-TO-33]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ LOG ( _N:Int ) W0:Int W2:Int ]
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ] )
             ~> LOG ( _N:Int ) W0:Int W2:Int
             ~> #pc [ LOG ( _N:Int ) ]
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
                   WS0:WordStack
                 </wordStack>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) )
                 </memoryUsed>
                 <static>
                   false
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
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-17-TO-33)]
    
    rule [BASIC-BLOCK-25-TO-36]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) W0:Int W1:Int ] ~> .K => ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int ( _N:Int *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
             ~> #deductGas )
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ]
             ~> LOG ( _N:Int ) W0:Int W1:Int
             ~> #pc [ LOG ( _N:Int ) ]
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
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int )
                 </memoryUsed>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               ))))))
      [priority(20), label(BASIC-BLOCK-25-TO-36)]
    
    rule [BASIC-BLOCK-29-TO-42]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W3:Int ] ~> .K => .K )
             ~> LOG ( _N:Int ) W0:Int W3:Int
             ~> #pc [ LOG ( _N:Int ) ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   WS1:WordStack
                 </wordStack>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W3:Int : WS1:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W3:Int andBool _WS ==K WS1:WordStack ) )
       andBool ( ( notBool ( _W2 ==Int W3:Int andBool _WS0 ==K WS1:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS1:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-29-TO-42)]
    
    rule [BASIC-BLOCK-26-TO-43]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #gas [ LOG ( _N:Int ) W0:Int W1:Int ]
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ]
             ~> LOG ( _N:Int ) W0:Int W1:Int
             ~> #pc [ LOG ( _N:Int ) ] => #halt ~> .K )
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
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int )
                 </memoryUsed>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-26-TO-43)]
    
    rule [BASIC-BLOCK-28-TO-47]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W3:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ LOG ( _N:Int ) W0:Int W3:Int ]
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W3:Int ] )
             ~> LOG ( _N:Int ) W0:Int W3:Int
             ~> #pc [ LOG ( _N:Int ) ]
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
                   WS1:WordStack
                 </wordStack>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W3:Int ) )
                 </memoryUsed>
                 <static>
                   false
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
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W3:Int : WS1:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W3:Int andBool _WS ==K WS1:WordStack ) )
       andBool ( ( notBool ( _W2 ==Int W3:Int andBool _WS0 ==K WS1:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS1:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-28-TO-47)]
    
    rule [BASIC-BLOCK-37-TO-52]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) W0:Int W2:Int ] ~> .K => ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W2:Int ) ) +Int ( _N:Int *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
             ~> #deductGas )
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ]
             ~> LOG ( _N:Int ) W0:Int W2:Int
             ~> #pc [ LOG ( _N:Int ) ]
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
                   WS0:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int )
                 </memoryUsed>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               )))))))
      [priority(20), label(BASIC-BLOCK-37-TO-52)]
    
    rule [BASIC-BLOCK-41-TO-53]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W4:Int ] ~> .K => .K )
             ~> LOG ( _N:Int ) W0:Int W4:Int
             ~> #pc [ LOG ( _N:Int ) ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   WS2:WordStack
                 </wordStack>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W4:Int : WS2:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS2:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W4:Int andBool _WS ==K WS2:WordStack ) )
       andBool ( ( notBool ( _W2 ==Int W4:Int andBool _WS0 ==K WS2:WordStack ) )
       andBool ( ( notBool ( _W3 ==Int W4:Int andBool _WS1 ==K WS2:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS2:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               ))))))))
      [priority(20), label(BASIC-BLOCK-41-TO-53)]
    
    rule [BASIC-BLOCK-44-TO-54]: <kevm>
           <k>
             ( #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ] ~> .K => .K )
             ~> LOG ( _N:Int ) W0:Int W1:Int
             ~> #pc [ LOG ( _N:Int ) ]
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
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int ( _N:Int *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int )
                 </memoryUsed>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int ( _N:Int *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))))))
      [priority(20), label(BASIC-BLOCK-44-TO-54)]
    
    rule [BASIC-BLOCK-40-TO-55]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W4:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W4:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ LOG ( _N:Int ) W0:Int W4:Int ]
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W4:Int ] )
             ~> LOG ( _N:Int ) W0:Int W4:Int
             ~> #pc [ LOG ( _N:Int ) ]
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
                   WS2:WordStack
                 </wordStack>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W4:Int ) )
                 </memoryUsed>
                 <static>
                   false
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
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W4:Int : WS2:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS2:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W4:Int andBool _WS ==K WS2:WordStack ) )
       andBool ( ( notBool ( _W2 ==Int W4:Int andBool _WS0 ==K WS2:WordStack ) )
       andBool ( ( notBool ( _W3 ==Int W4:Int andBool _WS1 ==K WS2:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS2:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
               ))))))))
      [priority(20), label(BASIC-BLOCK-40-TO-55)]
    
    rule [BASIC-BLOCK-38-TO-59]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #gas [ LOG ( _N:Int ) W0:Int W2:Int ]
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ]
             ~> LOG ( _N:Int ) W0:Int W2:Int
             ~> #pc [ LOG ( _N:Int ) ] => #halt ~> .K )
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
                   WS0:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int )
                 </memoryUsed>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))))))
      [priority(20), label(BASIC-BLOCK-38-TO-59)]
    
    rule [BASIC-BLOCK-45-TO-72]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W1:Int ]
             ~> LOG ( _N:Int ) W0:Int W1:Int
             ~> #pc [ LOG ( _N:Int ) ] => #halt ~> .K )
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
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int )
                 </memoryUsed>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int ( _N:Int *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
               )))))))
      [priority(20), label(BASIC-BLOCK-45-TO-72)]
    
    rule [BASIC-BLOCK-56-TO-75]: <kevm>
           <k>
             ( #gas [ LOG ( _N:Int ) W0:Int W3:Int ] ~> .K => ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W3:Int ) ) +Int ( _N:Int *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
             ~> #deductGas )
             ~> #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W3:Int ]
             ~> LOG ( _N:Int ) W0:Int W3:Int
             ~> #pc [ LOG ( _N:Int ) ]
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
                   WS1:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W3:Int )
                 </memoryUsed>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W3:Int : WS1:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W3:Int andBool _WS ==K WS1:WordStack ) )
       andBool ( ( notBool ( _W2 ==Int W3:Int andBool _WS0 ==K WS1:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS1:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W3:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               ))))))))
      [priority(20), label(BASIC-BLOCK-56-TO-75)]
    
    rule [BASIC-BLOCK-60-TO-76]: <kevm>
           <k>
             ( #access [ LOG ( _N:Int ) , LOG ( _N:Int ) W0:Int W2:Int ] ~> .K => .K )
             ~> LOG ( _N:Int ) W0:Int W2:Int
             ~> #pc [ LOG ( _N:Int ) ]
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
                   WS0:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W2:Int ) ) +Int ( _N:Int *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int )
                 </memoryUsed>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int ( _N:Int +Int 2 ) )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int ( -2 -Int _N:Int ) ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W2:Int ) ) +Int ( _N:Int *Int Glogtopic < _SCHEDULE_CELL:Schedule > ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , W2:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))))))
      [priority(20), label(BASIC-BLOCK-60-TO-76)]

endmodule
