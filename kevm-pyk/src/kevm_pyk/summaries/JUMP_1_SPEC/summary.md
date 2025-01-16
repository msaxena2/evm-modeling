
┌─ 1 (root, init)
│   k: #next [ JUMP ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
│
│  (4 steps)
├─ 3
│   k: JUMP W0:Int ~> #pc [ JUMP ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
┃
┃ (1 step)
┣━━┓
┃  │
┃  ├─ 4
┃  │   k: #endBasicBlock ~> #pc [ JUMP ] ~> K_CELL:K
┃  │   pc: W0:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (1 step)
┃  ├─ 6
┃  │   k: #endBasicBlock ~> K_CELL:K
┃  │   pc: W0:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 7
┃  ┃  │   k: #execute ~> _DotVar2:K
┃  ┃  │   pc: W0:Int
┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  ┊  constraint: true
┃  ┃  ┊  subst: ...
┃  ┃  └─ 2 (leaf, target)
┃  ┃      k: K_CELL:K
┃  ┃      pc: FINAL_PC_CELL:Int
┃  ┃      callDepth: FINAL_CALLDEPTH_CELL:Int
┃  ┃      statusCode: FINAL_STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 8
┃  ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃  │   pc: W0:Int
┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (1 step)
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 13
┃  ┃  ┃  │   k: #execute ~> _DotVar3:K
┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ├─ 51
┃  ┃  ┃  │   k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  └─ 93 (leaf, pending)
┃  ┃  ┃  ┃      k: #execute ~> _DotVar3:K
┃  ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  └─ 94 (leaf, pending)
┃  ┃  ┃  ┃      k: #end EVMC_STACK_UNDERFLOW ~> #execute ~> _DotVar3:K
┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  └─ 95 (leaf, pending)
┃  ┃  ┃  ┃      k: #end EVMC_STACK_OVERFLOW ~> #execute ~> _DotVar3:K
┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  └─ 96 (leaf, pending)
┃  ┃  ┃  ┃      k: #addr [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  └─ 97 (leaf, pending)
┃  ┃  ┃  ┃      k: #end EVMC_STATIC_MODE_VIOLATION ~> #execute ~> _DotVar3:K
┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  └─ 98 (leaf, pending)
┃  ┃  ┃  ┃      k: #end EVMC_SUCCESS ~> #execute ~> _DotVar3:K
┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓
┃  ┃  ┃     │
┃  ┃  ┃     └─ 99 (leaf, pending)
┃  ┃  ┃         k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃         pc: W0:Int
┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 14
┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 23
┃  ┃  ┃  ┃  │   k: #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  ├─ 68
┃  ┃  ┃  ┃  │   k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 138 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 139 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #end EVMC_STACK_UNDERFLOW ~> #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 140 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #end EVMC_STACK_OVERFLOW ~> #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 141 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #addr [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 142 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #end EVMC_STATIC_MODE_VIOLATION ~> #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 143 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #end EVMC_SUCCESS ~> #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃     └─ 144 (leaf, pending)
┃  ┃  ┃  ┃         k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃         pc: W0:Int
┃  ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 24
┃  ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ├─ 41
┃  ┃  ┃  ┃  ┃  │   k: #execute ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  ┃  └─ 114 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ├─ 42
┃  ┃  ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  └─ 80 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃      k: #execute ~> _DotVar6:K
┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  ├─ 81
┃  ┃  ┃  ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar6:K
┃  ┃  ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  ┃  └─ 185 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃  ┃      k: #execute ~> _DotVar7:K
┃  ┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  ┃  └─ 186 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar7:K
┃  ┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃  ┃  ┃     └─ 187 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃         k: #endBasicBlock ~> _DotVar6:K
┃  ┃  ┃  ┃  ┃  ┃         pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃  ┃     ├─ 82
┃  ┃  ┃  ┃  ┃     │   k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃     │   pc: W0:Int
┃  ┃  ┃  ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃  ┃     ┃ (1 step)
┃  ┃  ┃  ┃  ┃     ┣━━┓
┃  ┃  ┃  ┃  ┃     ┃  │
┃  ┃  ┃  ┃  ┃     ┃  └─ 188 (leaf, pending)
┃  ┃  ┃  ┃  ┃     ┃      k: #endBasicBlock ~> _DotVar6:K
┃  ┃  ┃  ┃  ┃     ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃  ┃     ┗━━┓
┃  ┃  ┃  ┃  ┃        │
┃  ┃  ┃  ┃  ┃        └─ 189 (leaf, pending)
┃  ┃  ┃  ┃  ┃            k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃            pc: W0:Int
┃  ┃  ┃  ┃  ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃     ├─ 43
┃  ┃  ┃  ┃     │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃     │   pc: W0:Int
┃  ┃  ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃     ┃ (1 step)
┃  ┃  ┃  ┃     ┣━━┓
┃  ┃  ┃  ┃     ┃  │
┃  ┃  ┃  ┃     ┃  ├─ 83
┃  ┃  ┃  ┃     ┃  │   k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃     ┃  │   pc: W0:Int
┃  ┃  ┃  ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃  ┃
┃  ┃  ┃  ┃     ┃  ┃ (1 step)
┃  ┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃  ┃     ┃  ┃  └─ 192 (leaf, pending)
┃  ┃  ┃  ┃     ┃  ┃      k: #execute ~> _DotVar6:K
┃  ┃  ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃  ┃
┃  ┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃  ┃     ┃  ┃  └─ 193 (leaf, pending)
┃  ┃  ┃  ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar6:K
┃  ┃  ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃  ┃
┃  ┃  ┃  ┃     ┃  ┗━━┓
┃  ┃  ┃  ┃     ┃     │
┃  ┃  ┃  ┃     ┃     └─ 194 (leaf, pending)
┃  ┃  ┃  ┃     ┃         k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃     ┃         pc: W0:Int
┃  ┃  ┃  ┃     ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃     ┗━━┓
┃  ┃  ┃  ┃        │
┃  ┃  ┃  ┃        ├─ 84
┃  ┃  ┃  ┃        │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃        │   pc: W0:Int
┃  ┃  ┃  ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃        ┃
┃  ┃  ┃  ┃        ┃ (1 step)
┃  ┃  ┃  ┃        ┣━━┓
┃  ┃  ┃  ┃        ┃  │
┃  ┃  ┃  ┃        ┃  └─ 190 (leaf, pending)
┃  ┃  ┃  ┃        ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃        ┃      pc: W0:Int
┃  ┃  ┃  ┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃        ┃
┃  ┃  ┃  ┃        ┗━━┓
┃  ┃  ┃  ┃           │
┃  ┃  ┃  ┃           └─ 191 (leaf, pending)
┃  ┃  ┃  ┃               k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃               pc: W0:Int
┃  ┃  ┃  ┃               callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃               statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓
┃  ┃  ┃     │
┃  ┃  ┃     ├─ 25
┃  ┃  ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃     │   pc: W0:Int
┃  ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃
┃  ┃  ┃     ┃ (1 step)
┃  ┃  ┃     ┣━━┓
┃  ┃  ┃     ┃  │
┃  ┃  ┃     ┃  ├─ 44
┃  ┃  ┃     ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃     ┃  │   pc: W0:Int
┃  ┃  ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃
┃  ┃  ┃     ┃  ┃ (1 step)
┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃     ┃  ┃  └─ 87 (leaf, pending)
┃  ┃  ┃     ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃
┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃     ┃  ┃  └─ 88 (leaf, pending)
┃  ┃  ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃
┃  ┃  ┃     ┃  ┗━━┓
┃  ┃  ┃     ┃     │
┃  ┃  ┃     ┃     ├─ 89
┃  ┃  ┃     ┃     │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃     ┃     │   pc: W0:Int
┃  ┃  ┃     ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃     ┃
┃  ┃  ┃     ┃     ┃ (1 step)
┃  ┃  ┃     ┃     ┣━━┓
┃  ┃  ┃     ┃     ┃  │
┃  ┃  ┃     ┃     ┃  └─ 201 (leaf, pending)
┃  ┃  ┃     ┃     ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃     ┃     ┃      pc: W0:Int
┃  ┃  ┃     ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃     ┃
┃  ┃  ┃     ┃     ┗━━┓
┃  ┃  ┃     ┃        │
┃  ┃  ┃     ┃        └─ 202 (leaf, pending)
┃  ┃  ┃     ┃            k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃     ┃            pc: W0:Int
┃  ┃  ┃     ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃
┃  ┃  ┃     ┗━━┓
┃  ┃  ┃        │
┃  ┃  ┃        ├─ 45
┃  ┃  ┃        │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃        │   pc: W0:Int
┃  ┃  ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃
┃  ┃  ┃        ┃ (1 step)
┃  ┃  ┃        ┣━━┓
┃  ┃  ┃        ┃  │
┃  ┃  ┃        ┃  ├─ 85
┃  ┃  ┃        ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃        ┃  │   pc: W0:Int
┃  ┃  ┃        ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃  ┃
┃  ┃  ┃        ┃  ┃ (1 step)
┃  ┃  ┃        ┃  ┣━━┓
┃  ┃  ┃        ┃  ┃  │
┃  ┃  ┃        ┃  ┃  └─ 196 (leaf, pending)
┃  ┃  ┃        ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃  ┃        ┃  ┃      pc: W0:Int
┃  ┃  ┃        ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃  ┃
┃  ┃  ┃        ┃  ┣━━┓
┃  ┃  ┃        ┃  ┃  │
┃  ┃  ┃        ┃  ┃  └─ 197 (leaf, pending)
┃  ┃  ┃        ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃        ┃  ┃      pc: W0:Int
┃  ┃  ┃        ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃  ┃
┃  ┃  ┃        ┃  ┗━━┓
┃  ┃  ┃        ┃     │
┃  ┃  ┃        ┃     └─ 198 (leaf, pending)
┃  ┃  ┃        ┃         k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃        ┃         pc: W0:Int
┃  ┃  ┃        ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃
┃  ┃  ┃        ┗━━┓
┃  ┃  ┃           │
┃  ┃  ┃           ├─ 86
┃  ┃  ┃           │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃           │   pc: W0:Int
┃  ┃  ┃           │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃           │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃           ┃
┃  ┃  ┃           ┃ (1 step)
┃  ┃  ┃           ┣━━┓
┃  ┃  ┃           ┃  │
┃  ┃  ┃           ┃  └─ 199 (leaf, pending)
┃  ┃  ┃           ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃           ┃      pc: W0:Int
┃  ┃  ┃           ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃           ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃           ┃
┃  ┃  ┃           ┗━━┓
┃  ┃  ┃              │
┃  ┃  ┃              └─ 200 (leaf, pending)
┃  ┃  ┃                  k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃                  pc: W0:Int
┃  ┃  ┃                  callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃                  statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓
┃  ┃     │
┃  ┃     ├─ 15
┃  ┃     │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃     │   pc: W0:Int
┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┃ (1 step)
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  ├─ 21
┃  ┃     ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃  │   pc: W0:Int
┃  ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃
┃  ┃     ┃  ┃ (1 step)
┃  ┃     ┃  ┣━━┓
┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃  ├─ 38
┃  ┃     ┃  ┃  │   k: #execute ~> _DotVar4:K
┃  ┃     ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃  │  (1 step)
┃  ┃     ┃  ┃  └─ 108 (leaf, pending)
┃  ┃     ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃
┃  ┃     ┃  ┣━━┓
┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃  ├─ 39
┃  ┃     ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃ (1 step)
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ├─ 75
┃  ┃     ┃  ┃  ┃  │   k: #execute ~> _DotVar5:K
┃  ┃     ┃  ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  │  (1 step)
┃  ┃     ┃  ┃  ┃  └─ 203 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ├─ 76
┃  ┃     ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar5:K
┃  ┃     ┃  ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃  ┃ (1 step)
┃  ┃     ┃  ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ┃  └─ 176 (leaf, pending)
┃  ┃     ┃  ┃  ┃  ┃      k: #execute ~> _DotVar6:K
┃  ┃     ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ┃  └─ 177 (leaf, pending)
┃  ┃     ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar6:K
┃  ┃     ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃  ┗━━┓
┃  ┃     ┃  ┃  ┃     │
┃  ┃     ┃  ┃  ┃     └─ 178 (leaf, pending)
┃  ┃     ┃  ┃  ┃         k: #endBasicBlock ~> _DotVar5:K
┃  ┃     ┃  ┃  ┃         pc: W0:Int
┃  ┃     ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┗━━┓
┃  ┃     ┃  ┃     │
┃  ┃     ┃  ┃     ├─ 77
┃  ┃     ┃  ┃     │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃  ┃     │   pc: W0:Int
┃  ┃     ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃     ┃
┃  ┃     ┃  ┃     ┃ (1 step)
┃  ┃     ┃  ┃     ┣━━┓
┃  ┃     ┃  ┃     ┃  │
┃  ┃     ┃  ┃     ┃  └─ 174 (leaf, pending)
┃  ┃     ┃  ┃     ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃     ┃  ┃     ┃      pc: W0:Int
┃  ┃     ┃  ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃     ┃
┃  ┃     ┃  ┃     ┗━━┓
┃  ┃     ┃  ┃        │
┃  ┃     ┃  ┃        └─ 175 (leaf, pending)
┃  ┃     ┃  ┃            k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃  ┃            pc: W0:Int
┃  ┃     ┃  ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃
┃  ┃     ┃  ┗━━┓
┃  ┃     ┃     │
┃  ┃     ┃     ├─ 40
┃  ┃     ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃     │   pc: W0:Int
┃  ┃     ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃
┃  ┃     ┃     ┃ (1 step)
┃  ┃     ┃     ┣━━┓
┃  ┃     ┃     ┃  │
┃  ┃     ┃     ┃  ├─ 78
┃  ┃     ┃     ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃     ┃  │   pc: W0:Int
┃  ┃     ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃
┃  ┃     ┃     ┃  ┃ (1 step)
┃  ┃     ┃     ┃  ┣━━┓
┃  ┃     ┃     ┃  ┃  │
┃  ┃     ┃     ┃  ┃  └─ 180 (leaf, pending)
┃  ┃     ┃     ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃     ┃     ┃  ┃      pc: W0:Int
┃  ┃     ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃
┃  ┃     ┃     ┃  ┣━━┓
┃  ┃     ┃     ┃  ┃  │
┃  ┃     ┃     ┃  ┃  └─ 181 (leaf, pending)
┃  ┃     ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃     ┃     ┃  ┃      pc: W0:Int
┃  ┃     ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃
┃  ┃     ┃     ┃  ┗━━┓
┃  ┃     ┃     ┃     │
┃  ┃     ┃     ┃     └─ 182 (leaf, pending)
┃  ┃     ┃     ┃         k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃     ┃         pc: W0:Int
┃  ┃     ┃     ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃
┃  ┃     ┃     ┗━━┓
┃  ┃     ┃        │
┃  ┃     ┃        ├─ 79
┃  ┃     ┃        │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃        │   pc: W0:Int
┃  ┃     ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃        ┃
┃  ┃     ┃        ┃ (1 step)
┃  ┃     ┃        ┣━━┓
┃  ┃     ┃        ┃  │
┃  ┃     ┃        ┃  └─ 183 (leaf, pending)
┃  ┃     ┃        ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃        ┃      pc: W0:Int
┃  ┃     ┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃        ┃
┃  ┃     ┃        ┗━━┓
┃  ┃     ┃           │
┃  ┃     ┃           └─ 184 (leaf, pending)
┃  ┃     ┃               k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃               pc: W0:Int
┃  ┃     ┃               callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃               statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┗━━┓
┃  ┃        │
┃  ┃        ├─ 22
┃  ┃        │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃        │   pc: W0:Int
┃  ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┃ (1 step)
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  ├─ 33
┃  ┃        ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃        ┃  │   pc: W0:Int
┃  ┃        ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃
┃  ┃        ┃  ┃ (1 step)
┃  ┃        ┃  ┣━━┓
┃  ┃        ┃  ┃  │
┃  ┃        ┃  ┃  ├─ 63
┃  ┃        ┃  ┃  │   k: #execute ~> _DotVar4:K
┃  ┃        ┃  ┃  │   pc: W0:Int
┃  ┃        ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  │
┃  ┃        ┃  ┃  │  (1 step)
┃  ┃        ┃  ┃  └─ 179 (leaf, pending)
┃  ┃        ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃        ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃
┃  ┃        ┃  ┣━━┓
┃  ┃        ┃  ┃  │
┃  ┃        ┃  ┃  ├─ 64
┃  ┃        ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃        ┃  ┃  │   pc: W0:Int
┃  ┃        ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┃ (1 step)
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  └─ 147 (leaf, pending)
┃  ┃        ┃  ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  └─ 148 (leaf, pending)
┃  ┃        ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┗━━┓
┃  ┃        ┃  ┃     │
┃  ┃        ┃  ┃     └─ 149 (leaf, pending)
┃  ┃        ┃  ┃         k: #endBasicBlock ~> _DotVar4:K
┃  ┃        ┃  ┃         pc: W0:Int
┃  ┃        ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃
┃  ┃        ┃  ┗━━┓
┃  ┃        ┃     │
┃  ┃        ┃     ├─ 65
┃  ┃        ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃        ┃     │   pc: W0:Int
┃  ┃        ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃     ┃
┃  ┃        ┃     ┃ (1 step)
┃  ┃        ┃     ┣━━┓
┃  ┃        ┃     ┃  │
┃  ┃        ┃     ┃  └─ 145 (leaf, pending)
┃  ┃        ┃     ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃        ┃     ┃      pc: W0:Int
┃  ┃        ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃     ┃
┃  ┃        ┃     ┗━━┓
┃  ┃        ┃        │
┃  ┃        ┃        └─ 146 (leaf, pending)
┃  ┃        ┃            k: #endBasicBlock ~> _DotVar3:K
┃  ┃        ┃            pc: W0:Int
┃  ┃        ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┗━━┓
┃  ┃           │
┃  ┃           ├─ 34
┃  ┃           │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃           │   pc: W0:Int
┃  ┃           │   callDepth: CALLDEPTH_CELL:Int
┃  ┃           │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┃ (1 step)
┃  ┃           ┣━━┓
┃  ┃           ┃  │
┃  ┃           ┃  ├─ 66
┃  ┃           ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃           ┃  │   pc: W0:Int
┃  ┃           ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃
┃  ┃           ┃  ┃ (1 step)
┃  ┃           ┃  ┣━━┓
┃  ┃           ┃  ┃  │
┃  ┃           ┃  ┃  └─ 152 (leaf, pending)
┃  ┃           ┃  ┃      k: #execute ~> _DotVar4:K
┃  ┃           ┃  ┃      pc: W0:Int
┃  ┃           ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃
┃  ┃           ┃  ┣━━┓
┃  ┃           ┃  ┃  │
┃  ┃           ┃  ┃  └─ 153 (leaf, pending)
┃  ┃           ┃  ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃           ┃  ┃      pc: W0:Int
┃  ┃           ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃
┃  ┃           ┃  ┗━━┓
┃  ┃           ┃     │
┃  ┃           ┃     └─ 154 (leaf, pending)
┃  ┃           ┃         k: #endBasicBlock ~> _DotVar3:K
┃  ┃           ┃         pc: W0:Int
┃  ┃           ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┗━━┓
┃  ┃              │
┃  ┃              ├─ 67
┃  ┃              │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃              │   pc: W0:Int
┃  ┃              │   callDepth: CALLDEPTH_CELL:Int
┃  ┃              │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃              ┃
┃  ┃              ┃ (1 step)
┃  ┃              ┣━━┓
┃  ┃              ┃  │
┃  ┃              ┃  └─ 150 (leaf, pending)
┃  ┃              ┃      k: #endBasicBlock ~> _DotVar3:K
┃  ┃              ┃      pc: W0:Int
┃  ┃              ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃              ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃              ┃
┃  ┃              ┗━━┓
┃  ┃                 │
┃  ┃                 └─ 151 (leaf, pending)
┃  ┃                     k: #endBasicBlock ~> _DotVar2:K
┃  ┃                     pc: W0:Int
┃  ┃                     callDepth: CALLDEPTH_CELL:Int
┃  ┃                     statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 9
┃     │   k: #endBasicBlock ~> K_CELL:K
┃     │   pc: W0:Int
┃     │   callDepth: CALLDEPTH_CELL:Int
┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  ├─ 11
┃     ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃     ┃  │   pc: W0:Int
┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┃ (1 step)
┃     ┃  ┣━━┓
┃     ┃  ┃  │
┃     ┃  ┃  ├─ 18
┃     ┃  ┃  │   k: #execute ~> _DotVar3:K
┃     ┃  ┃  │   pc: W0:Int
┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  │
┃     ┃  ┃  │  (1 step)
┃     ┃  ┃  ├─ 62
┃     ┃  ┃  │   k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃     ┃  ┃  │   pc: W0:Int
┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┃ (1 step)
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 120 (leaf, pending)
┃     ┃  ┃  ┃      k: #execute ~> _DotVar3:K
┃     ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃     ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 121 (leaf, pending)
┃     ┃  ┃  ┃      k: #end EVMC_STACK_UNDERFLOW ~> #execute ~> _DotVar3:K
┃     ┃  ┃  ┃      pc: W0:Int
┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 122 (leaf, pending)
┃     ┃  ┃  ┃      k: #end EVMC_STACK_OVERFLOW ~> #execute ~> _DotVar3:K
┃     ┃  ┃  ┃      pc: W0:Int
┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 123 (leaf, pending)
┃     ┃  ┃  ┃      k: #addr [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃     ┃  ┃  ┃      pc: W0:Int
┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 124 (leaf, pending)
┃     ┃  ┃  ┃      k: #end EVMC_STATIC_MODE_VIOLATION ~> #execute ~> _DotVar3:K
┃     ┃  ┃  ┃      pc: W0:Int
┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 125 (leaf, pending)
┃     ┃  ┃  ┃      k: #end EVMC_SUCCESS ~> #execute ~> _DotVar3:K
┃     ┃  ┃  ┃      pc: W0:Int
┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┗━━┓
┃     ┃  ┃     │
┃     ┃  ┃     └─ 126 (leaf, pending)
┃     ┃  ┃         k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃     ┃  ┃         pc: W0:Int
┃     ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┣━━┓
┃     ┃  ┃  │
┃     ┃  ┃  ├─ 19
┃     ┃  ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃     ┃  ┃  │   pc: W0:Int
┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┃ (1 step)
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ├─ 35
┃     ┃  ┃  ┃  │   k: #execute ~> _DotVar4:K
┃     ┃  ┃  ┃  │   pc: W0:Int
┃     ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  │  (1 step)
┃     ┃  ┃  ┃  └─ 104 (leaf, pending)
┃     ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃     ┃  ┃  ┃      pc: W0:Int
┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ├─ 36
┃     ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃     ┃  ┃  ┃  │   pc: W0:Int
┃     ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃
┃     ┃  ┃  ┃  ┃ (1 step)
┃     ┃  ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ┃  ├─ 71
┃     ┃  ┃  ┃  ┃  │   k: #execute ~> _DotVar5:K
┃     ┃  ┃  ┃  ┃  │   pc: W0:Int
┃     ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ┃  │  (1 step)
┃     ┃  ┃  ┃  ┃  └─ 195 (leaf, pending)
┃     ┃  ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃     ┃  ┃  ┃  ┃      pc: W0:Int
┃     ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃
┃     ┃  ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ┃  ├─ 72
┃     ┃  ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar5:K
┃     ┃  ┃  ┃  ┃  │   pc: W0:Int
┃     ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃  ┃
┃     ┃  ┃  ┃  ┃  ┃ (1 step)
┃     ┃  ┃  ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ┃  ┃  └─ 169 (leaf, pending)
┃     ┃  ┃  ┃  ┃  ┃      k: #execute ~> _DotVar6:K
┃     ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃     ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃  ┃
┃     ┃  ┃  ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  ┃  ┃  │
┃     ┃  ┃  ┃  ┃  ┃  └─ 170 (leaf, pending)
┃     ┃  ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar6:K
┃     ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃     ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃  ┃
┃     ┃  ┃  ┃  ┃  ┗━━┓
┃     ┃  ┃  ┃  ┃     │
┃     ┃  ┃  ┃  ┃     └─ 171 (leaf, pending)
┃     ┃  ┃  ┃  ┃         k: #endBasicBlock ~> _DotVar5:K
┃     ┃  ┃  ┃  ┃         pc: W0:Int
┃     ┃  ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃  ┃
┃     ┃  ┃  ┃  ┗━━┓
┃     ┃  ┃  ┃     │
┃     ┃  ┃  ┃     ├─ 73
┃     ┃  ┃  ┃     │   k: #endBasicBlock ~> _DotVar4:K
┃     ┃  ┃  ┃     │   pc: W0:Int
┃     ┃  ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃     ┃
┃     ┃  ┃  ┃     ┃ (1 step)
┃     ┃  ┃  ┃     ┣━━┓
┃     ┃  ┃  ┃     ┃  │
┃     ┃  ┃  ┃     ┃  └─ 172 (leaf, pending)
┃     ┃  ┃  ┃     ┃      k: #endBasicBlock ~> _DotVar5:K
┃     ┃  ┃  ┃     ┃      pc: W0:Int
┃     ┃  ┃  ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃     ┃
┃     ┃  ┃  ┃     ┗━━┓
┃     ┃  ┃  ┃        │
┃     ┃  ┃  ┃        └─ 173 (leaf, pending)
┃     ┃  ┃  ┃            k: #endBasicBlock ~> _DotVar4:K
┃     ┃  ┃  ┃            pc: W0:Int
┃     ┃  ┃  ┃            callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃            statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┗━━┓
┃     ┃  ┃     │
┃     ┃  ┃     ├─ 37
┃     ┃  ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃     ┃  ┃     │   pc: W0:Int
┃     ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃     ┃
┃     ┃  ┃     ┃ (1 step)
┃     ┃  ┃     ┣━━┓
┃     ┃  ┃     ┃  │
┃     ┃  ┃     ┃  ├─ 69
┃     ┃  ┃     ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃     ┃  ┃     ┃  │   pc: W0:Int
┃     ┃  ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃     ┃  ┃
┃     ┃  ┃     ┃  ┃ (1 step)
┃     ┃  ┃     ┃  ┣━━┓
┃     ┃  ┃     ┃  ┃  │
┃     ┃  ┃     ┃  ┃  └─ 156 (leaf, pending)
┃     ┃  ┃     ┃  ┃      k: #execute ~> _DotVar5:K
┃     ┃  ┃     ┃  ┃      pc: W0:Int
┃     ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃     ┃  ┃
┃     ┃  ┃     ┃  ┣━━┓
┃     ┃  ┃     ┃  ┃  │
┃     ┃  ┃     ┃  ┃  └─ 157 (leaf, pending)
┃     ┃  ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃     ┃  ┃     ┃  ┃      pc: W0:Int
┃     ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃     ┃  ┃
┃     ┃  ┃     ┃  ┗━━┓
┃     ┃  ┃     ┃     │
┃     ┃  ┃     ┃     └─ 158 (leaf, pending)
┃     ┃  ┃     ┃         k: #endBasicBlock ~> _DotVar4:K
┃     ┃  ┃     ┃         pc: W0:Int
┃     ┃  ┃     ┃         callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃     ┃         statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃     ┃
┃     ┃  ┃     ┗━━┓
┃     ┃  ┃        │
┃     ┃  ┃        ├─ 70
┃     ┃  ┃        │   k: #endBasicBlock ~> _DotVar3:K
┃     ┃  ┃        │   pc: W0:Int
┃     ┃  ┃        │   callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃        ┃
┃     ┃  ┃        ┃ (1 step)
┃     ┃  ┃        ┣━━┓
┃     ┃  ┃        ┃  │
┃     ┃  ┃        ┃  └─ 160 (leaf, pending)
┃     ┃  ┃        ┃      k: #endBasicBlock ~> _DotVar4:K
┃     ┃  ┃        ┃      pc: W0:Int
┃     ┃  ┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃        ┃
┃     ┃  ┃        ┗━━┓
┃     ┃  ┃           │
┃     ┃  ┃           └─ 161 (leaf, pending)
┃     ┃  ┃               k: #endBasicBlock ~> _DotVar3:K
┃     ┃  ┃               pc: W0:Int
┃     ┃  ┃               callDepth: CALLDEPTH_CELL:Int
┃     ┃  ┃               statusCode: STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┗━━┓
┃     ┃     │
┃     ┃     ├─ 20
┃     ┃     │   k: #endBasicBlock ~> _DotVar2:K
┃     ┃     │   pc: W0:Int
┃     ┃     │   callDepth: CALLDEPTH_CELL:Int
┃     ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃
┃     ┃     ┃ (1 step)
┃     ┃     ┣━━┓
┃     ┃     ┃  │
┃     ┃     ┃  ├─ 31
┃     ┃     ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃     ┃     ┃  │   pc: W0:Int
┃     ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃  ┃
┃     ┃     ┃  ┃ (1 step)
┃     ┃     ┃  ┣━━┓
┃     ┃     ┃  ┃  │
┃     ┃     ┃  ┃  ├─ 57
┃     ┃     ┃  ┃  │   k: #execute ~> _DotVar4:K
┃     ┃     ┃  ┃  │   pc: W0:Int
┃     ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃  ┃  │
┃     ┃     ┃  ┃  │  (1 step)
┃     ┃     ┃  ┃  └─ 159 (leaf, pending)
┃     ┃     ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃     ┃     ┃  ┃      pc: W0:Int
┃     ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃  ┃
┃     ┃     ┃  ┣━━┓
┃     ┃     ┃  ┃  │
┃     ┃     ┃  ┃  ├─ 58
┃     ┃     ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃     ┃     ┃  ┃  │   pc: W0:Int
┃     ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃  ┃  ┃
┃     ┃     ┃  ┃  ┃ (1 step)
┃     ┃     ┃  ┃  ┣━━┓
┃     ┃     ┃  ┃  ┃  │
┃     ┃     ┃  ┃  ┃  └─ 129 (leaf, pending)
┃     ┃     ┃  ┃  ┃      k: #execute ~> _DotVar5:K
┃     ┃     ┃  ┃  ┃      pc: W0:Int
┃     ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃  ┃  ┃
┃     ┃     ┃  ┃  ┣━━┓
┃     ┃     ┃  ┃  ┃  │
┃     ┃     ┃  ┃  ┃  └─ 130 (leaf, pending)
┃     ┃     ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃     ┃     ┃  ┃  ┃      pc: W0:Int
┃     ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃  ┃  ┃
┃     ┃     ┃  ┃  ┗━━┓
┃     ┃     ┃  ┃     │
┃     ┃     ┃  ┃     └─ 131 (leaf, pending)
┃     ┃     ┃  ┃         k: #endBasicBlock ~> _DotVar4:K
┃     ┃     ┃  ┃         pc: W0:Int
┃     ┃     ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃  ┃
┃     ┃     ┃  ┗━━┓
┃     ┃     ┃     │
┃     ┃     ┃     ├─ 59
┃     ┃     ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃     ┃     ┃     │   pc: W0:Int
┃     ┃     ┃     │   callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃     ┃
┃     ┃     ┃     ┃ (1 step)
┃     ┃     ┃     ┣━━┓
┃     ┃     ┃     ┃  │
┃     ┃     ┃     ┃  └─ 127 (leaf, pending)
┃     ┃     ┃     ┃      k: #endBasicBlock ~> _DotVar4:K
┃     ┃     ┃     ┃      pc: W0:Int
┃     ┃     ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃     ┃
┃     ┃     ┃     ┗━━┓
┃     ┃     ┃        │
┃     ┃     ┃        └─ 128 (leaf, pending)
┃     ┃     ┃            k: #endBasicBlock ~> _DotVar3:K
┃     ┃     ┃            pc: W0:Int
┃     ┃     ┃            callDepth: CALLDEPTH_CELL:Int
┃     ┃     ┃            statusCode: STATUSCODE_CELL:StatusCode
┃     ┃     ┃
┃     ┃     ┗━━┓
┃     ┃        │
┃     ┃        ├─ 32
┃     ┃        │   k: #endBasicBlock ~> _DotVar2:K
┃     ┃        │   pc: W0:Int
┃     ┃        │   callDepth: CALLDEPTH_CELL:Int
┃     ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃        ┃
┃     ┃        ┃ (1 step)
┃     ┃        ┣━━┓
┃     ┃        ┃  │
┃     ┃        ┃  ├─ 60
┃     ┃        ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃     ┃        ┃  │   pc: W0:Int
┃     ┃        ┃  │   callDepth: CALLDEPTH_CELL:Int
┃     ┃        ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃        ┃  ┃
┃     ┃        ┃  ┃ (1 step)
┃     ┃        ┃  ┣━━┓
┃     ┃        ┃  ┃  │
┃     ┃        ┃  ┃  └─ 132 (leaf, pending)
┃     ┃        ┃  ┃      k: #execute ~> _DotVar4:K
┃     ┃        ┃  ┃      pc: W0:Int
┃     ┃        ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃        ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃        ┃  ┃
┃     ┃        ┃  ┣━━┓
┃     ┃        ┃  ┃  │
┃     ┃        ┃  ┃  └─ 133 (leaf, pending)
┃     ┃        ┃  ┃      k: #endBasicBlock ~> _DotVar4:K
┃     ┃        ┃  ┃      pc: W0:Int
┃     ┃        ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃        ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃        ┃  ┃
┃     ┃        ┃  ┗━━┓
┃     ┃        ┃     │
┃     ┃        ┃     └─ 134 (leaf, pending)
┃     ┃        ┃         k: #endBasicBlock ~> _DotVar3:K
┃     ┃        ┃         pc: W0:Int
┃     ┃        ┃         callDepth: CALLDEPTH_CELL:Int
┃     ┃        ┃         statusCode: STATUSCODE_CELL:StatusCode
┃     ┃        ┃
┃     ┃        ┗━━┓
┃     ┃           │
┃     ┃           ├─ 61
┃     ┃           │   k: #endBasicBlock ~> _DotVar2:K
┃     ┃           │   pc: W0:Int
┃     ┃           │   callDepth: CALLDEPTH_CELL:Int
┃     ┃           │   statusCode: STATUSCODE_CELL:StatusCode
┃     ┃           ┃
┃     ┃           ┃ (1 step)
┃     ┃           ┣━━┓
┃     ┃           ┃  │
┃     ┃           ┃  └─ 135 (leaf, pending)
┃     ┃           ┃      k: #endBasicBlock ~> _DotVar3:K
┃     ┃           ┃      pc: W0:Int
┃     ┃           ┃      callDepth: CALLDEPTH_CELL:Int
┃     ┃           ┃      statusCode: STATUSCODE_CELL:StatusCode
┃     ┃           ┃
┃     ┃           ┗━━┓
┃     ┃              │
┃     ┃              └─ 136 (leaf, pending)
┃     ┃                  k: #endBasicBlock ~> _DotVar2:K
┃     ┃                  pc: W0:Int
┃     ┃                  callDepth: CALLDEPTH_CELL:Int
┃     ┃                  statusCode: STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 12
┃        │   k: #endBasicBlock ~> K_CELL:K
┃        │   pc: W0:Int
┃        │   callDepth: CALLDEPTH_CELL:Int
┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  ├─ 16
┃        ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃        ┃  │   pc: W0:Int
┃        ┃  │   callDepth: CALLDEPTH_CELL:Int
┃        ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┃ (1 step)
┃        ┃  ┣━━┓
┃        ┃  ┃  │
┃        ┃  ┃  ├─ 28
┃        ┃  ┃  │   k: #execute ~> _DotVar3:K
┃        ┃  ┃  │   pc: W0:Int
┃        ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  │
┃        ┃  ┃  │  (1 step)
┃        ┃  ┃  ├─ 74
┃        ┃  ┃  │   k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃        ┃  ┃  │   pc: W0:Int
┃        ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┃ (1 step)
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  └─ 162 (leaf, pending)
┃        ┃  ┃  ┃      k: #execute ~> _DotVar3:K
┃        ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃        ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  └─ 163 (leaf, pending)
┃        ┃  ┃  ┃      k: #end EVMC_STACK_UNDERFLOW ~> #execute ~> _DotVar3:K
┃        ┃  ┃  ┃      pc: W0:Int
┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  └─ 164 (leaf, pending)
┃        ┃  ┃  ┃      k: #end EVMC_STACK_OVERFLOW ~> #execute ~> _DotVar3:K
┃        ┃  ┃  ┃      pc: W0:Int
┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  └─ 165 (leaf, pending)
┃        ┃  ┃  ┃      k: #addr [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃        ┃  ┃  ┃      pc: W0:Int
┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  └─ 166 (leaf, pending)
┃        ┃  ┃  ┃      k: #end EVMC_STATIC_MODE_VIOLATION ~> #execute ~> _DotVar3:K
┃        ┃  ┃  ┃      pc: W0:Int
┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  └─ 167 (leaf, pending)
┃        ┃  ┃  ┃      k: #end EVMC_SUCCESS ~> #execute ~> _DotVar3:K
┃        ┃  ┃  ┃      pc: W0:Int
┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┗━━┓
┃        ┃  ┃     │
┃        ┃  ┃     └─ 168 (leaf, pending)
┃        ┃  ┃         k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃        ┃  ┃         pc: W0:Int
┃        ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┣━━┓
┃        ┃  ┃  │
┃        ┃  ┃  ├─ 29
┃        ┃  ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃        ┃  ┃  │   pc: W0:Int
┃        ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┃ (1 step)
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  ├─ 54
┃        ┃  ┃  ┃  │   k: #execute ~> _DotVar4:K
┃        ┃  ┃  ┃  │   pc: W0:Int
┃        ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  │  (1 step)
┃        ┃  ┃  ┃  └─ 155 (leaf, pending)
┃        ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃        ┃  ┃  ┃      pc: W0:Int
┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  │
┃        ┃  ┃  ┃  ├─ 55
┃        ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃        ┃  ┃  ┃  │   pc: W0:Int
┃        ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃  ┃
┃        ┃  ┃  ┃  ┃ (1 step)
┃        ┃  ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  ┃  │
┃        ┃  ┃  ┃  ┃  └─ 117 (leaf, pending)
┃        ┃  ┃  ┃  ┃      k: #execute ~> _DotVar5:K
┃        ┃  ┃  ┃  ┃      pc: W0:Int
┃        ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃  ┃
┃        ┃  ┃  ┃  ┣━━┓
┃        ┃  ┃  ┃  ┃  │
┃        ┃  ┃  ┃  ┃  └─ 118 (leaf, pending)
┃        ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃        ┃  ┃  ┃  ┃      pc: W0:Int
┃        ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃  ┃
┃        ┃  ┃  ┃  ┗━━┓
┃        ┃  ┃  ┃     │
┃        ┃  ┃  ┃     └─ 119 (leaf, pending)
┃        ┃  ┃  ┃         k: #endBasicBlock ~> _DotVar4:K
┃        ┃  ┃  ┃         pc: W0:Int
┃        ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃  ┃
┃        ┃  ┃  ┗━━┓
┃        ┃  ┃     │
┃        ┃  ┃     ├─ 56
┃        ┃  ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃        ┃  ┃     │   pc: W0:Int
┃        ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃     ┃
┃        ┃  ┃     ┃ (1 step)
┃        ┃  ┃     ┣━━┓
┃        ┃  ┃     ┃  │
┃        ┃  ┃     ┃  └─ 115 (leaf, pending)
┃        ┃  ┃     ┃      k: #endBasicBlock ~> _DotVar4:K
┃        ┃  ┃     ┃      pc: W0:Int
┃        ┃  ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃     ┃
┃        ┃  ┃     ┗━━┓
┃        ┃  ┃        │
┃        ┃  ┃        └─ 116 (leaf, pending)
┃        ┃  ┃            k: #endBasicBlock ~> _DotVar3:K
┃        ┃  ┃            pc: W0:Int
┃        ┃  ┃            callDepth: CALLDEPTH_CELL:Int
┃        ┃  ┃            statusCode: STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┗━━┓
┃        ┃     │
┃        ┃     ├─ 30
┃        ┃     │   k: #endBasicBlock ~> _DotVar2:K
┃        ┃     │   pc: W0:Int
┃        ┃     │   callDepth: CALLDEPTH_CELL:Int
┃        ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃     ┃
┃        ┃     ┃ (1 step)
┃        ┃     ┣━━┓
┃        ┃     ┃  │
┃        ┃     ┃  ├─ 52
┃        ┃     ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃        ┃     ┃  │   pc: W0:Int
┃        ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃        ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃     ┃  ┃
┃        ┃     ┃  ┃ (1 step)
┃        ┃     ┃  ┣━━┓
┃        ┃     ┃  ┃  │
┃        ┃     ┃  ┃  └─ 111 (leaf, pending)
┃        ┃     ┃  ┃      k: #execute ~> _DotVar4:K
┃        ┃     ┃  ┃      pc: W0:Int
┃        ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃     ┃  ┃
┃        ┃     ┃  ┣━━┓
┃        ┃     ┃  ┃  │
┃        ┃     ┃  ┃  └─ 112 (leaf, pending)
┃        ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar4:K
┃        ┃     ┃  ┃      pc: W0:Int
┃        ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃     ┃  ┃
┃        ┃     ┃  ┗━━┓
┃        ┃     ┃     │
┃        ┃     ┃     └─ 113 (leaf, pending)
┃        ┃     ┃         k: #endBasicBlock ~> _DotVar3:K
┃        ┃     ┃         pc: W0:Int
┃        ┃     ┃         callDepth: CALLDEPTH_CELL:Int
┃        ┃     ┃         statusCode: STATUSCODE_CELL:StatusCode
┃        ┃     ┃
┃        ┃     ┗━━┓
┃        ┃        │
┃        ┃        ├─ 53
┃        ┃        │   k: #endBasicBlock ~> _DotVar2:K
┃        ┃        │   pc: W0:Int
┃        ┃        │   callDepth: CALLDEPTH_CELL:Int
┃        ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃        ┃        ┃
┃        ┃        ┃ (1 step)
┃        ┃        ┣━━┓
┃        ┃        ┃  │
┃        ┃        ┃  └─ 109 (leaf, pending)
┃        ┃        ┃      k: #endBasicBlock ~> _DotVar3:K
┃        ┃        ┃      pc: W0:Int
┃        ┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃        ┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃        ┃        ┃
┃        ┃        ┗━━┓
┃        ┃           │
┃        ┃           └─ 110 (leaf, pending)
┃        ┃               k: #endBasicBlock ~> _DotVar2:K
┃        ┃               pc: W0:Int
┃        ┃               callDepth: CALLDEPTH_CELL:Int
┃        ┃               statusCode: STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 17
┃           │   k: #endBasicBlock ~> K_CELL:K
┃           │   pc: W0:Int
┃           │   callDepth: CALLDEPTH_CELL:Int
┃           │   statusCode: STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  ├─ 26
┃           ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃           ┃  │   pc: W0:Int
┃           ┃  │   callDepth: CALLDEPTH_CELL:Int
┃           ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┃ (1 step)
┃           ┃  ┣━━┓
┃           ┃  ┃  │
┃           ┃  ┃  ├─ 48
┃           ┃  ┃  │   k: #execute ~> _DotVar3:K
┃           ┃  ┃  │   pc: W0:Int
┃           ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃           ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃           ┃  ┃  │
┃           ┃  ┃  │  (1 step)
┃           ┃  ┃  └─ 137 (leaf, pending)
┃           ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃           ┃  ┃      pc: W0:Int
┃           ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃           ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┣━━┓
┃           ┃  ┃  │
┃           ┃  ┃  ├─ 49
┃           ┃  ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃           ┃  ┃  │   pc: W0:Int
┃           ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃           ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃           ┃  ┃  ┃
┃           ┃  ┃  ┃ (1 step)
┃           ┃  ┃  ┣━━┓
┃           ┃  ┃  ┃  │
┃           ┃  ┃  ┃  └─ 105 (leaf, pending)
┃           ┃  ┃  ┃      k: #execute ~> _DotVar4:K
┃           ┃  ┃  ┃      pc: W0:Int
┃           ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃           ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃           ┃  ┃  ┃
┃           ┃  ┃  ┣━━┓
┃           ┃  ┃  ┃  │
┃           ┃  ┃  ┃  └─ 106 (leaf, pending)
┃           ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar4:K
┃           ┃  ┃  ┃      pc: W0:Int
┃           ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃           ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃           ┃  ┃  ┃
┃           ┃  ┃  ┗━━┓
┃           ┃  ┃     │
┃           ┃  ┃     └─ 107 (leaf, pending)
┃           ┃  ┃         k: #endBasicBlock ~> _DotVar3:K
┃           ┃  ┃         pc: W0:Int
┃           ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃           ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃           ┃  ┃
┃           ┃  ┗━━┓
┃           ┃     │
┃           ┃     ├─ 50
┃           ┃     │   k: #endBasicBlock ~> _DotVar2:K
┃           ┃     │   pc: W0:Int
┃           ┃     │   callDepth: CALLDEPTH_CELL:Int
┃           ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃           ┃     ┃
┃           ┃     ┃ (1 step)
┃           ┃     ┣━━┓
┃           ┃     ┃  │
┃           ┃     ┃  └─ 102 (leaf, pending)
┃           ┃     ┃      k: #endBasicBlock ~> _DotVar3:K
┃           ┃     ┃      pc: W0:Int
┃           ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃           ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃           ┃     ┃
┃           ┃     ┗━━┓
┃           ┃        │
┃           ┃        └─ 103 (leaf, pending)
┃           ┃            k: #endBasicBlock ~> _DotVar2:K
┃           ┃            pc: W0:Int
┃           ┃            callDepth: CALLDEPTH_CELL:Int
┃           ┃            statusCode: STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              ├─ 27
┃              │   k: #endBasicBlock ~> K_CELL:K
┃              │   pc: W0:Int
┃              │   callDepth: CALLDEPTH_CELL:Int
┃              │   statusCode: STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┃ (1 step)
┃              ┣━━┓
┃              ┃  │
┃              ┃  ├─ 46
┃              ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃              ┃  │   pc: W0:Int
┃              ┃  │   callDepth: CALLDEPTH_CELL:Int
┃              ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃              ┃  ┃
┃              ┃  ┃ (1 step)
┃              ┃  ┣━━┓
┃              ┃  ┃  │
┃              ┃  ┃  └─ 90 (leaf, pending)
┃              ┃  ┃      k: #execute ~> _DotVar3:K
┃              ┃  ┃      pc: W0:Int
┃              ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃              ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃              ┃  ┃
┃              ┃  ┣━━┓
┃              ┃  ┃  │
┃              ┃  ┃  └─ 91 (leaf, pending)
┃              ┃  ┃      k: #endBasicBlock ~> _DotVar3:K
┃              ┃  ┃      pc: W0:Int
┃              ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃              ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃              ┃  ┃
┃              ┃  ┗━━┓
┃              ┃     │
┃              ┃     └─ 92 (leaf, pending)
┃              ┃         k: #endBasicBlock ~> _DotVar2:K
┃              ┃         pc: W0:Int
┃              ┃         callDepth: CALLDEPTH_CELL:Int
┃              ┃         statusCode: STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┗━━┓
┃                 │
┃                 ├─ 47
┃                 │   k: #endBasicBlock ~> K_CELL:K
┃                 │   pc: W0:Int
┃                 │   callDepth: CALLDEPTH_CELL:Int
┃                 │   statusCode: STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┃ (1 step)
┃                 ┣━━┓
┃                 ┃  │
┃                 ┃  └─ 100 (leaf, pending)
┃                 ┃      k: #endBasicBlock ~> _DotVar2:K
┃                 ┃      pc: W0:Int
┃                 ┃      callDepth: CALLDEPTH_CELL:Int
┃                 ┃      statusCode: STATUSCODE_CELL:StatusCode
┃                 ┃
┃                 ┗━━┓
┃                    │
┃                    └─ 101 (leaf, pending)
┃                        k: #endBasicBlock ~> K_CELL:K
┃                        pc: W0:Int
┃                        callDepth: CALLDEPTH_CELL:Int
┃                        statusCode: STATUSCODE_CELL:StatusCode
┃
┗━━┓
   │
   ├─ 5
   │   k: #end EVMC_BAD_JUMP_DESTINATION ~> #pc [ JUMP ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   └─ 10 (leaf, terminal)
       k: #halt ~> K_CELL:K
       pc: PC_CELL:Int
       callDepth: CALLDEPTH_CELL:Int
       statusCode: EVMC_BAD_JUMP_DESTINATION




