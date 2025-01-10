
┌─ 1 (root, split, init)
│   k: #next [ NOT ] ~> _K_CELL:K
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
┃  │   k: #next [ NOT ] ~> _K_CELL:K
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
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ NOT ] ~> _K_CELL:K
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
   │   k: #next [ NOT ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 6
   │   k: #exec [ NOT ] ~> #pc [ NOT ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 8 (split)
   ┃  │   k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
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
   ┃  ┃  │   k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 19
   ┃  ┃  │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ NOT , NOT W0:Int ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  └─ 20 (leaf, pending)
   ┃  ┃  ┃      k: #access [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 21
   ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT  ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  │  (4 steps)
   ┃  ┃  ┃  └─ 36 (leaf, terminal)
   ┃  ┃  ┃      k: #halt ~> _K_CELL:K
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 22 (stuck, leaf)
   ┃  ┃         k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ NOT , NOT W0:Int ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     └─ 12 (leaf, pending)
   ┃         k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 9
      │   k: #exec [ NOT ] ~> #pc [ NOT ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13 (split)
      ┃  │   k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
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
      ┃  ┃  │   k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (4 steps)
      ┃  ┃  ├─ 27
      ┃  ┃  │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ NOT , NOT W0:Int ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  └─ 30 (leaf, pending)
      ┃  ┃  ┃      k: #access [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 31
      ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT  ...
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  │
      ┃  ┃  ┃  │  (4 steps)
      ┃  ┃  ┃  └─ 38 (leaf, terminal)
      ┃  ┃  ┃      k: #halt ~> _K_CELL:K
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 32 (stuck, leaf)
      ┃  ┃         k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ NOT , NOT W0:Int ...
      ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     └─ 16 (leaf, pending)
      ┃         k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
      ┃         pc: _PC_CELL:Int
      ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 14
         │   k: #exec [ NOT ] ~> #pc [ NOT ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 17 (split)
         ┃  │   k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
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
         ┃  ┃  │   k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  │
         ┃  ┃  │  (4 steps)
         ┃  ┃  ├─ 33
         ┃  ┃  │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ NOT , NOT W0:Int ...
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┃ (1 step)
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 39 (leaf, pending)
         ┃  ┃  ┃      k: #access [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  ├─ 40
         ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT  ...
         ┃  ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃  │
         ┃  ┃  ┃  │  (4 steps)
         ┃  ┃  ┃  └─ 49 (leaf, pending)
         ┃  ┃  ┃      k: #halt ~> _K_CELL:K
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
         ┃  ┃  ┃
         ┃  ┃  ┗━━┓
         ┃  ┃     │
         ┃  ┃     └─ 41 (stuck, leaf)
         ┃  ┃         k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ NOT , NOT W0:Int ...
         ┃  ┃         pc: _PC_CELL:Int
         ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     └─ 24 (leaf, pending)
         ┃         k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
         ┃         pc: _PC_CELL:Int
         ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 18
            │   k: #exec [ NOT ] ~> #pc [ NOT ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  ├─ 25 (split)
            ┃  │   k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
            ┃  │   pc: _PC_CELL:Int
            ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┃ (branch)
            ┃  ┣━━┓ subst: .Subst
            ┃  ┃  ┃ constraint:
            ┃  ┃  ┃     _USEGAS_CELL:Bool
            ┃  ┃  │
            ┃  ┃  ├─ 28
            ┃  ┃  │   k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
            ┃  ┃  │   pc: _PC_CELL:Int
            ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  │
            ┃  ┃  │  (4 steps)
            ┃  ┃  ├─ 37
            ┃  ┃  │   k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ NOT , NOT W0:Int ...
            ┃  ┃  │   pc: _PC_CELL:Int
            ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┃ (1 step)
            ┃  ┃  ┣━━┓
            ┃  ┃  ┃  │
            ┃  ┃  ┃  └─ 44 (leaf, pending)
            ┃  ┃  ┃      k: #access [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
            ┃  ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┣━━┓
            ┃  ┃  ┃  │
            ┃  ┃  ┃  └─ 45 (leaf, pending)
            ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT  ...
            ┃  ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┗━━┓
            ┃  ┃     │
            ┃  ┃     └─ 46 (leaf, pending)
            ┃  ┃         k: Gverylow < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ NOT , NOT W0:Int ...
            ┃  ┃         pc: _PC_CELL:Int
            ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┗━━┓ subst: .Subst
            ┃     ┃ constraint:
            ┃     ┃     ( notBool _USEGAS_CELL:Bool )
            ┃     │
            ┃     └─ 29 (leaf, pending)
            ┃         k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
            ┃         pc: _PC_CELL:Int
            ┃         callDepth: _CALLDEPTH_CELL:Int
            ┃         statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               ├─ 26
               │   k: #exec [ NOT ] ~> #pc [ NOT ] ~> _K_CELL:K
               │   pc: _PC_CELL:Int
               │   callDepth: _CALLDEPTH_CELL:Int
               │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┃ (1 step)
               ┣━━┓
               ┃  │
               ┃  ├─ 34 (split)
               ┃  │   k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
               ┃  │   pc: _PC_CELL:Int
               ┃  │   callDepth: _CALLDEPTH_CELL:Int
               ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┃ (branch)
               ┃  ┣━━┓ subst: .Subst
               ┃  ┃  ┃ constraint:
               ┃  ┃  ┃     _USEGAS_CELL:Bool
               ┃  ┃  │
               ┃  ┃  └─ 42 (leaf, pending)
               ┃  ┃      k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
               ┃  ┃      pc: _PC_CELL:Int
               ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
               ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┗━━┓ subst: .Subst
               ┃     ┃ constraint:
               ┃     ┃     ( notBool _USEGAS_CELL:Bool )
               ┃     │
               ┃     └─ 43 (leaf, pending)
               ┃         k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
               ┃         pc: _PC_CELL:Int
               ┃         callDepth: _CALLDEPTH_CELL:Int
               ┃         statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┗━━┓
                  │
                  ├─ 35
                  │   k: #exec [ NOT ] ~> #pc [ NOT ] ~> _K_CELL:K
                  │   pc: _PC_CELL:Int
                  │   callDepth: _CALLDEPTH_CELL:Int
                  │   statusCode: _STATUSCODE_CELL:StatusCode
                  ┃
                  ┃ (1 step)
                  ┣━━┓
                  ┃  │
                  ┃  └─ 47 (leaf, pending)
                  ┃      k: #gas [ NOT , NOT W0:Int ] ~> NOT W0:Int ~> #pc [ NOT ] ~> _K_CELL:K
                  ┃      pc: _PC_CELL:Int
                  ┃      callDepth: _CALLDEPTH_CELL:Int
                  ┃      statusCode: _STATUSCODE_CELL:StatusCode
                  ┃
                  ┗━━┓
                     │
                     └─ 48 (leaf, pending)
                         k: #exec [ NOT ] ~> #pc [ NOT ] ~> _K_CELL:K
                         pc: _PC_CELL:Int
                         callDepth: _CALLDEPTH_CELL:Int
                         statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-NOT-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ NOT ] ~> .K => #exec [ NOT ]
             ~> #pc [ NOT ] )
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
             ( #next [ NOT ] => #halt )
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
    
    rule [BASIC-BLOCK-3-TO-10]: <kevm>
           <k>
             ( #next [ NOT ] => #halt )
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
    
    rule [BASIC-BLOCK-11-TO-19]: <kevm>
           <k>
             ( #gas [ NOT , NOT W0:Int ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ NOT , NOT W0:Int ] )
             ~> NOT W0:Int
             ~> #pc [ NOT ]
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-11-TO-19)]
    
    rule [BASIC-BLOCK-15-TO-27]: <kevm>
           <k>
             ( #gas [ NOT , NOT W0:Int ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ NOT , NOT W0:Int ] )
             ~> NOT W0:Int
             ~> #pc [ NOT ]
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
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-15-TO-27)]
    
    rule [BASIC-BLOCK-23-TO-33]: <kevm>
           <k>
             ( #gas [ NOT , NOT W0:Int ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ NOT , NOT W0:Int ] )
             ~> NOT W0:Int
             ~> #pc [ NOT ]
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
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-23-TO-33)]
    
    rule [BASIC-BLOCK-21-TO-36]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ NOT , NOT W0:Int ]
             ~> NOT W0:Int
             ~> #pc [ NOT ] => #halt ~> .K )
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) >Int 1024 )
       andBool ( _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
               )))))
      [priority(20), label(BASIC-BLOCK-21-TO-36)]
    
    rule [BASIC-BLOCK-28-TO-37]: <kevm>
           <k>
             ( #gas [ NOT , NOT W0:Int ] ~> .K => Gverylow < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ NOT , NOT W0:Int ] )
             ~> NOT W0:Int
             ~> #pc [ NOT ]
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
      [priority(20), label(BASIC-BLOCK-28-TO-37)]
    
    rule [BASIC-BLOCK-31-TO-38]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ NOT , NOT W0:Int ]
             ~> NOT W0:Int
             ~> #pc [ NOT ] => #halt ~> .K )
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
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) >Int 1024 )
       andBool ( _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
               ))))))
      [priority(20), label(BASIC-BLOCK-31-TO-38)]
    
    rule [BASIC-BLOCK-40-TO-49]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ NOT , NOT W0:Int ]
             ~> NOT W0:Int
             ~> #pc [ NOT ] => #halt ~> .K )
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
                   WS1:WordStack
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
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS1:WordStack )
       andBool ( _WS ~> .K =/=K WS1:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS1:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 1 ) >Int 1024 )
       andBool ( _GAS_CELL:Gas <Gas Gverylow < _SCHEDULE_CELL:Schedule >
               )))))))
      [priority(20), label(BASIC-BLOCK-40-TO-49)]

endmodule
