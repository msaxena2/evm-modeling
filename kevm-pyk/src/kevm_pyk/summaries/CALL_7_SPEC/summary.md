
┌─ 1 (root, split, init)
│   k: #next [ CALL ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _STATIC_CELL:Bool
┃  ┃     #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) )
┃  │
┃  ├─ 4
┃  │   k: #next [ CALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 6 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STATIC_MODE_VIOLATION
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  ┃     ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
┃  │
┃  ├─ 51
┃  │   k: #next [ CALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 9
┃  │   k: CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int ~ ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 10
┃  ┃  │   k: #accessAccounts ( _W1:Int modInt pow160 ) ~> #checkCall ACCTFROM:Int _W2:Int ~>  ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (2 steps)
┃  ┃  ├─ 15
┃  ┃  │   k: #checkBalanceUnderflow ACCTFROM:Int _W2:Int ~> #checkDepthExceeded ~> #call ACCT ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (1 step)
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  └─ 16 (leaf, pending)
┃  ┃  ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 17 (split)
┃  ┃  ┃  │   k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┃ (branch)
┃  ┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃  ┃     _CALLDEPTH_CELL:Int <Int 1024
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ├─ 19
┃  ┃  ┃  ┃  │   k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  ├─ 32 (split)
┃  ┃  ┃  ┃  │   k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _ ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┃ (branch)
┃  ┃  ┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃  ┃  ┃     _Gen0:CodeCell ==K <code>
  CODE:Bytes
</code>
┃  ┃  ┃  ┃  ┃  ┃     ACCTFROM:Int ==Int ( _W1:Int modInt pow160 )
┃  ┃  ┃  ┃  ┃  ┃     _ID_CELL:Account ==K ( _W1:Int modInt pow160 )
┃  ┃  ┃  ┃  ┃  ┃     ( notBool <acctID>
  ( _W1:Int modInt pow160 )
</acctID> in_keys ( _DotVar5:AccountCellMap ) )
┃  ┃  ┃  ┃  ┃  ┃     _ACCOUNTS_CELL:AccountCellMap ==K ( <account>
  <acctID>
    ( _W1:Int modInt pow160 )
  </acctID>
  <balance>
    BAL:Int
  </balance>
  <code>
    CODE:Bytes
  </code>
  _Gen1:StorageCell
  _Gen2:OrigStorageCell
  _Gen3:TransientStorageCell
  _Gen4:NonceCell
</account>
_DotVar5:AccountCellMap )
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 38 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _ ...
┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃  ┃  ┃     ( notBool <acctID>
  ACCTFROM:Int
</acctID> in_keys ( AC3_:AccountCellMap ) )
┃  ┃  ┃  ┃  ┃  ┃     ( notBool ACCTFROM:Int ==Int ( _W1:Int modInt pow160 ) )
┃  ┃  ┃  ┃  ┃  ┃     ( notBool <acctID>
  ( _W1:Int modInt pow160 )
</acctID> in_keys ( AC3_:AccountCellMap ) )
┃  ┃  ┃  ┃  ┃  ┃     _DotVar5:AccountCellMap ==K ( <account>
  <acctID>
    ( _W1:Int modInt pow160 )
  </acctID>
  _Gen0:BalanceCell
  <code>
    CODE:Bytes
  </code>
  _Gen1:StorageCell
  _Gen2:OrigStorageCell
  _Gen3:TransientStorageCell
  _Gen4:NonceCell
</account>
AC3_:AccountCellMap )
┃  ┃  ┃  ┃  ┃  ┃     _ACCOUNTS_CELL:AccountCellMap ==K ( <account>
  <acctID>
    ( _W1:Int modInt pow160 )
  </acctID>
  _Gen0:BalanceCell
  <code>
    CODE:Bytes
  </code>
  _Gen1:StorageCell
  _Gen2:OrigStorageCell
  _Gen3:TransientStorageCell
  _Gen4:NonceCell
</account>
( <account>
  <acctID>
    ACCTFROM:Int
  </acctID>
  <balance>
    BAL:Int
  </balance>
  _Gen0:CodeCell
  _Gen1:StorageCell
  _Gen2:OrigStorageCell
  _Gen3:TransientStorageCell
  _Gen4:NonceCell
</account>
AC3_:AccountCellMap ) )
┃  ┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  ┃  └─ 39 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _ ...
┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┗━━┓ subst: .Subst
┃  ┃  ┃  ┃     ┃ constraint: true
┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃     └─ 40 (leaf, pending)
┃  ┃  ┃  ┃         k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _ ...
┃  ┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓ subst: .Subst
┃  ┃  ┃     ┃ constraint:
┃  ┃  ┃     ┃     1024 <=Int _CALLDEPTH_CELL:Int
┃  ┃  ┃     │
┃  ┃  ┃     └─ 20 (leaf, pending)
┃  ┃  ┃         k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓
┃  ┃     │
┃  ┃     ├─ 18
┃  ┃     │   k: #checkBalanceUnderflow ACCTFROM:Int _W2:Int ~> #checkDepthExceeded ~> #call ACCT ...
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┃ (1 step)
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  └─ 21 (leaf, pending)
┃  ┃     ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  ├─ 22 (split)
┃  ┃     ┃  │   k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃     ┃  │   pc: _PC_CELL:Int
┃  ┃     ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃
┃  ┃     ┃  ┃ (branch)
┃  ┃     ┃  ┣━━┓ subst: .Subst
┃  ┃     ┃  ┃  ┃ constraint:
┃  ┃     ┃  ┃  ┃     _CALLDEPTH_CELL:Int <Int 1024
┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃  ├─ 27
┃  ┃     ┃  ┃  │   k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃     ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃  │  (1 step)
┃  ┃     ┃  ┃  ├─ 35 (split)
┃  ┃     ┃  ┃  │   k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _ ...
┃  ┃     ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┃ (branch)
┃  ┃     ┃  ┃  ┣━━┓ subst: .Subst
┃  ┃     ┃  ┃  ┃  ┃ constraint:
┃  ┃     ┃  ┃  ┃  ┃     _Gen28:CodeCell ==K <code>
  CODE:Bytes
