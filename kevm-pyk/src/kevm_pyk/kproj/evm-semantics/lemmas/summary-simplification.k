requires "../gas.md"

module SUMMARY-SIMPLIFICATION
    imports SUMMARY-SIMPLIFICATION-COMMON
endmodule

module SUMMARY-SIMPLIFICATION-COMMON
    imports GAS

 //   rule { true #Equals ( notBool G0 <Gas G1 ) } #And  { true #Equals ( notBool G1 <=Gas G0 ) } => false [simplification]

 // ---------------------------------------------------------------------
 // simpification rules for stack underflow check
 //   rule notBool #sizeWordStack ( WORDSTACK:WordStack , 0 ) <Int 1 => { WORDSTACK #Equals ( ?W0:Int : ?WS:WordStack ) } [simplification, symbolic]
 //   rule notBool #sizeWordStack ( WORDSTACK:WordStack , 0 ) <Int 2 => { WORDSTACK #Equals ( ?W0:Int : ( ?W1:Int : ?WS:WordStack ) ) } [simplification, symbolic]
 //   rule { true #Equals ( notBool #sizeWordStack ( WORDSTACK:WordStack , 0 ) <Int 2 ) } #And #Not ( #Exists W0:Int . #Exists W1:Int . #Exists WS:WordStack . { WORDSTACK:WordStack #Equals ( W0:Int : ( W1:Int : WS:WordStack ) ) } ) => false [simplification]
 //   rule notBool #sizeWordStack ( WORDSTACK:WordStack , 0 ) <Int 3 => { WORDSTACK #Equals ( ?W0:Int : ( ?W1:Int : ( ?W2:Int : ?WS:WordStack ) ) ) } [simplification, symbolic]
 //   rule notBool #sizeWordStack ( WORDSTACK:WordStack , 0 ) <Int 4 => { WORDSTACK #Equals ( ?W0:Int : ( ?W1:Int : ( ?W2:Int : ( ?W3:Int : ?WS:WordStack ) ) ) ) } [simplification, symbolic]

endmodule