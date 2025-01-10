
┌─ 1 (root, split, init)
│   k: #next [ TLOAD ] ~> _K_CELL:K
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
┃  │   k: #next [ TLOAD ] ~> _K_CELL:K
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
┃  │   k: #next [ TLOAD ] ~> _K_CELL:K
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
   │   k: #next [ TLOAD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 6
   │   k: #exec [ TLOAD ] ~> #pc [ TLOAD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9 (split)
   ┃  │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
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
   ┃  ┃  │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 22
   ┃  ┃  │   k: Gwarmstorageread < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TLOAD ,  ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 23
   ┃  ┃  ┃  │   k: #access [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  │  (1 step)
   ┃  ┃  ┃  ├─ 34
   ┃  ┃  ┃  │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃ (1 step)
   ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  └─ 46 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #lookup ( TSTORAGE:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┗━━┓
   ┃  ┃  ┃     │
   ┃  ┃  ┃     ├─ 47
   ┃  ┃  ┃     │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃     │   pc: _PC_CELL:Int
   ┃  ┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃     ┃
   ┃  ┃  ┃     ┃ (1 step)
   ┃  ┃  ┃     ┣━━┓
   ┃  ┃  ┃     ┃  │
   ┃  ┃  ┃     ┃  └─ 64 (leaf, pending)
   ┃  ┃  ┃     ┃      k: #lookup ( TSTORAGE0:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃     ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃     ┃
   ┃  ┃  ┃     ┗━━┓
   ┃  ┃  ┃        │
   ┃  ┃  ┃        └─ 65 (leaf, pending)
   ┃  ┃  ┃            k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃            pc: _PC_CELL:Int
   ┃  ┃  ┃            callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃            statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 24
   ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc  ...
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  │
   ┃  ┃  ┃  │  (4 steps)
   ┃  ┃  ┃  └─ 48 (leaf, terminal)
   ┃  ┃  ┃      k: #halt ~> _K_CELL:K
   ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
   ┃  ┃  ┃
   ┃  ┃  ┗━━┓
   ┃  ┃     │
   ┃  ┃     └─ 25 (stuck, leaf)
   ┃  ┃         k: Gwarmstorageread < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TLOAD ,  ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     ├─ 12
   ┃     │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     │
   ┃     │  (1 step)
   ┃     ├─ 19
   ┃     │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     ┃
   ┃     ┃ (1 step)
   ┃     ┣━━┓
   ┃     ┃  │
   ┃     ┃  └─ 20 (leaf, pending)
   ┃     ┃      k: #lookup ( TSTORAGE:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃     ┃      pc: _PC_CELL:Int
   ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃     ┃
   ┃     ┗━━┓
   ┃        │
   ┃        ├─ 21
   ┃        │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃        │   pc: _PC_CELL:Int
   ┃        │   callDepth: _CALLDEPTH_CELL:Int
   ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃        ┃
   ┃        ┃ (1 step)
   ┃        ┣━━┓
   ┃        ┃  │
   ┃        ┃  └─ 31 (leaf, pending)
   ┃        ┃      k: #lookup ( TSTORAGE0:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃        ┃      pc: _PC_CELL:Int
   ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃        ┃
   ┃        ┗━━┓
   ┃           │
   ┃           ├─ 32
   ┃           │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃           │   pc: _PC_CELL:Int
   ┃           │   callDepth: _CALLDEPTH_CELL:Int
   ┃           │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃           ┃
   ┃           ┃ (1 step)
   ┃           ┣━━┓
   ┃           ┃  │
   ┃           ┃  └─ 49 (leaf, pending)
   ┃           ┃      k: #lookup ( TSTORAGE1:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃           ┃      pc: _PC_CELL:Int
   ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃           ┃
   ┃           ┗━━┓
   ┃              │
   ┃              ├─ 50
   ┃              │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃              │   pc: _PC_CELL:Int
   ┃              │   callDepth: _CALLDEPTH_CELL:Int
   ┃              │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃              ┃
   ┃              ┃ (1 step)
   ┃              ┣━━┓
   ┃              ┃  │
   ┃              ┃  └─ 68 (leaf, pending)
   ┃              ┃      k: #lookup ( TSTORAGE2:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃              ┃      pc: _PC_CELL:Int
   ┃              ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃              ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃              ┃
   ┃              ┗━━┓
   ┃                 │
   ┃                 └─ 69 (leaf, pending)
   ┃                     k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
   ┃                     pc: _PC_CELL:Int
   ┃                     callDepth: _CALLDEPTH_CELL:Int
   ┃                     statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #exec [ TLOAD ] ~> #pc [ TLOAD ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13 (split)
      ┃  │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
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
      ┃  ┃  │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (4 steps)
      ┃  ┃  ├─ 33
      ┃  ┃  │   k: Gwarmstorageread < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TLOAD ,  ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 39
      ┃  ┃  ┃  │   k: #access [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  │
      ┃  ┃  ┃  │  (1 step)
      ┃  ┃  ┃  ├─ 53
      ┃  ┃  ┃  │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┃ (1 step)
      ┃  ┃  ┃  ┣━━┓
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  └─ 70 (leaf, pending)
      ┃  ┃  ┃  ┃      k: #lookup ( TSTORAGE:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┗━━┓
      ┃  ┃  ┃     │
      ┃  ┃  ┃     └─ 71 (leaf, pending)
      ┃  ┃  ┃         k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃  ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 40
      ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc  ...
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  │
      ┃  ┃  ┃  │  (4 steps)
      ┃  ┃  ┃  └─ 63 (leaf, pending)
      ┃  ┃  ┃      k: #halt ~> _K_CELL:K
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 41 (stuck, leaf)
      ┃  ┃         k: Gwarmstorageread < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TLOAD ,  ...
      ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     ├─ 16
      ┃     │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃     │   pc: _PC_CELL:Int
      ┃     │   callDepth: _CALLDEPTH_CELL:Int
      ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃     │
      ┃     │  (1 step)
      ┃     ├─ 30
      ┃     │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃     │   pc: _PC_CELL:Int
      ┃     │   callDepth: _CALLDEPTH_CELL:Int
      ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃     ┃
      ┃     ┃ (1 step)
      ┃     ┣━━┓
      ┃     ┃  │
      ┃     ┃  └─ 35 (leaf, pending)
      ┃     ┃      k: #lookup ( TSTORAGE:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃     ┃      pc: _PC_CELL:Int
      ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃     ┃
      ┃     ┗━━┓
      ┃        │
      ┃        ├─ 36
      ┃        │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃        │   pc: _PC_CELL:Int
      ┃        │   callDepth: _CALLDEPTH_CELL:Int
      ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃        ┃
      ┃        ┃ (1 step)
      ┃        ┣━━┓
      ┃        ┃  │
      ┃        ┃  └─ 51 (leaf, pending)
      ┃        ┃      k: #lookup ( TSTORAGE0:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃        ┃      pc: _PC_CELL:Int
      ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃        ┃
      ┃        ┗━━┓
      ┃           │
      ┃           ├─ 52
      ┃           │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃           │   pc: _PC_CELL:Int
      ┃           │   callDepth: _CALLDEPTH_CELL:Int
      ┃           │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃           ┃
      ┃           ┃ (1 step)
      ┃           ┣━━┓
      ┃           ┃  │
      ┃           ┃  └─ 77 (leaf, pending)
      ┃           ┃      k: #lookup ( TSTORAGE1:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃           ┃      pc: _PC_CELL:Int
      ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃           ┃
      ┃           ┗━━┓
      ┃              │
      ┃              └─ 78 (leaf, pending)
      ┃                  k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
      ┃                  pc: _PC_CELL:Int
      ┃                  callDepth: _CALLDEPTH_CELL:Int
      ┃                  statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 14
         │   k: #exec [ TLOAD ] ~> #pc [ TLOAD ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 17 (split)
         ┃  │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
         ┃  │   pc: _PC_CELL:Int
         ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┃ (branch)
         ┃  ┣━━┓ subst: .Subst
         ┃  ┃  ┃ constraint:
         ┃  ┃  ┃     _USEGAS_CELL:Bool
         ┃  ┃  │
         ┃  ┃  ├─ 26
         ┃  ┃  │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  │
         ┃  ┃  │  (4 steps)
         ┃  ┃  ├─ 44
         ┃  ┃  │   k: Gwarmstorageread < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TLOAD ,  ...
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┃ (1 step)
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  ├─ 56
         ┃  ┃  ┃  │   k: #access [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
         ┃  ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃  │
         ┃  ┃  ┃  │  (1 step)
         ┃  ┃  ┃  └─ 79 (leaf, pending)
         ┃  ┃  ┃      k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  ├─ 57
         ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc  ...
         ┃  ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃  │
         ┃  ┃  ┃  │  (4 steps)
         ┃  ┃  ┃  └─ 80 (leaf, pending)
         ┃  ┃  ┃      k: #halt ~> _K_CELL:K
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
         ┃  ┃  ┃
         ┃  ┃  ┗━━┓
         ┃  ┃     │
         ┃  ┃     └─ 58 (stuck, leaf)
         ┃  ┃         k: Gwarmstorageread < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TLOAD ,  ...
         ┃  ┃         pc: _PC_CELL:Int
         ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     ├─ 27
         ┃     │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
         ┃     │   pc: _PC_CELL:Int
         ┃     │   callDepth: _CALLDEPTH_CELL:Int
         ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃     │
         ┃     │  (1 step)
         ┃     ├─ 45
         ┃     │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
         ┃     │   pc: _PC_CELL:Int
         ┃     │   callDepth: _CALLDEPTH_CELL:Int
         ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃     ┃
         ┃     ┃ (1 step)
         ┃     ┣━━┓
         ┃     ┃  │
         ┃     ┃  └─ 59 (leaf, pending)
         ┃     ┃      k: #lookup ( TSTORAGE:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
         ┃     ┃      pc: _PC_CELL:Int
         ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃     ┃
         ┃     ┗━━┓
         ┃        │
         ┃        └─ 60 (leaf, pending)
         ┃            k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
         ┃            pc: _PC_CELL:Int
         ┃            callDepth: _CALLDEPTH_CELL:Int
         ┃            statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 18
            │   k: #exec [ TLOAD ] ~> #pc [ TLOAD ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  ├─ 28 (split)
            ┃  │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
            ┃  │   pc: _PC_CELL:Int
            ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┃ (branch)
            ┃  ┣━━┓ subst: .Subst
            ┃  ┃  ┃ constraint:
            ┃  ┃  ┃     _USEGAS_CELL:Bool
            ┃  ┃  │
            ┃  ┃  ├─ 37
            ┃  ┃  │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
            ┃  ┃  │   pc: _PC_CELL:Int
            ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  │
            ┃  ┃  │  (4 steps)
            ┃  ┃  ├─ 55
            ┃  ┃  │   k: Gwarmstorageread < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TLOAD ,  ...
            ┃  ┃  │   pc: _PC_CELL:Int
            ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┃ (1 step)
            ┃  ┃  ┣━━┓
            ┃  ┃  ┃  │
            ┃  ┃  ┃  └─ 74 (leaf, pending)
            ┃  ┃  ┃      k: #access [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
            ┃  ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┣━━┓
            ┃  ┃  ┃  │
            ┃  ┃  ┃  └─ 75 (leaf, pending)
            ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc  ...
            ┃  ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┗━━┓
            ┃  ┃     │
            ┃  ┃     └─ 76 (leaf, pending)
            ┃  ┃         k: Gwarmstorageread < _SCHEDULE_CELL:Schedule > ~> #deductGas ~> #access [ TLOAD ,  ...
            ┃  ┃         pc: _PC_CELL:Int
            ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┗━━┓ subst: .Subst
            ┃     ┃ constraint:
            ┃     ┃     ( notBool _USEGAS_CELL:Bool )
            ┃     │
            ┃     ├─ 38
            ┃     │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
            ┃     │   pc: _PC_CELL:Int
            ┃     │   callDepth: _CALLDEPTH_CELL:Int
            ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃     │
            ┃     │  (1 step)
            ┃     ├─ 54
            ┃     │   k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
            ┃     │   pc: _PC_CELL:Int
            ┃     │   callDepth: _CALLDEPTH_CELL:Int
            ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃     ┃
            ┃     ┃ (1 step)
            ┃     ┣━━┓
            ┃     ┃  │
            ┃     ┃  └─ 72 (leaf, pending)
            ┃     ┃      k: #lookup ( TSTORAGE:Map , W0:Int ) ~> #push ~> #pc [ TLOAD ] ~> _K_CELL:K
            ┃     ┃      pc: _PC_CELL:Int
            ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃     ┃
            ┃     ┗━━┓
            ┃        │
            ┃        └─ 73 (leaf, pending)
            ┃            k: TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
            ┃            pc: _PC_CELL:Int
            ┃            callDepth: _CALLDEPTH_CELL:Int
            ┃            statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               ├─ 29
               │   k: #exec [ TLOAD ] ~> #pc [ TLOAD ] ~> _K_CELL:K
               │   pc: _PC_CELL:Int
               │   callDepth: _CALLDEPTH_CELL:Int
               │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┃ (1 step)
               ┣━━┓
               ┃  │
               ┃  ├─ 42 (split)
               ┃  │   k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
               ┃  │   pc: _PC_CELL:Int
               ┃  │   callDepth: _CALLDEPTH_CELL:Int
               ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┃ (branch)
               ┃  ┣━━┓ subst: .Subst
               ┃  ┃  ┃ constraint:
               ┃  ┃  ┃     _USEGAS_CELL:Bool
               ┃  ┃  │
               ┃  ┃  └─ 61 (leaf, pending)
               ┃  ┃      k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
               ┃  ┃      pc: _PC_CELL:Int
               ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
               ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┗━━┓ subst: .Subst
               ┃     ┃ constraint:
               ┃     ┃     ( notBool _USEGAS_CELL:Bool )
               ┃     │
               ┃     └─ 62 (leaf, pending)
               ┃         k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
               ┃         pc: _PC_CELL:Int
               ┃         callDepth: _CALLDEPTH_CELL:Int
               ┃         statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┗━━┓
                  │
                  ├─ 43
                  │   k: #exec [ TLOAD ] ~> #pc [ TLOAD ] ~> _K_CELL:K
                  │   pc: _PC_CELL:Int
                  │   callDepth: _CALLDEPTH_CELL:Int
                  │   statusCode: _STATUSCODE_CELL:StatusCode
                  ┃
                  ┃ (1 step)
                  ┣━━┓
                  ┃  │
                  ┃  └─ 66 (leaf, pending)
                  ┃      k: #gas [ TLOAD , TLOAD W0:Int ] ~> TLOAD W0:Int ~> #pc [ TLOAD ] ~> _K_CELL:K
                  ┃      pc: _PC_CELL:Int
                  ┃      callDepth: _CALLDEPTH_CELL:Int
                  ┃      statusCode: _STATUSCODE_CELL:StatusCode
                  ┃
                  ┗━━┓
                     │
                     └─ 67 (leaf, pending)
                         k: #exec [ TLOAD ] ~> #pc [ TLOAD ] ~> _K_CELL:K
                         pc: _PC_CELL:Int
                         callDepth: _CALLDEPTH_CELL:Int
                         statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-TLOAD-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ TLOAD ] ~> .K => #exec [ TLOAD ]
             ~> #pc [ TLOAD ] )
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
             ( #next [ TLOAD ] => #halt )
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
             ( #next [ TLOAD ] => #halt )
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
    
    rule [BASIC-BLOCK-12-TO-19]: <kevm>
           <k>
             ( #gas [ TLOAD , TLOAD W0:Int ] ~> .K => .K )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) >Int 1024 )
               ))))
      [priority(20), label(BASIC-BLOCK-12-TO-19)]
    
    rule [BASIC-BLOCK-11-TO-22]: <kevm>
           <k>
             ( #gas [ TLOAD , TLOAD W0:Int ] ~> .K => Gwarmstorageread < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ TLOAD , TLOAD W0:Int ] )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
      [priority(20), label(BASIC-BLOCK-11-TO-22)]
    
    rule [BASIC-BLOCK-16-TO-30]: <kevm>
           <k>
             ( #gas [ TLOAD , TLOAD W0:Int ] ~> .K => .K )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-16-TO-30)]
    
    rule [BASIC-BLOCK-15-TO-33]: <kevm>
           <k>
             ( #gas [ TLOAD , TLOAD W0:Int ] ~> .K => Gwarmstorageread < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ TLOAD , TLOAD W0:Int ] )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
      [priority(20), label(BASIC-BLOCK-15-TO-33)]
    
    rule [BASIC-BLOCK-23-TO-34]: <kevm>
           <k>
             ( #access [ TLOAD , TLOAD W0:Int ] ~> .K => .K )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
                   _GAS_CELL:Gas -Gas Gwarmstorageread < _SCHEDULE_CELL:Schedule >
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
       andBool ( Gwarmstorageread < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               )))))
      [priority(20), label(BASIC-BLOCK-23-TO-34)]
    
    rule [BASIC-BLOCK-26-TO-44]: <kevm>
           <k>
             ( #gas [ TLOAD , TLOAD W0:Int ] ~> .K => Gwarmstorageread < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ TLOAD , TLOAD W0:Int ] )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
      [priority(20), label(BASIC-BLOCK-26-TO-44)]
    
    rule [BASIC-BLOCK-27-TO-45]: <kevm>
           <k>
             ( #gas [ TLOAD , TLOAD W0:Int ] ~> .K => .K )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
       andBool ( ( notBool #sizeWordStack ( WS1:WordStack , 1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-27-TO-45)]
    
    rule [BASIC-BLOCK-24-TO-48]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ TLOAD , TLOAD W0:Int ]
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ] => #halt ~> .K )
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
       andBool ( _GAS_CELL:Gas <Gas Gwarmstorageread < _SCHEDULE_CELL:Schedule >
               )))))
      [priority(20), label(BASIC-BLOCK-24-TO-48)]
    
    rule [BASIC-BLOCK-39-TO-53]: <kevm>
           <k>
             ( #access [ TLOAD , TLOAD W0:Int ] ~> .K => .K )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
                   _GAS_CELL:Gas -Gas Gwarmstorageread < _SCHEDULE_CELL:Schedule >
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
       andBool ( Gwarmstorageread < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               ))))))
      [priority(20), label(BASIC-BLOCK-39-TO-53)]
    
    rule [BASIC-BLOCK-38-TO-54]: <kevm>
           <k>
             ( #gas [ TLOAD , TLOAD W0:Int ] ~> .K => .K )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _USEGAS_CELL:Bool )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS2:WordStack )
       andBool ( _WS ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS0 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( _WS1 ~> .K =/=K WS2:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS2:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( WS2:WordStack , 1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-38-TO-54)]
    
    rule [BASIC-BLOCK-37-TO-55]: <kevm>
           <k>
             ( #gas [ TLOAD , TLOAD W0:Int ] ~> .K => Gwarmstorageread < _SCHEDULE_CELL:Schedule >
             ~> #deductGas
             ~> #access [ TLOAD , TLOAD W0:Int ] )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
      [priority(20), label(BASIC-BLOCK-37-TO-55)]
    
    rule [BASIC-BLOCK-40-TO-63]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ TLOAD , TLOAD W0:Int ]
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ] => #halt ~> .K )
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
       andBool ( _GAS_CELL:Gas <Gas Gwarmstorageread < _SCHEDULE_CELL:Schedule >
               ))))))
      [priority(20), label(BASIC-BLOCK-40-TO-63)]
    
    rule [BASIC-BLOCK-56-TO-79]: <kevm>
           <k>
             ( #access [ TLOAD , TLOAD W0:Int ] ~> .K => .K )
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ]
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
                   _GAS_CELL:Gas -Gas Gwarmstorageread < _SCHEDULE_CELL:Schedule >
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
       andBool ( Gwarmstorageread < _SCHEDULE_CELL:Schedule > <=Gas _GAS_CELL:Gas
               )))))))
      [priority(20), label(BASIC-BLOCK-56-TO-79)]
    
    rule [BASIC-BLOCK-57-TO-80]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ TLOAD , TLOAD W0:Int ]
             ~> TLOAD W0:Int
             ~> #pc [ TLOAD ] => #halt ~> .K )
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
       andBool ( _GAS_CELL:Gas <Gas Gwarmstorageread < _SCHEDULE_CELL:Schedule >
               )))))))
      [priority(20), label(BASIC-BLOCK-57-TO-80)]

endmodule