</code>
┃  ┃     ┃  ┃  ┃  ┃     ACCTFROM:Int ==Int ( _W1:Int modInt pow160 )
┃  ┃     ┃  ┃  ┃  ┃     _ID_CELL:Account ==K ( _W1:Int modInt pow160 )
┃  ┃     ┃  ┃  ┃  ┃     ( notBool <acctID>
  ( _W1:Int modInt pow160 )
</acctID> in_keys ( _DotVar5:AccountCellMap ) )
┃  ┃     ┃  ┃  ┃  ┃     _ACCOUNTS_CELL:AccountCellMap ==K ( <account>
  <acctID>
    ( _W1:Int modInt pow160 )
  </acctID>
  <balance>
    BAL0:Int
  </balance>
  <code>
    CODE:Bytes
  </code>
  _Gen29:StorageCell
  _Gen30:OrigStorageCell
  _Gen31:TransientStorageCell
  _Gen32:NonceCell
</account>
_DotVar5:AccountCellMap )
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  └─ 46 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _ ...
┃  ┃     ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃     ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┣━━┓ subst: .Subst
┃  ┃     ┃  ┃  ┃  ┃ constraint:
┃  ┃     ┃  ┃  ┃  ┃     ( notBool <acctID>
  ACCTFROM:Int
</acctID> in_keys ( AC3_:AccountCellMap ) )
┃  ┃     ┃  ┃  ┃  ┃     ( notBool ACCTFROM:Int ==Int ( _W1:Int modInt pow160 ) )
┃  ┃     ┃  ┃  ┃  ┃     ( notBool <acctID>
  ( _W1:Int modInt pow160 )
</acctID> in_keys ( AC3_:AccountCellMap ) )
┃  ┃     ┃  ┃  ┃  ┃     _DotVar5:AccountCellMap ==K ( <account>
  <acctID>
    ( _W1:Int modInt pow160 )
  </acctID>
  _Gen0:BalanceCell
  <code>
    CODE:Bytes
  </code>
  _Gen1:StorageCell
  _Gen2:OrigStorageCell
  _Gen3:TransientStorageCell
  _Gen4:NonceCell
</account>
AC3_:AccountCellMap )
┃  ┃     ┃  ┃  ┃  ┃     _ACCOUNTS_CELL:AccountCellMap ==K ( <account>
  <acctID>
    ( _W1:Int modInt pow160 )
  </acctID>
  _Gen0:BalanceCell
  <code>
    CODE:Bytes
  </code>
  _Gen1:StorageCell
  _Gen2:OrigStorageCell
  _Gen3:TransientStorageCell
  _Gen4:NonceCell
</account>
( <account>
  <acctID>
    ACCTFROM:Int
  </acctID>
  <balance>
    BAL0:Int
  </balance>
  _Gen28:CodeCell
  _Gen29:StorageCell
  _Gen30:OrigStorageCell
  _Gen31:TransientStorageCell
  _Gen32:NonceCell
</account>
AC3_:AccountCellMap ) )
┃  ┃     ┃  ┃  ┃  │
┃  ┃     ┃  ┃  ┃  └─ 47 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _ ...
┃  ┃     ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃     ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃  ┃     ┃ constraint: true
┃  ┃     ┃  ┃     │
┃  ┃     ┃  ┃     └─ 48 (leaf, pending)
┃  ┃     ┃  ┃         k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _ ...
┃  ┃     ┃  ┃         pc: _PC_CELL:Int
┃  ┃     ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃
┃  ┃     ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃     ┃ constraint:
┃  ┃     ┃     ┃     1024 <=Int _CALLDEPTH_CELL:Int
┃  ┃     ┃     │
┃  ┃     ┃     └─ 28 (leaf, pending)
┃  ┃     ┃         k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃     ┃         pc: _PC_CELL:Int
┃  ┃     ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┗━━┓
┃  ┃        │
┃  ┃        ├─ 23
┃  ┃        │   k: #checkBalanceUnderflow ACCTFROM:Int _W2:Int ~> #checkDepthExceeded ~> #call ACCT ...
┃  ┃        │   pc: _PC_CELL:Int
┃  ┃        │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┃ (1 step)
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  └─ 29 (leaf, pending)
┃  ┃        ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃        ┃      pc: _PC_CELL:Int
┃  ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  ├─ 30 (split)
┃  ┃        ┃  │   k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃        ┃  │   pc: _PC_CELL:Int
┃  ┃        ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃
┃  ┃        ┃  ┃ (branch)
┃  ┃        ┃  ┣━━┓ subst: .Subst
┃  ┃        ┃  ┃  ┃ constraint:
┃  ┃        ┃  ┃  ┃     _CALLDEPTH_CELL:Int <Int 1024
┃  ┃        ┃  ┃  │
┃  ┃        ┃  ┃  ├─ 36
┃  ┃        ┃  ┃  │   k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃        ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃        ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  │
┃  ┃        ┃  ┃  │  (1 step)
┃  ┃        ┃  ┃  └─ 49 (leaf, pending)
┃  ┃        ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _ ...
┃  ┃        ┃  ┃      pc: _PC_CELL:Int
┃  ┃        ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃
┃  ┃        ┃  ┗━━┓ subst: .Subst
┃  ┃        ┃     ┃ constraint:
┃  ┃        ┃     ┃     1024 <=Int _CALLDEPTH_CELL:Int
┃  ┃        ┃     │
┃  ┃        ┃     └─ 37 (leaf, pending)
┃  ┃        ┃         k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃        ┃         pc: _PC_CELL:Int
┃  ┃        ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┗━━┓
┃  ┃           │
┃  ┃           ├─ 31
┃  ┃           │   k: #checkBalanceUnderflow ACCTFROM:Int _W2:Int ~> #checkDepthExceeded ~> #call ACCT ...
┃  ┃           │   pc: _PC_CELL:Int
┃  ┃           │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┃ (1 step)
┃  ┃           ┣━━┓
┃  ┃           ┃  │
┃  ┃           ┃  └─ 43 (leaf, pending)
┃  ┃           ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃           ┃      pc: _PC_CELL:Int
┃  ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┣━━┓
┃  ┃           ┃  │
┃  ┃           ┃  └─ 44 (leaf, pending)
┃  ┃           ┃      k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃           ┃      pc: _PC_CELL:Int
┃  ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┗━━┓
┃  ┃              │
┃  ┃              └─ 45 (leaf, pending)
┃  ┃                  k: #checkBalanceUnderflow ACCTFROM:Int _W2:Int ~> #checkDepthExceeded ~> #call ACCT ...
┃  ┃                  pc: _PC_CELL:Int
┃  ┃                  callDepth: _CALLDEPTH_CELL:Int
┃  ┃                  statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 11 (stuck, leaf)
┃         k: CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int ~ ...
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  ┃     ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
┃  │
┃  ├─ 59
┃  │   k: #next [ CALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 33 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
┃  ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) )
┃  │
┃  ├─ 65
┃  │   k: #next [ CALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (19 steps)
┃  └─ 26 (leaf, pending)
┃      k: Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
┃  ┃     Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 68
┃  │   k: #next [ CALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (20 steps)
┃  └─ 41 (leaf, pending)
┃      k: #access [ CALL , CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int  ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
   ┃     ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
   ┃     Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
   │
   ├─ 69
   │   k: #next [ CALL ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (20 steps)
   └─ 42 (leaf, pending)
       k: #access [ CALL , CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int  ...
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-CALL-7-SPEC
    
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             ( #next [ CALL ] => #halt )
             ~> __K_CELL
           </k>
           <ethereum>
             <evm>
               <statusCode>
                 ( __STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
                 <wordStack>
                   ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) )
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
       andBool ( #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) )
               ))
      [priority(20), label(BASIC-BLOCK-4-TO-6)]
    
    rule [BASIC-BLOCK-10-TO-15]: <kevm>
           <k>
             ( #accessAccounts ( _W1:Int modInt pow160 )
             ~> #checkCall ACCTFROM:Int _W2:Int => #checkBalanceUnderflow ACCTFROM:Int _W2:Int
             ~> #checkDepthExceeded )
             ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _W2:Int #range ( _LOCALMEM_CELL:Bytes , _W3:Int , _W4:Int ) false
             ~> #return _W5:Int _W6:Int
             ~> #pc [ CALL ]
             ~> __K_CELL
           </k>
           <useGas>
             false
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
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   _STATIC_CELL:Bool
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( _ACCESSEDACCOUNTS_CELL:Set => _ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( ( _W1:Int modInt pow160 ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( __ID_CELL ==K ACCTFROM:Int
       andBool ( ( notBool __USEGAS_CELL )
       andBool ( ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( __W0 : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
               )))
      [priority(20), label(BASIC-BLOCK-10-TO-15)]
    
    rule [BASIC-BLOCK-19-TO-32]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _W2:Int #range ( _LOCALMEM_CELL:Bytes , _W3:Int , _W4:Int ) false
             ~> #return _W5:Int _W6:Int
             ~> #pc [ CALL ]
             ~> __K_CELL
           </k>
           <useGas>
             false
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
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   _STATIC_CELL:Bool
                 </static>
                 <callDepth>
                   _CALLDEPTH_CELL:Int
                 </callDepth>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   __ACCESSEDACCOUNTS_CELL |Set SetItem ( ( _W1:Int modInt pow160 ) )
                 </accessedAccounts>
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
                   _Gen0:CodeCell
                   _Gen1:StorageCell
                   _Gen2:OrigStorageCell
                   _Gen3:TransientStorageCell
                   _Gen4:NonceCell
                 </account>
                 _DotVar5:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( __ID_CELL ==K ACCTFROM:Int
       andBool ( ( notBool __USEGAS_CELL )
       andBool ( _W2:Int <=Int BAL:Int
       andBool ( _CALLDEPTH_CELL:Int <Int 1024
       andBool ( ( notBool <acctID>
          ACCTFROM:Int
        </acctID> in_keys ( _DotVar5:AccountCellMap ) )
       andBool ( __ACCOUNTS_CELL ==K ( <account>
          <acctID>
            ACCTFROM:Int
          </acctID>
          <balance>
            BAL:Int
          </balance>
          _Gen0:CodeCell
          _Gen1:StorageCell
          _Gen2:OrigStorageCell
          _Gen3:TransientStorageCell
          _Gen4:NonceCell
        </account>
        _DotVar5:AccountCellMap )
       andBool ( ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( __W0 : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
               )))))))
      [priority(20), label(BASIC-BLOCK-19-TO-32)]
    
    rule [BASIC-BLOCK-27-TO-35]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _W2:Int #range ( _LOCALMEM_CELL:Bytes , _W3:Int , _W4:Int ) false
             ~> #return _W5:Int _W6:Int
             ~> #pc [ CALL ]
             ~> __K_CELL
           </k>
           <useGas>
             false
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
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   _STATIC_CELL:Bool
                 </static>
                 <callDepth>
                   _CALLDEPTH_CELL:Int
                 </callDepth>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   __ACCESSEDACCOUNTS_CELL |Set SetItem ( ( _W1:Int modInt pow160 ) )
                 </accessedAccounts>
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
                     BAL0:Int
                   </balance>
                   _Gen28:CodeCell
                   _Gen29:StorageCell
                   _Gen30:OrigStorageCell
                   _Gen31:TransientStorageCell
                   _Gen32:NonceCell
                 </account>
                 _DotVar5:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( __ID_CELL ==K ACCTFROM:Int
       andBool ( ( notBool __USEGAS_CELL )
       andBool ( _W2:Int <=Int BAL0:Int
       andBool ( _CALLDEPTH_CELL:Int <Int 1024
       andBool ( ( notBool <acctID>
          ACCTFROM:Int
        </acctID> in_keys ( _DotVar5:AccountCellMap ) )
       andBool ( __ACCOUNTS_CELL ==K ( <account>
          <acctID>
            ACCTFROM:Int
          </acctID>
          <balance>
            BAL0:Int
          </balance>
          _Gen28:CodeCell
          _Gen29:StorageCell
          _Gen30:OrigStorageCell
          _Gen31:TransientStorageCell
          _Gen32:NonceCell
        </account>
        _DotVar5:AccountCellMap )
       andBool ( ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( __W0 : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
       andBool ( ( notBool ( _W2:Int <=Int BAL:Int andBool ( __Gen0 ==K _Gen28:CodeCell andBool ( __Gen1 ==K _Gen29:StorageCell andBool ( __Gen2 ==K _Gen30:OrigStorageCell andBool ( __Gen3 ==K _Gen31:TransientStorageCell andBool ( __Gen4 ==K _Gen32:NonceCell andBool BAL:Int ==Int BAL0:Int ) ) ) ) ) ) )
       andBool ( ( notBool ( BAL:Int <Int _W2:Int andBool ( __Gen23 ==K _Gen28:CodeCell andBool ( __Gen24 ==K _Gen29:StorageCell andBool ( __Gen25 ==K _Gen30:OrigStorageCell andBool ( __Gen26 ==K _Gen31:TransientStorageCell andBool ( __Gen27 ==K _Gen32:NonceCell andBool BAL:Int ==Int BAL0:Int ) ) ) ) ) ) )
               )))))))))
      [priority(20), label(BASIC-BLOCK-27-TO-35)]
    
    rule [BASIC-BLOCK-36-TO-49]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) _W2:Int _W2:Int #range ( _LOCALMEM_CELL:Bytes , _W3:Int , _W4:Int ) false
             ~> #return _W5:Int _W6:Int
             ~> #pc [ CALL ]
             ~> __K_CELL
           </k>
           <useGas>
             false
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
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   _STATIC_CELL:Bool
                 </static>
                 <callDepth>
                   _CALLDEPTH_CELL:Int
                 </callDepth>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   __ACCESSEDACCOUNTS_CELL |Set SetItem ( ( _W1:Int modInt pow160 ) )
                 </accessedAccounts>
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
                     BAL1:Int
                   </balance>
                   _Gen33:CodeCell
                   _Gen34:StorageCell
                   _Gen35:OrigStorageCell
                   _Gen36:TransientStorageCell
                   _Gen37:NonceCell
                 </account>
                 _DotVar5:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( __ID_CELL ==K ACCTFROM:Int
       andBool ( ( notBool __USEGAS_CELL )
       andBool ( _W2:Int <=Int BAL1:Int
       andBool ( _CALLDEPTH_CELL:Int <Int 1024
       andBool ( ( notBool <acctID>
          ACCTFROM:Int
        </acctID> in_keys ( _DotVar5:AccountCellMap ) )
       andBool ( __ACCOUNTS_CELL ==K ( <account>
          <acctID>
            ACCTFROM:Int
          </acctID>
          <balance>
            BAL1:Int
          </balance>
          _Gen33:CodeCell
          _Gen34:StorageCell
          _Gen35:OrigStorageCell
          _Gen36:TransientStorageCell
          _Gen37:NonceCell
        </account>
        _DotVar5:AccountCellMap )
       andBool ( ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( __W0 : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
       andBool ( ( notBool ( _W2:Int <=Int BAL:Int andBool ( __Gen0 ==K _Gen33:CodeCell andBool ( __Gen1 ==K _Gen34:StorageCell andBool ( __Gen2 ==K _Gen35:OrigStorageCell andBool ( __Gen3 ==K _Gen36:TransientStorageCell andBool ( __Gen4 ==K _Gen37:NonceCell andBool BAL:Int ==Int BAL1:Int ) ) ) ) ) ) )
       andBool ( ( notBool ( BAL:Int <Int _W2:Int andBool ( __Gen23 ==K _Gen33:CodeCell andBool ( __Gen24 ==K _Gen34:StorageCell andBool ( __Gen25 ==K _Gen35:OrigStorageCell andBool ( __Gen26 ==K _Gen36:TransientStorageCell andBool ( __Gen27 ==K _Gen37:NonceCell andBool BAL:Int ==Int BAL1:Int ) ) ) ) ) ) )
       andBool ( ( notBool ( BAL0:Int <Int _W2:Int andBool ( _Gen28:CodeCell ==K _Gen33:CodeCell andBool ( _Gen29:StorageCell ==K _Gen34:StorageCell andBool ( _Gen30:OrigStorageCell ==K _Gen35:OrigStorageCell andBool ( _Gen31:TransientStorageCell ==K _Gen36:TransientStorageCell andBool ( _Gen32:NonceCell ==K _Gen37:NonceCell andBool BAL0:Int ==Int BAL1:Int ) ) ) ) ) ) )
       andBool ( ( notBool ( _W2:Int <=Int BAL0:Int andBool ( _Gen28:CodeCell ==K _Gen33:CodeCell andBool ( _Gen29:StorageCell ==K _Gen34:StorageCell andBool ( _Gen30:OrigStorageCell ==K _Gen35:OrigStorageCell andBool ( _Gen31:TransientStorageCell ==K _Gen36:TransientStorageCell andBool ( _Gen32:NonceCell ==K _Gen37:NonceCell andBool BAL0:Int ==Int BAL1:Int ) ) ) ) ) ) )
               )))))))))))
      [priority(20), label(BASIC-BLOCK-36-TO-49)]
    
    rule [BASIC-BLOCK-51-TO-9]: <kevm>
           <k>
             ( #next [ CALL ] ~> .K => CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int
             ~> #pc [ CALL ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <static>
                   _STATIC_CELL:Bool
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
       andBool ( ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
               ))
      [priority(20), label(BASIC-BLOCK-51-TO-9)]
    
    rule [BASIC-BLOCK-59-TO-33]: <kevm>
           <k>
             ( #next [ CALL ] => #halt )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) )
                 </memoryUsed>
                 <static>
                   _STATIC_CELL:Bool
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
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
       andBool ( ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
               )))
      [priority(20), label(BASIC-BLOCK-59-TO-33)]
    
    rule [BASIC-BLOCK-65-TO-26]: <kevm>
           <k>
             ( #next [ CALL ] ~> .K => Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) )
             ~> #deductGas
             ~> #access [ CALL , CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int ]
             ~> CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int
             ~> #pc [ CALL ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) )
                 </memoryUsed>
                 <callGas>
                   ( __CALLGAS_CELL => Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) +Gas #if _W2:Int ==Int 0 #then 0 #else Gcallstipend < _SCHEDULE_CELL:Schedule > #fi )
                 </callGas>
                 <static>
                   _STATIC_CELL:Bool
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) )
               ))))
      [priority(20), label(BASIC-BLOCK-65-TO-26)]
    
    rule [BASIC-BLOCK-68-TO-41]: <kevm>
           <k>
             ( #next [ CALL ] ~> .K => #access [ CALL , CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int ]
             ~> CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int
             ~> #pc [ CALL ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) )
                 </memoryUsed>
                 <callGas>
                   ( __CALLGAS_CELL => Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) +Gas #if _W2:Int ==Int 0 #then 0 #else Gcallstipend < _SCHEDULE_CELL:Schedule > #fi )
                 </callGas>
                 <static>
                   _STATIC_CELL:Bool
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
       andBool ( Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))))
      [priority(20), label(BASIC-BLOCK-68-TO-41)]
    
    rule [BASIC-BLOCK-69-TO-42]: <kevm>
           <k>
             ( #next [ CALL ] ~> .K => #access [ CALL , CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int ]
             ~> CALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int _W6:Int
             ~> #pc [ CALL ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) )
                 </memoryUsed>
                 <callGas>
                   ( __CALLGAS_CELL => Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) +Gas #if _W2:Int ==Int 0 #then 0 #else Gcallstipend < _SCHEDULE_CELL:Schedule > #fi )
                 </callGas>
                 <static>
                   _STATIC_CELL:Bool
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL:Set
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( _USEGAS_CELL:Bool
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( ( notBool ( _STATIC_CELL:Bool andBool #changesState ( CALL , ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : ( _W6:Int : _WS:WordStack ) ) ) ) ) ) ) ) ) )
       andBool ( Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , _W2:Int , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W3:Int , _W4:Int ) , _W5:Int , _W6:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))
      [priority(20), label(BASIC-BLOCK-69-TO-42)]

endmodule