module SUMMARY-JUMP-1-SPEC
    
    
    rule [BASIC-BLOCK-1-TO-3]: <kevm>
           <k>
             ( #next [ JUMP ] ~> .K => JUMP W0:Int
             ~> #pc [ JUMP ] )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( W0:Int : WS:WordStack ) => WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      [priority(20), label(BASIC-BLOCK-1-TO-3)]
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             #endBasicBlock
             ~> ( #pc [ JUMP ] ~> .K => .K )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))
      [priority(20), label(BASIC-BLOCK-4-TO-6)]
    
    rule [BASIC-BLOCK-5-TO-10]: <kevm>
           <k>
             ( #end EVMC_BAD_JUMP_DESTINATION
             ~> #pc [ JUMP ] => #halt ~> .K )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <statusCode>
                 ( _STATUSCODE_CELL => EVMC_BAD_JUMP_DESTINATION )
               </statusCode>
               <callState>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( notBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes ) andBool 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ] ) )
      [priority(20), label(BASIC-BLOCK-5-TO-10)]
    
    rule [BASIC-BLOCK-13-TO-51]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar3:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar2 ==K #execute
        ~> _DotVar3:K
       andBool ( _K_CELL ==K __Gen0
        ~> #execute
        ~> _DotVar3:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))
      [priority(20), label(BASIC-BLOCK-13-TO-51)]
    
    rule [BASIC-BLOCK-18-TO-62]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar3:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar2 ==K #execute
        ~> _DotVar3:K
       andBool ( _K_CELL ==K _Gen1:OpCode
        ~> #execute
        ~> _DotVar3:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen1:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))
      [priority(20), label(BASIC-BLOCK-18-TO-62)]
    
    rule [BASIC-BLOCK-23-TO-68]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar4:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar3 ==K #execute
        ~> _DotVar4:K
       andBool ( __DotVar2 ==K _Gen1:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( _K_CELL ==K __Gen0
        ~> _Gen1:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))
      [priority(20), label(BASIC-BLOCK-23-TO-68)]
    
    rule [BASIC-BLOCK-28-TO-74]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar3:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar2 ==K #execute
        ~> _DotVar3:K
       andBool ( _K_CELL ==K _Gen2:OpCode
        ~> #execute
        ~> _DotVar3:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( __Gen1 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))))
      [priority(20), label(BASIC-BLOCK-28-TO-74)]
    
    rule [BASIC-BLOCK-35-TO-104]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar4:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar3 ==K #execute
        ~> _DotVar4:K
       andBool ( __DotVar2 ==K _Gen2:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( _K_CELL ==K _Gen1:OpCode
        ~> _Gen2:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen1:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))))
      [priority(20), label(BASIC-BLOCK-35-TO-104)]
    
    rule [BASIC-BLOCK-38-TO-108]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar4:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar3 ==K #execute
        ~> _DotVar4:K
       andBool ( __DotVar2 ==K _Gen2:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( _K_CELL ==K __Gen0
        ~> _Gen2:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen1 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))))
      [priority(20), label(BASIC-BLOCK-38-TO-108)]
    
    rule [BASIC-BLOCK-41-TO-114]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar5:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar4 ==K #execute
        ~> _DotVar5:K
       andBool ( __DotVar3 ==K _Gen2:OpCode
        ~> #execute
        ~> _DotVar5:K
       andBool ( __DotVar2 ==K _Gen1:OpCode
        ~> _Gen2:OpCode
        ~> #execute
        ~> _DotVar5:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( _K_CELL ==K __Gen0
        ~> _Gen1:OpCode
        ~> _Gen2:OpCode
        ~> #execute
        ~> _DotVar5:K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))))
      [priority(20), label(BASIC-BLOCK-41-TO-114)]
    
    rule [BASIC-BLOCK-48-TO-137]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar3:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar2 ==K #execute
        ~> _DotVar3:K
       andBool ( _K_CELL ==K _Gen3:OpCode
        ~> #execute
        ~> _DotVar3:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( __Gen1 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( __Gen2 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))))
      [priority(20), label(BASIC-BLOCK-48-TO-137)]
    
    rule [BASIC-BLOCK-54-TO-155]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar4:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar3 ==K #execute
        ~> _DotVar4:K
       andBool ( __DotVar2 ==K _Gen3:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( _K_CELL ==K _Gen2:OpCode
        ~> _Gen3:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( __Gen1 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))))
      [priority(20), label(BASIC-BLOCK-54-TO-155)]
    
    rule [BASIC-BLOCK-57-TO-159]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar4:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar3 ==K #execute
        ~> _DotVar4:K
       andBool ( __DotVar2 ==K _Gen3:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( _K_CELL ==K _Gen1:OpCode
        ~> _Gen3:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen1:OpCode ~> .K
       andBool ( __Gen2 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))))
      [priority(20), label(BASIC-BLOCK-57-TO-159)]
    
    rule [BASIC-BLOCK-63-TO-179]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar4:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar3 ==K #execute
        ~> _DotVar4:K
       andBool ( __DotVar2 ==K _Gen3:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( _K_CELL ==K __Gen0
        ~> _Gen3:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen1 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( __Gen2 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))))
      [priority(20), label(BASIC-BLOCK-63-TO-179)]
    
    rule [BASIC-BLOCK-71-TO-195]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar5:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar4 ==K #execute
        ~> _DotVar5:K
       andBool ( __DotVar3 ==K _Gen3:OpCode
        ~> #execute
        ~> _DotVar5:K
       andBool ( __DotVar2 ==K _Gen2:OpCode
        ~> _Gen3:OpCode
        ~> #execute
        ~> _DotVar5:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen1:OpCode ~> .K
       andBool ( _K_CELL ==K _Gen1:OpCode
        ~> _Gen2:OpCode
        ~> _Gen3:OpCode
        ~> #execute
        ~> _DotVar5:K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))))
      [priority(20), label(BASIC-BLOCK-71-TO-195)]
    
    rule [BASIC-BLOCK-75-TO-203]: <kevm>
           <k>
             ( .K => #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ~> .K )
             ~> #execute
             ~> _DotVar5:K
           </k>
           <schedule>
             SCHEDULE_CELL:Schedule
           </schedule>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <program>
                   PROGRAM_CELL:Bytes
                 </program>
                 <jumpDests>
                   JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <pc>
                   W0:Int
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __DotVar4 ==K #execute
        ~> _DotVar5:K
       andBool ( __DotVar3 ==K _Gen3:OpCode
        ~> #execute
        ~> _DotVar5:K
       andBool ( __DotVar2 ==K _Gen2:OpCode
        ~> _Gen3:OpCode
        ~> #execute
        ~> _DotVar5:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen1 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( _K_CELL ==K __Gen0
        ~> _Gen2:OpCode
        ~> _Gen3:OpCode
        ~> #execute
        ~> _DotVar5:K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))))
      [priority(20), label(BASIC-BLOCK-75-TO-203)]

endmodule
