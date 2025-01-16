
┌─ 1 (root, split, init)
│   k: #next [ JUMPI ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool W1:Int ==Int 0 )
┃  │
┃  ├─ 196
┃  │   k: #next [ JUMPI ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (5 steps)
┃  ├─ 6
┃  │   k: JUMP W0:Int ~> #pc [ JUMPI ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 7
┃  ┃  │   k: #endBasicBlock ~> #pc [ JUMPI ] ~> K_CELL:K
┃  ┃  │   pc: W0:Int
┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (1 step)
┃  ┃  ├─ 9
┃  ┃  │   k: #endBasicBlock ~> K_CELL:K
┃  ┃  │   pc: W0:Int
┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (1 step)
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 10
┃  ┃  ┃  │   k: #execute ~> _DotVar2:K
┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  ┊  constraint: true
┃  ┃  ┃  ┊  subst: ...
┃  ┃  ┃  └─ 2 (leaf, target)
┃  ┃  ┃      k: K_CELL:K
┃  ┃  ┃      pc: FINAL_PC_CELL:Int
┃  ┃  ┃      callDepth: FINAL_CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: FINAL_STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 11
┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 16
┃  ┃  ┃  ┃  │   k: #execute ~> _DotVar3:K
┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  ├─ 49
┃  ┃  ┃  ┃  │   k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 90 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #execute ~> _DotVar3:K
┃  ┃  ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 91 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #end EVMC_STACK_UNDERFLOW ~> #execute ~> _DotVar3:K
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 92 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #end EVMC_STACK_OVERFLOW ~> #execute ~> _DotVar3:K
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 93 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #addr [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 94 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #end EVMC_STATIC_MODE_VIOLATION ~> #execute ~> _DotVar3:K
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 95 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #end EVMC_SUCCESS ~> #execute ~> _DotVar3:K
┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃     └─ 96 (leaf, pending)
┃  ┃  ┃  ┃         k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃         pc: W0:Int
┃  ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 17
┃  ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ├─ 26
┃  ┃  ┃  ┃  ┃  │   k: #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  ┃  ├─ 66
┃  ┃  ┃  ┃  ┃  │   k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  └─ 135 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃      k: #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  └─ 136 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃      k: #end EVMC_STACK_UNDERFLOW ~> #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  └─ 137 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃      k: #end EVMC_STACK_OVERFLOW ~> #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  └─ 138 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃      k: #addr [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  └─ 139 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃      k: #end EVMC_STATIC_MODE_VIOLATION ~> #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  └─ 140 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃      k: #end EVMC_SUCCESS ~> #execute ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃  ┃     └─ 141 (leaf, pending)
┃  ┃  ┃  ┃  ┃         k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃  ┃         pc: W0:Int
┃  ┃  ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ├─ 27
┃  ┃  ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  ├─ 44
┃  ┃  ┃  ┃  ┃  ┃  │   k: #execute ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  ┃  ┃  └─ 115 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  ├─ 45
┃  ┃  ┃  ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  ┃  └─ 85 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃  ┃      k: #execute ~> _DotVar6:K
┃  ┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  ┃  ┃  └─ 86 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar6:K
┃  ┃  ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃  ┃  ┃     ├─ 87
┃  ┃  ┃  ┃  ┃  ┃     │   k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃  ┃     │   pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃  ┃  ┃     ┃ (1 step)
┃  ┃  ┃  ┃  ┃  ┃     ┣━━┓
┃  ┃  ┃  ┃  ┃  ┃     ┃  │
┃  ┃  ┃  ┃  ┃  ┃     ┃  └─ 194 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃     ┃      k: #endBasicBlock ~> _DotVar6:K
┃  ┃  ┃  ┃  ┃  ┃     ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃  ┃  ┃     ┗━━┓
┃  ┃  ┃  ┃  ┃  ┃        │
┃  ┃  ┃  ┃  ┃  ┃        └─ 195 (leaf, pending)
┃  ┃  ┃  ┃  ┃  ┃            k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃  ┃            pc: W0:Int
┃  ┃  ┃  ┃  ┃  ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃  ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃  ┃     ├─ 46
┃  ┃  ┃  ┃  ┃     │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃     │   pc: W0:Int
┃  ┃  ┃  ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃  ┃     ┃ (1 step)
┃  ┃  ┃  ┃  ┃     ┣━━┓
┃  ┃  ┃  ┃  ┃     ┃  │
┃  ┃  ┃  ┃  ┃     ┃  ├─ 83
┃  ┃  ┃  ┃  ┃     ┃  │   k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃     ┃  │   pc: W0:Int
┃  ┃  ┃  ┃  ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃     ┃  ┃
┃  ┃  ┃  ┃  ┃     ┃  ┃ (1 step)
┃  ┃  ┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃  ┃  ┃     ┃  ┃  └─ 191 (leaf, pending)
┃  ┃  ┃  ┃  ┃     ┃  ┃      k: #execute ~> _DotVar6:K
┃  ┃  ┃  ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃     ┃  ┃
┃  ┃  ┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃  ┃  ┃     ┃  ┃  └─ 192 (leaf, pending)
┃  ┃  ┃  ┃  ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar6:K
┃  ┃  ┃  ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃     ┃  ┃
┃  ┃  ┃  ┃  ┃     ┃  ┗━━┓
┃  ┃  ┃  ┃  ┃     ┃     │
┃  ┃  ┃  ┃  ┃     ┃     └─ 193 (leaf, pending)
┃  ┃  ┃  ┃  ┃     ┃         k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃     ┃         pc: W0:Int
┃  ┃  ┃  ┃  ┃     ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃     ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃  ┃     ┗━━┓
┃  ┃  ┃  ┃  ┃        │
┃  ┃  ┃  ┃  ┃        ├─ 84
┃  ┃  ┃  ┃  ┃        │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃        │   pc: W0:Int
┃  ┃  ┃  ┃  ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃        ┃
┃  ┃  ┃  ┃  ┃        ┃ (1 step)
┃  ┃  ┃  ┃  ┃        ┣━━┓
┃  ┃  ┃  ┃  ┃        ┃  │
┃  ┃  ┃  ┃  ┃        ┃  └─ 189 (leaf, pending)
┃  ┃  ┃  ┃  ┃        ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃  ┃        ┃      pc: W0:Int
┃  ┃  ┃  ┃  ┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃        ┃
┃  ┃  ┃  ┃  ┃        ┗━━┓
┃  ┃  ┃  ┃  ┃           │
┃  ┃  ┃  ┃  ┃           └─ 190 (leaf, pending)
┃  ┃  ┃  ┃  ┃               k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃  ┃               pc: W0:Int
┃  ┃  ┃  ┃  ┃               callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃               statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃     ├─ 28
┃  ┃  ┃  ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃  ┃     │   pc: W0:Int
┃  ┃  ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃     ┃ (1 step)
┃  ┃  ┃  ┃     ┣━━┓
┃  ┃  ┃  ┃     ┃  │
┃  ┃  ┃  ┃     ┃  ├─ 47
┃  ┃  ┃  ┃     ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃     ┃  │   pc: W0:Int
┃  ┃  ┃  ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃  ┃
┃  ┃  ┃  ┃     ┃  ┃ (1 step)
┃  ┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃  ┃     ┃  ┃  └─ 97 (leaf, pending)
┃  ┃  ┃  ┃     ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃  ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃  ┃
┃  ┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃  ┃     ┃  ┃  └─ 98 (leaf, pending)
┃  ┃  ┃  ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃  ┃
┃  ┃  ┃  ┃     ┃  ┗━━┓
┃  ┃  ┃  ┃     ┃     │
┃  ┃  ┃  ┃     ┃     └─ 99 (leaf, pending)
┃  ┃  ┃  ┃     ┃         k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃     ┃         pc: W0:Int
┃  ┃  ┃  ┃     ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃     ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃     ┃
┃  ┃  ┃  ┃     ┗━━┓
┃  ┃  ┃  ┃        │
┃  ┃  ┃  ┃        ├─ 48
┃  ┃  ┃  ┃        │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃  ┃        │   pc: W0:Int
┃  ┃  ┃  ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃        ┃
┃  ┃  ┃  ┃        ┃ (1 step)
┃  ┃  ┃  ┃        ┣━━┓
┃  ┃  ┃  ┃        ┃  │
┃  ┃  ┃  ┃        ┃  └─ 88 (leaf, pending)
┃  ┃  ┃  ┃        ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃  ┃        ┃      pc: W0:Int
┃  ┃  ┃  ┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃        ┃
┃  ┃  ┃  ┃        ┗━━┓
┃  ┃  ┃  ┃           │
┃  ┃  ┃  ┃           └─ 89 (leaf, pending)
┃  ┃  ┃  ┃               k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃  ┃               pc: W0:Int
┃  ┃  ┃  ┃               callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃               statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓
┃  ┃  ┃     │
┃  ┃  ┃     ├─ 18
┃  ┃  ┃     │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃  ┃     │   pc: W0:Int
┃  ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃
┃  ┃  ┃     ┃ (1 step)
┃  ┃  ┃     ┣━━┓
┃  ┃  ┃     ┃  │
┃  ┃  ┃     ┃  ├─ 24
┃  ┃  ┃     ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃     ┃  │   pc: W0:Int
┃  ┃  ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃
┃  ┃  ┃     ┃  ┃ (1 step)
┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃     ┃  ┃  ├─ 39
┃  ┃  ┃     ┃  ┃  │   k: #execute ~> _DotVar4:K
┃  ┃  ┃     ┃  ┃  │   pc: W0:Int
┃  ┃  ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃     ┃  ┃  │  (1 step)
┃  ┃  ┃     ┃  ┃  └─ 101 (leaf, pending)
┃  ┃  ┃     ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃
┃  ┃  ┃     ┃  ┣━━┓
┃  ┃  ┃     ┃  ┃  │
┃  ┃  ┃     ┃  ┃  ├─ 40
┃  ┃  ┃     ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃     ┃  ┃  │   pc: W0:Int
┃  ┃  ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃  ┃
┃  ┃  ┃     ┃  ┃  ┃ (1 step)
┃  ┃  ┃     ┃  ┃  ┣━━┓
┃  ┃  ┃     ┃  ┃  ┃  │
┃  ┃  ┃     ┃  ┃  ┃  ├─ 72
┃  ┃  ┃     ┃  ┃  ┃  │   k: #execute ~> _DotVar5:K
┃  ┃  ┃     ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃     ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃  ┃  │
┃  ┃  ┃     ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃     ┃  ┃  ┃  └─ 188 (leaf, pending)
┃  ┃  ┃     ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃  ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃  ┃
┃  ┃  ┃     ┃  ┃  ┣━━┓
┃  ┃  ┃     ┃  ┃  ┃  │
┃  ┃  ┃     ┃  ┃  ┃  ├─ 73
┃  ┃  ┃     ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃     ┃  ┃  ┃  │   pc: W0:Int
┃  ┃  ┃     ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃  ┃  ┃
┃  ┃  ┃     ┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃     ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃     ┃  ┃  ┃  ┃  │
┃  ┃  ┃     ┃  ┃  ┃  ┃  └─ 162 (leaf, pending)
┃  ┃  ┃     ┃  ┃  ┃  ┃      k: #execute ~> _DotVar6:K
┃  ┃  ┃     ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃     ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃  ┃  ┃
┃  ┃  ┃     ┃  ┃  ┃  ┣━━┓
┃  ┃  ┃     ┃  ┃  ┃  ┃  │
┃  ┃  ┃     ┃  ┃  ┃  ┃  └─ 163 (leaf, pending)
┃  ┃  ┃     ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar6:K
┃  ┃  ┃     ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃     ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃  ┃  ┃
┃  ┃  ┃     ┃  ┃  ┃  ┗━━┓
┃  ┃  ┃     ┃  ┃  ┃     │
┃  ┃  ┃     ┃  ┃  ┃     └─ 164 (leaf, pending)
┃  ┃  ┃     ┃  ┃  ┃         k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃     ┃  ┃  ┃         pc: W0:Int
┃  ┃  ┃     ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃  ┃
┃  ┃  ┃     ┃  ┃  ┗━━┓
┃  ┃  ┃     ┃  ┃     │
┃  ┃  ┃     ┃  ┃     ├─ 74
┃  ┃  ┃     ┃  ┃     │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃     ┃  ┃     │   pc: W0:Int
┃  ┃  ┃     ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃     ┃
┃  ┃  ┃     ┃  ┃     ┃ (1 step)
┃  ┃  ┃     ┃  ┃     ┣━━┓
┃  ┃  ┃     ┃  ┃     ┃  │
┃  ┃  ┃     ┃  ┃     ┃  └─ 160 (leaf, pending)
┃  ┃  ┃     ┃  ┃     ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃     ┃  ┃     ┃      pc: W0:Int
┃  ┃  ┃     ┃  ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃     ┃
┃  ┃  ┃     ┃  ┃     ┗━━┓
┃  ┃  ┃     ┃  ┃        │
┃  ┃  ┃     ┃  ┃        └─ 161 (leaf, pending)
┃  ┃  ┃     ┃  ┃            k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃     ┃  ┃            pc: W0:Int
┃  ┃  ┃     ┃  ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃  ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃  ┃
┃  ┃  ┃     ┃  ┗━━┓
┃  ┃  ┃     ┃     │
┃  ┃  ┃     ┃     ├─ 41
┃  ┃  ┃     ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃     ┃     │   pc: W0:Int
┃  ┃  ┃     ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃     ┃
┃  ┃  ┃     ┃     ┃ (1 step)
┃  ┃  ┃     ┃     ┣━━┓
┃  ┃  ┃     ┃     ┃  │
┃  ┃  ┃     ┃     ┃  ├─ 75
┃  ┃  ┃     ┃     ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃     ┃     ┃  │   pc: W0:Int
┃  ┃  ┃     ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃     ┃  ┃
┃  ┃  ┃     ┃     ┃  ┃ (1 step)
┃  ┃  ┃     ┃     ┃  ┣━━┓
┃  ┃  ┃     ┃     ┃  ┃  │
┃  ┃  ┃     ┃     ┃  ┃  └─ 167 (leaf, pending)
┃  ┃  ┃     ┃     ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃  ┃     ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃     ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃     ┃  ┃
┃  ┃  ┃     ┃     ┃  ┣━━┓
┃  ┃  ┃     ┃     ┃  ┃  │
┃  ┃  ┃     ┃     ┃  ┃  └─ 168 (leaf, pending)
┃  ┃  ┃     ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃     ┃     ┃  ┃      pc: W0:Int
┃  ┃  ┃     ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃     ┃  ┃
┃  ┃  ┃     ┃     ┃  ┗━━┓
┃  ┃  ┃     ┃     ┃     │
┃  ┃  ┃     ┃     ┃     └─ 169 (leaf, pending)
┃  ┃  ┃     ┃     ┃         k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃     ┃     ┃         pc: W0:Int
┃  ┃  ┃     ┃     ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃     ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃     ┃
┃  ┃  ┃     ┃     ┗━━┓
┃  ┃  ┃     ┃        │
┃  ┃  ┃     ┃        ├─ 76
┃  ┃  ┃     ┃        │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃     ┃        │   pc: W0:Int
┃  ┃  ┃     ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃        ┃
┃  ┃  ┃     ┃        ┃ (1 step)
┃  ┃  ┃     ┃        ┣━━┓
┃  ┃  ┃     ┃        ┃  │
┃  ┃  ┃     ┃        ┃  └─ 165 (leaf, pending)
┃  ┃  ┃     ┃        ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃     ┃        ┃      pc: W0:Int
┃  ┃  ┃     ┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃        ┃
┃  ┃  ┃     ┃        ┗━━┓
┃  ┃  ┃     ┃           │
┃  ┃  ┃     ┃           └─ 166 (leaf, pending)
┃  ┃  ┃     ┃               k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃     ┃               pc: W0:Int
┃  ┃  ┃     ┃               callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃               statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃
┃  ┃  ┃     ┗━━┓
┃  ┃  ┃        │
┃  ┃  ┃        ├─ 25
┃  ┃  ┃        │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃  ┃        │   pc: W0:Int
┃  ┃  ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃
┃  ┃  ┃        ┃ (1 step)
┃  ┃  ┃        ┣━━┓
┃  ┃  ┃        ┃  │
┃  ┃  ┃        ┃  ├─ 42
┃  ┃  ┃        ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃        ┃  │   pc: W0:Int
┃  ┃  ┃        ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃  ┃
┃  ┃  ┃        ┃  ┃ (1 step)
┃  ┃  ┃        ┃  ┣━━┓
┃  ┃  ┃        ┃  ┃  │
┃  ┃  ┃        ┃  ┃  └─ 79 (leaf, pending)
┃  ┃  ┃        ┃  ┃      k: #execute ~> _DotVar4:K
┃  ┃  ┃        ┃  ┃      pc: W0:Int
┃  ┃  ┃        ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃  ┃
┃  ┃  ┃        ┃  ┣━━┓
┃  ┃  ┃        ┃  ┃  │
┃  ┃  ┃        ┃  ┃  ├─ 80
┃  ┃  ┃        ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃        ┃  ┃  │   pc: W0:Int
┃  ┃  ┃        ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃  ┃  ┃
┃  ┃  ┃        ┃  ┃  ┃ (1 step)
┃  ┃  ┃        ┃  ┃  ┣━━┓
┃  ┃  ┃        ┃  ┃  ┃  │
┃  ┃  ┃        ┃  ┃  ┃  └─ 184 (leaf, pending)
┃  ┃  ┃        ┃  ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃  ┃  ┃
┃  ┃  ┃        ┃  ┃  ┣━━┓
┃  ┃  ┃        ┃  ┃  ┃  │
┃  ┃  ┃        ┃  ┃  ┃  └─ 185 (leaf, pending)
┃  ┃  ┃        ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃  ┃  ┃
┃  ┃  ┃        ┃  ┃  ┗━━┓
┃  ┃  ┃        ┃  ┃     │
┃  ┃  ┃        ┃  ┃     └─ 186 (leaf, pending)
┃  ┃  ┃        ┃  ┃         k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃        ┃  ┃         pc: W0:Int
┃  ┃  ┃        ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃  ┃
┃  ┃  ┃        ┃  ┗━━┓
┃  ┃  ┃        ┃     │
┃  ┃  ┃        ┃     ├─ 81
┃  ┃  ┃        ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃        ┃     │   pc: W0:Int
┃  ┃  ┃        ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃     ┃
┃  ┃  ┃        ┃     ┃ (1 step)
┃  ┃  ┃        ┃     ┣━━┓
┃  ┃  ┃        ┃     ┃  │
┃  ┃  ┃        ┃     ┃  └─ 172 (leaf, pending)
┃  ┃  ┃        ┃     ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃        ┃     ┃      pc: W0:Int
┃  ┃  ┃        ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃     ┃
┃  ┃  ┃        ┃     ┗━━┓
┃  ┃  ┃        ┃        │
┃  ┃  ┃        ┃        └─ 173 (leaf, pending)
┃  ┃  ┃        ┃            k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃        ┃            pc: W0:Int
┃  ┃  ┃        ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃        ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃        ┃
┃  ┃  ┃        ┗━━┓
┃  ┃  ┃           │
┃  ┃  ┃           ├─ 43
┃  ┃  ┃           │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃  ┃           │   pc: W0:Int
┃  ┃  ┃           │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃           │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃           ┃
┃  ┃  ┃           ┃ (1 step)
┃  ┃  ┃           ┣━━┓
┃  ┃  ┃           ┃  │
┃  ┃  ┃           ┃  ├─ 77
┃  ┃  ┃           ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃           ┃  │   pc: W0:Int
┃  ┃  ┃           ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃           ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃           ┃  ┃
┃  ┃  ┃           ┃  ┃ (1 step)
┃  ┃  ┃           ┃  ┣━━┓
┃  ┃  ┃           ┃  ┃  │
┃  ┃  ┃           ┃  ┃  └─ 174 (leaf, pending)
┃  ┃  ┃           ┃  ┃      k: #execute ~> _DotVar4:K
┃  ┃  ┃           ┃  ┃      pc: W0:Int
┃  ┃  ┃           ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃           ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃           ┃  ┃
┃  ┃  ┃           ┃  ┣━━┓
┃  ┃  ┃           ┃  ┃  │
┃  ┃  ┃           ┃  ┃  └─ 175 (leaf, pending)
┃  ┃  ┃           ┃  ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃  ┃           ┃  ┃      pc: W0:Int
┃  ┃  ┃           ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃           ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃           ┃  ┃
┃  ┃  ┃           ┃  ┗━━┓
┃  ┃  ┃           ┃     │
┃  ┃  ┃           ┃     └─ 176 (leaf, pending)
┃  ┃  ┃           ┃         k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃           ┃         pc: W0:Int
┃  ┃  ┃           ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃           ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃           ┃
┃  ┃  ┃           ┗━━┓
┃  ┃  ┃              │
┃  ┃  ┃              ├─ 78
┃  ┃  ┃              │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃  ┃              │   pc: W0:Int
┃  ┃  ┃              │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃              │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃              ┃
┃  ┃  ┃              ┃ (1 step)
┃  ┃  ┃              ┣━━┓
┃  ┃  ┃              ┃  │
┃  ┃  ┃              ┃  └─ 170 (leaf, pending)
┃  ┃  ┃              ┃      k: #endBasicBlock ~> _DotVar3:K
┃  ┃  ┃              ┃      pc: W0:Int
┃  ┃  ┃              ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃              ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃              ┃
┃  ┃  ┃              ┗━━┓
┃  ┃  ┃                 │
┃  ┃  ┃                 └─ 171 (leaf, pending)
┃  ┃  ┃                     k: #endBasicBlock ~> _DotVar2:K
┃  ┃  ┃                     pc: W0:Int
┃  ┃  ┃                     callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃                     statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓
┃  ┃     │
┃  ┃     ├─ 12
┃  ┃     │   k: #endBasicBlock ~> K_CELL:K
┃  ┃     │   pc: W0:Int
┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┃ (1 step)
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  ├─ 14
┃  ┃     ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃     ┃  │   pc: W0:Int
┃  ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃
┃  ┃     ┃  ┃ (1 step)
┃  ┃     ┃  ┣━━┓
┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃  ├─ 21
┃  ┃     ┃  ┃  │   k: #execute ~> _DotVar3:K
┃  ┃     ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃  │  (1 step)
┃  ┃     ┃  ┃  ├─ 60
┃  ┃     ┃  ┃  │   k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃     ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃ (1 step)
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  └─ 116 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #execute ~> _DotVar3:K
┃  ┃     ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃     ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  └─ 117 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #end EVMC_STACK_UNDERFLOW ~> #execute ~> _DotVar3:K
┃  ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  └─ 118 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #end EVMC_STACK_OVERFLOW ~> #execute ~> _DotVar3:K
┃  ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  └─ 119 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #addr [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  └─ 120 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #end EVMC_STATIC_MODE_VIOLATION ~> #execute ~> _DotVar3:K
┃  ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  └─ 121 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #end EVMC_SUCCESS ~> #execute ~> _DotVar3:K
┃  ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┗━━┓
┃  ┃     ┃  ┃     │
┃  ┃     ┃  ┃     └─ 122 (leaf, pending)
┃  ┃     ┃  ┃         k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃     ┃  ┃         pc: W0:Int
┃  ┃     ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃
┃  ┃     ┃  ┣━━┓
┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃  ├─ 22
┃  ┃     ┃  ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃ (1 step)
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ├─ 36
┃  ┃     ┃  ┃  ┃  │   k: #execute ~> _DotVar4:K
┃  ┃     ┃  ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  │  (1 step)
┃  ┃     ┃  ┃  ┃  └─ 100 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ├─ 37
┃  ┃     ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃  ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃  ┃ (1 step)
┃  ┃     ┃  ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ┃  ├─ 69
┃  ┃     ┃  ┃  ┃  ┃  │   k: #execute ~> _DotVar5:K
┃  ┃     ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ┃  │  (1 step)
┃  ┃     ┃  ┃  ┃  ┃  └─ 187 (leaf, pending)
┃  ┃     ┃  ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃     ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ┃  ├─ 70
┃  ┃     ┃  ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar5:K
┃  ┃     ┃  ┃  ┃  ┃  │   pc: W0:Int
┃  ┃     ┃  ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃  ┃  ┃ (1 step)
┃  ┃     ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ┃  ┃  └─ 155 (leaf, pending)
┃  ┃     ┃  ┃  ┃  ┃  ┃      k: #execute ~> _DotVar6:K
┃  ┃     ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃  ┃  ┣━━┓
┃  ┃     ┃  ┃  ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  ┃  ┃  └─ 156 (leaf, pending)
┃  ┃     ┃  ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar6:K
┃  ┃     ┃  ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃  ┃  ┗━━┓
┃  ┃     ┃  ┃  ┃  ┃     │
┃  ┃     ┃  ┃  ┃  ┃     └─ 157 (leaf, pending)
┃  ┃     ┃  ┃  ┃  ┃         k: #endBasicBlock ~> _DotVar5:K
┃  ┃     ┃  ┃  ┃  ┃         pc: W0:Int
┃  ┃     ┃  ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃  ┗━━┓
┃  ┃     ┃  ┃  ┃     │
┃  ┃     ┃  ┃  ┃     ├─ 71
┃  ┃     ┃  ┃  ┃     │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃  ┃  ┃     │   pc: W0:Int
┃  ┃     ┃  ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃     ┃
┃  ┃     ┃  ┃  ┃     ┃ (1 step)
┃  ┃     ┃  ┃  ┃     ┣━━┓
┃  ┃     ┃  ┃  ┃     ┃  │
┃  ┃     ┃  ┃  ┃     ┃  └─ 153 (leaf, pending)
┃  ┃     ┃  ┃  ┃     ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃     ┃  ┃  ┃     ┃      pc: W0:Int
┃  ┃     ┃  ┃  ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃     ┃
┃  ┃     ┃  ┃  ┃     ┗━━┓
┃  ┃     ┃  ┃  ┃        │
┃  ┃     ┃  ┃  ┃        └─ 154 (leaf, pending)
┃  ┃     ┃  ┃  ┃            k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃  ┃  ┃            pc: W0:Int
┃  ┃     ┃  ┃  ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┗━━┓
┃  ┃     ┃  ┃     │
┃  ┃     ┃  ┃     ├─ 38
┃  ┃     ┃  ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃  ┃     │   pc: W0:Int
┃  ┃     ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃     ┃
┃  ┃     ┃  ┃     ┃ (1 step)
┃  ┃     ┃  ┃     ┣━━┓
┃  ┃     ┃  ┃     ┃  │
┃  ┃     ┃  ┃     ┃  ├─ 67
┃  ┃     ┃  ┃     ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃  ┃     ┃  │   pc: W0:Int
┃  ┃     ┃  ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃     ┃  ┃
┃  ┃     ┃  ┃     ┃  ┃ (1 step)
┃  ┃     ┃  ┃     ┃  ┣━━┓
┃  ┃     ┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃     ┃  ┃  └─ 150 (leaf, pending)
┃  ┃     ┃  ┃     ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃     ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃     ┃  ┃
┃  ┃     ┃  ┃     ┃  ┣━━┓
┃  ┃     ┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃     ┃  ┃  └─ 151 (leaf, pending)
┃  ┃     ┃  ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃     ┃  ┃     ┃  ┃      pc: W0:Int
┃  ┃     ┃  ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃     ┃  ┃
┃  ┃     ┃  ┃     ┃  ┗━━┓
┃  ┃     ┃  ┃     ┃     │
┃  ┃     ┃  ┃     ┃     └─ 152 (leaf, pending)
┃  ┃     ┃  ┃     ┃         k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃  ┃     ┃         pc: W0:Int
┃  ┃     ┃  ┃     ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃     ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃     ┃
┃  ┃     ┃  ┃     ┗━━┓
┃  ┃     ┃  ┃        │
┃  ┃     ┃  ┃        ├─ 68
┃  ┃     ┃  ┃        │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃  ┃        │   pc: W0:Int
┃  ┃     ┃  ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃        ┃
┃  ┃     ┃  ┃        ┃ (1 step)
┃  ┃     ┃  ┃        ┣━━┓
┃  ┃     ┃  ┃        ┃  │
┃  ┃     ┃  ┃        ┃  └─ 148 (leaf, pending)
┃  ┃     ┃  ┃        ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃  ┃        ┃      pc: W0:Int
┃  ┃     ┃  ┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃        ┃
┃  ┃     ┃  ┃        ┗━━┓
┃  ┃     ┃  ┃           │
┃  ┃     ┃  ┃           └─ 149 (leaf, pending)
┃  ┃     ┃  ┃               k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃  ┃               pc: W0:Int
┃  ┃     ┃  ┃               callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃               statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃
┃  ┃     ┃  ┗━━┓
┃  ┃     ┃     │
┃  ┃     ┃     ├─ 23
┃  ┃     ┃     │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃     ┃     │   pc: W0:Int
┃  ┃     ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃
┃  ┃     ┃     ┃ (1 step)
┃  ┃     ┃     ┣━━┓
┃  ┃     ┃     ┃  │
┃  ┃     ┃     ┃  ├─ 34
┃  ┃     ┃     ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃     ┃  │   pc: W0:Int
┃  ┃     ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃
┃  ┃     ┃     ┃  ┃ (1 step)
┃  ┃     ┃     ┃  ┣━━┓
┃  ┃     ┃     ┃  ┃  │
┃  ┃     ┃     ┃  ┃  ├─ 61
┃  ┃     ┃     ┃  ┃  │   k: #execute ~> _DotVar4:K
┃  ┃     ┃     ┃  ┃  │   pc: W0:Int
┃  ┃     ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃  │
┃  ┃     ┃     ┃  ┃  │  (1 step)
┃  ┃     ┃     ┃  ┃  └─ 159 (leaf, pending)
┃  ┃     ┃     ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃     ┃     ┃  ┃      pc: W0:Int
┃  ┃     ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃
┃  ┃     ┃     ┃  ┣━━┓
┃  ┃     ┃     ┃  ┃  │
┃  ┃     ┃     ┃  ┃  ├─ 62
┃  ┃     ┃     ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃     ┃  ┃  │   pc: W0:Int
┃  ┃     ┃     ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃  ┃
┃  ┃     ┃     ┃  ┃  ┃ (1 step)
┃  ┃     ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃     ┃  ┃  ┃  │
┃  ┃     ┃     ┃  ┃  ┃  └─ 132 (leaf, pending)
┃  ┃     ┃     ┃  ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃     ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃  ┃
┃  ┃     ┃     ┃  ┃  ┣━━┓
┃  ┃     ┃     ┃  ┃  ┃  │
┃  ┃     ┃     ┃  ┃  ┃  └─ 133 (leaf, pending)
┃  ┃     ┃     ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃     ┃     ┃  ┃  ┃      pc: W0:Int
┃  ┃     ┃     ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃  ┃
┃  ┃     ┃     ┃  ┃  ┗━━┓
┃  ┃     ┃     ┃  ┃     │
┃  ┃     ┃     ┃  ┃     └─ 134 (leaf, pending)
┃  ┃     ┃     ┃  ┃         k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃     ┃  ┃         pc: W0:Int
┃  ┃     ┃     ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃  ┃
┃  ┃     ┃     ┃  ┗━━┓
┃  ┃     ┃     ┃     │
┃  ┃     ┃     ┃     ├─ 63
┃  ┃     ┃     ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃     ┃     │   pc: W0:Int
┃  ┃     ┃     ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃     ┃
┃  ┃     ┃     ┃     ┃ (1 step)
┃  ┃     ┃     ┃     ┣━━┓
┃  ┃     ┃     ┃     ┃  │
┃  ┃     ┃     ┃     ┃  └─ 130 (leaf, pending)
┃  ┃     ┃     ┃     ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃     ┃     ┃      pc: W0:Int
┃  ┃     ┃     ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃     ┃
┃  ┃     ┃     ┃     ┗━━┓
┃  ┃     ┃     ┃        │
┃  ┃     ┃     ┃        └─ 131 (leaf, pending)
┃  ┃     ┃     ┃            k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃     ┃            pc: W0:Int
┃  ┃     ┃     ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃     ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃     ┃
┃  ┃     ┃     ┗━━┓
┃  ┃     ┃        │
┃  ┃     ┃        ├─ 35
┃  ┃     ┃        │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃     ┃        │   pc: W0:Int
┃  ┃     ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃        ┃
┃  ┃     ┃        ┃ (1 step)
┃  ┃     ┃        ┣━━┓
┃  ┃     ┃        ┃  │
┃  ┃     ┃        ┃  ├─ 64
┃  ┃     ┃        ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃        ┃  │   pc: W0:Int
┃  ┃     ┃        ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃        ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃        ┃  ┃
┃  ┃     ┃        ┃  ┃ (1 step)
┃  ┃     ┃        ┃  ┣━━┓
┃  ┃     ┃        ┃  ┃  │
┃  ┃     ┃        ┃  ┃  └─ 144 (leaf, pending)
┃  ┃     ┃        ┃  ┃      k: #execute ~> _DotVar4:K
┃  ┃     ┃        ┃  ┃      pc: W0:Int
┃  ┃     ┃        ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃        ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃        ┃  ┃
┃  ┃     ┃        ┃  ┣━━┓
┃  ┃     ┃        ┃  ┃  │
┃  ┃     ┃        ┃  ┃  └─ 145 (leaf, pending)
┃  ┃     ┃        ┃  ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃     ┃        ┃  ┃      pc: W0:Int
┃  ┃     ┃        ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃        ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃        ┃  ┃
┃  ┃     ┃        ┃  ┗━━┓
┃  ┃     ┃        ┃     │
┃  ┃     ┃        ┃     └─ 146 (leaf, pending)
┃  ┃     ┃        ┃         k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃        ┃         pc: W0:Int
┃  ┃     ┃        ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃        ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃        ┃
┃  ┃     ┃        ┗━━┓
┃  ┃     ┃           │
┃  ┃     ┃           ├─ 65
┃  ┃     ┃           │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃     ┃           │   pc: W0:Int
┃  ┃     ┃           │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃           │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃           ┃
┃  ┃     ┃           ┃ (1 step)
┃  ┃     ┃           ┣━━┓
┃  ┃     ┃           ┃  │
┃  ┃     ┃           ┃  └─ 142 (leaf, pending)
┃  ┃     ┃           ┃      k: #endBasicBlock ~> _DotVar3:K
┃  ┃     ┃           ┃      pc: W0:Int
┃  ┃     ┃           ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃           ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃           ┃
┃  ┃     ┃           ┗━━┓
┃  ┃     ┃              │
┃  ┃     ┃              └─ 143 (leaf, pending)
┃  ┃     ┃                  k: #endBasicBlock ~> _DotVar2:K
┃  ┃     ┃                  pc: W0:Int
┃  ┃     ┃                  callDepth: CALLDEPTH_CELL:Int
┃  ┃     ┃                  statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┗━━┓
┃  ┃        │
┃  ┃        ├─ 15
┃  ┃        │   k: #endBasicBlock ~> K_CELL:K
┃  ┃        │   pc: W0:Int
┃  ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┃ (1 step)
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  ├─ 19
┃  ┃        ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃        ┃  │   pc: W0:Int
┃  ┃        ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃
┃  ┃        ┃  ┃ (1 step)
┃  ┃        ┃  ┣━━┓
┃  ┃        ┃  ┃  │
┃  ┃        ┃  ┃  ├─ 31
┃  ┃        ┃  ┃  │   k: #execute ~> _DotVar3:K
┃  ┃        ┃  ┃  │   pc: W0:Int
┃  ┃        ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  │
┃  ┃        ┃  ┃  │  (1 step)
┃  ┃        ┃  ┃  ├─ 82
┃  ┃        ┃  ┃  │   k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃        ┃  ┃  │   pc: W0:Int
┃  ┃        ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┃ (1 step)
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  └─ 177 (leaf, pending)
┃  ┃        ┃  ┃  ┃      k: #execute ~> _DotVar3:K
┃  ┃        ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
┃  ┃        ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  └─ 178 (leaf, pending)
┃  ┃        ┃  ┃  ┃      k: #end EVMC_STACK_UNDERFLOW ~> #execute ~> _DotVar3:K
┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  └─ 179 (leaf, pending)
┃  ┃        ┃  ┃  ┃      k: #end EVMC_STACK_OVERFLOW ~> #execute ~> _DotVar3:K
┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  └─ 180 (leaf, pending)
┃  ┃        ┃  ┃  ┃      k: #addr [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  └─ 181 (leaf, pending)
┃  ┃        ┃  ┃  ┃      k: #end EVMC_STATIC_MODE_VIOLATION ~> #execute ~> _DotVar3:K
┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  └─ 182 (leaf, pending)
┃  ┃        ┃  ┃  ┃      k: #end EVMC_SUCCESS ~> #execute ~> _DotVar3:K
┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┗━━┓
┃  ┃        ┃  ┃     │
┃  ┃        ┃  ┃     └─ 183 (leaf, pending)
┃  ┃        ┃  ┃         k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃        ┃  ┃         pc: W0:Int
┃  ┃        ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃
┃  ┃        ┃  ┣━━┓
┃  ┃        ┃  ┃  │
┃  ┃        ┃  ┃  ├─ 32
┃  ┃        ┃  ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃        ┃  ┃  │   pc: W0:Int
┃  ┃        ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┃ (1 step)
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  ├─ 57
┃  ┃        ┃  ┃  ┃  │   k: #execute ~> _DotVar4:K
┃  ┃        ┃  ┃  ┃  │   pc: W0:Int
┃  ┃        ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  │  (1 step)
┃  ┃        ┃  ┃  ┃  └─ 158 (leaf, pending)
┃  ┃        ┃  ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃        ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  ├─ 58
┃  ┃        ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar4:K
┃  ┃        ┃  ┃  ┃  │   pc: W0:Int
┃  ┃        ┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃  ┃
┃  ┃        ┃  ┃  ┃  ┃ (1 step)
┃  ┃        ┃  ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  ┃  └─ 125 (leaf, pending)
┃  ┃        ┃  ┃  ┃  ┃      k: #execute ~> _DotVar5:K
┃  ┃        ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃  ┃
┃  ┃        ┃  ┃  ┃  ┣━━┓
┃  ┃        ┃  ┃  ┃  ┃  │
┃  ┃        ┃  ┃  ┃  ┃  └─ 126 (leaf, pending)
┃  ┃        ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar5:K
┃  ┃        ┃  ┃  ┃  ┃      pc: W0:Int
┃  ┃        ┃  ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃  ┃
┃  ┃        ┃  ┃  ┃  ┗━━┓
┃  ┃        ┃  ┃  ┃     │
┃  ┃        ┃  ┃  ┃     └─ 127 (leaf, pending)
┃  ┃        ┃  ┃  ┃         k: #endBasicBlock ~> _DotVar4:K
┃  ┃        ┃  ┃  ┃         pc: W0:Int
┃  ┃        ┃  ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  ┃
┃  ┃        ┃  ┃  ┗━━┓
┃  ┃        ┃  ┃     │
┃  ┃        ┃  ┃     ├─ 59
┃  ┃        ┃  ┃     │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃        ┃  ┃     │   pc: W0:Int
┃  ┃        ┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃     ┃
┃  ┃        ┃  ┃     ┃ (1 step)
┃  ┃        ┃  ┃     ┣━━┓
┃  ┃        ┃  ┃     ┃  │
┃  ┃        ┃  ┃     ┃  └─ 128 (leaf, pending)
┃  ┃        ┃  ┃     ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃        ┃  ┃     ┃      pc: W0:Int
┃  ┃        ┃  ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃     ┃
┃  ┃        ┃  ┃     ┗━━┓
┃  ┃        ┃  ┃        │
┃  ┃        ┃  ┃        └─ 129 (leaf, pending)
┃  ┃        ┃  ┃            k: #endBasicBlock ~> _DotVar3:K
┃  ┃        ┃  ┃            pc: W0:Int
┃  ┃        ┃  ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃
┃  ┃        ┃  ┗━━┓
┃  ┃        ┃     │
┃  ┃        ┃     ├─ 33
┃  ┃        ┃     │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃        ┃     │   pc: W0:Int
┃  ┃        ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃     ┃
┃  ┃        ┃     ┃ (1 step)
┃  ┃        ┃     ┣━━┓
┃  ┃        ┃     ┃  │
┃  ┃        ┃     ┃  ├─ 55
┃  ┃        ┃     ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃        ┃     ┃  │   pc: W0:Int
┃  ┃        ┃     ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃     ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃     ┃  ┃
┃  ┃        ┃     ┃  ┃ (1 step)
┃  ┃        ┃     ┃  ┣━━┓
┃  ┃        ┃     ┃  ┃  │
┃  ┃        ┃     ┃  ┃  └─ 112 (leaf, pending)
┃  ┃        ┃     ┃  ┃      k: #execute ~> _DotVar4:K
┃  ┃        ┃     ┃  ┃      pc: W0:Int
┃  ┃        ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃     ┃  ┃
┃  ┃        ┃     ┃  ┣━━┓
┃  ┃        ┃     ┃  ┃  │
┃  ┃        ┃     ┃  ┃  └─ 113 (leaf, pending)
┃  ┃        ┃     ┃  ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃        ┃     ┃  ┃      pc: W0:Int
┃  ┃        ┃     ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃     ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃     ┃  ┃
┃  ┃        ┃     ┃  ┗━━┓
┃  ┃        ┃     ┃     │
┃  ┃        ┃     ┃     └─ 114 (leaf, pending)
┃  ┃        ┃     ┃         k: #endBasicBlock ~> _DotVar3:K
┃  ┃        ┃     ┃         pc: W0:Int
┃  ┃        ┃     ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃     ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃     ┃
┃  ┃        ┃     ┗━━┓
┃  ┃        ┃        │
┃  ┃        ┃        ├─ 56
┃  ┃        ┃        │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃        ┃        │   pc: W0:Int
┃  ┃        ┃        │   callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃        │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃        ┃
┃  ┃        ┃        ┃ (1 step)
┃  ┃        ┃        ┣━━┓
┃  ┃        ┃        ┃  │
┃  ┃        ┃        ┃  └─ 123 (leaf, pending)
┃  ┃        ┃        ┃      k: #endBasicBlock ~> _DotVar3:K
┃  ┃        ┃        ┃      pc: W0:Int
┃  ┃        ┃        ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃        ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃        ┃
┃  ┃        ┃        ┗━━┓
┃  ┃        ┃           │
┃  ┃        ┃           └─ 124 (leaf, pending)
┃  ┃        ┃               k: #endBasicBlock ~> _DotVar2:K
┃  ┃        ┃               pc: W0:Int
┃  ┃        ┃               callDepth: CALLDEPTH_CELL:Int
┃  ┃        ┃               statusCode: STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┗━━┓
┃  ┃           │
┃  ┃           ├─ 20
┃  ┃           │   k: #endBasicBlock ~> K_CELL:K
┃  ┃           │   pc: W0:Int
┃  ┃           │   callDepth: CALLDEPTH_CELL:Int
┃  ┃           │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┃ (1 step)
┃  ┃           ┣━━┓
┃  ┃           ┃  │
┃  ┃           ┃  ├─ 29
┃  ┃           ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃           ┃  │   pc: W0:Int
┃  ┃           ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃
┃  ┃           ┃  ┃ (1 step)
┃  ┃           ┃  ┣━━┓
┃  ┃           ┃  ┃  │
┃  ┃           ┃  ┃  ├─ 50
┃  ┃           ┃  ┃  │   k: #execute ~> _DotVar3:K
┃  ┃           ┃  ┃  │   pc: W0:Int
┃  ┃           ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃  │
┃  ┃           ┃  ┃  │  (1 step)
┃  ┃           ┃  ┃  └─ 147 (leaf, pending)
┃  ┃           ┃  ┃      k: #next [ #lookupOpCode ( PROGRAM_CELL:Bytes , W0:Int , SCHEDULE_CELL:Schedule ) ] ...
┃  ┃           ┃  ┃      pc: W0:Int
┃  ┃           ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃
┃  ┃           ┃  ┣━━┓
┃  ┃           ┃  ┃  │
┃  ┃           ┃  ┃  ├─ 51
┃  ┃           ┃  ┃  │   k: #endBasicBlock ~> _DotVar3:K
┃  ┃           ┃  ┃  │   pc: W0:Int
┃  ┃           ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃  ┃
┃  ┃           ┃  ┃  ┃ (1 step)
┃  ┃           ┃  ┃  ┣━━┓
┃  ┃           ┃  ┃  ┃  │
┃  ┃           ┃  ┃  ┃  └─ 104 (leaf, pending)
┃  ┃           ┃  ┃  ┃      k: #execute ~> _DotVar4:K
┃  ┃           ┃  ┃  ┃      pc: W0:Int
┃  ┃           ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃  ┃
┃  ┃           ┃  ┃  ┣━━┓
┃  ┃           ┃  ┃  ┃  │
┃  ┃           ┃  ┃  ┃  └─ 105 (leaf, pending)
┃  ┃           ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar4:K
┃  ┃           ┃  ┃  ┃      pc: W0:Int
┃  ┃           ┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃  ┃
┃  ┃           ┃  ┃  ┗━━┓
┃  ┃           ┃  ┃     │
┃  ┃           ┃  ┃     └─ 106 (leaf, pending)
┃  ┃           ┃  ┃         k: #endBasicBlock ~> _DotVar3:K
┃  ┃           ┃  ┃         pc: W0:Int
┃  ┃           ┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃  ┃
┃  ┃           ┃  ┗━━┓
┃  ┃           ┃     │
┃  ┃           ┃     ├─ 52
┃  ┃           ┃     │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃           ┃     │   pc: W0:Int
┃  ┃           ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃     ┃
┃  ┃           ┃     ┃ (1 step)
┃  ┃           ┃     ┣━━┓
┃  ┃           ┃     ┃  │
┃  ┃           ┃     ┃  └─ 102 (leaf, pending)
┃  ┃           ┃     ┃      k: #endBasicBlock ~> _DotVar3:K
┃  ┃           ┃     ┃      pc: W0:Int
┃  ┃           ┃     ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃     ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃     ┃
┃  ┃           ┃     ┗━━┓
┃  ┃           ┃        │
┃  ┃           ┃        └─ 103 (leaf, pending)
┃  ┃           ┃            k: #endBasicBlock ~> _DotVar2:K
┃  ┃           ┃            pc: W0:Int
┃  ┃           ┃            callDepth: CALLDEPTH_CELL:Int
┃  ┃           ┃            statusCode: STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┗━━┓
┃  ┃              │
┃  ┃              ├─ 30
┃  ┃              │   k: #endBasicBlock ~> K_CELL:K
┃  ┃              │   pc: W0:Int
┃  ┃              │   callDepth: CALLDEPTH_CELL:Int
┃  ┃              │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃              ┃
┃  ┃              ┃ (1 step)
┃  ┃              ┣━━┓
┃  ┃              ┃  │
┃  ┃              ┃  ├─ 53
┃  ┃              ┃  │   k: #endBasicBlock ~> _DotVar2:K
┃  ┃              ┃  │   pc: W0:Int
┃  ┃              ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃              ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃              ┃  ┃
┃  ┃              ┃  ┃ (1 step)
┃  ┃              ┃  ┣━━┓
┃  ┃              ┃  ┃  │
┃  ┃              ┃  ┃  └─ 107 (leaf, pending)
┃  ┃              ┃  ┃      k: #execute ~> _DotVar3:K
┃  ┃              ┃  ┃      pc: W0:Int
┃  ┃              ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃              ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃              ┃  ┃
┃  ┃              ┃  ┣━━┓
┃  ┃              ┃  ┃  │
┃  ┃              ┃  ┃  └─ 108 (leaf, pending)
┃  ┃              ┃  ┃      k: #endBasicBlock ~> _DotVar3:K
┃  ┃              ┃  ┃      pc: W0:Int
┃  ┃              ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃              ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃              ┃  ┃
┃  ┃              ┃  ┗━━┓
┃  ┃              ┃     │
┃  ┃              ┃     └─ 109 (leaf, pending)
┃  ┃              ┃         k: #endBasicBlock ~> _DotVar2:K
┃  ┃              ┃         pc: W0:Int
┃  ┃              ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃              ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃              ┃
┃  ┃              ┗━━┓
┃  ┃                 │
┃  ┃                 ├─ 54
┃  ┃                 │   k: #endBasicBlock ~> K_CELL:K
┃  ┃                 │   pc: W0:Int
┃  ┃                 │   callDepth: CALLDEPTH_CELL:Int
┃  ┃                 │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃                 ┃
┃  ┃                 ┃ (1 step)
┃  ┃                 ┣━━┓
┃  ┃                 ┃  │
┃  ┃                 ┃  └─ 110 (leaf, pending)
┃  ┃                 ┃      k: #endBasicBlock ~> _DotVar2:K
┃  ┃                 ┃      pc: W0:Int
┃  ┃                 ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃                 ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃                 ┃
┃  ┃                 ┗━━┓
┃  ┃                    │
┃  ┃                    └─ 111 (leaf, pending)
┃  ┃                        k: #endBasicBlock ~> K_CELL:K
┃  ┃                        pc: W0:Int
┃  ┃                        callDepth: CALLDEPTH_CELL:Int
┃  ┃                        statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 8
┃     │   k: #end EVMC_BAD_JUMP_DESTINATION ~> #pc [ JUMPI ] ~> K_CELL:K
┃     │   pc: PC_CELL:Int
┃     │   callDepth: CALLDEPTH_CELL:Int
┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     │
┃     │  (2 steps)
┃     └─ 13 (leaf, terminal)
┃         k: #halt ~> K_CELL:K
┃         pc: PC_CELL:Int
┃         callDepth: CALLDEPTH_CELL:Int
┃         statusCode: EVMC_BAD_JUMP_DESTINATION
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     W1:Int ==Int 0
   │
   ├─ 197
   │   k: #next [ JUMPI ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   │
   │  (4 steps)
   └─ 5 (leaf, pending)
       k: JUMPI W0:Int W1:Int ~> #pc [ JUMPI ] ~> K_CELL:K
       pc: PC_CELL:Int
       callDepth: CALLDEPTH_CELL:Int
       statusCode: STATUSCODE_CELL:StatusCode




