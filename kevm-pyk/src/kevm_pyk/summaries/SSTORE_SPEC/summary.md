
┌─ 1 (root, split, init)
│   k: #next [ SSTORE ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2
┃  │
┃  ├─ 3
┃  │   k: #next [ SSTORE ] ~> _K_CELL:K
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
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ SSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 8 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
┃  ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024 )
┃  │
┃  ├─ 5
┃  │   k: #next [ SSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  ├─ 7
┃  │   k: #exec [ SSTORE ] ~> #pc [ SSTORE ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 11 (split)
┃  ┃  │   k: #gas [ SSTORE , SSTORE W0:Int W1:Int ] ~> SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ...
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
┃  ┃  ┃  │   k: #gas [ SSTORE , SSTORE W0:Int W1:Int ] ~> SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (3 steps)
┃  ┃  ┃  ├─ 22
┃  ┃  ┃  │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE W0:Int W1:Int ) ~> #deductGas ~> #ac ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 25
┃  ┃  ┃  ┃  │   k: Csstore ( _SCHEDULE_CELL:Schedule , W1:Int , #lookup ( STORAGE:Map , W0:Int ) ,  ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 36 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #access [ SSTORE , SSTORE W0:Int W1:Int ] ~> SSTORE W0:Int W1:Int ~> #pc [ SSTOR ...
┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 37 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ SSTORE , SSTORE W0:Int W1:Int ] ~> SSTORE W0:I ...
┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃     └─ 38 (leaf, pending)
┃  ┃  ┃  ┃         k: Csstore ( _SCHEDULE_CELL:Schedule , W1:Int , #lookup ( STORAGE:Map , W0:Int ) ,  ...
┃  ┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 26
┃  ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #deductGas ~> #access [ SSTORE , SSTORE W0:Int W1:Int ]  ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  │  (5 steps)
┃  ┃  ┃  ┃  └─ 41 (leaf, pending)
┃  ┃  ┃  ┃      k: #halt ~> _K_CELL:K
┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓
┃  ┃  ┃     │
┃  ┃  ┃     ├─ 27
┃  ┃  ┃     │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE W0:Int W1:Int ) ~> #deductGas ~> #ac ...
┃  ┃  ┃     │   pc: _PC_CELL:Int
┃  ┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃
┃  ┃  ┃     ┃ (1 step)
┃  ┃  ┃     ┣━━┓
┃  ┃  ┃     ┃  │
┃  ┃  ┃     ┃  └─ 39 (leaf, pending)
┃  ┃  ┃     ┃      k: Csstore ( _SCHEDULE_CELL:Schedule , W1:Int , #lookup ( STORAGE0:Map , W0:Int ) , ...
┃  ┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃
┃  ┃  ┃     ┗━━┓
┃  ┃  ┃        │
┃  ┃  ┃        └─ 40 (leaf, pending)
┃  ┃  ┃            k: #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE W0:Int W1:Int ) ~> #deductGas ~> #ac ...
┃  ┃  ┃            pc: _PC_CELL:Int
┃  ┃  ┃            callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃            statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃  ┃     │
┃  ┃     ├─ 14
┃  ┃     │   k: #gas [ SSTORE , SSTORE W0:Int W1:Int ] ~> SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ...
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     │
┃  ┃     │  (1 step)
┃  ┃     ├─ 17
┃  ┃     │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┃ (1 step)
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  └─ 20 (leaf, pending)
┃  ┃     ┃      k: #pc [ SSTORE ] ~> _K_CELL:K
┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┗━━┓
┃  ┃        │
┃  ┃        ├─ 21
┃  ┃        │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
┃  ┃        │   pc: _PC_CELL:Int
┃  ┃        │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┃ (1 step)
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  └─ 28 (leaf, pending)
┃  ┃        ┃      k: #pc [ SSTORE ] ~> _K_CELL:K
┃  ┃        ┃      pc: _PC_CELL:Int
┃  ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┗━━┓
┃  ┃           │
┃  ┃           ├─ 29
┃  ┃           │   k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
┃  ┃           │   pc: _PC_CELL:Int
┃  ┃           │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┃ (1 step)
┃  ┃           ┣━━┓
┃  ┃           ┃  │
┃  ┃           ┃  └─ 42 (leaf, pending)
┃  ┃           ┃      k: #pc [ SSTORE ] ~> _K_CELL:K
┃  ┃           ┃      pc: _PC_CELL:Int
┃  ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┗━━┓
┃  ┃              │
┃  ┃              └─ 43 (leaf, pending)
┃  ┃                  k: SSTORE W0:Int W1:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
┃  ┃                  pc: _PC_CELL:Int
┃  ┃                  callDepth: _CALLDEPTH_CELL:Int
┃  ┃                  statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 12
┃     │   k: #exec [ SSTORE ] ~> #pc [ SSTORE ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  ├─ 15 (split)
┃     ┃  │   k: #gas [ SSTORE , SSTORE W0:Int W2:Int ] ~> SSTORE W0:Int W2:Int ~> #pc [ SSTORE ] ...
┃     ┃  │   pc: _PC_CELL:Int
┃     ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┃ (branch)
┃     ┃  ┣━━┓ subst: .Subst
┃     ┃  ┃  ┃ constraint:
┃     ┃  ┃  ┃     _USEGAS_CELL:Bool
┃     ┃  ┃  │
┃     ┃  ┃  ├─ 18
┃     ┃  ┃  │   k: #gas [ SSTORE , SSTORE W0:Int W2:Int ] ~> SSTORE W0:Int W2:Int ~> #pc [ SSTORE ] ...
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  │
┃     ┃  ┃  │  (3 steps)
┃     ┃  ┃  ├─ 35
┃     ┃  ┃  │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE W0:Int W2:Int ) ~> #deductGas ~> #ac ...
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┃ (1 step)
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 46 (leaf, pending)
┃     ┃  ┃  ┃      k: Csstore ( _SCHEDULE_CELL:Schedule , W2:Int , #lookup ( STORAGE:Map , W0:Int ) ,  ...
┃     ┃  ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 47 (leaf, pending)
┃     ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #deductGas ~> #access [ SSTORE , SSTORE W0:Int W2:Int ]  ...
┃     ┃  ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┗━━┓
┃     ┃  ┃     │
┃     ┃  ┃     └─ 48 (leaf, pending)
┃     ┃  ┃         k: #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE W0:Int W2:Int ) ~> #deductGas ~> #ac ...
┃     ┃  ┃         pc: _PC_CELL:Int
┃     ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┗━━┓ subst: .Subst
┃     ┃     ┃ constraint:
┃     ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃     ┃     │
┃     ┃     ├─ 19
┃     ┃     │   k: #gas [ SSTORE , SSTORE W0:Int W2:Int ] ~> SSTORE W0:Int W2:Int ~> #pc [ SSTORE ] ...
┃     ┃     │   pc: _PC_CELL:Int
┃     ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     │
┃     ┃     │  (1 step)
┃     ┃     ├─ 34
┃     ┃     │   k: SSTORE W0:Int W2:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
┃     ┃     │   pc: _PC_CELL:Int
┃     ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     ┃
┃     ┃     ┃ (1 step)
┃     ┃     ┣━━┓
┃     ┃     ┃  │
┃     ┃     ┃  └─ 44 (leaf, pending)
┃     ┃     ┃      k: #pc [ SSTORE ] ~> _K_CELL:K
┃     ┃     ┃      pc: _PC_CELL:Int
┃     ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     ┃
┃     ┃     ┗━━┓
┃     ┃        │
┃     ┃        └─ 45 (leaf, pending)
┃     ┃            k: SSTORE W0:Int W2:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
┃     ┃            pc: _PC_CELL:Int
┃     ┃            callDepth: _CALLDEPTH_CELL:Int
┃     ┃            statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 16
┃        │   k: #exec [ SSTORE ] ~> #pc [ SSTORE ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  ├─ 23 (split)
┃        ┃  │   k: #gas [ SSTORE , SSTORE W0:Int W3:Int ] ~> SSTORE W0:Int W3:Int ~> #pc [ SSTORE ] ...
┃        ┃  │   pc: _PC_CELL:Int
┃        ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┃ (branch)
┃        ┃  ┣━━┓ subst: .Subst
┃        ┃  ┃  ┃ constraint:
┃        ┃  ┃  ┃     _USEGAS_CELL:Bool
┃        ┃  ┃  │
┃        ┃  ┃  └─ 30 (leaf, pending)
┃        ┃  ┃      k: #gas [ SSTORE , SSTORE W0:Int W3:Int ] ~> SSTORE W0:Int W3:Int ~> #pc [ SSTORE ] ...
┃        ┃  ┃      pc: _PC_CELL:Int
┃        ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┗━━┓ subst: .Subst
┃        ┃     ┃ constraint:
┃        ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃        ┃     │
┃        ┃     ├─ 31
┃        ┃     │   k: #gas [ SSTORE , SSTORE W0:Int W3:Int ] ~> SSTORE W0:Int W3:Int ~> #pc [ SSTORE ] ...
┃        ┃     │   pc: _PC_CELL:Int
┃        ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃     │
┃        ┃     │  (1 step)
┃        ┃     └─ 51 (leaf, pending)
┃        ┃         k: SSTORE W0:Int W3:Int ~> #pc [ SSTORE ] ~> _K_CELL:K
┃        ┃         pc: _PC_CELL:Int
┃        ┃         callDepth: _CALLDEPTH_CELL:Int
┃        ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 24
┃           │   k: #exec [ SSTORE ] ~> #pc [ SSTORE ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  ├─ 32 (split)
┃           ┃  │   k: #gas [ SSTORE , SSTORE W0:Int W4:Int ] ~> SSTORE W0:Int W4:Int ~> #pc [ SSTORE ] ...
┃           ┃  │   pc: _PC_CELL:Int
┃           ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┃ (branch)
┃           ┃  ┣━━┓ subst: .Subst
┃           ┃  ┃  ┃ constraint:
┃           ┃  ┃  ┃     _USEGAS_CELL:Bool
┃           ┃  ┃  │
┃           ┃  ┃  └─ 49 (leaf, pending)
┃           ┃  ┃      k: #gas [ SSTORE , SSTORE W0:Int W4:Int ] ~> SSTORE W0:Int W4:Int ~> #pc [ SSTORE ] ...
┃           ┃  ┃      pc: _PC_CELL:Int
┃           ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┗━━┓ subst: .Subst
┃           ┃     ┃ constraint:
┃           ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃           ┃     │
┃           ┃     └─ 50 (leaf, pending)
┃           ┃         k: #gas [ SSTORE , SSTORE W0:Int W4:Int ] ~> SSTORE W0:Int W4:Int ~> #pc [ SSTORE ] ...
┃           ┃         pc: _PC_CELL:Int
┃           ┃         callDepth: _CALLDEPTH_CELL:Int
┃           ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              └─ 33 (leaf, pending)
┃                  k: #exec [ SSTORE ] ~> #pc [ SSTORE ] ~> _K_CELL:K
┃                  pc: _PC_CELL:Int
┃                  callDepth: _CALLDEPTH_CELL:Int
┃                  statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _STATIC_CELL:Bool
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024 )
   │
   ├─ 6
   │   k: #next [ SSTORE ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   └─ 9 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_STATIC_MODE_VIOLATION


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SSTORE-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-7]: <kevm>
           <k>
             ( #next [ SSTORE ] ~> .K => #exec [ SSTORE ]
             ~> #pc [ SSTORE ] )
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-5-TO-7)]
    
    rule [BASIC-BLOCK-4-TO-8]: <kevm>
           <k>
             ( #next [ SSTORE ] => #halt )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-8)]
    
    rule [BASIC-BLOCK-6-TO-9]: <kevm>
           <k>
             ( #next [ SSTORE ] => #halt )
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -2 ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-6-TO-9)]
    
    rule [BASIC-BLOCK-3-TO-10]: <kevm>
           <k>
             ( #next [ SSTORE ] => #halt )
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
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 2
      [priority(20), label(BASIC-BLOCK-3-TO-10)]
    
    rule [BASIC-BLOCK-14-TO-17]: <kevm>
           <k>
             ( #gas [ SSTORE , SSTORE W0:Int W1:Int ] ~> .K => .K )
             ~> SSTORE W0:Int W1:Int
             ~> #pc [ SSTORE ]
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -2 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-14-TO-17)]
    
    rule [BASIC-BLOCK-13-TO-22]: <kevm>
           <k>
             ( #gas [ SSTORE , SSTORE W0:Int W1:Int ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE W0:Int W1:Int )
             ~> #deductGas
             ~> #access [ SSTORE , SSTORE W0:Int W1:Int ] )
             ~> SSTORE W0:Int W1:Int
             ~> #pc [ SSTORE ]
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -2 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-13-TO-22)]
    
    rule [BASIC-BLOCK-19-TO-34]: <kevm>
           <k>
             ( #gas [ SSTORE , SSTORE W0:Int W2:Int ] ~> .K => .K )
             ~> SSTORE W0:Int W2:Int
             ~> #pc [ SSTORE ]
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
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int -2 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-19-TO-34)]
    
    rule [BASIC-BLOCK-18-TO-35]: <kevm>
           <k>
             ( #gas [ SSTORE , SSTORE W0:Int W2:Int ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , SSTORE W0:Int W2:Int )
             ~> #deductGas
             ~> #access [ SSTORE , SSTORE W0:Int W2:Int ] )
             ~> SSTORE W0:Int W2:Int
             ~> #pc [ SSTORE ]
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
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W2:Int : WS0:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 2 ) +Int -2 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W2:Int andBool _WS ==K WS0:WordStack ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-18-TO-35)]
    
    rule [BASIC-BLOCK-26-TO-41]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #deductGas
             ~> #access [ SSTORE , SSTORE W0:Int W1:Int ]
             ~> SSTORE W0:Int W1:Int
             ~> #pc [ SSTORE ] => #halt ~> .K )
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
       andBool ( Ghassstorestipend << _SCHEDULE_CELL:Schedule >>
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W1:Int : WS:WordStack ) )
       andBool ( _GAS_CELL:Gas <=Gas Gcallstipend < _SCHEDULE_CELL:Schedule >
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 2 ) +Int -2 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-26-TO-41)]
    
    rule [BASIC-BLOCK-31-TO-51]: <kevm>
           <k>
             ( #gas [ SSTORE , SSTORE W0:Int W3:Int ] ~> .K => .K )
             ~> SSTORE W0:Int W3:Int
             ~> #pc [ SSTORE ]
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
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 2 ) <Int 2 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : ( W3:Int : WS1:WordStack ) )
       andBool ( ( notBool ( #sizeWordStack ( WS1:WordStack , 2 ) +Int -2 ) >Int 1024 )
       andBool ( ( notBool ( _W1 ==Int W3:Int andBool _WS ==K WS1:WordStack ) )
       andBool ( ( notBool ( _W2 ==Int W3:Int andBool _WS0 ==K WS1:WordStack ) )
               )))))))
      [priority(20), label(BASIC-BLOCK-31-TO-51)]

endmodule
