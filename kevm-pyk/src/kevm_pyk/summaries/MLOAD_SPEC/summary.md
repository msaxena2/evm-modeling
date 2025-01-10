
┌─ 1 (root, split, init)
│   k: #next [ MLOAD ] ~> _K_CELL:K
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
┃  │   k: #next [ MLOAD ] ~> _K_CELL:K
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
┃  │   k: #next [ MLOAD ] ~> _K_CELL:K
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
   │   k: #next [ MLOAD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 6
   │   k: #exec [ MLOAD ] ~> #pc [ MLOAD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9 (split)
   ┃  │   k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
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
   ┃  ┃  │   k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 19
   ┃  ┃  │   k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 20
   ┃  ┃  ┃  │   k: #gas [ MLOAD W0:Int ] ~> #access [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  │  (2 steps)
   ┃  ┃  ┃  ├─ 28
   ┃  ┃  ┃  │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ MLOAD , MLOAD W0 ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃ (1 step)
   ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  └─ 32 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #access [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ├─ 33
   ┃  ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc  ...
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  │  (4 steps)
   ┃  ┃  ┃  ┃  └─ 47 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #halt ~> _K_CELL:K
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┗━━┓
   ┃  ┃  ┃     │
   ┃  ┃  ┃     └─ 34 (stuck, leaf)
   ┃  ┃  ┃         k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ MLOAD , MLOAD W0 ...
   ┃  ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 21
   ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #gas [ MLOAD W0:Int ] ~> #access [ MLOAD , MLOAD W0:Int  ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  │  (5 steps)
   ┃  ┃  ┃  └─ 38 (leaf, terminal)
   ┃  ┃  ┃      k: #halt ~> _K_CELL:K
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 22 (stuck, leaf)
   ┃  ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     └─ 12 (leaf, pending)
   ┃         k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #exec [ MLOAD ] ~> #pc [ MLOAD ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13 (split)
      ┃  │   k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
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
      ┃  ┃  │   k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (4 steps)
      ┃  ┃  ├─ 27
      ┃  ┃  │   k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 29
      ┃  ┃  ┃  │   k: #gas [ MLOAD W0:Int ] ~> #access [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc ...
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  │
      ┃  ┃  ┃  │  (2 steps)
      ┃  ┃  ┃  ├─ 41
      ┃  ┃  ┃  │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ MLOAD , MLOAD W0 ...
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┃ (1 step)
      ┃  ┃  ┃  ┣━━┓
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  └─ 48 (leaf, pending)
      ┃  ┃  ┃  ┃      k: #access [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
      ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┣━━┓
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  └─ 49 (leaf, pending)
      ┃  ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc  ...
      ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┗━━┓
      ┃  ┃  ┃     │
      ┃  ┃  ┃     └─ 50 (leaf, pending)
      ┃  ┃  ┃         k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ MLOAD , MLOAD W0 ...
      ┃  ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 30
      ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #gas [ MLOAD W0:Int ] ~> #access [ MLOAD , MLOAD W0:Int  ...
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  │
      ┃  ┃  ┃  │  (5 steps)
      ┃  ┃  ┃  └─ 42 (leaf, terminal)
      ┃  ┃  ┃      k: #halt ~> _K_CELL:K
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 31 (stuck, leaf)
      ┃  ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
      ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     └─ 16 (leaf, pending)
      ┃         k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 14
         │   k: #exec [ MLOAD ] ~> #pc [ MLOAD ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 17 (split)
         ┃  │   k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
         ┃  │   pc: _PC_CELL:Int
         ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┃ (branch)
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     _USEGAS_CELL:Bool
         ┃  ┃  │
         ┃  ┃  ├─ 23
         ┃  ┃  │   k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  │
         ┃  ┃  │  (4 steps)
         ┃  ┃  ├─ 37
         ┃  ┃  │   k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┃ (1 step)
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 43 (leaf, pending)
         ┃  ┃  ┃      k: #gas [ MLOAD W0:Int ] ~> #access [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc ...
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 44 (leaf, pending)
         ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #gas [ MLOAD W0:Int ] ~> #access [ MLOAD , MLOAD W0:Int  ...
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┗━━┓
         ┃  ┃     │
         ┃  ┃     └─ 45 (leaf, pending)
         ┃  ┃         k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
         ┃  ┃         pc: _PC_CELL:Int
         ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     └─ 24 (leaf, pending)
         ┃         k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
         ┃         pc: _PC_CELL:Int
         ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 18
            │   k: #exec [ MLOAD ] ~> #pc [ MLOAD ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  ├─ 25 (split)
            ┃  │   k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
            ┃  │   pc: _PC_CELL:Int
            ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┃ (branch)
            ┃  ┣━━┓ subst: .Subst
            ┃  ┃  ┃ constraint:
            ┃  ┃  ┃     _USEGAS_CELL:Bool
            ┃  ┃  │
            ┃  ┃  ├─ 35
            ┃  ┃  │   k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
            ┃  ┃  │   pc: _PC_CELL:Int
            ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  │
            ┃  ┃  │  (4 steps)
            ┃  ┃  └─ 46 (leaf, pending)
            ┃  ┃      k: ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W ...
            ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┗━━┓ subst: .Subst
            ┃     ┃ constraint:
            ┃     ┃     ( notBool _USEGAS_CELL:Bool )
            ┃     │
            ┃     └─ 36 (leaf, pending)
            ┃         k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
            ┃         pc: _PC_CELL:Int
            ┃         callDepth: _CALLDEPTH_CELL:Int
            ┃         statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               ├─ 26
               │   k: #exec [ MLOAD ] ~> #pc [ MLOAD ] ~> _K_CELL:K
               │   pc: _PC_CELL:Int
               │   callDepth: _CALLDEPTH_CELL:Int
               │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┃ (1 step)
               ┣━━┓
               ┃  │
               ┃  ├─ 39 (split)
               ┃  │   k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
               ┃  │   pc: _PC_CELL:Int
               ┃  │   callDepth: _CALLDEPTH_CELL:Int
               ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┃ (branch)
               ┃  ┣━━┓ subst: .Subst
               ┃  ┃  ┃ constraint:
               ┃  ┃  ┃     _USEGAS_CELL:Bool
               ┃  ┃  │
               ┃  ┃  └─ 51 (leaf, pending)
               ┃  ┃      k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
               ┃  ┃      pc: _PC_CELL:Int
               ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
               ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┗━━┓ subst: .Subst
               ┃     ┃ constraint:
               ┃     ┃     ( notBool _USEGAS_CELL:Bool )
               ┃     │
               ┃     └─ 52 (leaf, pending)
               ┃         k: #gas [ MLOAD , MLOAD W0:Int ] ~> MLOAD W0:Int ~> #pc [ MLOAD ] ~> _K_CELL:K
               ┃         pc: _PC_CELL:Int
               ┃         callDepth: _CALLDEPTH_CELL:Int
               ┃         statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┗━━┓
                  │
                  └─ 40 (leaf, pending)
                      k: #exec [ MLOAD ] ~> #pc [ MLOAD ] ~> _K_CELL:K
                      pc: _PC_CELL:Int
                      callDepth: _CALLDEPTH_CELL:Int
                      statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-MLOAD-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ MLOAD ] ~> .K => #exec [ MLOAD ]
             ~> #pc [ MLOAD ] )
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
             ( #next [ MLOAD ] => #halt )
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
             ( #next [ MLOAD ] => #halt )
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
    
    rule [BASIC-BLOCK-11-TO-19]: <kevm>
           <k>
             ( #gas [ MLOAD , MLOAD W0:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ MLOAD W0:Int ]
             ~> #access [ MLOAD , MLOAD W0:Int ] )
             ~> MLOAD W0:Int
             ~> #pc [ MLOAD ]
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
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) )
                 </memoryUsed>
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-11-TO-19)]
    
    rule [BASIC-BLOCK-15-TO-27]: <kevm>
           <k>
             ( #gas [ MLOAD , MLOAD W0:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ MLOAD W0:Int ]
             ~> #access [ MLOAD , MLOAD W0:Int ] )
             ~> MLOAD W0:Int
             ~> #pc [ MLOAD ]
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
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) )
                 </memoryUsed>
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
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-15-TO-27)]
    
    rule [BASIC-BLOCK-20-TO-28]: <kevm>
           <k>
             ( #gas [ MLOAD W0:Int ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas )
             ~> #access [ MLOAD , MLOAD W0:Int ]
             ~> MLOAD W0:Int
             ~> #pc [ MLOAD ]
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
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 )
                 </memoryUsed>
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               )))))
      [priority(20), label(BASIC-BLOCK-20-TO-28)]
    
    rule [BASIC-BLOCK-23-TO-37]: <kevm>
           <k>
             ( #gas [ MLOAD , MLOAD W0:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ MLOAD W0:Int ]
             ~> #access [ MLOAD , MLOAD W0:Int ] )
             ~> MLOAD W0:Int
             ~> #pc [ MLOAD ]
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
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) )
                 </memoryUsed>
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
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-23-TO-37)]
    
    rule [BASIC-BLOCK-21-TO-38]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #gas [ MLOAD W0:Int ]
             ~> #access [ MLOAD , MLOAD W0:Int ]
             ~> MLOAD W0:Int
             ~> #pc [ MLOAD ] => #halt ~> .K )
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
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 )
                 </memoryUsed>
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) >Int 1024 )
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))))
      [priority(20), label(BASIC-BLOCK-21-TO-38)]
    
    rule [BASIC-BLOCK-29-TO-41]: <kevm>
           <k>
             ( #gas [ MLOAD W0:Int ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas )
             ~> #access [ MLOAD , MLOAD W0:Int ]
             ~> MLOAD W0:Int
             ~> #pc [ MLOAD ]
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
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 )
                 </memoryUsed>
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
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
               ))))))
      [priority(20), label(BASIC-BLOCK-29-TO-41)]
    
    rule [BASIC-BLOCK-30-TO-42]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #gas [ MLOAD W0:Int ]
             ~> #access [ MLOAD , MLOAD W0:Int ]
             ~> MLOAD W0:Int
             ~> #pc [ MLOAD ] => #halt ~> .K )
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
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 )
                 </memoryUsed>
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
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) >Int 1024 )
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-30-TO-42)]
    
    rule [BASIC-BLOCK-35-TO-46]: <kevm>
           <k>
             ( #gas [ MLOAD , MLOAD W0:Int ] ~> .K => ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
             ~> #deductGas
             ~> #gas [ MLOAD W0:Int ]
             ~> #access [ MLOAD , MLOAD W0:Int ] )
             ~> MLOAD W0:Int
             ~> #pc [ MLOAD ]
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
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) )
                 </memoryUsed>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS2:WordStack )
       andBool ( _WS ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS1 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS2:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( WS2:WordStack , 1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-35-TO-46)]
    
    rule [BASIC-BLOCK-33-TO-47]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ MLOAD , MLOAD W0:Int ]
             ~> MLOAD W0:Int
             ~> #pc [ MLOAD ] => #halt ~> .K )
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
                   _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
                 </gas>
                 <memoryUsed>
                   #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 )
                 </memoryUsed>
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) >Int 1024 )
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , W0:Int , 32 ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas Gverylow < _SCHEDULE_CELL:Schedule >
               ))))))
      [priority(20), label(BASIC-BLOCK-33-TO-47)]

endmodule