module SUMMARY-JUMPI-2-SPEC
    
    
    rule [BASIC-BLOCK-7-TO-9]: <kevm>
           <k>
             #endBasicBlock
             ~> ( #pc [ JUMPI ] ~> .K => .K )
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
      requires ( _W1 =/=Int 0
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))
      [priority(20), label(BASIC-BLOCK-7-TO-9)]
    
    rule [BASIC-BLOCK-8-TO-13]: <kevm>
           <k>
             ( #end EVMC_BAD_JUMP_DESTINATION
             ~> #pc [ JUMPI ] => #halt ~> .K )
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
      requires ( _W1 =/=Int 0
       andBool ( ( notBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes ) andBool 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ] ) )
               ))
      [priority(20), label(BASIC-BLOCK-8-TO-13)]
    
    rule [BASIC-BLOCK-16-TO-49]: <kevm>
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
       andBool ( _W1 =/=Int 0
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))
      [priority(20), label(BASIC-BLOCK-16-TO-49)]
    
    rule [BASIC-BLOCK-21-TO-60]: <kevm>
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
       andBool ( _W1 =/=Int 0
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen1:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))))
      [priority(20), label(BASIC-BLOCK-21-TO-60)]
    
    rule [BASIC-BLOCK-26-TO-66]: <kevm>
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
       andBool ( _W1 =/=Int 0
       andBool ( _K_CELL ==K __Gen0
        ~> _Gen1:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))))
      [priority(20), label(BASIC-BLOCK-26-TO-66)]
    
    rule [BASIC-BLOCK-31-TO-82]: <kevm>
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
       andBool ( _W1 =/=Int 0
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( __Gen1 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))))
      [priority(20), label(BASIC-BLOCK-31-TO-82)]
    
    rule [BASIC-BLOCK-36-TO-100]: <kevm>
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
       andBool ( _W1 =/=Int 0
       andBool ( _K_CELL ==K _Gen1:OpCode
        ~> _Gen2:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen1:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))))
      [priority(20), label(BASIC-BLOCK-36-TO-100)]
    
    rule [BASIC-BLOCK-39-TO-101]: <kevm>
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
       andBool ( _W1 =/=Int 0
       andBool ( _K_CELL ==K __Gen0
        ~> _Gen2:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen1 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               )))))))
      [priority(20), label(BASIC-BLOCK-39-TO-101)]
    
    rule [BASIC-BLOCK-44-TO-115]: <kevm>
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
       andBool ( _W1 =/=Int 0
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
               )))))))
      [priority(20), label(BASIC-BLOCK-44-TO-115)]
    
    rule [BASIC-BLOCK-50-TO-147]: <kevm>
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
       andBool ( _W1 =/=Int 0
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( __Gen1 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( __Gen2 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))))))
      [priority(20), label(BASIC-BLOCK-50-TO-147)]
    
    rule [BASIC-BLOCK-57-TO-158]: <kevm>
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
       andBool ( _W1 =/=Int 0
       andBool ( _K_CELL ==K _Gen2:OpCode
        ~> _Gen3:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( __Gen1 ~> .K =/=K _Gen2:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))))))
      [priority(20), label(BASIC-BLOCK-57-TO-158)]
    
    rule [BASIC-BLOCK-61-TO-159]: <kevm>
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
       andBool ( _W1 =/=Int 0
       andBool ( _K_CELL ==K _Gen1:OpCode
        ~> _Gen3:OpCode
        ~> #execute
        ~> _DotVar4:K
       andBool ( W0:Int <Int lengthBytes ( JUMPDESTS_CELL:Bytes )
       andBool ( __Gen0 ~> .K =/=K _Gen1:OpCode ~> .K
       andBool ( __Gen2 ~> .K =/=K _Gen3:OpCode ~> .K
       andBool ( 1 ==Int JUMPDESTS_CELL:Bytes [ W0:Int ]
               ))))))))
      [priority(20), label(BASIC-BLOCK-61-TO-159)]
    
    rule [BASIC-BLOCK-69-TO-187]: <kevm>
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
       andBool ( _W1 =/=Int 0
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
               ))))))))
      [priority(20), label(BASIC-BLOCK-69-TO-187)]
    
    rule [BASIC-BLOCK-72-TO-188]: <kevm>
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
       andBool ( _W1 =/=Int 0
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
               ))))))))
      [priority(20), label(BASIC-BLOCK-72-TO-188)]
    
    rule [BASIC-BLOCK-197-TO-5]: <kevm>
           <k>
             ( #next [ JUMPI ] ~> .K => JUMPI W0:Int W1:Int
             ~> #pc [ JUMPI ] )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : WS:WordStack ) ) => WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires W1:Int ==Int 0
      [priority(20), label(BASIC-BLOCK-197-TO-5)]
    
    rule [BASIC-BLOCK-196-TO-6]: <kevm>
           <k>
             ( #next [ JUMPI ] ~> .K => JUMP W0:Int
             ~> #pc [ JUMPI ] )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : WS:WordStack ) ) => WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires W1:Int =/=Int 0
      [priority(20), label(BASIC-BLOCK-196-TO-6)]

endmodule
