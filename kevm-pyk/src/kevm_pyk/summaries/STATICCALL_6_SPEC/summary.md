
┌─ 1 (root, split, init)
│   k: #next [ STATICCALL ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool _USEGAS_CELL:Bool )
┃  │
┃  ├─ 49
┃  │   k: #next [ STATICCALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  ├─ 6
┃  │   k: STATICCALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ~>  ...
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 7
┃  ┃  │   k: #accessAccounts ( _W1:Int modInt pow160 ) ~> #checkCall ACCTFROM:Int 0 ~> #call  ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  │
┃  ┃  │  (2 steps)
┃  ┃  ├─ 12
┃  ┃  │   k: #checkBalanceUnderflow ACCTFROM:Int 0 ~> #checkDepthExceeded ~> #call ACCTFROM:I ...
┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (1 step)
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  └─ 13 (leaf, pending)
┃  ┃  ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┣━━┓
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 14 (split)
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
┃  ┃  ┃  ┃  ├─ 16
┃  ┃  ┃  ┃  │   k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃  ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃  ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  │
┃  ┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  ┃  ├─ 29 (split)
┃  ┃  ┃  ┃  │   k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #rang ...
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
┃  ┃  ┃  ┃  ┃  └─ 35 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #rang ...
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
┃  ┃  ┃  ┃  ┃  └─ 36 (leaf, pending)
┃  ┃  ┃  ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #rang ...
┃  ┃  ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃  ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃  ┃
┃  ┃  ┃  ┃  ┗━━┓ subst: .Subst
┃  ┃  ┃  ┃     ┃ constraint: true
┃  ┃  ┃  ┃     │
┃  ┃  ┃  ┃     └─ 37 (leaf, pending)
┃  ┃  ┃  ┃         k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #rang ...
┃  ┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃  ┃
┃  ┃  ┃  ┗━━┓ subst: .Subst
┃  ┃  ┃     ┃ constraint:
┃  ┃  ┃     ┃     1024 <=Int _CALLDEPTH_CELL:Int
┃  ┃  ┃     │
┃  ┃  ┃     └─ 17 (leaf, pending)
┃  ┃  ┃         k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃  ┃         pc: _PC_CELL:Int
┃  ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓
┃  ┃     │
┃  ┃     ├─ 15
┃  ┃     │   k: #checkBalanceUnderflow ACCTFROM:Int 0 ~> #checkDepthExceeded ~> #call ACCTFROM:I ...
┃  ┃     │   pc: _PC_CELL:Int
┃  ┃     │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┃ (1 step)
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  └─ 19 (leaf, pending)
┃  ┃     ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃     ┃      pc: _PC_CELL:Int
┃  ┃     ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┣━━┓
┃  ┃     ┃  │
┃  ┃     ┃  ├─ 20 (split)
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
┃  ┃     ┃  ┃  ├─ 24
┃  ┃     ┃  ┃  │   k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃     ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃     ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  │
┃  ┃     ┃  ┃  │  (1 step)
┃  ┃     ┃  ┃  ├─ 34 (split)
┃  ┃     ┃  ┃  │   k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #rang ...
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
┃  ┃     ┃  ┃  ┃  └─ 44 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #rang ...
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
┃  ┃     ┃  ┃  ┃  └─ 45 (leaf, pending)
┃  ┃     ┃  ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #rang ...
┃  ┃     ┃  ┃  ┃      pc: _PC_CELL:Int
┃  ┃     ┃  ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃  ┃
┃  ┃     ┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃  ┃     ┃ constraint: true
┃  ┃     ┃  ┃     │
┃  ┃     ┃  ┃     └─ 46 (leaf, pending)
┃  ┃     ┃  ┃         k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #rang ...
┃  ┃     ┃  ┃         pc: _PC_CELL:Int
┃  ┃     ┃  ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃  ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃  ┃
┃  ┃     ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃     ┃ constraint:
┃  ┃     ┃     ┃     1024 <=Int _CALLDEPTH_CELL:Int
┃  ┃     ┃     │
┃  ┃     ┃     └─ 25 (leaf, pending)
┃  ┃     ┃         k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃     ┃         pc: _PC_CELL:Int
┃  ┃     ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃     ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃     ┃
┃  ┃     ┗━━┓
┃  ┃        │
┃  ┃        ├─ 21
┃  ┃        │   k: #checkBalanceUnderflow ACCTFROM:Int 0 ~> #checkDepthExceeded ~> #call ACCTFROM:I ...
┃  ┃        │   pc: _PC_CELL:Int
┃  ┃        │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃        │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┃ (1 step)
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  └─ 26 (leaf, pending)
┃  ┃        ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃        ┃      pc: _PC_CELL:Int
┃  ┃        ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┣━━┓
┃  ┃        ┃  │
┃  ┃        ┃  ├─ 27 (split)
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
┃  ┃        ┃  ┃  ├─ 32
┃  ┃        ┃  ┃  │   k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃        ┃  ┃  │   pc: _PC_CELL:Int
┃  ┃        ┃  ┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃  │
┃  ┃        ┃  ┃  │  (1 step)
┃  ┃        ┃  ┃  └─ 43 (leaf, pending)
┃  ┃        ┃  ┃      k: #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #rang ...
┃  ┃        ┃  ┃      pc: _PC_CELL:Int
┃  ┃        ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃  ┃
┃  ┃        ┃  ┗━━┓ subst: .Subst
┃  ┃        ┃     ┃ constraint:
┃  ┃        ┃     ┃     1024 <=Int _CALLDEPTH_CELL:Int
┃  ┃        ┃     │
┃  ┃        ┃     └─ 33 (leaf, pending)
┃  ┃        ┃         k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃        ┃         pc: _PC_CELL:Int
┃  ┃        ┃         callDepth: _CALLDEPTH_CELL:Int
┃  ┃        ┃         statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃        ┃
┃  ┃        ┗━━┓
┃  ┃           │
┃  ┃           ├─ 28
┃  ┃           │   k: #checkBalanceUnderflow ACCTFROM:Int 0 ~> #checkDepthExceeded ~> #call ACCTFROM:I ...
┃  ┃           │   pc: _PC_CELL:Int
┃  ┃           │   callDepth: _CALLDEPTH_CELL:Int
┃  ┃           │   statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┃ (1 step)
┃  ┃           ┣━━┓
┃  ┃           ┃  │
┃  ┃           ┃  └─ 40 (leaf, pending)
┃  ┃           ┃      k: #refund _CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALA ...
┃  ┃           ┃      pc: _PC_CELL:Int
┃  ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┣━━┓
┃  ┃           ┃  │
┃  ┃           ┃  └─ 41 (leaf, pending)
┃  ┃           ┃      k: #checkDepthExceeded ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int mo ...
┃  ┃           ┃      pc: _PC_CELL:Int
┃  ┃           ┃      callDepth: _CALLDEPTH_CELL:Int
┃  ┃           ┃      statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃           ┃
┃  ┃           ┗━━┓
┃  ┃              │
┃  ┃              └─ 42 (leaf, pending)
┃  ┃                  k: #checkBalanceUnderflow ACCTFROM:Int 0 ~> #checkDepthExceeded ~> #call ACCTFROM:I ...
┃  ┃                  pc: _PC_CELL:Int
┃  ┃                  callDepth: _CALLDEPTH_CELL:Int
┃  ┃                  statusCode: _STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 8 (stuck, leaf)
┃         k: STATICCALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ~>  ...
┃         pc: _PC_CELL:Int
┃         callDepth: _CALLDEPTH_CELL:Int
┃         statusCode: _STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 57
┃  │   k: #next [ STATICCALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (13 steps)
┃  └─ 30 (leaf, terminal)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) )
┃  │
┃  ├─ 63
┃  │   k: #next [ STATICCALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (24 steps)
┃  └─ 47 (leaf, pending)
┃      k: #halt ~> _K_CELL:K
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: EVMC_OUT_OF_GAS
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     _USEGAS_CELL:Bool
┃  ┃     Ghasaccesslist << _SCHEDULE_CELL:Schedule >>
┃  ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
┃  ┃     Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
┃  │
┃  ├─ 66
┃  │   k: #next [ STATICCALL ] ~> _K_CELL:K
┃  │   pc: _PC_CELL:Int
┃  │   callDepth: _CALLDEPTH_CELL:Int
┃  │   statusCode: _STATUSCODE_CELL:StatusCode
┃  │
┃  │  (20 steps)
┃  └─ 38 (leaf, pending)
┃      k: #access [ STATICCALL , STATICCALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3: ...
┃      pc: _PC_CELL:Int
┃      callDepth: _CALLDEPTH_CELL:Int
┃      statusCode: _STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     _USEGAS_CELL:Bool
   ┃     ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
   ┃     Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
   │
   ├─ 67
   │   k: #next [ STATICCALL ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (20 steps)
   └─ 39 (leaf, pending)
       k: #access [ STATICCALL , STATICCALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3: ...
       pc: _PC_CELL:Int
       callDepth: _CALLDEPTH_CELL:Int
       statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-STATICCALL-6-SPEC
    
    
    rule [BASIC-BLOCK-7-TO-12]: <kevm>
           <k>
             ( #accessAccounts ( _W1:Int modInt pow160 )
             ~> #checkCall ACCTFROM:Int 0 => #checkBalanceUnderflow ACCTFROM:Int 0
             ~> #checkDepthExceeded )
             ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #range ( _LOCALMEM_CELL:Bytes , __W2 , __W3 ) true
             ~> #return __W4 __W5
             ~> #pc [ STATICCALL ]
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
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
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
               ))
      [priority(20), label(BASIC-BLOCK-7-TO-12)]
    
    rule [BASIC-BLOCK-16-TO-29]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #range ( _LOCALMEM_CELL:Bytes , __W2 , __W3 ) true
             ~> #return __W4 __W5
             ~> #pc [ STATICCALL ]
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
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
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
       andBool ( 0 <=Int BAL:Int
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
               ))))))
      [priority(20), label(BASIC-BLOCK-16-TO-29)]
    
    rule [BASIC-BLOCK-24-TO-34]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #range ( _LOCALMEM_CELL:Bytes , __W2 , __W3 ) true
             ~> #return __W4 __W5
             ~> #pc [ STATICCALL ]
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
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
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
       andBool ( 0 <=Int BAL0:Int
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
       andBool ( ( notBool ( 0 <=Int BAL:Int andBool ( __Gen0 ==K _Gen28:CodeCell andBool ( __Gen1 ==K _Gen29:StorageCell andBool ( __Gen2 ==K _Gen30:OrigStorageCell andBool ( __Gen3 ==K _Gen31:TransientStorageCell andBool ( __Gen4 ==K _Gen32:NonceCell andBool BAL:Int ==Int BAL0:Int ) ) ) ) ) ) )
       andBool ( ( notBool ( BAL:Int <Int 0 andBool ( __Gen23 ==K _Gen28:CodeCell andBool ( __Gen24 ==K _Gen29:StorageCell andBool ( __Gen25 ==K _Gen30:OrigStorageCell andBool ( __Gen26 ==K _Gen31:TransientStorageCell andBool ( __Gen27 ==K _Gen32:NonceCell andBool BAL:Int ==Int BAL0:Int ) ) ) ) ) ) )
               ))))))))
      [priority(20), label(BASIC-BLOCK-24-TO-34)]
    
    rule [BASIC-BLOCK-32-TO-43]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #call ACCTFROM:Int ( _W1:Int modInt pow160 ) ( _W1:Int modInt pow160 ) 0 0 #range ( _LOCALMEM_CELL:Bytes , __W2 , __W3 ) true
             ~> #return __W4 __W5
             ~> #pc [ STATICCALL ]
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
                 <localMem>
                   _LOCALMEM_CELL:Bytes
                 </localMem>
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
       andBool ( 0 <=Int BAL1:Int
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
       andBool ( ( notBool ( 0 <=Int BAL:Int andBool ( __Gen0 ==K _Gen33:CodeCell andBool ( __Gen1 ==K _Gen34:StorageCell andBool ( __Gen2 ==K _Gen35:OrigStorageCell andBool ( __Gen3 ==K _Gen36:TransientStorageCell andBool ( __Gen4 ==K _Gen37:NonceCell andBool BAL:Int ==Int BAL1:Int ) ) ) ) ) ) )
       andBool ( ( notBool ( BAL:Int <Int 0 andBool ( __Gen23 ==K _Gen33:CodeCell andBool ( __Gen24 ==K _Gen34:StorageCell andBool ( __Gen25 ==K _Gen35:OrigStorageCell andBool ( __Gen26 ==K _Gen36:TransientStorageCell andBool ( __Gen27 ==K _Gen37:NonceCell andBool BAL:Int ==Int BAL1:Int ) ) ) ) ) ) )
       andBool ( ( notBool ( BAL0:Int <Int 0 andBool ( _Gen28:CodeCell ==K _Gen33:CodeCell andBool ( _Gen29:StorageCell ==K _Gen34:StorageCell andBool ( _Gen30:OrigStorageCell ==K _Gen35:OrigStorageCell andBool ( _Gen31:TransientStorageCell ==K _Gen36:TransientStorageCell andBool ( _Gen32:NonceCell ==K _Gen37:NonceCell andBool BAL0:Int ==Int BAL1:Int ) ) ) ) ) ) )
       andBool ( ( notBool ( 0 <=Int BAL0:Int andBool ( _Gen28:CodeCell ==K _Gen33:CodeCell andBool ( _Gen29:StorageCell ==K _Gen34:StorageCell andBool ( _Gen30:OrigStorageCell ==K _Gen35:OrigStorageCell andBool ( _Gen31:TransientStorageCell ==K _Gen36:TransientStorageCell andBool ( _Gen32:NonceCell ==K _Gen37:NonceCell andBool BAL0:Int ==Int BAL1:Int ) ) ) ) ) ) )
               ))))))))))
      [priority(20), label(BASIC-BLOCK-32-TO-43)]
    
    rule [BASIC-BLOCK-49-TO-6]: <kevm>
           <k>
             ( #next [ STATICCALL ] ~> .K => STATICCALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int
             ~> #pc [ STATICCALL ] )
             ~> __K_CELL
           </k>
           <useGas>
             ( _USEGAS_CELL:Bool => false )
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : _WS:WordStack ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      requires ( notBool _USEGAS_CELL:Bool )
      [priority(20), label(BASIC-BLOCK-49-TO-6)]
    
    rule [BASIC-BLOCK-57-TO-30]: <kevm>
           <k>
             ( #next [ STATICCALL ] => #halt )
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
                   ( ( __W0 : ( __W1 : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : _WS:WordStack ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   _GAS_CELL:Gas
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) )
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
       andBool ( _GAS_CELL:Gas <Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))
      [priority(20), label(BASIC-BLOCK-57-TO-30)]
    
    rule [BASIC-BLOCK-63-TO-47]: <kevm>
           <k>
             ( #next [ STATICCALL ] => #halt )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : _WS:WordStack ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) )
                 </memoryUsed>
                 <callGas>
                   ( __CALLGAS_CELL => Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) +Gas 0 )
                 </callGas>
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
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <Gas Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) )
               )))
      [priority(20), label(BASIC-BLOCK-63-TO-47)]
    
    rule [BASIC-BLOCK-66-TO-38]: <kevm>
           <k>
             ( #next [ STATICCALL ] ~> .K => #access [ STATICCALL , STATICCALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ]
             ~> STATICCALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int
             ~> #pc [ STATICCALL ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : _WS:WordStack ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) )
                 </memoryUsed>
                 <callGas>
                   ( __CALLGAS_CELL => Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) +Gas 0 )
                 </callGas>
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
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               ))))
      [priority(20), label(BASIC-BLOCK-66-TO-38)]
    
    rule [BASIC-BLOCK-67-TO-39]: <kevm>
           <k>
             ( #next [ STATICCALL ] ~> .K => #access [ STATICCALL , STATICCALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int ]
             ~> STATICCALL _W0:Int ( _W1:Int modInt pow160 ) _W2:Int _W3:Int _W4:Int _W5:Int
             ~> #pc [ STATICCALL ] )
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
                   ( ( _W0:Int : ( _W1:Int : ( _W2:Int : ( _W3:Int : ( _W4:Int : ( _W5:Int : _WS:WordStack ) ) ) ) ) ) => _WS:WordStack )
                 </wordStack>
                 <gas>
                   ( _GAS_CELL:Gas => _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) -Gas Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) )
                 </gas>
                 <memoryUsed>
                   ( _MEMORYUSED_CELL:Int => #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) )
                 </memoryUsed>
                 <callGas>
                   ( __CALLGAS_CELL => Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) +Gas 0 )
                 </callGas>
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
       andBool ( ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) <=Gas _GAS_CELL:Gas
       andBool ( Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) +Gas Cgascap ( _SCHEDULE_CELL:Schedule , _W0:Int , _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) ) , Cextra ( _SCHEDULE_CELL:Schedule , true , 0 , ( _W1:Int modInt pow160 ) in _ACCESSEDACCOUNTS_CELL:Set ) ) <=Gas _GAS_CELL:Gas -Gas ( Cmem ( _SCHEDULE_CELL:Schedule , #memoryUsageUpdate ( #memoryUsageUpdate ( _MEMORYUSED_CELL:Int , _W2:Int , _W3:Int ) , _W4:Int , _W5:Int ) ) -Int Cmem ( _SCHEDULE_CELL:Schedule , _MEMORYUSED_CELL:Int ) )
               )))
      [priority(20), label(BASIC-BLOCK-67-TO-39)]

endmodule
