
┌─ 1 (root, split, init)
│   k: #next [ LOG ( 1 ) ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WS:WordStack , 1 ) <Int 3
┃  │
┃  ├─ 3
┃  │   k: #next [ LOG ( 1 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 7 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_UNDERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     3 <=Int #sizeWordStack ( _WS:WordStack , 1 )
┃  │
┃  ├─ 4
┃  │   k: #next [ LOG ( 1 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  ├─ 6
┃  │   k: #exec [ LOG ( 1 ) ] ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 9 (split)
┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 12
┃  ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ├─ 19
┃  ┃  ┃  │   k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  └─ 20 (leaf, pending)
┃  ┃  ┃  ┃      k: #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓
┃  ┃  ┃     │
┃  ┃  ┃     └─ 21 (stuck, leaf)
┃  ┃  ┃         k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     _USEGAS_CELL:Bool
┃  ┃  ┃  ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 68
┃  ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (10 steps)
┃  ┃  ┃  └─ 49 (leaf, terminal)
┃  ┃  ┃      k: #halt ~> _K_CELL:K
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
┃  ┃  ┃
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     _USEGAS_CELL:Bool
┃  ┃  ┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃  ┃  ┃     ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 79
┃  ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (9 steps)
┃  ┃  ┃  └─ 58 (leaf, pending)
┃  ┃  ┃      k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     _USEGAS_CELL:Bool
┃  ┃     ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > )
┃  ┃     │
┃  ┃     ├─ 80
┃  ┃     │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     │
┃  ┃     │  (7 steps)
┃  ┃     └─ 42 (leaf, pending)
┃  ┃         k: ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > ...
┃  ┃         pc: _PC_CELL:Int
┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 10
┃     │   k: #exec [ LOG ( 1 ) ] ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  ├─ 13 (split)
┃     ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃     ┃  │   pc: _PC_CELL:Int
┃     ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┃ (branch)
┃     ┃  ┣━━┓ subst: .Subst
┃     ┃  ┃  ┃ constraint:
┃     ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃     ┃  ┃  │
┃     ┃  ┃  ├─ 16
┃     ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  │
┃     ┃  ┃  │  (1 step)
┃     ┃  ┃  ├─ 29
┃     ┃  ┃  │   k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┃ (1 step)
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 31 (leaf, pending)
┃     ┃  ┃  ┃      k: #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃     ┃  ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┗━━┓
┃     ┃  ┃     │
┃     ┃  ┃     └─ 32 (stuck, leaf)
┃     ┃  ┃         k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃     ┃  ┃         pc: _PC_CELL:Int
┃     ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┣━━┓ subst: .Subst
┃     ┃  ┃  ┃ constraint:
┃     ┃  ┃  ┃     _USEGAS_CELL:Bool
┃     ┃  ┃  ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃     ┃  ┃  │
┃     ┃  ┃  ├─ 70
┃     ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  │
┃     ┃  ┃  │  (10 steps)
┃     ┃  ┃  └─ 61 (leaf, pending)
┃     ┃  ┃      k: #halt ~> _K_CELL:K
┃     ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃      statusCode: EVMC_OUT_OF_GAS
┃     ┃  ┃
┃     ┃  ┣━━┓ subst: .Subst
┃     ┃  ┃  ┃ constraint:
┃     ┃  ┃  ┃     _USEGAS_CELL:Bool
┃     ┃  ┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃     ┃  ┃  ┃     ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃     ┃  ┃  │
┃     ┃  ┃  ├─ 81
┃     ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  │
┃     ┃  ┃  │  (7 steps)
┃     ┃  ┃  └─ 56 (leaf, pending)
┃     ┃  ┃      k: ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > ...
┃     ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┗━━┓ subst: .Subst
┃     ┃     ┃ constraint:
┃     ┃     ┃     _USEGAS_CELL:Bool
┃     ┃     ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃     ┃     ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > )
┃     ┃     │
┃     ┃     ├─ 82
┃     ┃     │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃     ┃     │   pc: _PC_CELL:Int
┃     ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     │
┃     ┃     │  (7 steps)
┃     ┃     └─ 57 (leaf, pending)
┃     ┃         k: ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > ...
┃     ┃         pc: _PC_CELL:Int
┃     ┃         callDepth: _CALLDEPTH_CELL:Int
┃     ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 14
┃        │   k: #exec [ LOG ( 1 ) ] ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  ├─ 17 (split)
┃        ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃        ┃  │   pc: _PC_CELL:Int
┃        ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┃ (branch)
┃        ┃  ┣━━┓ subst: .Subst
┃        ┃  ┃  ┃ constraint:
┃        ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃        ┃  ┃  │
┃        ┃  ┃  ├─ 26
┃        ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃        ┃  ┃  │   pc: _PC_CELL:Int
┃        ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  │
┃        ┃  ┃  │  (1 step)
┃        ┃  ┃  ├─ 38
┃        ┃  ┃  │   k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃        ┃  ┃  │   pc: _PC_CELL:Int
┃        ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┃ (1 step)
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  └─ 44 (leaf, pending)
┃        ┃  ┃  ┃      k: #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃        ┃  ┃  ┃      pc: _PC_CELL:Int
┃        ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┗━━┓
┃        ┃  ┃     │
┃        ┃  ┃     └─ 45 (stuck, leaf)
┃        ┃  ┃         k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃        ┃  ┃         pc: _PC_CELL:Int
┃        ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┣━━┓ subst: .Subst
┃        ┃  ┃  ┃ constraint:
┃        ┃  ┃  ┃     _USEGAS_CELL:Bool
┃        ┃  ┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃        ┃  ┃  │
┃        ┃  ┃  ├─ 73
┃        ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃        ┃  ┃  │   pc: _PC_CELL:Int
┃        ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  │
┃        ┃  ┃  │  (7 steps)
┃        ┃  ┃  └─ 66 (leaf, pending)
┃        ┃  ┃      k: ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > ...
┃        ┃  ┃      pc: _PC_CELL:Int
┃        ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┗━━┓ subst: .Subst
┃        ┃     ┃ constraint:
┃        ┃     ┃     _USEGAS_CELL:Bool
┃        ┃     ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃        ┃     │
┃        ┃     ├─ 74
┃        ┃     │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃        ┃     │   pc: _PC_CELL:Int
┃        ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃     │
┃        ┃     │  (4 steps)
┃        ┃     └─ 52 (leaf, pending)
┃        ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _ ...
┃        ┃         pc: _PC_CELL:Int
┃        ┃         callDepth: _CALLDEPTH_CELL:Int
┃        ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 18
┃           │   k: #exec [ LOG ( 1 ) ] ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  ├─ 27 (split)
┃           ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃           ┃  │   pc: _PC_CELL:Int
┃           ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┃ (branch)
┃           ┃  ┣━━┓ subst: .Subst
┃           ┃  ┃  ┃ constraint:
┃           ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃           ┃  ┃  │
┃           ┃  ┃  ├─ 37
┃           ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃           ┃  ┃  │   pc: _PC_CELL:Int
┃           ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃  │
┃           ┃  ┃  │  (1 step)
┃           ┃  ┃  ├─ 50
┃           ┃  ┃  │   k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃           ┃  ┃  │   pc: _PC_CELL:Int
┃           ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃  ┃
┃           ┃  ┃  ┃ (1 step)
┃           ┃  ┃  ┣━━┓
┃           ┃  ┃  ┃  │
┃           ┃  ┃  ┃  └─ 59 (leaf, pending)
┃           ┃  ┃  ┃      k: #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃           ┃  ┃  ┃      pc: _PC_CELL:Int
┃           ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃  ┃
┃           ┃  ┃  ┗━━┓
┃           ┃  ┃     │
┃           ┃  ┃     └─ 60 (leaf, pending)
┃           ┃  ┃         k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃           ┃  ┃         pc: _PC_CELL:Int
┃           ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┣━━┓ subst: .Subst
┃           ┃  ┃  ┃ constraint:
┃           ┃  ┃  ┃     _USEGAS_CELL:Bool
┃           ┃  ┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃           ┃  ┃  │
┃           ┃  ┃  ├─ 77
┃           ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃           ┃  ┃  │   pc: _PC_CELL:Int
┃           ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃  │
┃           ┃  ┃  │  (4 steps)
┃           ┃  ┃  └─ 64 (leaf, pending)
┃           ┃  ┃      k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _ ...
┃           ┃  ┃      pc: _PC_CELL:Int
┃           ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┗━━┓ subst: .Subst
┃           ┃     ┃ constraint:
┃           ┃     ┃     _USEGAS_CELL:Bool
┃           ┃     ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃           ┃     │
┃           ┃     ├─ 78
┃           ┃     │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃           ┃     │   pc: _PC_CELL:Int
┃           ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃     │
┃           ┃     │  (4 steps)
┃           ┃     └─ 65 (leaf, pending)
┃           ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _ ...
┃           ┃         pc: _PC_CELL:Int
┃           ┃         callDepth: _CALLDEPTH_CELL:Int
┃           ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              ├─ 28
┃              │   k: #exec [ LOG ( 1 ) ] ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃              │   pc: _PC_CELL:Int
┃              │   callDepth: _CALLDEPTH_CELL:Int
┃              │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┃ (1 step)
┃              ┣━━┓
┃              ┃  │
┃              ┃  ├─ 39 (split)
┃              ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃              ┃  │   pc: _PC_CELL:Int
┃              ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃              ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃  ┃
┃              ┃  ┃ (branch)
┃              ┃  ┣━━┓ subst: .Subst
┃              ┃  ┃  ┃ constraint:
┃              ┃  ┃  ┃     _USEGAS_CELL:Bool
┃              ┃  ┃  │
┃              ┃  ┃  ├─ 47
┃              ┃  ┃  │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃              ┃  ┃  │   pc: _PC_CELL:Int
┃              ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃              ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃  ┃  │
┃              ┃  ┃  │  (4 steps)
┃              ┃  ┃  └─ 63 (leaf, pending)
┃              ┃  ┃      k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _ ...
┃              ┃  ┃      pc: _PC_CELL:Int
┃              ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃              ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃  ┃
┃              ┃  ┗━━┓ subst: .Subst
┃              ┃     ┃ constraint:
┃              ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃              ┃     │
┃              ┃     ├─ 48
┃              ┃     │   k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃              ┃     │   pc: _PC_CELL:Int
┃              ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃              ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃     │
┃              ┃     │  (1 step)
┃              ┃     └─ 62 (leaf, pending)
┃              ┃         k: LOG ( 1 ) _W0:Int W1:Int ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃              ┃         pc: _PC_CELL:Int
┃              ┃         callDepth: _CALLDEPTH_CELL:Int
┃              ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┗━━┓
┃                 │
┃                 ├─ 40
┃                 │   k: #exec [ LOG ( 1 ) ] ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃                 │   pc: _PC_CELL:Int
┃                 │   callDepth: _CALLDEPTH_CELL:Int
┃                 │   statusCode: _STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┃ (1 step)
┃                 ┣━━┓
┃                 ┃  │
┃                 ┃  └─ 54 (leaf, pending)
┃                 ┃      k: #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> LOG ( 1 ) _W0:Int W1:Int ~> #pc ...
┃                 ┃      pc: _PC_CELL:Int
┃                 ┃      callDepth: _CALLDEPTH_CELL:Int
┃                 ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┗━━┓
┃                    │
┃                    └─ 55 (leaf, pending)
┃                        k: #exec [ LOG ( 1 ) ] ~> #pc [ LOG ( 1 ) ] ~> _K_CELL:K
┃                        pc: _PC_CELL:Int
┃                        callDepth: _CALLDEPTH_CELL:Int
┃                        statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _STATIC_CELL:Bool
   ┃     3 <=Int #sizeWordStack ( _WS:WordStack , 1 )
   │
   ├─ 5
   │   k: #next [ LOG ( 1 ) ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   └─ 8 (leaf, terminal)
       k: #halt ~> _K_CELL:K
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: EVMC_STATIC_MODE_VIOLATION


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-LOG-1-SPEC
    
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             ( #next [ LOG ( 1 ) ] ~> .K => #exec [ LOG ( 1 ) ]
             ~> #pc [ LOG ( 1 ) ] )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( __W0 : _WS:WordStack )
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
       andBool ( 3 <=Int #sizeWordStack ( _WS:WordStack , 1 )
               ))
      [priority(20), label(BASIC-BLOCK-4-TO-6)]
    
    rule [BASIC-BLOCK-3-TO-7]: <kevm>
           <k>
             ( #next [ LOG ( 1 ) ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STACK_UNDERFLOW )
               </statusCode>
               <callState>
                 <wordStack>
                   ( __W0 : _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires #sizeWordStack ( _WS:WordStack , 1 ) <Int 3
      [priority(20), label(BASIC-BLOCK-3-TO-7)]
    
    rule [BASIC-BLOCK-5-TO-8]: <kevm>
           <k>
             ( #next [ LOG ( 1 ) ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
                 <wordStack>
                   ( __W0 : _WS:WordStack )
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
       andBool ( 3 <=Int #sizeWordStack ( _WS:WordStack , 1 )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-8)]
    
    rule [BASIC-BLOCK-12-TO-19]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => .K )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
       andBool ( __WS ==K ( W1:Int : WS:WordStack )
       andBool ( 3 <=Int #sizeWordStack ( WS:WordStack , 2 )
               ))))
      [priority(20), label(BASIC-BLOCK-12-TO-19)]
    
    rule [BASIC-BLOCK-16-TO-29]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => .K )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
       andBool ( __WS ==K ( W1:Int : WS0:WordStack )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS0:WordStack , 2 )
               )))))
      [priority(20), label(BASIC-BLOCK-16-TO-29)]
    
    rule [BASIC-BLOCK-26-TO-38]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => .K )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
       andBool ( __WS ==K ( W1:Int : WS1:WordStack )
       andBool ( _WS ~> .K =/=K WS1:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS1:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS1:WordStack , 2 )
               ))))))
      [priority(20), label(BASIC-BLOCK-26-TO-38)]
    
    rule [BASIC-BLOCK-37-TO-50]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => .K )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
       andBool ( __WS ==K ( W1:Int : WS2:WordStack )
       andBool ( _WS ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS1 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS2:WordStack , 2 )
               )))))))
      [priority(20), label(BASIC-BLOCK-37-TO-50)]
    
    rule [BASIC-BLOCK-48-TO-62]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => .K )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   WS3:WordStack
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
       andBool ( __WS ==K ( W1:Int : WS3:WordStack )
       andBool ( _WS ~> .K =/=K WS3:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS3:WordStack ~> .K
       andBool ( _WS1 ~> .K =/=K WS3:WordStack ~> .K
       andBool ( _WS2 ~> .K =/=K WS3:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS3:WordStack , 2 )
               ))))))))
      [priority(20), label(BASIC-BLOCK-48-TO-62)]
    
    rule [BASIC-BLOCK-47-TO-63]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ LOG ( 1 ) _W0:Int W1:Int ]
             ~> #access [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
                   WS3:WordStack
                 </wordStack>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS3:WordStack )
       andBool ( _WS ~> .K =/=K WS3:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS3:WordStack ~> .K
       andBool ( _WS1 ~> .K =/=K WS3:WordStack ~> .K
       andBool ( _WS2 ~> .K =/=K WS3:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS3:WordStack , 2 )
               ))))))))
      [priority(20), label(BASIC-BLOCK-47-TO-63)]
    
    rule [BASIC-BLOCK-74-TO-52]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ LOG ( 1 ) _W0:Int W1:Int ]
             ~> #access [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS1:WordStack )
       andBool ( _WS ~> .K =/=K WS1:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS1:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS1:WordStack , 2 )
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))))))
      [priority(20), label(BASIC-BLOCK-74-TO-52)]
    
    rule [BASIC-BLOCK-77-TO-64]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ LOG ( 1 ) _W0:Int W1:Int ]
             ~> #access [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS2:WordStack )
       andBool ( _WS ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS1 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS2:WordStack , 2 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               ))))))))
      [priority(20), label(BASIC-BLOCK-77-TO-64)]
    
    rule [BASIC-BLOCK-78-TO-65]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ LOG ( 1 ) _W0:Int W1:Int ]
             ~> #access [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS2:WordStack )
       andBool ( _WS ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS1 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS2:WordStack , 2 )
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))))))
      [priority(20), label(BASIC-BLOCK-78-TO-65)]
    
    rule [BASIC-BLOCK-68-TO-49]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ]
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ] => #halt ~> .K )
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
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS:WordStack )
       andBool ( 3 <=Int #sizeWordStack ( WS:WordStack , 2 )
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))))
      [priority(20), label(BASIC-BLOCK-68-TO-49)]
    
    rule [BASIC-BLOCK-70-TO-61]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ]
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ] => #halt ~> .K )
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
                   WS0:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS0:WordStack )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS0:WordStack , 2 )
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-70-TO-61)]
    
    rule [BASIC-BLOCK-73-TO-66]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > )
             ~> #deductGas
             ~> #access [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS1:WordStack )
       andBool ( _WS ~> .K =/=K WS1:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS1:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS1:WordStack , 2 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               )))))))
      [priority(20), label(BASIC-BLOCK-73-TO-66)]
    
    rule [BASIC-BLOCK-79-TO-58]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => .K )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS:WordStack )
       andBool ( 3 <=Int #sizeWordStack ( WS:WordStack , 2 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-79-TO-58)]
    
    rule [BASIC-BLOCK-80-TO-42]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > )
             ~> #deductGas
             ~> #access [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS:WordStack )
       andBool ( 3 <=Int #sizeWordStack ( WS:WordStack , 2 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > )
               ))))))
      [priority(20), label(BASIC-BLOCK-80-TO-42)]
    
    rule [BASIC-BLOCK-81-TO-56]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > )
             ~> #deductGas
             ~> #access [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS0:WordStack )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS0:WordStack , 2 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))))))
      [priority(20), label(BASIC-BLOCK-81-TO-56)]
    
    rule [BASIC-BLOCK-82-TO-57]: <kevm>
           <k>
             ( #gas [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] ~> .K => ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > )
             ~> #deductGas
             ~> #access [ LOG ( 1 ) , LOG ( 1 ) _W0:Int W1:Int ] )
             ~> LOG ( 1 ) _W0:Int W1:Int
             ~> #pc [ LOG ( 1 ) ]
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
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) )
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
       andBool ( __WS ==K ( W1:Int : WS0:WordStack )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( 3 <=Int #sizeWordStack ( WS0:WordStack , 2 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W0:Int , W1:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas ( ( Glog < _SCHEDULE_CELL:Schedule > +Int ( Glogdata < _SCHEDULE_CELL:Schedule > *Int W1:Int ) ) +Int Glogtopic < _SCHEDULE_CELL:Schedule > )
               )))))))
      [priority(20), label(BASIC-BLOCK-82-TO-57)]

endmodule
