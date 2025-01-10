
┌─ 1 (root, init)
│   k: #next [ CALL ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (1 step)
┣━━┓
┃  │
┃  └─ 3 (leaf, pending)
┃      k: #end EVMC_STACK_UNDERFLOW ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓
┃  │
┃  └─ 4 (leaf, pending)
┃      k: #end EVMC_STACK_OVERFLOW ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓
┃  │
┃  ├─ 5
┃  │   k: #addr [ CALL ] ~> #exec [ CALL ] ~> #pc [ CALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 8 (leaf, pending)
┃  ┃      k: #exec [ CALL ] ~> #pc [ CALL ] ~> _K_CELL:K
┃  ┃      pc: _PC_CELL:Int
┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 9 (leaf, pending)
┃         k: #addr [ CALL ] ~> #exec [ CALL ] ~> #pc [ CALL ] ~> _K_CELL:K
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓
┃  │
┃  └─ 6 (leaf, pending)
┃      k: #end EVMC_STATIC_MODE_VIOLATION ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓
   │
   ├─ 7
   │   k: #next [ CALL ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   ┊  constraint:
   ┊      false
   ┊  subst: .Subst
   └─ 2 (leaf, target)
       k: _K_CELL:K
       pc: ?_FINAL_PC_CELL:Int
       callDepth: ?_FINAL_CALLDEPTH_CELL:Int
       statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode




module SUMMARY-CALL-SPEC
    
    
    

endmodule
