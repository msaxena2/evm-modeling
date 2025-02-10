module BYTES-SIMPLIFICATION [symbolic]
    imports INT-SYMBOLIC
    imports EVM
    imports BUF

  // ########################
  // Buffer Reasoning
  // ########################

    rule [bytes-not-equal-length]:
      BA1:Bytes ==K BA2:Bytes => false
      requires lengthBytes(BA1) =/=Int lengthBytes(BA2)
      [simplification]

    rule [bytes-equal-concat-split-k]:
      A:Bytes +Bytes B:Bytes ==K C:Bytes +Bytes D:Bytes => A ==K C andBool B ==K D
      requires lengthBytes(A) ==Int lengthBytes(C)
        orBool lengthBytes(B) ==Int lengthBytes(D)
      [simplification]

    rule [bytes-equal-concat-split-ml]:
      { A:Bytes +Bytes B:Bytes #Equals C:Bytes +Bytes D:Bytes } => { A #Equals C } #And { B #Equals D }
      requires lengthBytes(A) ==Int lengthBytes(C)
        orBool lengthBytes(B) ==Int lengthBytes(D)
      [simplification]

    rule [signextend-min]: (signextend( _ , W:Int) s<Word minSInt128Word ) => 0 requires W <Int pow128 [simplification, symbolic(W)]
    rule [signextend-max]: (maxSInt128 s<Word signextend( _ , W:Int) ) => 0 requires W <Int pow128 [simplification, symbolic(W)]

    rule [bytes-concat-empty-right]: B:Bytes +Bytes .Bytes  => B [simplification]
    rule [bytes-concat-empty-left]:   .Bytes +Bytes B:Bytes => B [simplification]

    rule [bytes-concat-right-assoc-symb-l]: (B1:Bytes +Bytes B2:Bytes) +Bytes B3:Bytes => B1 +Bytes (B2 +Bytes B3) [symbolic(B1), simplification(40)]
    rule [bytes-concat-right-assoc-symb-r]: (B1:Bytes +Bytes B2:Bytes) +Bytes B3:Bytes => B1 +Bytes (B2 +Bytes B3) [symbolic(B2), simplification(40)]
    rule [bytes-concat-left-assoc-conc]:    B1:Bytes +Bytes (B2:Bytes +Bytes B3:Bytes) => (B1 +Bytes B2) +Bytes B3 [concrete(B1, B2), symbolic(B3), simplification(40)]

    // #buf

    rule [buf-empty]: #buf(N:Int, _) => b"" requires N ==Int 0 [simplification]

    rule [buf-inject-k]:
      #buf(W:Int, X:Int) ==K #buf(W:Int, Y:Int) => X ==Int Y
      requires 0 <=Int W
       andBool 0 <=Int X andBool X <Int 2 ^Int (8 *Int W)
       andBool 0 <=Int Y andBool Y <Int 2 ^Int (8 *Int W)
      [simplification, preserves-definedness]

    rule [buf-inject-ml]:
      { #buf(W:Int, X:Int) #Equals #buf(W:Int, Y:Int) } => { X #Equals Y }
      requires 0 <=Int W
       andBool 0 <=Int X andBool X <Int 2 ^Int (8 *Int W)
       andBool 0 <=Int Y andBool Y <Int 2 ^Int (8 *Int W)
      [simplification, preserves-definedness]

    rule [buf-as-int]: B:Bytes ==K #buf(32, X:Int) => X ==Int #asInteger(B)
      requires lengthBytes(B) <=Int 32
       andBool #rangeUInt(256, X) [simplification, concrete(B), comm]

    rule [buf-as-int-ml]:
      { B:Bytes #Equals #buf(32, X:Int) } => { X #Equals #asInteger(B) }
      requires lengthBytes(B) <=Int 32
       andBool #rangeUInt(256, X) [simplification, concrete(B), comm]

    rule [buf-asWord-invert-lr-len-leq]:
      #buf (W:Int , #asWord(B:Bytes)) => #buf(W -Int lengthBytes(B), 0) +Bytes B
      requires lengthBytes(B) <=Int W andBool W <=Int 32
      [simplification, concrete(W)]

    rule [buf-asWord-invert-lr-len-gt]:
      #buf (W:Int , #asWord(B:Bytes)) => #range(B, lengthBytes(B) -Int W, W)
      requires 0 <=Int W andBool W <Int lengthBytes(B) andBool lengthBytes(B) <=Int 32
       andBool #asWord(B) <Int 2 ^Int (8 *Int W)
      [simplification, concrete(W), preserves-definedness]

    rule [buf-zero-concat-base]:
      #buf(W1:Int, 0) +Bytes #buf(W2:Int, 0) => #buf(W1 +Int W2, 0)
      requires 0 <=Int W1 andBool 0 <=Int W2
      [simplification]

    rule [buf-zero-concat-conc]:
      #buf(W1:Int, 0) +Bytes #buf(W2:Int, 0) +Bytes B => #buf(W1 +Int W2, 0) +Bytes B
      requires 0 <=Int W1 andBool 0 <=Int W2
      [simplification]

    rule [shift-as-asWord]:
      X <<Int Y => #asWord ( #buf ( 32 -Int (Y /Int 8) , X ) +Bytes #buf ( Y /Int 8 , 0 ) )
      requires 0 <=Int X andBool X <Int 2 ^Int (256 -Int Y)
       andBool 0 <=Int Y andBool Y <=Int 256 andBool Y modInt 8 ==Int 0
      [simplification, concrete(Y), preserves-definedness]

    // #range

    rule [range-empty]:
      #range(_:Bytes, S:Int, W:Int) => .Bytes
      requires S <Int 0 orBool W <=Int 0
      [simplification(30)]

    rule [range-full]:
      #range(B:Bytes, 0, W:Int) => B +Bytes #buf(W -Int lengthBytes(B), 0)
      requires lengthBytes(B) <=Int W
      [simplification]

    rule [range-params-equal-ml]:
      { #range (B1:Bytes, S1:Int, W1:Int) #Equals #range (B2:Bytes, S2:Int, W2:Int) } => #Top
      requires B1 ==K B2 andBool S1 ==Int S2 andBool W1 ==Int W2
      [simplification]

    rule [range-included-in-cHead]:
      #range(B1:Bytes +Bytes _:Bytes, S:Int, W:Int) => #range(B1, S, W)
      requires S +Int W <=Int lengthBytes(B1)
      [simplification]

    rule [range-outside-cHead]:
      #range(B1:Bytes +Bytes B2:Bytes, S:Int, W:Int) => #range(B2, S -Int lengthBytes(B1), W)
      requires lengthBytes(B1) <=Int S
      [simplification]

    rule [range-includes-cHead]:
      #range(B1:Bytes +Bytes B2:Bytes, 0, W:Int) => B1 +Bytes #range(B2, 0, W -Int lengthBytes(B1))
      requires lengthBytes(B1) <=Int W
      [simplification]

    rule [range-inside-cHead-base-conc]:
      #range(B:Bytes, S1:Int +Int S2:Int, W:Int) => #range(#range(B, S2, lengthBytes(B) -Int S2), S1, W)
      requires 0 <=Int S1 andBool 0 <=Int S2 andBool 0 <Int S1 +Int S2 andBool S1 +Int S2 <=Int lengthBytes(B)
      [concrete(B, S2), simplification]

    rule [range-inside-cHead-concat]:
      #range(B1:Bytes +Bytes B2:Bytes, S:Int, W:Int) => #range(#range(B1, S, lengthBytes(B1) -Int S) +Bytes B2, 0, W)
      requires 0 <Int S andBool S <=Int lengthBytes(B1)
      [simplification]

    rule [range-of-range]:
      #range(#range(B:Bytes, S1:Int, W1:Int), S2:Int, W2:Int) =>
        #range(B, S1 +Int S2, minInt(W2, W1 -Int S2)) +Bytes #buf(maxInt(0, W2 -Int (W1 -Int S2)), 0)
      requires 0 <=Int S1 andBool 0 <=Int W1 andBool 0 <=Int S2 andBool 0 <=Int W2
      [simplification]

    rule [range-join-base]:
      #range(B, S1, W1) +Bytes #range(B, S2, W2) => #range(B, S1, W1 +Int W2)
      requires S2 ==Int S1 +Int W1
       andBool 0 <=Int S1 andBool 0 <=Int W1 andBool 0 <=Int S2 andBool 0 <=Int W2
      [simplification]

    rule [range-join-concat]:
      #range(B1, S1, W1) +Bytes ( #range(B1, S2, W2) +Bytes B2 ) => #range(B1, S1, W1 +Int W2) +Bytes B2
      requires S2 ==Int S1 +Int W1
       andBool 0 <=Int S1 andBool 0 <=Int W1 andBool 0 <=Int S2 andBool 0 <=Int W2
      [simplification]

    rule [range-reform-base]:
      #range(B:Bytes, S:Int, minInt(W1:Int, W2:Int)) +Bytes #buf(maxInt(0, W3:Int), 0) => #range (B, S, W1)
      requires W1 ==Int W2 +Int W3
       andBool W2 ==Int lengthBytes(B) -Int S
       andBool 0 <=Int S andBool 0 <=Int W1 andBool 0 <=Int W2
      [simplification]

    rule [range-reform-concat]:
      #range(B1:Bytes, S:Int, minInt(W1:Int, W2:Int)) +Bytes ( #buf(maxInt(0, W3:Int), 0) +Bytes B2:Bytes ) => #range (B1, S, W1) +Bytes B2
      requires W1 ==Int W2 +Int W3
       andBool W2 ==Int lengthBytes(B1) -Int S
       andBool 0 <=Int S andBool 0 <=Int W1 andBool 0 <=Int W2
      [simplification]

    rule [range-buf-zero-symb]:
      #range(#buf(W:Int, 0), S1:Int, W1:Int) => #buf(W1, 0)
      requires 0 <=Int W andBool 0 <=Int S1 andBool 0 <=Int W1
      [simplification]

    rule [range-buf-zero-conc]:
      #range(B, S1:Int, W1:Int) => #buf(W1, 0)
      requires 0 <=Int S1 andBool 0 <=Int W1
       andBool #asInteger(B) ==Int 0
      [concrete(B), simplification]

    rule [range-buf-zero-concat]:
      B:Bytes +Bytes #buf(W:Int, X:Int) => #buf(lengthBytes(B) +Int W, X)
      requires 0 <=Int W andBool 0 <=Int X andBool X <Int 2 ^Int (8 *Int W)
       andBool #asInteger(B) ==Int 0 andBool lengthBytes(B) +Int W <=Int 32
      [concrete(B, W), simplification, preserves-definedness]

    rule [range-buf-zero-concat-extend]:
      B1:Bytes +Bytes #buf(W:Int, X:Int) +Bytes B2 => #buf(lengthBytes(B1) +Int W, X) +Bytes B2
      requires 0 <=Int W andBool 0 <=Int X andBool X <Int 2 ^Int (8 *Int W)
       andBool #asInteger(B1) ==Int 0 andBool lengthBytes(B1) +Int W <=Int 32
      [concrete(B1, W), simplification, preserves-definedness]

    rule [range-memUpdate-before]:
      #range(B1:Bytes [ S1:Int := B2:Bytes ], S2:Int, W2:Int) =>
        #let W = minInt(W2, S1 -Int S2) #in
          #range(B1, S2, W) +Bytes #range(B1 [ S1 := B2 ], S1, W2 -Int W)
      requires 0 <=Int S2 andBool S2 <Int S1
      [simplification]

    rule [range-memUpdate-in-between]:
      #range(B1:Bytes [ S1:Int := B2:Bytes ], S2:Int, W2:Int) =>
        #let S = S2 -Int S1 #in
        #let W = minInt(W2, lengthBytes(B2) -Int S) #in
          #range(B2, S, W) +Bytes #range(B1, S1 +Int lengthBytes(B2), W2 -Int W)
      requires 0 <=Int S1 andBool S1 <=Int S2 andBool S2 <=Int S1 +Int lengthBytes(B2)
      [simplification]

    rule [range-memUpdate-outside]:
      #range(B1:Bytes [ S1:Int := B2:Bytes ], S2:Int, W2:Int) => #range(B1, S2, W2)
      requires 0 <=Int S1 andBool 0 <=Int W2 andBool S1 +Int lengthBytes(B2) <=Int S2 [simplification]

    rule [range-buf-zero]:
      #range (#buf(W1:Int, X:Int), S2:Int, W2:Int) => #buf(W2, 0)
      requires 0 <=Int X andBool X <Int 2 ^Int (8 *Int (W1 -Int (S2 +Int W2)))
       andBool 0 <=Int S2 andBool 0 <=Int W2 andBool S2 +Int W2 <=Int W1
      [simplification, concrete(W1, S2, W2), preserves-definedness]

    rule [range-buf-value]:
      #range (#buf(W1:Int, X:Int), S2:Int, W2:Int) => #buf(W2, X)
      requires 0 <=Int X andBool X <Int 2 ^Int (8 *Int W2)
       andBool 0 <=Int S2 andBool 0 <=Int W2 andBool W1 ==Int S2 +Int W2
      [simplification, concrete(W1, S2, W2), preserves-definedness]

    rule [range-padRightToWidth]:
      #range(#padRightToWidth(_, BUF), 0, WIDTH) => BUF
      requires lengthBytes(BUF) ==Int WIDTH [simplification]

    // Memory update

    rule [memUpdate-is-empty]:
      _:Bytes [ S:Int := _:Bytes ] => .Bytes
      requires S <Int 0
      [simplification]

    rule [memUpdate-concat-in-left]: (B1 +Bytes B2) [ S := B ] => (B1 [ S := B ]) +Bytes B2
      requires 0 <=Int S andBool S +Int lengthBytes(B) <Int lengthBytes(B1)
      [simplification(40)]

    rule [memUpdate-concat-in-right]: (B1 +Bytes B2) [ S := B ] => B1 +Bytes (B2 [ S -Int lengthBytes(B1) := B ])
      requires lengthBytes(B1) <=Int S
      [simplification(40)]

    rule [memUpdate-reorder]:
      B:Bytes [ S1:Int := B1:Bytes ] [ S2:Int := B2:Bytes ] => B [ S2 := B2 ] [ S1 := B1 ]
      requires 0 <=Int S2 andBool S2 <Int S1 andBool S2 +Int lengthBytes(B2) <=Int S1
      [simplification]

    rule [memUpdate-subsume]:
      B:Bytes [ S1:Int := B1:Bytes ] [ S2:Int := B2:Bytes ] => B [ S2 := B2 ]
      requires 0 <=Int S2 andBool S2 <=Int S1 andBool S1 +Int lengthBytes(B1) <=Int S2 +Int lengthBytes(B2)
      [simplification]

    rule [memUpdate-as-concat-inside]:
      B1:Bytes [ S:Int := B2:Bytes ] =>
        #range(B1, 0, S) +Bytes B2 +Bytes #range(B1 , S +Int lengthBytes(B2), lengthBytes(B1) -Int (S +Int lengthBytes(B2)))
      requires 0 <=Int S andBool S +Int lengthBytes(B2) <Int lengthBytes(B1)
      [simplification(60)]

    rule [memUpdate-as-concat-outside]:
      B1:Bytes [ S:Int := B2:Bytes ] => #range(B1, 0, S) +Bytes B2
      requires 0 <=Int S andBool lengthBytes(B1) <=Int S +Int lengthBytes(B2)
      [simplification(60)]

    // Memory lookup

    rule [bytes-concat-lookup-left]:
      ( B1:Bytes +Bytes B2:Bytes ) [ I:Int ] => B1 [ I ]
      requires 0 <=Int I andBool I <Int lengthBytes(B1)
      [simplification(40), preserves-definedness]

    rule [bytes-concat-lookup-right]:
      ( B1:Bytes +Bytes B2:Bytes ) [ I:Int ] => B2 [ I -Int lengthBytes(B1) ]
      requires lengthBytes(B1) <=Int I
      [simplification(40), preserves-definedness]

    rule [lookup-as-asWord]:
      B:Bytes [ I:Int ] => #asWord ( #range ( B, I, 1 ) )
      requires 0 <=Int I andBool I <=Int lengthBytes(B)
      [simplification(60)]

    // lengthBytes

    rule [lengthBytes-geq-zero]:   0 <=Int lengthBytes ( _ )                     => true                                     [simplification, smt-lemma]
    rule [lengthBytes-geq-nonPos]: X <=Int lengthBytes ( _ )                     => true requires X <=Int 0                  [simplification, concrete(X)]
    rule [lengthBytes-concat]:     lengthBytes(BUF1 +Bytes BUF2)                 => lengthBytes(BUF1) +Int lengthBytes(BUF2) [simplification]
    rule [lengthBytes-buf]:        lengthBytes(#buf(S, _))                       => S requires 0 <=Int S                     [simplification]
    rule [lengthBytes-range]:      lengthBytes(#range(_, S:Int, W:Int))          => maxInt(0, W) requires 0 <=Int S          [simplification]
    rule [lengthBytes-prtw]:       lengthBytes(#padRightToWidth(W:Int, B:Bytes)) => maxInt(lengthBytes(B), W)                [simplification]

    rule [lengthBytes-leq-zero]: lengthBytes(B:Bytes) <=Int 0 => B ==K .Bytes [simplification]

    // #padToWidth

    rule #padToWidth(32, #asByteStack(V)) => #buf(32, V)  requires #rangeUInt(256, V) [simplification]

    // #padRightToWidth

    rule #padRightToWidth ( X:Int, B:Bytes ) => B +Bytes padRightBytes(.Bytes, X -Int lengthBytes(B), 0 )
      requires lengthBytes(B) <=Int X
      [simplification, concrete(X)]

    // #ecrec

    rule lengthBytes ( #ecrec ( _ , _ , _ , _ ) ) <=Int 32 => true
        [simplification, smt-lemma]

    rule #asWord ( #ecrec ( _ , _ , _ , _ ) ) <Int pow160 => true
        [simplification, smt-lemma]

endmodule
