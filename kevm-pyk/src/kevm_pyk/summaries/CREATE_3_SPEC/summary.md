
┌─ 1 (root, split, init)
│   k: #next [ CREATE ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     STATIC_CELL:Bool
┃  │
┃  ├─ 4
┃  │   k: #next [ CREATE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (2 steps)
┃  └─ 6 (leaf, terminal)
┃      k: #halt ~> K_CELL:K
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: EVMC_STATIC_MODE_VIOLATION
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  ┃     ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> ) orBool W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule > )
┃  │
┃  ├─ 47
┃  │   k: #next [ CREATE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 11
┃  │   k: #checkBalanceUnderflow ID_CELL:Int W0:Int ~> #checkDepthExceeded ~> #checkNonceE ...
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 12 (leaf, pending)
┃  ┃      k: #refund CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALAN ...
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 13 (split)
┃  ┃  │   k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃  │   pc: PC_CELL:Int
┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     1024 <=Int CALLDEPTH_CELL:Int
┃  ┃  ┃  │
┃  ┃  ┃  └─ 22 (leaf, pending)
┃  ┃  ┃      k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃  ┃      pc: PC_CELL:Int
┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     CALLDEPTH_CELL:Int <Int 1024
┃  ┃  ┃  ┃     ( notBool #rangeNonce ( NONCE_CELL:Int ) )
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 49
┃  ┃  ┃  │   k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃  ┃  │   pc: PC_CELL:Int
┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  └─ 35 (leaf, pending)
┃  ┃  ┃      k: #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int ,  ...
┃  ┃  ┃      pc: PC_CELL:Int
┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     0 <=Int NONCE_CELL:Int
┃  ┃     ┃     CALLDEPTH_CELL:Int <Int 1024
┃  ┃     ┃     NONCE_CELL:Int <Int maxUInt64
┃  ┃     │
┃  ┃     ├─ 50
┃  ┃     │   k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃     │   pc: PC_CELL:Int
┃  ┃     │   callDepth: CALLDEPTH_CELL:Int
┃  ┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃     │
┃  ┃     │  (1 step)
┃  ┃     └─ 36 (leaf, pending)
┃  ┃         k: #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int ,  ...
┃  ┃         pc: PC_CELL:Int
┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 14
┃     │   k: #checkBalanceUnderflow ID_CELL:Int W0:Int ~> #checkDepthExceeded ~> #checkNonceE ...
┃     │   pc: PC_CELL:Int
┃     │   callDepth: CALLDEPTH_CELL:Int
┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     │
┃     ┊  constraint:
┃     ┊      false
┃     ┊  subst: .Subst
┃     └─ 2 (leaf, target)
┃         k: K_CELL:K
┃         pc: FINAL_PC_CELL:Int
┃         callDepth: FINAL_CALLDEPTH_CELL:Int
┃         statusCode: FINAL_STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  ┃     ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> ) orBool W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule > )
┃  │
┃  ├─ 51
┃  │   k: #next [ CREATE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 17
┃  │   k: #checkBalanceUnderflow ID_CELL:Int W0:Int ~> #checkDepthExceeded ~> #checkNonceE ...
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 18 (leaf, pending)
┃  ┃      k: #refund CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALAN ...
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 19 (split)
┃  ┃  │   k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃  │   pc: PC_CELL:Int
┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     CALLDEPTH_CELL:Int <Int 1024
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 29
┃  ┃  ┃  │   k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃  ┃  │   pc: PC_CELL:Int
┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  └─ 39 (leaf, pending)
┃  ┃  ┃      k: #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int ,  ...
┃  ┃  ┃      pc: PC_CELL:Int
┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     1024 <=Int CALLDEPTH_CELL:Int
┃  ┃     │
┃  ┃     └─ 30 (leaf, pending)
┃  ┃         k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃         pc: PC_CELL:Int
┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 20
┃     │   k: #checkBalanceUnderflow ID_CELL:Int W0:Int ~> #checkDepthExceeded ~> #checkNonceE ...
┃     │   pc: PC_CELL:Int
┃     │   callDepth: CALLDEPTH_CELL:Int
┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     │
┃     ┊  constraint:
┃     ┊      false
┃     ┊  subst: .Subst
┃     └─ 2 (leaf, target)
┃         k: K_CELL:K
┃         pc: FINAL_PC_CELL:Int
┃         callDepth: FINAL_CALLDEPTH_CELL:Int
┃         statusCode: FINAL_STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  ┃     ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> ) orBool W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule > )
┃  │
┃  ├─ 53
┃  │   k: #next [ CREATE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 25
┃  │   k: #checkBalanceUnderflow ID_CELL:Int W0:Int ~> #checkDepthExceeded ~> #checkNonceE ...
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 26 (leaf, pending)
┃  ┃      k: #refund CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALAN ...
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  ├─ 27 (split)
┃  ┃  │   k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃  │   pc: PC_CELL:Int
┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┃ (branch)
┃  ┃  ┣━━┓ subst: .Subst
┃  ┃  ┃  ┃ constraint:
┃  ┃  ┃  ┃     CALLDEPTH_CELL:Int <Int 1024
┃  ┃  ┃  │
┃  ┃  ┃  ├─ 37
┃  ┃  ┃  │   k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃  ┃  │   pc: PC_CELL:Int
┃  ┃  ┃  │   callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃  │
┃  ┃  ┃  │  (1 step)
┃  ┃  ┃  └─ 46 (leaf, pending)
┃  ┃  ┃      k: #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int ,  ...
┃  ┃  ┃      pc: PC_CELL:Int
┃  ┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃  ┃
┃  ┃  ┗━━┓ subst: .Subst
┃  ┃     ┃ constraint:
┃  ┃     ┃     1024 <=Int CALLDEPTH_CELL:Int
┃  ┃     │
┃  ┃     └─ 38 (leaf, pending)
┃  ┃         k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃         pc: PC_CELL:Int
┃  ┃         callDepth: CALLDEPTH_CELL:Int
┃  ┃         statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     ├─ 28
┃     │   k: #checkBalanceUnderflow ID_CELL:Int W0:Int ~> #checkDepthExceeded ~> #checkNonceE ...
┃     │   pc: PC_CELL:Int
┃     │   callDepth: CALLDEPTH_CELL:Int
┃     │   statusCode: STATUSCODE_CELL:StatusCode
┃     │
┃     ┊  constraint:
┃     ┊      false
┃     ┊  subst: .Subst
┃     └─ 2 (leaf, target)
┃         k: K_CELL:K
┃         pc: FINAL_PC_CELL:Int
┃         callDepth: FINAL_CALLDEPTH_CELL:Int
┃         statusCode: FINAL_STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  ┃     ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> ) orBool W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule > )
┃  │
┃  ├─ 55
┃  │   k: #next [ CREATE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  ├─ 34
┃  │   k: #checkBalanceUnderflow ID_CELL:Int W0:Int ~> #checkDepthExceeded ~> #checkNonceE ...
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┃ (1 step)
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 40 (leaf, pending)
┃  ┃      k: #refund CALLGAS_CELL:Gas ~> #pushCallStack ~> #pushWorldState ~> #end EVMC_BALAN ...
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┣━━┓
┃  ┃  │
┃  ┃  └─ 41 (leaf, pending)
┃  ┃      k: #checkDepthExceeded ~> #checkNonceExceeded ID_CELL:Int ~> #create ID_CELL:Int #n ...
┃  ┃      pc: PC_CELL:Int
┃  ┃      callDepth: CALLDEPTH_CELL:Int
┃  ┃      statusCode: STATUSCODE_CELL:StatusCode
┃  ┃
┃  ┗━━┓
┃     │
┃     └─ 42 (leaf, pending)
┃         k: #checkBalanceUnderflow ID_CELL:Int W0:Int ~> #checkDepthExceeded ~> #checkNonceE ...
┃         pc: PC_CELL:Int
┃         callDepth: CALLDEPTH_CELL:Int
┃         statusCode: STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  ┃     ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> ) orBool W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule > )
┃  │
┃  ├─ 57
┃  │   k: #next [ CREATE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (7 steps)
┃  └─ 45 (leaf, pending)
┃      k: #checkBalanceUnderflow ID_CELL:Int W0:Int ~> #checkDepthExceeded ~> #checkNonceE ...
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: STATUSCODE_CELL:StatusCode
┃
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     ( notBool STATIC_CELL:Bool )
┃  ┃     ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> ) orBool W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule > )
┃  │
┃  ├─ 59
┃  │   k: #next [ CREATE ] ~> K_CELL:K
┃  │   pc: PC_CELL:Int
┃  │   callDepth: CALLDEPTH_CELL:Int
┃  │   statusCode: STATUSCODE_CELL:StatusCode
┃  │
┃  │  (4 steps)
┃  └─ 43 (leaf, pending)
┃      k: CREATE W0:Int W1:Int W2:Int ~> #pc [ CREATE ] ~> K_CELL:K
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: STATUSCODE_CELL:StatusCode
┃
┗━━┓ subst: .Subst
   ┃ constraint:
   ┃     ( notBool STATIC_CELL:Bool )
   │
   ├─ 60
   │   k: #next [ CREATE ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   │
   │  (4 steps)
   └─ 44 (leaf, pending)
       k: CREATE W0:Int W1:Int W2:Int ~> #pc [ CREATE ] ~> K_CELL:K
       pc: PC_CELL:Int
       callDepth: CALLDEPTH_CELL:Int
       statusCode: STATUSCODE_CELL:StatusCode




