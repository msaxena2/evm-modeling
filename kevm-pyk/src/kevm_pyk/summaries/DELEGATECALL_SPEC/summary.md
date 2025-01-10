
┌─ 1 (root, split, init)
│   k: #next [ DELEGATECALL ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 6
┃  │
┃  ├─ 3
┃  │   k: #next [ DELEGATECALL ] ~> _K_CELL:K
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
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -5 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ DELEGATECALL ] ~> _K_CELL:K
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
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 6 )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -5 ) >Int 1024 )
   │
   ├─ 5
   │   k: #next [ DELEGATECALL ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (1 step)
   ├─ 6
   │   k: #addr [ DELEGATECALL ] ~> #exec [ DELEGATECALL ] ~> #pc [ DELEGATECALL ] ~> _K_C ...
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  └─ 9 (leaf, pending)
   ┃      k: #exec [ DELEGATECALL ] ~> #pc [ DELEGATECALL ] ~> _K_CELL:K
   ┃      pc: _PC_CELL:Int
   ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #addr [ DELEGATECALL ] ~> #exec [ DELEGATECALL ] ~> #pc [ DELEGATECALL ] ~> _K_C ...
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  └─ 11 (leaf, pending)
      ┃      k: #exec [ DELEGATECALL ] ~> #pc [ DELEGATECALL ] ~> _K_CELL:K
      ┃      pc: _PC_CELL:Int
      ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         └─ 12 (leaf, pending)
             k: #addr [ DELEGATECALL ] ~> #exec [ DELEGATECALL ] ~> #pc [ DELEGATECALL ] ~> _K_C ...
             pc: _PC_CELL:Int
             callDepth: _CALLDEPTH_CELL:Int
             statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-DELEGATECALL-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ DELEGATECALL ] ~> .K => #addr [ DELEGATECALL ]
             ~> #exec [ DELEGATECALL ]
             ~> #pc [ DELEGATECALL ] )
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
      requires ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 6 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -5 ) >Int 1024 )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-6)]
    
    rule [BASIC-BLOCK-4-TO-7]: <kevm>
           <k>
             ( #next [ DELEGATECALL ] => #halt )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -5 ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-7)]
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ DELEGATECALL ] => #halt )
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
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 6
      [priority(20), label(BASIC-BLOCK-3-TO-8)]

endmodule
