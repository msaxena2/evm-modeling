
┌─ 1 (root, split, init)
│   k: #next [ JUMP ] ~> _K_CELL:K
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
┃  │   k: #next [ JUMP ] ~> _K_CELL:K
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
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ JUMP ] ~> _K_CELL:K
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
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
   │
   ├─ 5
   │   k: #next [ JUMP ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 6
   │   k: #exec [ JUMP ] ~> #pc [ JUMP ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 8 (split)
   ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  │   pc: _PC_CELL:Int
   ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┃ (branch)
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     _USEGAS_CELL:Bool
   ┃  ┃  │
   ┃  ┃  ├─ 11
   ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 22
   ┃  ┃  │   k: Gmid < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ JUMP , JUMP W0:Int ] ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 23 (split)
   ┃  ┃  ┃  │   k: #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃ (branch)
   ┃  ┃  ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃  ┃  ┃ constraint:
   ┃  ┃  ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
   ┃  ┃  ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ├─ 91
   ┃  ┃  ┃  ┃  │   k: #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  │  (3 steps)
   ┃  ┃  ┃  ┃  └─ 72 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _K_CELL:K
   ┃  ┃  ┃  ┃      pc: W0:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃  ┃  ┃ constraint:
   ┃  ┃  ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
   ┃  ┃  ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ├─ 101
   ┃  ┃  ┃  ┃  │   k: #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  │  (1 step)
   ┃  ┃  ┃  ┃  └─ 65 (leaf, pending)
   ┃  ┃  ┃  ┃      k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┗━━┓ subst: .Subst
   ┃  ┃  ┃     ┃ constraint: true
   ┃  ┃  ┃     │
   ┃  ┃  ┃     ├─ 102
   ┃  ┃  ┃     │   k: #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  ┃     │   pc: _PC_CELL:Int
   ┃  ┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃     │
   ┃  ┃  ┃     │  (1 step)
   ┃  ┃  ┃     └─ 66 (leaf, pending)
   ┃  ┃  ┃         k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 24
   ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ J ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  │  (4 steps)
   ┃  ┃  ┃  └─ 49 (leaf, terminal)
   ┃  ┃  ┃      k: #halt ~> _K_CELL:K
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 25 (stuck, leaf)
   ┃  ┃         k: Gmid < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ JUMP , JUMP W0:Int ] ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
   ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
   ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
   ┃  ┃  │
   ┃  ┃  ├─ 87
   ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (3 steps)
   ┃  ┃  ├─ 32
   ┃  ┃  │   k: #endBasicBlock ~> _K_CELL:K
   ┃  ┃  │   pc: W0:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 41
   ┃  ┃  ┃  │   k: #execute ~> _DotVar2:K
   ┃  ┃  ┃  │   pc: W0:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ┊  constraint: true
   ┃  ┃  ┃  ┊  subst: ...
   ┃  ┃  ┃  └─ 2 (leaf, target)
   ┃  ┃  ┃      k: _K_CELL:K
   ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
   ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 42
   ┃  ┃  ┃  │   k: #endBasicBlock ~> _DotVar2:K
   ┃  ┃  ┃  │   pc: W0:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃ (1 step)
   ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  └─ 67 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #execute ~> _DotVar3:K
   ┃  ┃  ┃  ┃      pc: W0:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  └─ 68 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar3:K
   ┃  ┃  ┃  ┃      pc: W0:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┗━━┓
   ┃  ┃  ┃     │
   ┃  ┃  ┃     └─ 69 (leaf, pending)
   ┃  ┃  ┃         k: #endBasicBlock ~> _DotVar2:K
   ┃  ┃  ┃         pc: W0:Int
   ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     ├─ 43
   ┃  ┃     │   k: #endBasicBlock ~> _K_CELL:K
   ┃  ┃     │   pc: W0:Int
   ┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃     ┃
   ┃  ┃     ┃ (1 step)
   ┃  ┃     ┣━━┓
   ┃  ┃     ┃  │
   ┃  ┃     ┃  └─ 63 (leaf, pending)
   ┃  ┃     ┃      k: #endBasicBlock ~> _DotVar2:K
   ┃  ┃     ┃      pc: W0:Int
   ┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃     ┃
   ┃  ┃     ┗━━┓
   ┃  ┃        │
   ┃  ┃        └─ 64 (leaf, pending)
   ┃  ┃            k: #endBasicBlock ~> _K_CELL:K
   ┃  ┃            pc: W0:Int
   ┃  ┃            callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃            statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
   ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
   ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
   ┃  ┃  │
   ┃  ┃  ├─ 97
   ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (3 steps)
   ┃  ┃  ├─ 48
   ┃  ┃  │   k: #endBasicBlock ~> _K_CELL:K
   ┃  ┃  │   pc: W0:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 60
   ┃  ┃  ┃  │   k: #execute ~> _DotVar2:K
   ┃  ┃  ┃  │   pc: W0:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ┊  constraint: true
   ┃  ┃  ┃  ┊  subst: ...
   ┃  ┃  ┃  └─ 2 (leaf, target)
   ┃  ┃  ┃      k: _K_CELL:K
   ┃  ┃  ┃      pc: ?_FINAL_PC_CELL:Int
   ┃  ┃  ┃      callDepth: ?_FINAL_CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 61 (leaf, pending)
   ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar2:K
   ┃  ┃  ┃      pc: W0:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 62 (leaf, pending)
   ┃  ┃         k: #endBasicBlock ~> _K_CELL:K
   ┃  ┃         pc: W0:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
   ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
   ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
   ┃  ┃  │
   ┃  ┃  ├─ 103
   ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (3 steps)
   ┃  ┃  └─ 73 (leaf, pending)
   ┃  ┃      k: #endBasicBlock ~> _K_CELL:K
   ┃  ┃      pc: W0:Int
   ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃ constraint:
   ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
   ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
   ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
   ┃  ┃  │
   ┃  ┃  ├─ 107
   ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (1 step)
   ┃  ┃  └─ 83 (leaf, pending)
   ┃  ┃      k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     ├─ 108
   ┃     │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     │
   ┃     │  (1 step)
   ┃     └─ 84 (leaf, pending)
   ┃         k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 9
      │   k: #exec [ JUMP ] ~> #pc [ JUMP ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13 (split)
      ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  │   pc: _PC_CELL:Int
      ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┃ (branch)
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     _USEGAS_CELL:Bool
      ┃  ┃  │
      ┃  ┃  ├─ 15
      ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (4 steps)
      ┃  ┃  ├─ 31
      ┃  ┃  │   k: Gmid < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ JUMP , JUMP W0:Int ] ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 36 (split)
      ┃  ┃  ┃  │   k: #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┃ (branch)
      ┃  ┃  ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃  ┃  ┃ constraint:
      ┃  ┃  ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
      ┃  ┃  ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  ├─ 95
      ┃  ┃  ┃  ┃  │   k: #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  │  (1 step)
      ┃  ┃  ┃  ┃  └─ 77 (leaf, pending)
      ┃  ┃  ┃  ┃      k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┗━━┓ subst: .Subst
      ┃  ┃  ┃     ┃ constraint: true
      ┃  ┃  ┃     │
      ┃  ┃  ┃     ├─ 96
      ┃  ┃  ┃     │   k: #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃  ┃     │   pc: _PC_CELL:Int
      ┃  ┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃     │
      ┃  ┃  ┃     │  (1 step)
      ┃  ┃  ┃     └─ 78 (leaf, pending)
      ┃  ┃  ┃         k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 37
      ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ J ...
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  │
      ┃  ┃  ┃  │  (4 steps)
      ┃  ┃  ┃  └─ 82 (leaf, pending)
      ┃  ┃  ┃      k: #halt ~> _K_CELL:K
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 38 (stuck, leaf)
      ┃  ┃         k: Gmid < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ JUMP , JUMP W0:Int ] ...
      ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
      ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
      ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
      ┃  ┃  │
      ┃  ┃  ├─ 89
      ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (3 steps)
      ┃  ┃  ├─ 53
      ┃  ┃  │   k: #endBasicBlock ~> _K_CELL:K
      ┃  ┃  │   pc: W0:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  └─ 74 (leaf, pending)
      ┃  ┃  ┃      k: #execute ~> _DotVar2:K
      ┃  ┃  ┃      pc: W0:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  └─ 75 (leaf, pending)
      ┃  ┃  ┃      k: #endBasicBlock ~> _DotVar2:K
      ┃  ┃  ┃      pc: W0:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 76 (leaf, pending)
      ┃  ┃         k: #endBasicBlock ~> _K_CELL:K
      ┃  ┃         pc: W0:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
      ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
      ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
      ┃  ┃  │
      ┃  ┃  ├─ 99
      ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (1 step)
      ┃  ┃  └─ 51 (leaf, pending)
      ┃  ┃      k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃ constraint:
      ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
      ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
      ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
      ┃  ┃  │
      ┃  ┃  ├─ 105
      ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (1 step)
      ┃  ┃  └─ 85 (leaf, pending)
      ┃  ┃      k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     ├─ 106
      ┃     │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃     │   pc: _PC_CELL:Int
      ┃     │   callDepth: _CALLDEPTH_CELL:Int
      ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃     │
      ┃     │  (1 step)
      ┃     └─ 86 (leaf, pending)
      ┃         k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 14
         │   k: #exec [ JUMP ] ~> #pc [ JUMP ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 18 (split)
         ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
         ┃  │   pc: _PC_CELL:Int
         ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┃ (branch)
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     _USEGAS_CELL:Bool
         ┃  ┃  │
         ┃  ┃  ├─ 29
         ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  │
         ┃  ┃  │  (4 steps)
         ┃  ┃  ├─ 55
         ┃  ┃  │   k: Gmid < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ JUMP , JUMP W0:Int ] ...
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┃ (1 step)
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 79 (leaf, pending)
         ┃  ┃  ┃      k: #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 80 (leaf, pending)
         ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ J ...
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┗━━┓
         ┃  ┃     │
         ┃  ┃     └─ 81 (leaf, pending)
         ┃  ┃         k: Gmid < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ JUMP , JUMP W0:Int ] ...
         ┃  ┃         pc: _PC_CELL:Int
         ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     ( notBool _USEGAS_CELL:Bool )
         ┃  ┃  ┃     1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
         ┃  ┃  ┃     W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
         ┃  ┃  │
         ┃  ┃  ├─ 93
         ┃  ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  │
         ┃  ┃  │  (1 step)
         ┃  ┃  └─ 70 (leaf, pending)
         ┃  ┃      k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
         ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     ├─ 94
         ┃     │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
         ┃     │   pc: _PC_CELL:Int
         ┃     │   callDepth: _CALLDEPTH_CELL:Int
         ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃     │
         ┃     │  (1 step)
         ┃     └─ 71 (leaf, pending)
         ┃         k: JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
         ┃         pc: _PC_CELL:Int
         ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 19
            │   k: #exec [ JUMP ] ~> #pc [ JUMP ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  ├─ 39 (split)
            ┃  │   k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
            ┃  │   pc: _PC_CELL:Int
            ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┃ (branch)
            ┃  ┣━━┓ subst: .Subst
            ┃  ┃  ┃ constraint:
            ┃  ┃  ┃     _USEGAS_CELL:Bool
            ┃  ┃  │
            ┃  ┃  └─ 56 (leaf, pending)
            ┃  ┃      k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
            ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┗━━┓ subst: .Subst
            ┃     ┃ constraint:
            ┃     ┃     ( notBool _USEGAS_CELL:Bool )
            ┃     │
            ┃     └─ 57 (leaf, pending)
            ┃         k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
            ┃         pc: _PC_CELL:Int
            ┃         callDepth: _CALLDEPTH_CELL:Int
            ┃         statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               ├─ 40
               │   k: #exec [ JUMP ] ~> #pc [ JUMP ] ~> _K_CELL:K
               │   pc: _PC_CELL:Int
               │   callDepth: _CALLDEPTH_CELL:Int
               │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┃ (1 step)
               ┣━━┓
               ┃  │
               ┃  └─ 58 (leaf, pending)
               ┃      k: #gas [ JUMP , JUMP W0:Int ] ~> JUMP W0:Int ~> #pc [ JUMP ] ~> _K_CELL:K
               ┃      pc: _PC_CELL:Int
               ┃      callDepth: _CALLDEPTH_CELL:Int
               ┃      statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┗━━┓
                  │
                  └─ 59 (leaf, pending)
                      k: #exec [ JUMP ] ~> #pc [ JUMP ] ~> _K_CELL:K
                      pc: _PC_CELL:Int
                      callDepth: _CALLDEPTH_CELL:Int
                      statusCode: _STATUSCODE_CELL:StatusCode




