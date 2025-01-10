
┌─ 1 (root, split, init)
│   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
│   pc: _PC_CELL:Int
│   callDepth: _CALLDEPTH_CELL:Int
│   statusCode: _STATUSCODE_CELL:StatusCode
┃
┃ (branch)
┣━━┓ subst: .Subst
┃  ┃ constraint:
┃  ┃     #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 4
┃  │
┃  ├─ 3
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
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
┃  ┃     ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -4 ) >Int 1024
┃  │
┃  ├─ 4
┃  │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
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
   ┃     ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 4 )
   ┃     ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -4 ) >Int 1024 )
   │
   ├─ 5
   │   k: #next [ EXTCODECOPY ] ~> _K_CELL:K
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   │
   │  (1 step)
   ├─ 6
   │   k: #addr [ EXTCODECOPY ] ~> #exec [ EXTCODECOPY ] ~> #pc [ EXTCODECOPY ] ~> _K_CELL ...
   │   pc: _PC_CELL:Int
   │   callDepth: _CALLDEPTH_CELL:Int
   │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  ├─ 9
   ┃  │   k: #exec [ EXTCODECOPY ] ~> #pc [ EXTCODECOPY ] ~> _K_CELL:K
   ┃  │   pc: _PC_CELL:Int
   ┃  │   callDepth: _CALLDEPTH_CELL:Int
   ┃  │   statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┃ (1 step)
   ┃  ┣━━┓
   ┃  ┃  │
   ┃  ┃  └─ 11 (leaf, pending)
   ┃  ┃      k: #gas [ EXTCODECOPY , EXTCODECOPY ( W0:Int modInt pow160 ) W1:Int W2:Int W3:Int ] ...
   ┃  ┃      pc: _PC_CELL:Int
   ┃  ┃      callDepth: _CALLDEPTH_CELL:Int
   ┃  ┃      statusCode: _STATUSCODE_CELL:StatusCode
   ┃  ┃
   ┃  ┗━━┓
   ┃     │
   ┃     └─ 12 (leaf, pending)
   ┃         k: #exec [ EXTCODECOPY ] ~> #pc [ EXTCODECOPY ] ~> _K_CELL:K
   ┃         pc: _PC_CELL:Int
   ┃         callDepth: _CALLDEPTH_CELL:Int
   ┃         statusCode: _STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 10
      │   k: #addr [ EXTCODECOPY ] ~> #exec [ EXTCODECOPY ] ~> #pc [ EXTCODECOPY ] ~> _K_CELL ...
      │   pc: _PC_CELL:Int
      │   callDepth: _CALLDEPTH_CELL:Int
      │   statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  └─ 13 (leaf, pending)
      ┃      k: #exec [ EXTCODECOPY ] ~> #pc [ EXTCODECOPY ] ~> _K_CELL:K
      ┃      pc: _PC_CELL:Int
      ┃      callDepth: _CALLDEPTH_CELL:Int
      ┃      statusCode: _STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         └─ 14 (leaf, pending)
             k: #addr [ EXTCODECOPY ] ~> #exec [ EXTCODECOPY ] ~> #pc [ EXTCODECOPY ] ~> _K_CELL ...
             pc: _PC_CELL:Int
             callDepth: _CALLDEPTH_CELL:Int
             statusCode: _STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: _K_CELL:K
│   pc: ?_FINAL_PC_CELL:Int
│   callDepth: ?_FINAL_CALLDEPTH_CELL:Int
│   statusCode: ?_FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-EXTCODECOPY-SPEC
    
    
    rule [BASIC-BLOCK-5-TO-6]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] ~> .K => #addr [ EXTCODECOPY ]
             ~> #exec [ EXTCODECOPY ]
             ~> #pc [ EXTCODECOPY ] )
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
      requires ( ( notBool #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 4 )
       andBool ( ( notBool ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -4 ) >Int 1024 )
               ))
      [priority(20), label(BASIC-BLOCK-5-TO-6)]
    
    rule [BASIC-BLOCK-4-TO-7]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] => #halt )
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
      requires ( #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) +Int -4 ) >Int 1024
      [priority(20), label(BASIC-BLOCK-4-TO-7)]
    
    rule [BASIC-BLOCK-3-TO-8]: <kevm>
           <k>
             ( #next [ EXTCODECOPY ] => #halt )
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
      requires #sizeWordStack ( _WORDSTACK_CELL:WordStack , 0 ) <Int 4
      [priority(20), label(BASIC-BLOCK-3-TO-8)]

endmodule
