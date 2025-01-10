
┌─ 1 (root, split, init)
│   k: #next [ SLOAD ] ~> _K_CELL:K
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
┃  │   k: #next [ SLOAD ] ~> _K_CELL:K
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
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ SLOAD ] ~> _K_CELL:K
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
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1 )
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) >Int 1024 )
   │
   ├─ 5
   │   k: #next [ SLOAD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (2 steps)
   ├─ 6
   │   k: #exec [ SLOAD ] ~> #pc [ SLOAD ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9 (split)
   ┃  │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
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
   ┃  ┃  │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  │
   ┃  ┃  │  (4 steps)
   ┃  ┃  ├─ 22
   ┃  ┃  │   k: Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_ ...
   ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┃ (1 step)
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 23 (split)
   ┃  ┃  ┃  │   k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃ (branch)
   ┃  ┃  ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃  ┃  ┃ constraint:
   ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ├─ 34
   ┃  ┃  ┃  ┃  │   k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  │  (2 steps)
   ┃  ┃  ┃  ┃  ├─ 54
   ┃  ┃  ┃  ┃  │   k: #accessStorage _ID_CELL:Account W0:Int ~> 0 ~> #deductGas ~> SLOAD W0:Int ~> #pc ...
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃  ┃ (1 step)
   ┃  ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ┃  └─ 72 (leaf, pending)
   ┃  ┃  ┃  ┃  ┃      k: 0 ~> #deductGas ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃  ┣━━┓
   ┃  ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ┃  └─ 73 (leaf, pending)
   ┃  ┃  ┃  ┃  ┃      k: 0 ~> #deductGas ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┃  ┗━━┓
   ┃  ┃  ┃  ┃     │
   ┃  ┃  ┃  ┃     └─ 74 (leaf, pending)
   ┃  ┃  ┃  ┃         k: #accessStorage _ID_CELL:Account W0:Int ~> 0 ~> #deductGas ~> SLOAD W0:Int ~> #pc ...
   ┃  ┃  ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃  ┃  ┃ constraint:
   ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  ├─ 50
   ┃  ┃  ┃  ┃  │   k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  │  (2 steps)
   ┃  ┃  ┃  ┃  └─ 71 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #accessStorage _ID_CELL:Account W0:Int ~> 0 ~> #deductGas ~> SLOAD W0:Int ~> #pc ...
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┣━━┓ subst: .Subst
   ┃  ┃  ┃  ┃  ┃ constraint:
   ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
   ┃  ┃  ┃  ┃  │
   ┃  ┃  ┃  ┃  └─ 77 (leaf, pending)
   ┃  ┃  ┃  ┃      k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃  ┃
   ┃  ┃  ┃  ┗━━┓ subst: .Subst
   ┃  ┃  ┃     ┃ constraint: true
   ┃  ┃  ┃     │
   ┃  ┃  ┃     └─ 78 (leaf, pending)
   ┃  ┃  ┃         k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃  ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃  ┃
   ┃  ┃  ┣━━┓
   ┃  ┃  ┃  │
   ┃  ┃  ┃  ├─ 24
   ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc  ...
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
   ┃  ┃         k: Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_ ...
   ┃  ┃         pc: _PC_CELL:Int
   ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓ subst: .Subst
   ┃     ┃ constraint:
   ┃     ┃     ( notBool _USEGAS_CELL:Bool )
   ┃     │
   ┃     ├─ 12
   ┃     │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     │
   ┃     │  (1 step)
   ┃     ├─ 19
   ┃     │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃     │   pc: _PC_CELL:Int
   ┃     │   callDepth: _CALLDEPTH_CELL:Int
   ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃     ┃
   ┃     ┃ (1 step)
   ┃     ┣━━┓
   ┃     ┃  │
   ┃     ┃  └─ 20 (leaf, pending)
   ┃     ┃      k: #lookup ( STORAGE:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃     ┃      pc: _PC_CELL:Int
   ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃     ┃
   ┃     ┗━━┓
   ┃        │
   ┃        ├─ 21
   ┃        │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃        │   pc: _PC_CELL:Int
   ┃        │   callDepth: _CALLDEPTH_CELL:Int
   ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃        ┃
   ┃        ┃ (1 step)
   ┃        ┣━━┓
   ┃        ┃  │
   ┃        ┃  └─ 31 (leaf, pending)
   ┃        ┃      k: #lookup ( STORAGE0:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃        ┃      pc: _PC_CELL:Int
   ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃        ┃
   ┃        ┗━━┓
   ┃           │
   ┃           ├─ 32
   ┃           │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃           │   pc: _PC_CELL:Int
   ┃           │   callDepth: _CALLDEPTH_CELL:Int
   ┃           │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃           ┃
   ┃           ┃ (1 step)
   ┃           ┣━━┓
   ┃           ┃  │
   ┃           ┃  └─ 47 (leaf, pending)
   ┃           ┃      k: #lookup ( STORAGE1:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃           ┃      pc: _PC_CELL:Int
   ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃           ┃
   ┃           ┗━━┓
   ┃              │
   ┃              ├─ 48
   ┃              │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃              │   pc: _PC_CELL:Int
   ┃              │   callDepth: _CALLDEPTH_CELL:Int
   ┃              │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃              ┃
   ┃              ┃ (1 step)
   ┃              ┣━━┓
   ┃              ┃  │
   ┃              ┃  └─ 66 (leaf, pending)
   ┃              ┃      k: #lookup ( STORAGE2:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃              ┃      pc: _PC_CELL:Int
   ┃              ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃              ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃              ┃
   ┃              ┗━━┓
   ┃                 │
   ┃                 └─ 67 (leaf, pending)
   ┃                     k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
   ┃                     pc: _PC_CELL:Int
   ┃                     callDepth: _CALLDEPTH_CELL:Int
   ┃                     statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #exec [ SLOAD ] ~> #pc [ SLOAD ] ~> _K_CELL:K
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  ├─ 13 (split)
      ┃  │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
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
      ┃  ┃  │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  │
      ┃  ┃  │  (4 steps)
      ┃  ┃  ├─ 33
      ┃  ┃  │   k: Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_ ...
      ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┃ (1 step)
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 40 (split)
      ┃  ┃  ┃  │   k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┃ (branch)
      ┃  ┃  ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃  ┃  ┃ constraint:
      ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  ├─ 59
      ┃  ┃  ┃  ┃  │   k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  │  (2 steps)
      ┃  ┃  ┃  ┃  └─ 86 (leaf, pending)
      ┃  ┃  ┃  ┃      k: #accessStorage _ID_CELL:Account W0:Int ~> 0 ~> #deductGas ~> SLOAD W0:Int ~> #pc ...
      ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┣━━┓ subst: .Subst
      ┃  ┃  ┃  ┃  ┃ constraint:
      ┃  ┃  ┃  ┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
      ┃  ┃  ┃  ┃  │
      ┃  ┃  ┃  ┃  └─ 87 (leaf, pending)
      ┃  ┃  ┃  ┃      k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  ┃
      ┃  ┃  ┃  ┗━━┓ subst: .Subst
      ┃  ┃  ┃     ┃ constraint: true
      ┃  ┃  ┃     │
      ┃  ┃  ┃     └─ 88 (leaf, pending)
      ┃  ┃  ┃         k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃  ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃
      ┃  ┃  ┣━━┓
      ┃  ┃  ┃  │
      ┃  ┃  ┃  ├─ 41
      ┃  ┃  ┃  │   k: #end EVMC_OUT_OF_GAS ~> #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc  ...
      ┃  ┃  ┃  │   pc: _PC_CELL:Int
      ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃  ┃  │
      ┃  ┃  ┃  │  (4 steps)
      ┃  ┃  ┃  └─ 70 (leaf, pending)
      ┃  ┃  ┃      k: #halt ~> _K_CELL:K
      ┃  ┃  ┃      pc: _PC_CELL:Int
      ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃  ┃      statusCode: EVMC_OUT_OF_GAS
      ┃  ┃  ┃
      ┃  ┃  ┗━━┓
      ┃  ┃     │
      ┃  ┃     └─ 42 (stuck, leaf)
      ┃  ┃         k: Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_ ...
      ┃  ┃         pc: _PC_CELL:Int
      ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
      ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
      ┃  ┃
      ┃  ┗━━┓ subst: .Subst
      ┃     ┃ constraint:
      ┃     ┃     ( notBool _USEGAS_CELL:Bool )
      ┃     │
      ┃     ├─ 16
      ┃     │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃     │   pc: _PC_CELL:Int
      ┃     │   callDepth: _CALLDEPTH_CELL:Int
      ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃     │
      ┃     │  (1 step)
      ┃     ├─ 30
      ┃     │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃     │   pc: _PC_CELL:Int
      ┃     │   callDepth: _CALLDEPTH_CELL:Int
      ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃     ┃
      ┃     ┃ (1 step)
      ┃     ┣━━┓
      ┃     ┃  │
      ┃     ┃  └─ 36 (leaf, pending)
      ┃     ┃      k: #lookup ( STORAGE:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃     ┃      pc: _PC_CELL:Int
      ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃     ┃
      ┃     ┗━━┓
      ┃        │
      ┃        ├─ 37
      ┃        │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃        │   pc: _PC_CELL:Int
      ┃        │   callDepth: _CALLDEPTH_CELL:Int
      ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃        ┃
      ┃        ┃ (1 step)
      ┃        ┣━━┓
      ┃        ┃  │
      ┃        ┃  └─ 52 (leaf, pending)
      ┃        ┃      k: #lookup ( STORAGE0:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃        ┃      pc: _PC_CELL:Int
      ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃        ┃
      ┃        ┗━━┓
      ┃           │
      ┃           ├─ 53
      ┃           │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃           │   pc: _PC_CELL:Int
      ┃           │   callDepth: _CALLDEPTH_CELL:Int
      ┃           │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃           ┃
      ┃           ┃ (1 step)
      ┃           ┣━━┓
      ┃           ┃  │
      ┃           ┃  └─ 79 (leaf, pending)
      ┃           ┃      k: #lookup ( STORAGE1:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃           ┃      pc: _PC_CELL:Int
      ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃           ┃
      ┃           ┗━━┓
      ┃              │
      ┃              └─ 80 (leaf, pending)
      ┃                  k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
      ┃                  pc: _PC_CELL:Int
      ┃                  callDepth: _CALLDEPTH_CELL:Int
      ┃                  statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 14
         │   k: #exec [ SLOAD ] ~> #pc [ SLOAD ] ~> _K_CELL:K
         │   pc: _PC_CELL:Int
         │   callDepth: _CALLDEPTH_CELL:Int
         │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  ├─ 17 (split)
         ┃  │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
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
         ┃  ┃  │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  │
         ┃  ┃  │  (4 steps)
         ┃  ┃  ├─ 46
         ┃  ┃  │   k: Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_ ...
         ┃  ┃  │   pc: _PC_CELL:Int
         ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┃ (1 step)
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 61 (leaf, pending)
         ┃  ┃  ┃      k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┣━━┓
         ┃  ┃  ┃  │
         ┃  ┃  ┃  └─ 62 (leaf, pending)
         ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc  ...
         ┃  ┃  ┃      pc: _PC_CELL:Int
         ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃  ┃
         ┃  ┃  ┗━━┓
         ┃  ┃     │
         ┃  ┃     └─ 63 (leaf, pending)
         ┃  ┃         k: Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_ ...
         ┃  ┃         pc: _PC_CELL:Int
         ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
         ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
         ┃  ┃
         ┃  ┗━━┓ subst: .Subst
         ┃     ┃ constraint:
         ┃     ┃     ( notBool _USEGAS_CELL:Bool )
         ┃     │
         ┃     ├─ 27
         ┃     │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
         ┃     │   pc: _PC_CELL:Int
         ┃     │   callDepth: _CALLDEPTH_CELL:Int
         ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃     │
         ┃     │  (1 step)
         ┃     ├─ 43
         ┃     │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
         ┃     │   pc: _PC_CELL:Int
         ┃     │   callDepth: _CALLDEPTH_CELL:Int
         ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃     ┃
         ┃     ┃ (1 step)
         ┃     ┣━━┓
         ┃     ┃  │
         ┃     ┃  └─ 56 (leaf, pending)
         ┃     ┃      k: #lookup ( STORAGE:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
         ┃     ┃      pc: _PC_CELL:Int
         ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃     ┃
         ┃     ┗━━┓
         ┃        │
         ┃        ├─ 57
         ┃        │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
         ┃        │   pc: _PC_CELL:Int
         ┃        │   callDepth: _CALLDEPTH_CELL:Int
         ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
         ┃        ┃
         ┃        ┃ (1 step)
         ┃        ┣━━┓
         ┃        ┃  │
         ┃        ┃  └─ 84 (leaf, pending)
         ┃        ┃      k: #lookup ( STORAGE0:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
         ┃        ┃      pc: _PC_CELL:Int
         ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
         ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
         ┃        ┃
         ┃        ┗━━┓
         ┃           │
         ┃           └─ 85 (leaf, pending)
         ┃               k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
         ┃               pc: _PC_CELL:Int
         ┃               callDepth: _CALLDEPTH_CELL:Int
         ┃               statusCode: _STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 18
            │   k: #exec [ SLOAD ] ~> #pc [ SLOAD ] ~> _K_CELL:K
            │   pc: _PC_CELL:Int
            │   callDepth: _CALLDEPTH_CELL:Int
            │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  ├─ 28 (split)
            ┃  │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
            ┃  │   pc: _PC_CELL:Int
            ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┃ (branch)
            ┃  ┣━━┓ subst: .Subst
            ┃  ┃  ┃ constraint:
            ┃  ┃  ┃     _USEGAS_CELL:Bool
            ┃  ┃  │
            ┃  ┃  ├─ 38
            ┃  ┃  │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
            ┃  ┃  │   pc: _PC_CELL:Int
            ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  │
            ┃  ┃  │  (4 steps)
            ┃  ┃  ├─ 58
            ┃  ┃  │   k: Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_ ...
            ┃  ┃  │   pc: _PC_CELL:Int
            ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┃ (1 step)
            ┃  ┃  ┣━━┓
            ┃  ┃  ┃  │
            ┃  ┃  ┃  └─ 81 (leaf, pending)
            ┃  ┃  ┃      k: #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
            ┃  ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┣━━┓
            ┃  ┃  ┃  │
            ┃  ┃  ┃  └─ 82 (leaf, pending)
            ┃  ┃  ┃      k: #end EVMC_OUT_OF_GAS ~> #access [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc  ...
            ┃  ┃  ┃      pc: _PC_CELL:Int
            ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃  ┃
            ┃  ┃  ┗━━┓
            ┃  ┃     │
            ┃  ┃     └─ 83 (leaf, pending)
            ┃  ┃         k: Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_ ...
            ┃  ┃         pc: _PC_CELL:Int
            ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
            ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
            ┃  ┃
            ┃  ┗━━┓ subst: .Subst
            ┃     ┃ constraint:
            ┃     ┃     ( notBool _USEGAS_CELL:Bool )
            ┃     │
            ┃     ├─ 39
            ┃     │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
            ┃     │   pc: _PC_CELL:Int
            ┃     │   callDepth: _CALLDEPTH_CELL:Int
            ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃     │
            ┃     │  (1 step)
            ┃     ├─ 55
            ┃     │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
            ┃     │   pc: _PC_CELL:Int
            ┃     │   callDepth: _CALLDEPTH_CELL:Int
            ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
            ┃     ┃
            ┃     ┃ (1 step)
            ┃     ┣━━┓
            ┃     ┃  │
            ┃     ┃  └─ 75 (leaf, pending)
            ┃     ┃      k: #lookup ( STORAGE:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> _K_CELL:K
            ┃     ┃      pc: _PC_CELL:Int
            ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
            ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
            ┃     ┃
            ┃     ┗━━┓
            ┃        │
            ┃        └─ 76 (leaf, pending)
            ┃            k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
            ┃            pc: _PC_CELL:Int
            ┃            callDepth: _CALLDEPTH_CELL:Int
            ┃            statusCode: _STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               ├─ 29
               │   k: #exec [ SLOAD ] ~> #pc [ SLOAD ] ~> _K_CELL:K
               │   pc: _PC_CELL:Int
               │   callDepth: _CALLDEPTH_CELL:Int
               │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┃ (1 step)
               ┣━━┓
               ┃  │
               ┃  ├─ 44 (split)
               ┃  │   k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
               ┃  │   pc: _PC_CELL:Int
               ┃  │   callDepth: _CALLDEPTH_CELL:Int
               ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┃ (branch)
               ┃  ┣━━┓ subst: .Subst
               ┃  ┃  ┃ constraint:
               ┃  ┃  ┃     _USEGAS_CELL:Bool
               ┃  ┃  │
               ┃  ┃  └─ 64 (leaf, pending)
               ┃  ┃      k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
               ┃  ┃      pc: _PC_CELL:Int
               ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
               ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
               ┃  ┃
               ┃  ┗━━┓ subst: .Subst
               ┃     ┃ constraint:
               ┃     ┃     ( notBool _USEGAS_CELL:Bool )
               ┃     │
               ┃     └─ 65 (leaf, pending)
               ┃         k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
               ┃         pc: _PC_CELL:Int
               ┃         callDepth: _CALLDEPTH_CELL:Int
               ┃         statusCode: _STATUSCODE_CELL:StatusCode
               ┃
               ┗━━┓
                  │
                  ├─ 45
                  │   k: #exec [ SLOAD ] ~> #pc [ SLOAD ] ~> _K_CELL:K
                  │   pc: _PC_CELL:Int
                  │   callDepth: _CALLDEPTH_CELL:Int
                  │   statusCode: _STATUSCODE_CELL:StatusCode
                  ┃
                  ┃ (1 step)
                  ┣━━┓
                  ┃  │
                  ┃  └─ 68 (leaf, pending)
                  ┃      k: #gas [ SLOAD , SLOAD W0:Int ] ~> SLOAD W0:Int ~> #pc [ SLOAD ] ~> _K_CELL:K
                  ┃      pc: _PC_CELL:Int
                  ┃      callDepth: _CALLDEPTH_CELL:Int
                  ┃      statusCode: _STATUSCODE_CELL:StatusCode
                  ┃
                  ┗━━┓
                     │
                     └─ 69 (leaf, pending)
                         k: #exec [ SLOAD ] ~> #pc [ SLOAD ] ~> _K_CELL:K
                         pc: _PC_CELL:Int
                         callDepth: _CALLDEPTH_CELL:Int
                         statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SLOAD-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ SLOAD ] ~> .K => #exec [ SLOAD ]
             ~> #pc [ SLOAD ] )
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
    
    rule [BASIC-BLOCK-3-TO-7]: <kevm>
           <k>
             ( #next [ SLOAD ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-3-TO-7)]
    
    rule [BASIC-BLOCK-4-TO-8]: <kevm>
           <k>
             ( #next [ SLOAD ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-4-TO-8)]
    
    rule [BASIC-BLOCK-12-TO-19]: <kevm>
           <k>
             ( #gas [ SLOAD , SLOAD W0:Int ] ~> .K => .K )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
             ( #gas [ SLOAD , SLOAD W0:Int ] ~> .K => Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) )
             ~> #deductGas
             ~> #access [ SLOAD , SLOAD W0:Int ] )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
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
             ( #gas [ SLOAD , SLOAD W0:Int ] ~> .K => .K )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
             ( #gas [ SLOAD , SLOAD W0:Int ] ~> .K => Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) )
             ~> #deductGas
             ~> #access [ SLOAD , SLOAD W0:Int ] )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   WS0:WordStack
                 </wordStack>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
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
    
    rule [BASIC-BLOCK-27-TO-43]: <kevm>
           <k>
             ( #gas [ SLOAD , SLOAD W0:Int ] ~> .K => .K )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
      [priority(20), label(BASIC-BLOCK-27-TO-43)]
    
    rule [BASIC-BLOCK-26-TO-46]: <kevm>
           <k>
             ( #gas [ SLOAD , SLOAD W0:Int ] ~> .K => Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) )
             ~> #deductGas
             ~> #access [ SLOAD , SLOAD W0:Int ] )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   WS1:WordStack
                 </wordStack>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
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
      [priority(20), label(BASIC-BLOCK-26-TO-46)]
    
    rule [BASIC-BLOCK-24-TO-49]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ SLOAD , SLOAD W0:Int ]
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ] => #halt ~> .K )
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
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
       andBool ( _GAS_CELL:Gas <Gas Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) )
               )))))
      [priority(20), label(BASIC-BLOCK-24-TO-49)]
    
    rule [BASIC-BLOCK-34-TO-54]: <kevm>
           <k>
             ( #access [ SLOAD , SLOAD W0:Int ] ~> .K => #accessStorage _ID_CELL:Account W0:Int
             ~> 0
             ~> #deductGas )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) ) => #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) >Int 1024 )
       andBool ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) ) <=Gas _GAS_CELL:Gas
               ))))))
       ensures #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-34-TO-54)]
    
    rule [BASIC-BLOCK-39-TO-55]: <kevm>
           <k>
             ( #gas [ SLOAD , SLOAD W0:Int ] ~> .K => .K )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
      [priority(20), label(BASIC-BLOCK-39-TO-55)]
    
    rule [BASIC-BLOCK-38-TO-58]: <kevm>
           <k>
             ( #gas [ SLOAD , SLOAD W0:Int ] ~> .K => Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) )
             ~> #deductGas
             ~> #access [ SLOAD , SLOAD W0:Int ] )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   WS2:WordStack
                 </wordStack>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
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
      [priority(20), label(BASIC-BLOCK-38-TO-58)]
    
    rule [BASIC-BLOCK-41-TO-70]: <kevm>
           <k>
             ( #end EVMC_OUT_OF_GAS
             ~> #access [ SLOAD , SLOAD W0:Int ]
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ] => #halt ~> .K )
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   WS0:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
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
       andBool ( _GAS_CELL:Gas <Gas Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) )
               ))))))
      [priority(20), label(BASIC-BLOCK-41-TO-70)]
    
    rule [BASIC-BLOCK-50-TO-71]: <kevm>
           <k>
             ( #access [ SLOAD , SLOAD W0:Int ] ~> .K => #accessStorage _ID_CELL:Account W0:Int
             ~> 0
             ~> #deductGas )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   WS:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) ) => #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS:WordStack )
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( WS:WordStack , 1 ) >Int 1024 )
       andBool ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) ) <=Gas _GAS_CELL:Gas
               ))))))
       ensures #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-50-TO-71)]
    
    rule [BASIC-BLOCK-59-TO-86]: <kevm>
           <k>
             ( #access [ SLOAD , SLOAD W0:Int ] ~> .K => #accessStorage _ID_CELL:Account W0:Int
             ~> 0
             ~> #deductGas )
             ~> SLOAD W0:Int
             ~> #pc [ SLOAD ]
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
                 <id>
                   _ID_CELL:Account
                 </id>
                 <wordStack>
                   WS0:WordStack
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas -Gas ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) ) => #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi )
                 </gas>
                 ...
               </callState>
               <substate>
                 <accessedStorage>
                   _ACCESSEDSTORAGE_CELL:Map
                 </accessedStorage>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : WS0:WordStack )
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( _WS ~> .K =/=K WS0:WordStack ~> .K
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool #sizeWordStack ( WS0:WordStack , 1 ) >Int 1024 )
       andBool ( Csload ( _SCHEDULE_CELL:Schedule , #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) ) <=Gas _GAS_CELL:Gas
               )))))))
       ensures #if #inStorage ( _ACCESSEDSTORAGE_CELL:Map , _ID_CELL:Account , W0:Int ) #then Gwarmstorageread < _SCHEDULE_CELL:Schedule > #else Gcoldsload < _SCHEDULE_CELL:Schedule > #fi <=Gas _GAS_CELL:Gas
      [priority(20), label(BASIC-BLOCK-59-TO-86)]

endmodule
