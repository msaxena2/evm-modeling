
┌─ 1 (root, init)
│   k: #next [ SLOAD ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
│
│  (4 steps)
├─ 3
│   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> K_CELL:K
│   pc: PC_CELL:Int
│   callDepth: CALLDEPTH_CELL:Int
│   statusCode: STATUSCODE_CELL:StatusCode
┃
┃ (1 step)
┣━━┓
┃  │
┃  └─ 4 (leaf, pending)
┃      k: #lookup ( STORAGE:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> K_CELL:K
┃      pc: PC_CELL:Int
┃      callDepth: CALLDEPTH_CELL:Int
┃      statusCode: STATUSCODE_CELL:StatusCode
┃
┗━━┓
   │
   ├─ 5
   │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> K_CELL:K
   │   pc: PC_CELL:Int
   │   callDepth: CALLDEPTH_CELL:Int
   │   statusCode: STATUSCODE_CELL:StatusCode
   ┃
   ┃ (1 step)
   ┣━━┓
   ┃  │
   ┃  └─ 6 (leaf, pending)
   ┃      k: #lookup ( STORAGE0:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> K_CELL:K
   ┃      pc: PC_CELL:Int
   ┃      callDepth: CALLDEPTH_CELL:Int
   ┃      statusCode: STATUSCODE_CELL:StatusCode
   ┃
   ┗━━┓
      │
      ├─ 7
      │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> K_CELL:K
      │   pc: PC_CELL:Int
      │   callDepth: CALLDEPTH_CELL:Int
      │   statusCode: STATUSCODE_CELL:StatusCode
      ┃
      ┃ (1 step)
      ┣━━┓
      ┃  │
      ┃  └─ 8 (leaf, pending)
      ┃      k: #lookup ( STORAGE1:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> K_CELL:K
      ┃      pc: PC_CELL:Int
      ┃      callDepth: CALLDEPTH_CELL:Int
      ┃      statusCode: STATUSCODE_CELL:StatusCode
      ┃
      ┗━━┓
         │
         ├─ 9
         │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> K_CELL:K
         │   pc: PC_CELL:Int
         │   callDepth: CALLDEPTH_CELL:Int
         │   statusCode: STATUSCODE_CELL:StatusCode
         ┃
         ┃ (1 step)
         ┣━━┓
         ┃  │
         ┃  └─ 10 (leaf, pending)
         ┃      k: #lookup ( STORAGE2:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> K_CELL:K
         ┃      pc: PC_CELL:Int
         ┃      callDepth: CALLDEPTH_CELL:Int
         ┃      statusCode: STATUSCODE_CELL:StatusCode
         ┃
         ┗━━┓
            │
            ├─ 11
            │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> K_CELL:K
            │   pc: PC_CELL:Int
            │   callDepth: CALLDEPTH_CELL:Int
            │   statusCode: STATUSCODE_CELL:StatusCode
            ┃
            ┃ (1 step)
            ┣━━┓
            ┃  │
            ┃  └─ 12 (leaf, pending)
            ┃      k: #lookup ( STORAGE3:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> K_CELL:K
            ┃      pc: PC_CELL:Int
            ┃      callDepth: CALLDEPTH_CELL:Int
            ┃      statusCode: STATUSCODE_CELL:StatusCode
            ┃
            ┗━━┓
               │
               ├─ 13
               │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> K_CELL:K
               │   pc: PC_CELL:Int
               │   callDepth: CALLDEPTH_CELL:Int
               │   statusCode: STATUSCODE_CELL:StatusCode
               ┃
               ┃ (1 step)
               ┣━━┓
               ┃  │
               ┃  └─ 14 (leaf, pending)
               ┃      k: #lookup ( STORAGE4:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> K_CELL:K
               ┃      pc: PC_CELL:Int
               ┃      callDepth: CALLDEPTH_CELL:Int
               ┃      statusCode: STATUSCODE_CELL:StatusCode
               ┃
               ┗━━┓
                  │
                  ├─ 15
                  │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> K_CELL:K
                  │   pc: PC_CELL:Int
                  │   callDepth: CALLDEPTH_CELL:Int
                  │   statusCode: STATUSCODE_CELL:StatusCode
                  ┃
                  ┃ (1 step)
                  ┣━━┓
                  ┃  │
                  ┃  └─ 16 (leaf, pending)
                  ┃      k: #lookup ( STORAGE5:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> K_CELL:K
                  ┃      pc: PC_CELL:Int
                  ┃      callDepth: CALLDEPTH_CELL:Int
                  ┃      statusCode: STATUSCODE_CELL:StatusCode
                  ┃
                  ┗━━┓
                     │
                     ├─ 17
                     │   k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> K_CELL:K
                     │   pc: PC_CELL:Int
                     │   callDepth: CALLDEPTH_CELL:Int
                     │   statusCode: STATUSCODE_CELL:StatusCode
                     ┃
                     ┃ (1 step)
                     ┣━━┓
                     ┃  │
                     ┃  └─ 18 (leaf, pending)
                     ┃      k: #lookup ( STORAGE6:Map , W0:Int ) ~> #push ~> #pc [ SLOAD ] ~> K_CELL:K
                     ┃      pc: PC_CELL:Int
                     ┃      callDepth: CALLDEPTH_CELL:Int
                     ┃      statusCode: STATUSCODE_CELL:StatusCode
                     ┃
                     ┗━━┓
                        │
                        └─ 19 (leaf, pending)
                            k: SLOAD W0:Int ~> #pc [ SLOAD ] ~> K_CELL:K
                            pc: PC_CELL:Int
                            callDepth: CALLDEPTH_CELL:Int
                            statusCode: STATUSCODE_CELL:StatusCode


┌─ 2 (root, leaf, target)
│   k: K_CELL:K
│   pc: FINAL_PC_CELL:Int
│   callDepth: FINAL_CALLDEPTH_CELL:Int
│   statusCode: FINAL_STATUSCODE_CELL:StatusCode



module SUMMARY-SLOAD-1-SPEC
    
    
    rule [BASIC-BLOCK-1-TO-3]: <kevm>
           <k>
             ( #next [ SLOAD ] ~> .K => SLOAD W0:Int
             ~> #pc [ SLOAD ] )
             ~> _K_CELL
           </k>
           <useGas>
             false
           </useGas>
           <ethereum>
             <evm>
               <callState>
                 <wordStack>
                   ( ( W0:Int : WS:WordStack ) => WS:WordStack )
                 </wordStack>
                 ...
               </callState>
               ...
             </evm>
             ...
           </ethereum>
           ...
         </kevm>
      [priority(20), label(BASIC-BLOCK-1-TO-3)]

endmodule