module SUMMARY-CREATE-3-SPEC
    
    
    rule [BASIC-BLOCK-4-TO-6]: <kevm>
           <k>
             ( #next [ CREATE ] => #halt )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <statusCode>
                 ( _STATUSCODE_CELL => EVMC_STATIC_MODE_VIOLATION )
               </statusCode>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( _W0 : ( _W1 : ( _W2 : _WS ) ) )
                 </wordStack>
                 <static>
                   ( STATIC_CELL:Bool => true )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( STATIC_CELL:Bool
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
               ))
      [priority(20), label(BASIC-BLOCK-4-TO-6)]
    
    rule [BASIC-BLOCK-29-TO-39]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #checkNonceExceeded ID_CELL:Int
             ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) W0:Int #range ( LOCALMEM_CELL:Bytes , _W1 , W2:Int )
             ~> #codeDeposit #newAddr ( ID_CELL:Int , NONCE_CELL:Int )
             ~> #pc [ CREATE ]
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   false
                 </static>
                 <callDepth>
                   CALLDEPTH_CELL:Int
                 </callDepth>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL |Set SetItem ( #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <balance>
                     BALANCE_CELL:Int
                   </balance>
                   <nonce>
                     NONCE_CELL:Int
                   </nonce>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _STATIC_CELL )
       andBool ( W0:Int <=Int BALANCE_CELL:Int
       andBool ( CALLDEPTH_CELL:Int <Int 1024
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               )))))
      [priority(20), label(BASIC-BLOCK-29-TO-39)]
    
    rule [BASIC-BLOCK-37-TO-46]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #checkNonceExceeded ID_CELL:Int
             ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) W0:Int #range ( LOCALMEM_CELL:Bytes , _W1 , W2:Int )
             ~> #codeDeposit #newAddr ( ID_CELL:Int , NONCE_CELL:Int )
             ~> #pc [ CREATE ]
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   false
                 </static>
                 <callDepth>
                   CALLDEPTH_CELL:Int
                 </callDepth>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL |Set SetItem ( #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <balance>
                     BALANCE_CELL:Int
                   </balance>
                   <nonce>
                     NONCE_CELL:Int
                   </nonce>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _STATIC_CELL )
       andBool ( W0:Int <=Int BALANCE_CELL:Int
       andBool ( CALLDEPTH_CELL:Int <Int 1024
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               )))))
      [priority(20), label(BASIC-BLOCK-37-TO-46)]
    
    rule [BASIC-BLOCK-49-TO-35]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #checkNonceExceeded ID_CELL:Int
             ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) W0:Int #range ( LOCALMEM_CELL:Bytes , _W1 , W2:Int )
             ~> #codeDeposit #newAddr ( ID_CELL:Int , NONCE_CELL:Int )
             ~> #pc [ CREATE ]
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   false
                 </static>
                 <callDepth>
                   CALLDEPTH_CELL:Int
                 </callDepth>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL |Set SetItem ( #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <balance>
                     BALANCE_CELL:Int
                   </balance>
                   <nonce>
                     NONCE_CELL:Int
                   </nonce>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _STATIC_CELL )
       andBool ( W0:Int <=Int BALANCE_CELL:Int
       andBool ( CALLDEPTH_CELL:Int <Int 1024
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( notBool #rangeNonce ( NONCE_CELL:Int ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               ))))))
      [priority(20), label(BASIC-BLOCK-49-TO-35)]
    
    rule [BASIC-BLOCK-50-TO-36]: <kevm>
           <k>
             ( #checkDepthExceeded ~> .K => .K )
             ~> #checkNonceExceeded ID_CELL:Int
             ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) W0:Int #range ( LOCALMEM_CELL:Bytes , _W1 , W2:Int )
             ~> #codeDeposit #newAddr ( ID_CELL:Int , NONCE_CELL:Int )
             ~> #pc [ CREATE ]
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   false
                 </static>
                 <callDepth>
                   CALLDEPTH_CELL:Int
                 </callDepth>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   _ACCESSEDACCOUNTS_CELL |Set SetItem ( #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <balance>
                     BALANCE_CELL:Int
                   </balance>
                   <nonce>
                     NONCE_CELL:Int
                   </nonce>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool _STATIC_CELL )
       andBool ( 0 <=Int NONCE_CELL:Int
       andBool ( W0:Int <=Int BALANCE_CELL:Int
       andBool ( CALLDEPTH_CELL:Int <Int 1024
       andBool ( NONCE_CELL:Int <Int maxUInt64
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               )))))))
      [priority(20), label(BASIC-BLOCK-50-TO-36)]
    
    rule [BASIC-BLOCK-59-TO-43]: <kevm>
           <k>
             ( #next [ CREATE ] ~> .K => CREATE W0:Int W1:Int W2:Int
             ~> #pc [ CREATE ] )
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : WS:WordStack ) ) ) => WS:WordStack )
                 </wordStack>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool STATIC_CELL:Bool )
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               )))
      [priority(20), label(BASIC-BLOCK-59-TO-43)]
    
    rule [BASIC-BLOCK-60-TO-44]: <kevm>
           <k>
             ( #next [ CREATE ] ~> .K => CREATE W0:Int W1:Int W2:Int
             ~> #pc [ CREATE ] )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : WS:WordStack ) ) ) => WS:WordStack )
                 </wordStack>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool STATIC_CELL:Bool )
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
               ))
      [priority(20), label(BASIC-BLOCK-60-TO-44)]
    
    rule [BASIC-BLOCK-47-TO-11]: <kevm>
           <k>
             ( #next [ CREATE ] ~> .K => #checkBalanceUnderflow ID_CELL:Int W0:Int
             ~> #checkDepthExceeded
             ~> #checkNonceExceeded ID_CELL:Int
             ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) W0:Int #range ( LOCALMEM_CELL:Bytes , W1:Int , W2:Int )
             ~> #codeDeposit #newAddr ( ID_CELL:Int , NONCE_CELL:Int )
             ~> #pc [ CREATE ] )
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : WS:WordStack ) ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( ACCESSEDACCOUNTS_CELL:Set => ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <nonce>
                     NONCE_CELL:Int
                   </nonce>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool STATIC_CELL:Bool )
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               )))
      [priority(20), label(BASIC-BLOCK-47-TO-11)]
    
    rule [BASIC-BLOCK-51-TO-17]: <kevm>
           <k>
             ( #next [ CREATE ] ~> .K => #checkBalanceUnderflow ID_CELL:Int W0:Int
             ~> #checkDepthExceeded
             ~> #checkNonceExceeded ID_CELL:Int
             ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) W0:Int #range ( LOCALMEM_CELL:Bytes , W1:Int , W2:Int )
             ~> #codeDeposit #newAddr ( ID_CELL:Int , NONCE_CELL:Int )
             ~> #pc [ CREATE ] )
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : WS:WordStack ) ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( ACCESSEDACCOUNTS_CELL:Set => ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <nonce>
                     NONCE_CELL:Int
                   </nonce>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool STATIC_CELL:Bool )
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               )))
      [priority(20), label(BASIC-BLOCK-51-TO-17)]
    
    rule [BASIC-BLOCK-53-TO-25]: <kevm>
           <k>
             ( #next [ CREATE ] ~> .K => #checkBalanceUnderflow ID_CELL:Int W0:Int
             ~> #checkDepthExceeded
             ~> #checkNonceExceeded ID_CELL:Int
             ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) W0:Int #range ( LOCALMEM_CELL:Bytes , W1:Int , W2:Int )
             ~> #codeDeposit #newAddr ( ID_CELL:Int , NONCE_CELL:Int )
             ~> #pc [ CREATE ] )
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : WS:WordStack ) ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( ACCESSEDACCOUNTS_CELL:Set => ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <nonce>
                     NONCE_CELL:Int
                   </nonce>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool STATIC_CELL:Bool )
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               )))
      [priority(20), label(BASIC-BLOCK-53-TO-25)]
    
    rule [BASIC-BLOCK-55-TO-34]: <kevm>
           <k>
             ( #next [ CREATE ] ~> .K => #checkBalanceUnderflow ID_CELL:Int W0:Int
             ~> #checkDepthExceeded
             ~> #checkNonceExceeded ID_CELL:Int
             ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) W0:Int #range ( LOCALMEM_CELL:Bytes , W1:Int , W2:Int )
             ~> #codeDeposit #newAddr ( ID_CELL:Int , NONCE_CELL:Int )
             ~> #pc [ CREATE ] )
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : WS:WordStack ) ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( ACCESSEDACCOUNTS_CELL:Set => ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <nonce>
                     NONCE_CELL:Int
                   </nonce>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool STATIC_CELL:Bool )
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               )))
      [priority(20), label(BASIC-BLOCK-55-TO-34)]
    
    rule [BASIC-BLOCK-57-TO-45]: <kevm>
           <k>
             ( #next [ CREATE ] ~> .K => #checkBalanceUnderflow ID_CELL:Int W0:Int
             ~> #checkDepthExceeded
             ~> #checkNonceExceeded ID_CELL:Int
             ~> #create ID_CELL:Int #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) W0:Int #range ( LOCALMEM_CELL:Bytes , W1:Int , W2:Int )
             ~> #codeDeposit #newAddr ( ID_CELL:Int , NONCE_CELL:Int )
             ~> #pc [ CREATE ] )
             ~> _K_CELL
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
                 <id>
                   ID_CELL:Int
                 </id>
                 <wordStack>
                   ( ( W0:Int : ( W1:Int : ( W2:Int : WS:WordStack ) ) ) => WS:WordStack )
                 </wordStack>
                 <localMem>
                   LOCALMEM_CELL:Bytes
                 </localMem>
                 <static>
                   ( STATIC_CELL:Bool => false )
                 </static>
                 ...
               </callState>
               <substate>
                 <accessedAccounts>
                   ( ACCESSEDACCOUNTS_CELL:Set => ACCESSEDACCOUNTS_CELL:Set |Set SetItem ( #newAddr ( ID_CELL:Int , NONCE_CELL:Int ) ) )
                 </accessedAccounts>
                 ...
               </substate>
               ...
             </evm>
             <network>
               <accounts>
                 ( <account>
                   <acctID>
                     ID_CELL:Int
                   </acctID>
                   <nonce>
                     NONCE_CELL:Int
                   </nonce>
                   ...
                 </account>
                 DotAccountVar:AccountCellMap )
               </accounts>
               ...
             </network>
           </ethereum>
           ...
         </kevm>
      requires ( ( notBool STATIC_CELL:Bool )
       andBool ( ( notBool <acctID>
          ID_CELL:Int
        </acctID> in_keys ( DotAccountVar:AccountCellMap ) )
       andBool ( ( ( notBool Ghasmaxinitcodesize << SCHEDULE_CELL:Schedule >> )
          orBool ( W2:Int <=Int maxInitCodeSize < SCHEDULE_CELL:Schedule >
                 ))
               )))
      [priority(20), label(BASIC-BLOCK-57-TO-45)]

endmodule
