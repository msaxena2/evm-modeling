
┌─ 1 (root, split, init)
│   k: #next [ SELFDESTRUCT ] ~> _K_CELL:K
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
┃  │   k: #next [ SELFDESTRUCT ] ~> _K_CELL:K
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
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ SELFDESTRUCT ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 10 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STACK_OVERFLOW
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _STATIC_CELL:Bool )
┃  ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1 )
┃  ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
┃  │
┃  ├─ 5
┃  │   k: #next [ SELFDESTRUCT ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (1 step)
┃  ├─ 7
┃  │   k: #addr [ SELFDESTRUCT ] ~> #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_C ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 11 (split)
┃  ┃  │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     _USEGAS_CELL:Bool
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 56
┃  ┃  ┃  │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (4 steps)
┃  ┃  ┃  ├─ 23
┃  ┃  ┃  │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( W0:Int modInt pow160 ) ) ~>  ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┃ (1 step)
┃  ┃  ┃  ┣━━┓
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 24
┃  ┃  ┃  ┃  │   k: Cselfdestruct ( _SCHEDULE_CELL:Schedule , #accountNonexistent ( ( W0:Int modInt  ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  ├─ 41 (split)
┃  ┃  ┃  ┃  │   k: #accountNonexistent ( ( W0:Int modInt pow160 ) ) ~> #freezerCselfdestruct1_ ( _S ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃ (branch)
┃  ┃  ┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃  ┃  ┃     _Gen29:NonceCell ==K <nonce>
  NONCE:Int
</nonce>
┃  ┃  ┃  ┃  ┃  ┃     _Gen25:CodeCell ==K <code>
  CODE:AccountCode
</code>
┃  ┃  ┃  ┃  ┃  ┃     ACCTFROM:Int ==Int ( W0:Int modInt pow160 )
┃  ┃  ┃  ┃  ┃  ┃     _ID_CELL:Account ==K ( W0:Int modInt pow160 )
┃  ┃  ┃  ┃  ┃  ┃     ( notBool <acctID>
  ( W0:Int modInt pow160 )
</acctID> in_keys ( _DotVar8:AccountCellMap ) )
┃  ┃  ┃  ┃  ┃  ┃     _ACCOUNTS_CELL:AccountCellMap ==K ( <account>
  <acctID>
    ( W0:Int modInt pow160 )
  </acctID>
  <balance>
    BAL:Int
  </balance>
  <code>
    CODE:AccountCode
  </code>
  _Gen26:StorageCell
  _Gen27:OrigStorageCell
  _Gen28:TransientStorageCell
  <nonce>
    NONCE:Int
  </nonce>
</account>
_DotVar8:AccountCellMap )
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 53 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #accountNonexistent ( ( W0:Int modInt pow160 ) ) ~> #freezerCselfdestruct1_ ( _S ...
┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃  ┃  ┃     ( notBool <acctID>
  ACCTFROM:Int
</acctID> in_keys ( AC3_:AccountCellMap ) )
┃  ┃  ┃  ┃  ┃  ┃     ( notBool ACCTFROM:Int ==Int ( W0:Int modInt pow160 ) )
┃  ┃  ┃  ┃  ┃  ┃     ( notBool <acctID>
  ( W0:Int modInt pow160 )
</acctID> in_keys ( AC3_:AccountCellMap ) )
┃  ┃  ┃  ┃  ┃  ┃     _DotVar8:AccountCellMap ==K ( <account>
  <acctID>
    ( W0:Int modInt pow160 )
  </acctID>
  <balance>
    BAL:Int
  </balance>
  <code>
    CODE:AccountCode
  </code>
  _Gen0:StorageCell
  _Gen1:OrigStorageCell
  _Gen2:TransientStorageCell
  <nonce>
    NONCE:Int
  </nonce>
</account>
AC3_:AccountCellMap )
┃  ┃  ┃  ┃  ┃  ┃     _ACCOUNTS_CELL:AccountCellMap ==K ( <account>
  <acctID>
    ( W0:Int modInt pow160 )
  </acctID>
  <balance>
    BAL:Int
  </balance>
  <code>
    CODE:AccountCode
  </code>
  _Gen0:StorageCell
  _Gen1:OrigStorageCell
  _Gen2:TransientStorageCell
  <nonce>
    NONCE:Int
  </nonce>
</account>
( <account>
  <acctID>
    ACCTFROM:Int
  </acctID>
  <balance>
    BAL:Int
  </balance>
  _Gen25:CodeCell
  _Gen26:StorageCell
  _Gen27:OrigStorageCell
  _Gen28:TransientStorageCell
  _Gen29:NonceCell
</account>
AC3_:AccountCellMap ) )
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 54 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #accountNonexistent ( ( W0:Int modInt pow160 ) ) ~> #freezerCselfdestruct1_ ( _S ...
┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┗━━┓ subst: .Subst
┃  ┃  ┃  ┃     ┃ constraint: true
┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃     └─ 55 (leaf, pending)
┃  ┃  ┃  ┃         k: #accountNonexistent ( ( W0:Int modInt pow160 ) ) ~> #freezerCselfdestruct1_ ( _S ...
┃  ┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓
┃  ┃  ┃     │
┃  ┃  ┃     ├─ 25
┃  ┃  ┃     │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( W0:Int modInt pow160 ) ) ~>  ...
┃  ┃  ┃     │   pc: _PC_CELL:Int
┃  ┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃
┃  ┃  ┃     ┃ (1 step)
┃  ┃  ┃     ┣━━┓
┃  ┃  ┃     ┃  │
┃  ┃  ┃     ┃  └─ 36 (leaf, pending)
┃  ┃  ┃     ┃      k: Cselfdestruct ( _SCHEDULE_CELL:Schedule , #accountNonexistent ( ( W0:Int modInt  ...
┃  ┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃     ┃
┃  ┃  ┃     ┗━━┓
┃  ┃  ┃        │
┃  ┃  ┃        └─ 37 (leaf, pending)
┃  ┃  ┃            k: #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( W0:Int modInt pow160 ) ) ~>  ...
┃  ┃  ┃            pc: _PC_CELL:Int
┃  ┃  ┃            callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃            statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃  ┃     │
┃  ┃     ├─ 57
┃  ┃     │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     │
┃  ┃     │  (2 steps)
┃  ┃     ├─ 26
┃  ┃     │   k: SELFDESTRUCT ( W0:Int modInt pow160 ) ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┃ (1 step)
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  ├─ 27
┃  ┃     ┃  │   k: #touchAccounts ACCT:Int ( W0:Int modInt pow160 ) ~> #accessAccounts ( W0:Int mod ...
┃  ┃     ┃  │   pc: _PC_CELL:Int
┃  ┃     ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  │
┃  ┃     ┃  │  (4 steps)
┃  ┃     ┃  └─ 42 (leaf, pending)
┃  ┃     ┃      k: #transferFunds ACCT:Int ( W0:Int modInt pow160 ) BALFROM:Int ~> #end EVMC_SUCCES ...
┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  ├─ 28
┃  ┃     ┃  │   k: #touchAccounts ( W0:Int modInt pow160 ) ~> #accessAccounts ( W0:Int modInt pow16 ...
┃  ┃     ┃  │   pc: _PC_CELL:Int
┃  ┃     ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  │
┃  ┃     ┃  │  (4 steps)
┃  ┃     ┃  └─ 50 (leaf, pending)
┃  ┃     ┃      k: #halt ~> _K_CELL:K
┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃      statusCode: EVMC_SUCCESS
┃  ┃     ┃
┃  ┃     ┗━━┓
┃  ┃        │
┃  ┃        ├─ 29
┃  ┃        │   k: SELFDESTRUCT ( W0:Int modInt pow160 ) ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃  ┃        │   pc: _PC_CELL:Int
┃  ┃        │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┃ (1 step)
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  └─ 43 (leaf, pending)
┃  ┃        ┃      k: #touchAccounts ACCT0:Int ( W0:Int modInt pow160 ) ~> #accessAccounts ( W0:Int mo ...
┃  ┃        ┃      pc: _PC_CELL:Int
┃  ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  └─ 44 (leaf, pending)
┃  ┃        ┃      k: #touchAccounts ( W0:Int modInt pow160 ) ~> #accessAccounts ( W0:Int modInt pow16 ...
┃  ┃        ┃      pc: _PC_CELL:Int
┃  ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┗━━┓
┃  ┃           │
┃  ┃           └─ 45 (leaf, pending)
┃  ┃               k: SELFDESTRUCT ( W0:Int modInt pow160 ) ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃  ┃               pc: _PC_CELL:Int
┃  ┃               callDepth: _CALLDEPTH_CELL:Int
┃  ┃               statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 12
┃     │   k: #addr [ SELFDESTRUCT ] ~> #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_C ...
┃     │   pc: _PC_CELL:Int
┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┃ (1 step)
┃     ┣━━┓
┃     ┃  │
┃     ┃  ├─ 14 (split)
┃     ┃  │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃     ┃  │   pc: _PC_CELL:Int
┃     ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┃ (branch)
┃     ┃  ┣━━┓ subst: .Subst
┃     ┃  ┃  ┃ constraint:
┃     ┃  ┃  ┃     _USEGAS_CELL:Bool
┃     ┃  ┃  │
┃     ┃  ┃  ├─ 58
┃     ┃  ┃  │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  │
┃     ┃  ┃  │  (4 steps)
┃     ┃  ┃  ├─ 33
┃     ┃  ┃  │   k: #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( W1:Int modInt pow160 ) ) ~>  ...
┃     ┃  ┃  │   pc: _PC_CELL:Int
┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┃ (1 step)
┃     ┃  ┃  ┣━━┓
┃     ┃  ┃  ┃  │
┃     ┃  ┃  ┃  └─ 39 (leaf, pending)
┃     ┃  ┃  ┃      k: Cselfdestruct ( _SCHEDULE_CELL:Schedule , #accountNonexistent ( ( W1:Int modInt  ...
┃     ┃  ┃  ┃      pc: _PC_CELL:Int
┃     ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃  ┃
┃     ┃  ┃  ┗━━┓
┃     ┃  ┃     │
┃     ┃  ┃     └─ 40 (leaf, pending)
┃     ┃  ┃         k: #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( W1:Int modInt pow160 ) ) ~>  ...
┃     ┃  ┃         pc: _PC_CELL:Int
┃     ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃     ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃  ┃
┃     ┃  ┗━━┓ subst: .Subst
┃     ┃     ┃ constraint:
┃     ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃     ┃     │
┃     ┃     ├─ 59
┃     ┃     │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃     ┃     │   pc: _PC_CELL:Int
┃     ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     │
┃     ┃     │  (2 steps)
┃     ┃     ├─ 38
┃     ┃     │   k: SELFDESTRUCT ( W1:Int modInt pow160 ) ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃     ┃     │   pc: _PC_CELL:Int
┃     ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃     ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     ┃
┃     ┃     ┃ (1 step)
┃     ┃     ┣━━┓
┃     ┃     ┃  │
┃     ┃     ┃  └─ 47 (leaf, pending)
┃     ┃     ┃      k: #touchAccounts ACCT:Int ( W1:Int modInt pow160 ) ~> #accessAccounts ( W1:Int mod ...
┃     ┃     ┃      pc: _PC_CELL:Int
┃     ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     ┃
┃     ┃     ┣━━┓
┃     ┃     ┃  │
┃     ┃     ┃  └─ 48 (leaf, pending)
┃     ┃     ┃      k: #touchAccounts ( W1:Int modInt pow160 ) ~> #accessAccounts ( W1:Int modInt pow16 ...
┃     ┃     ┃      pc: _PC_CELL:Int
┃     ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃     ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃     ┃
┃     ┃     ┗━━┓
┃     ┃        │
┃     ┃        └─ 49 (leaf, pending)
┃     ┃            k: SELFDESTRUCT ( W1:Int modInt pow160 ) ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃     ┃            pc: _PC_CELL:Int
┃     ┃            callDepth: _CALLDEPTH_CELL:Int
┃     ┃            statusCode: _STATUSCODE_CELL:StatusCode
┃     ┃
┃     ┗━━┓
┃        │
┃        ├─ 15
┃        │   k: #addr [ SELFDESTRUCT ] ~> #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_C ...
┃        │   pc: _PC_CELL:Int
┃        │   callDepth: _CALLDEPTH_CELL:Int
┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┃ (1 step)
┃        ┣━━┓
┃        ┃  │
┃        ┃  ├─ 19 (split)
┃        ┃  │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃        ┃  │   pc: _PC_CELL:Int
┃        ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┃ (branch)
┃        ┃  ┣━━┓ subst: .Subst
┃        ┃  ┃  ┃ constraint:
┃        ┃  ┃  ┃     _USEGAS_CELL:Bool
┃        ┃  ┃  │
┃        ┃  ┃  ├─ 60
┃        ┃  ┃  │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃        ┃  ┃  │   pc: _PC_CELL:Int
┃        ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃  │
┃        ┃  ┃  │  (1 step)
┃        ┃  ┃  └─ 34 (leaf, pending)
┃        ┃  ┃      k: #gas [ SELFDESTRUCT , SELFDESTRUCT ( W2:Int modInt pow160 ) ] ~> SELFDESTRUCT (  ...
┃        ┃  ┃      pc: _PC_CELL:Int
┃        ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃        ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃  ┃
┃        ┃  ┗━━┓ subst: .Subst
┃        ┃     ┃ constraint:
┃        ┃     ┃     ( notBool _USEGAS_CELL:Bool )
┃        ┃     │
┃        ┃     ├─ 61
┃        ┃     │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃        ┃     │   pc: _PC_CELL:Int
┃        ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃        ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃     │
┃        ┃     │  (1 step)
┃        ┃     └─ 35 (leaf, pending)
┃        ┃         k: #gas [ SELFDESTRUCT , SELFDESTRUCT ( W2:Int modInt pow160 ) ] ~> SELFDESTRUCT (  ...
┃        ┃         pc: _PC_CELL:Int
┃        ┃         callDepth: _CALLDEPTH_CELL:Int
┃        ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃        ┃
┃        ┗━━┓
┃           │
┃           ├─ 20
┃           │   k: #addr [ SELFDESTRUCT ] ~> #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_C ...
┃           │   pc: _PC_CELL:Int
┃           │   callDepth: _CALLDEPTH_CELL:Int
┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┃ (1 step)
┃           ┣━━┓
┃           ┃  │
┃           ┃  ├─ 31
┃           ┃  │   k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃           ┃  │   pc: _PC_CELL:Int
┃           ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃           ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃  │
┃           ┃  │  (1 step)
┃           ┃  └─ 46 (leaf, pending)
┃           ┃      k: #gas [ SELFDESTRUCT , SELFDESTRUCT ( W3:Int modInt pow160 ) ] ~> SELFDESTRUCT (  ...
┃           ┃      pc: _PC_CELL:Int
┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃           ┃
┃           ┗━━┓
┃              │
┃              ├─ 32
┃              │   k: #addr [ SELFDESTRUCT ] ~> #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_C ...
┃              │   pc: _PC_CELL:Int
┃              │   callDepth: _CALLDEPTH_CELL:Int
┃              │   statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┃ (1 step)
┃              ┣━━┓
┃              ┃  │
┃              ┃  └─ 51 (leaf, pending)
┃              ┃      k: #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_CELL:K
┃              ┃      pc: _PC_CELL:Int
┃              ┃      callDepth: _CALLDEPTH_CELL:Int
┃              ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃              ┃
┃              ┗━━┓
┃                 │
┃                 └─ 52 (leaf, pending)
┃                     k: #addr [ SELFDESTRUCT ] ~> #exec [ SELFDESTRUCT ] ~> #pc [ SELFDESTRUCT ] ~> _K_C ...
┃                     pc: _PC_CELL:Int
┃                     callDepth: _CALLDEPTH_CELL:Int
┃                     statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _STATIC_CELL:Bool
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1 )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
   │
   ├─ 6
   │   k: #next [ SELFDESTRUCT ] ~> _K_CELL:K
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



module SUMMARY-SELFDESTRUCT-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-7]: <kevm>
           <k>
             ( #next [ SELFDESTRUCT ] ~> .K => #addr [ SELFDESTRUCT ]
             ~> #exec [ SELFDESTRUCT ]
             ~> #pc [ SELFDESTRUCT ] )
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-5-TO-7)]
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ SELFDESTRUCT ] => #halt )
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
    
    rule [BASIC-BLOCK-6-TO-9]: <kevm>
           <k>
             ( #next [ SELFDESTRUCT ] => #halt )
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
       andBool ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -1 ) >Int 1024 )
               )))
      [priority(20), label(BASIC-BLOCK-6-TO-9)]
    
    rule [BASIC-BLOCK-4-TO-10]: <kevm>
           <k>
             ( #next [ SELFDESTRUCT ] => #halt )
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
      [priority(20), label(BASIC-BLOCK-4-TO-10)]
    
    rule [BASIC-BLOCK-24-TO-41]: <kevm>
           <k>
             ( Cselfdestruct ( _SCHEDULE_CELL:Schedule , #accountNonexistent ( ( W0:Int modInt pow160 ) ) , BAL:Int ) ~> .K => #accountNonexistent ( ( W0:Int modInt pow160 ) )
             ~> #freezerCselfdestruct1_ ( _SCHEDULE_CELL:Schedule ~> .K , BAL:Int ~> .K ) )
             ~> #deductGas
             ~> #access [ SELFDESTRUCT , SELFDESTRUCT ( W0:Int modInt pow160 ) ]
             ~> SELFDESTRUCT ( W0:Int modInt pow160 )
             ~> #pc [ SELFDESTRUCT ]
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
                   ACCTFROM:Int
                 </id>
                 <wordStack>
                   _WS:WordStack
                 </wordStack>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               <substate>
                 <selfDestruct>
                   _SELFDESTRUCT_CELL:Set
                 </selfDestruct>
                 <refund>
                   #if ACCTFROM:Int in _SELFDESTRUCT_CELL:Set #then _REFUND_CELL:Int #else chop ( ( _REFUND_CELL:Int +Int Rselfdestruct < _SCHEDULE_CELL:Schedule > ) ) #fi
                 </refund>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ACCTFROM:Int
                   </acctID>
                   <balance>
                     BAL:Int
                   </balance>
                   _Gen25:CodeCell
                   _Gen26:StorageCell
                   _Gen27:OrigStorageCell
                   _Gen28:TransientStorageCell
                   _Gen29:NonceCell
                 </account>
                 _DotVar8:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( __USEGAS_CELL
       andBool ( __ID_CELL ==K ACCTFROM:Int
       andBool ( ( notBool __STATIC_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( ( notBool <acctID>
          ACCTFROM:Int
        </acctID> in_keys ( _DotVar8:AccountCellMap ) )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
       andBool ( __ACCOUNTS_CELL ==K ( <account>
          <acctID>
            ACCTFROM:Int
          </acctID>
          <balance>
            BAL:Int
          </balance>
          _Gen25:CodeCell
          _Gen26:StorageCell
          _Gen27:OrigStorageCell
          _Gen28:TransientStorageCell
          _Gen29:NonceCell
        </account>
        _DotVar8:AccountCellMap )
               ))))))))
      [priority(20), label(BASIC-BLOCK-24-TO-41)]
    
    rule [BASIC-BLOCK-27-TO-42]: <kevm>
           <k>
             ( #touchAccounts ACCT:Int ( W0:Int modInt pow160 )
             ~> #accessAccounts ( W0:Int modInt pow160 ) => .K )
             ~> #transferFunds ACCT:Int ( W0:Int modInt pow160 ) BALFROM:Int
             ~> #end EVMC_SUCCESS
             ~> #pc [ SELFDESTRUCT ]
             ~> __K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <output>
                 b""
               </output>
               <touchedAccounts>
                 ( _TOUCHEDACCOUNTS_CELL:Set => _TOUCHEDACCOUNTS_CELL:Set |Set SetItem ( ACCT:Int ) |Set SetItem ( ( W0:Int modInt pow160 ) ) )
               </touchedAccounts>
               <callState>
                 <id>
                   ACCT:Int
                 </id>
                 <wordStack>
                   _WS:WordStack
                 </wordStack>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               <substate>
                 <selfDestruct>
                   __SELFDESTRUCT_CELL |Set SetItem ( ACCT:Int )
                 </selfDestruct>
                 <accessedAccounts>
                   ( _ACCESSEDACCOUNTS_CELL:Set => _ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( W0:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ACCT:Int
                   </acctID>
                   <balance>
                     BALFROM:Int
                   </balance>
                   _Gen26:CodeCell
                   _Gen27:StorageCell
                   _Gen28:OrigStorageCell
                   _Gen29:TransientStorageCell
                   _Gen30:NonceCell
                 </account>
                 _DotVar8:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( __ID_CELL ==K ACCT:Int
       andBool ( ( notBool __STATIC_CELL )
       andBool ( ( notBool __USEGAS_CELL )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( ( notBool <acctID>
          ACCT:Int
        </acctID> in_keys ( _DotVar8:AccountCellMap ) )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ACCT:Int =/=Int ( W0:Int modInt pow160 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
       andBool ( __ACCOUNTS_CELL ==K ( <account>
          <acctID>
            ACCT:Int
          </acctID>
          <balance>
            BALFROM:Int
          </balance>
          _Gen26:CodeCell
          _Gen27:StorageCell
          _Gen28:OrigStorageCell
          _Gen29:TransientStorageCell
          _Gen30:NonceCell
        </account>
        _DotVar8:AccountCellMap )
               )))))))))
      [priority(20), label(BASIC-BLOCK-27-TO-42)]
    
    rule [BASIC-BLOCK-31-TO-46]: <kevm>
           <k>
             ( #exec [ SELFDESTRUCT ] ~> .K => #gas [ SELFDESTRUCT , SELFDESTRUCT ( W3:Int modInt pow160 ) ]
             ~> SELFDESTRUCT ( W3:Int modInt pow160 ) )
             ~> #pc [ SELFDESTRUCT ]
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W3:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
      requires ( ( notBool __STATIC_CELL )
       andBool ( _W0 =/=Int W3:Int
       andBool ( _W1 =/=Int W3:Int
       andBool ( _W2 =/=Int W3:Int
       andBool ( __WORDSTACK_CELL ==K ( W3:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-31-TO-46)]
    
    rule [BASIC-BLOCK-28-TO-50]: <kevm>
           <k>
             ( #touchAccounts ( W0:Int modInt pow160 )
             ~> #accessAccounts ( W0:Int modInt pow160 )
             ~> #end EVMC_SUCCESS
             ~> #pc [ SELFDESTRUCT ] => #halt ~> .K )
             ~> __K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <output>
                 b""
               </output>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_SUCCESS )
               </statusCode>
               <touchedAccounts>
                 ( _TOUCHEDACCOUNTS_CELL:Set => _TOUCHEDACCOUNTS_CELL:Set |Set SetItem ( ( W0:Int modInt pow160 ) ) )
               </touchedAccounts>
               <callState>
                 <id>
                   ( W0:Int modInt pow160 )
                 </id>
                 <wordStack>
                   _WS:WordStack
                 </wordStack>
                 <static>
                   false
                 </static>
                 ...
               </callState>
               <substate>
                 <selfDestruct>
                   __SELFDESTRUCT_CELL |Set SetItem ( ( W0:Int modInt pow160 ) )
                 </selfDestruct>
                 <accessedAccounts>
                   ( _ACCESSEDACCOUNTS_CELL:Set => _ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( W0:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ( W0:Int modInt pow160 )
                   </acctID>
                   <balance>
                     0
                   </balance>
                   _Gen27:CodeCell
                   _Gen28:StorageCell
                   _Gen29:OrigStorageCell
                   _Gen30:TransientStorageCell
                   _Gen31:NonceCell
                 </account>
                 _DotVar8:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool __STATIC_CELL )
       andBool ( ( notBool __USEGAS_CELL )
       andBool ( __ID_CELL ==K ( W0:Int modInt pow160 )
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
       andBool ( ( notBool <acctID>
          ( W0:Int modInt pow160 )
        </acctID> in_keys ( _DotVar8:AccountCellMap ) )
       andBool ( __ACCOUNTS_CELL ==K ( <account>
          <acctID>
            ( W0:Int modInt pow160 )
          </acctID>
          <balance>
            __Gen0
          </balance>
          _Gen27:CodeCell
          _Gen28:StorageCell
          _Gen29:OrigStorageCell
          _Gen30:TransientStorageCell
          _Gen31:NonceCell
        </account>
        _DotVar8:AccountCellMap )
               ))))))))
      [priority(20), label(BASIC-BLOCK-28-TO-50)]
    
    rule [BASIC-BLOCK-60-TO-34]: <kevm>
           <k>
             ( #exec [ SELFDESTRUCT ] ~> .K => #gas [ SELFDESTRUCT , SELFDESTRUCT ( W2:Int modInt pow160 ) ]
             ~> SELFDESTRUCT ( W2:Int modInt pow160 ) )
             ~> #pc [ SELFDESTRUCT ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W2:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( _W0 =/=Int W2:Int
       andBool ( _W1 =/=Int W2:Int
       andBool ( __WORDSTACK_CELL ==K ( W2:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-60-TO-34)]
    
    rule [BASIC-BLOCK-61-TO-35]: <kevm>
           <k>
             ( #exec [ SELFDESTRUCT ] ~> .K => #gas [ SELFDESTRUCT , SELFDESTRUCT ( W2:Int modInt pow160 ) ]
             ~> SELFDESTRUCT ( W2:Int modInt pow160 ) )
             ~> #pc [ SELFDESTRUCT ]
             ~> __K_CELL
           </k>
           <useGas>
             _USEGAS_CELL:Bool
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W2:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( _W0 =/=Int W2:Int
       andBool ( _W1 =/=Int W2:Int
       andBool ( __WORDSTACK_CELL ==K ( W2:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))))
      [priority(20), label(BASIC-BLOCK-61-TO-35)]
    
    rule [BASIC-BLOCK-56-TO-23]: <kevm>
           <k>
             ( #exec [ SELFDESTRUCT ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( W0:Int modInt pow160 ) )
             ~> #deductGas
             ~> #access [ SELFDESTRUCT , SELFDESTRUCT ( W0:Int modInt pow160 ) ]
             ~> SELFDESTRUCT ( W0:Int modInt pow160 ) )
             ~> #pc [ SELFDESTRUCT ]
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
                   ( ( ( W0:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-56-TO-23)]
    
    rule [BASIC-BLOCK-57-TO-26]: <kevm>
           <k>
             ( #exec [ SELFDESTRUCT ] => SELFDESTRUCT ( W0:Int modInt pow160 ) )
             ~> #pc [ SELFDESTRUCT ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W0:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( __WORDSTACK_CELL ==K ( W0:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               )))))
      [priority(20), label(BASIC-BLOCK-57-TO-26)]
    
    rule [BASIC-BLOCK-58-TO-33]: <kevm>
           <k>
             ( #exec [ SELFDESTRUCT ] ~> .K => #gasExec ( _SCHEDULE_CELL:Schedule , SELFDESTRUCT ( W1:Int modInt pow160 ) )
             ~> #deductGas
             ~> #access [ SELFDESTRUCT , SELFDESTRUCT ( W1:Int modInt pow160 ) ]
             ~> SELFDESTRUCT ( W1:Int modInt pow160 ) )
             ~> #pc [ SELFDESTRUCT ]
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
                   ( ( ( W1:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( _W0 =/=Int W1:Int
       andBool ( __WORDSTACK_CELL ==K ( W1:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-58-TO-33)]
    
    rule [BASIC-BLOCK-59-TO-38]: <kevm>
           <k>
             ( #exec [ SELFDESTRUCT ] => SELFDESTRUCT ( W1:Int modInt pow160 ) )
             ~> #pc [ SELFDESTRUCT ]
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( ( W1:Int modInt pow160 ) : _WS:WordStack ) => _WS:WordStack )
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
       andBool ( _W0 =/=Int W1:Int
       andBool ( __WORDSTACK_CELL ==K ( W1:Int : _WS:WordStack )
       andBool ( ( notBool #sizeWordStack ( _WS:WordStack , 1 ) <Int 1 )
       andBool ( ( notBool ( #sizeWordStack ( _WS:WordStack , 1 ) +Int -1 ) >Int 1024 )
               ))))))
      [priority(20), label(BASIC-BLOCK-59-TO-38)]

endmodule