module SUMMARY-JUMP-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ JUMP ] ~> .K => #exec [ JUMP ]
             ~> #pc [ JUMP ] )
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
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-6)]
    
    rule [BASIC-BLOCK-4-TO-7]: <kevm>
           <k>
             ( #next [ JUMP ] => #halt )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-7)]
    
    rule [BASIC-BLOCK-3-TO-10]: <kevm>
           <k>
             ( #next [ JUMP ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-3-TO-10)]
    
    rule [BASIC-BLOCK-11-TO-22]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => Gmid < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ JUMP , JUMP W0:Int ] )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-11-TO-22)]
    
    rule [BASIC-BLOCK-15-TO-31]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => Gmid < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ JUMP , JUMP W0:Int ] )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS0:WordStack )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-15-TO-31)]
    
    rule [BASIC-BLOCK-24-TO-49]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ JUMP , JUMP W0:Int ]
             ~> JUMP W0:Int
             ~> #pc [ JUMP ] => #halt ~> .K )
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( _GAS_CELL:Gas <Gas Gmid < _SCHEDULE_CELL:Schedule >
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-24-TO-49)]
    
    rule [BASIC-BLOCK-29-TO-55]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => Gmid < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ JUMP , JUMP W0:Int ] )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS1:WordStack )
       andBool ( _WS ~> .K =/=K WS1:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS1:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS1:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-29-TO-55)]
    
    rule [BASIC-BLOCK-37-TO-82]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ JUMP , JUMP W0:Int ]
             ~> JUMP W0:Int
             ~> #pc [ JUMP ] => #halt ~> .K )
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS0:WordStack )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) <Int 1 )
       andBool ( _GAS_CELL:Gas <Gas Gmid < _SCHEDULE_CELL:Schedule >
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-37-TO-82)]
    
    rule [BASIC-BLOCK-93-TO-70]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS1:WordStack
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
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS1:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( _WS ~> .K =/=K WS1:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS1:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS1:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))))
      [priority(20), label(BASIC-BLOCK-93-TO-70)]
    
    rule [BASIC-BLOCK-94-TO-71]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS1:WordStack )
       andBool ( _WS ~> .K =/=K WS1:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS1:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS1:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-94-TO-71)]
    
    rule [BASIC-BLOCK-95-TO-77]: <kevm>
           <k>
             ( #access [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS0:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas Gmid < _SCHEDULE_CELL:Schedule >
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
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS0:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) <Int 1 )
       andBool ( Gmid < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))))
      [priority(20), label(BASIC-BLOCK-95-TO-77)]
    
    rule [BASIC-BLOCK-96-TO-78]: <kevm>
           <k>
             ( #access [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                   _GAS_CELL:Gas -Gas Gmid < _SCHEDULE_CELL:Schedule >
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
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS0:WordStack )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) <Int 1 )
       andBool ( Gmid < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-96-TO-78)]
    
    rule [BASIC-BLOCK-99-TO-51]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS0:WordStack
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
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS0:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-99-TO-51)]
    
    rule [BASIC-BLOCK-101-TO-65]: <kevm>
           <k>
             ( #access [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas Gmid < _SCHEDULE_CELL:Schedule >
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
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( Gmid < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-101-TO-65)]
    
    rule [BASIC-BLOCK-102-TO-66]: <kevm>
           <k>
             ( #access [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                   _GAS_CELL:Gas -Gas Gmid < _SCHEDULE_CELL:Schedule >
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
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( Gmid < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-102-TO-66)]
    
    rule [BASIC-BLOCK-105-TO-85]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS0:WordStack
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
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS0:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-105-TO-85)]
    
    rule [BASIC-BLOCK-106-TO-86]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS0:WordStack )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-106-TO-86)]
    
    rule [BASIC-BLOCK-107-TO-83]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS:WordStack
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
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-107-TO-83)]
    
    rule [BASIC-BLOCK-108-TO-84]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ] ~> .K => .K )
             ~> JUMP W0:Int
             ~> #pc [ JUMP ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-108-TO-84)]
    
    rule [BASIC-BLOCK-87-TO-32]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ]
             ~> JUMP W0:Int
             ~> #pc [ JUMP ] => #endBasicBlock ~> .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <pc>
                   ( __PC_CELL => W0:Int )
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-87-TO-32)]
    
    rule [BASIC-BLOCK-97-TO-48]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ]
             ~> JUMP W0:Int
             ~> #pc [ JUMP ] => #endBasicBlock ~> .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <pc>
                   ( __PC_CELL => W0:Int )
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-97-TO-48)]
    
    rule [BASIC-BLOCK-89-TO-53]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ]
             ~> JUMP W0:Int
             ~> #pc [ JUMP ] => #endBasicBlock ~> .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS0:WordStack
                 </wordStack>
                 <pc>
                   ( __PC_CELL => W0:Int )
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS0:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS0:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-89-TO-53)]
    
    rule [BASIC-BLOCK-91-TO-72]: <kevm>
           <k>
             ( #access [ JUMP , JUMP W0:Int ]
             ~> JUMP W0:Int
             ~> #pc [ JUMP ] => #endBasicBlock ~> .K )
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
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <pc>
                   ( __PC_CELL => W0:Int )
                 </pc>
                 <gas>
                   _GAS_CELL:Gas -Gas Gmid < _SCHEDULE_CELL:Schedule >
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
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( Gmid < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-91-TO-72)]
    
    rule [BASIC-BLOCK-103-TO-73]: <kevm>
           <k>
             ( #gas [ JUMP , JUMP W0:Int ]
             ~> JUMP W0:Int
             ~> #pc [ JUMP ] => #endBasicBlock ~> .K )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <jumpDests>
                   _JUMPDESTS_CELL:Bytes
                 </jumpDests>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <pc>
                   ( __PC_CELL => W0:Int )
                 </pc>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( 1 ==Int _JUMPDESTS_CELL:Bytes [ W0:Int ]
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( W0:Int <Int lengthBytes ( _JUMPDESTS_CELL:Bytes )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-103-TO-73)]

endmodule
