requires "evm.md"
requires "buf.md"
requires "bitwise-simplification.k"
requires "bytes-simplification.k"
requires "evm-int-simplification.k"
requires "int-simplification.k"
requires "slot-updates.k"

module LEMMAS [symbolic]
    imports LEMMAS-WITHOUT-SLOT-UPDATES
    imports SLOT-UPDATES
endmodule

module LEMMAS-WITHOUT-SLOT-UPDATES [symbolic]
    imports BITWISE-SIMPLIFICATION
    imports BYTES-SIMPLIFICATION
    imports INT-SIMPLIFICATION
    imports EVM-INT-SIMPLIFICATION
    imports LEMMAS-HASKELL

  // ########################
  // Arithmetic
  // ########################

    // For #bufStrict simplification in benchmarks
    rule 0 <=Int #ceil32(I)        => true requires 0 <=Int I [simplification, smt-lemma]
    rule 0 <=Int #ceil32(I) -Int I => true requires 0 <=Int I [simplification]

    rule X *Int Y <Int pow256 => true
      requires (0 <=Int X orBool 0 <=Int Y) andBool Y <=Int maxUInt256 /Int X
      [simplification]

    rule #if B #then C +Int C1 #else C +Int C2 #fi => C +Int #if B #then C1 #else C2 #fi [simplification]

  // ########################
  // Set Reasoning
  // ########################

    rule X in (SetItem(Y) _   ) => true      requires           X ==Int Y   [simplification]
    rule X in (SetItem(Y) REST) => X in REST requires notBool ( X ==Int Y ) [simplification]

    rule   ( S:Set |Set SetItem ( X )                      ) |Set SetItem( X ) =>   ( S:Set |Set SetItem ( X )                      ) [simplification]
    rule ( ( S:Set |Set SetItem ( X ) ) |Set SetItem ( Y ) ) |Set SetItem( X ) => ( ( S:Set |Set SetItem ( X ) ) |Set SetItem ( Y ) ) [simplification]

  // ########################
  // Word Reasoning
  // ########################

    rule N <=Int #sizeWordStack ( _ , N ) => true requires 0 <=Int N [simplification, smt-lemma]

    // #newAddr range
    rule 0 <=Int #newAddr(_,_)             => true   [simplification]
    rule         #newAddr(_,_) <Int pow160 => true   [simplification]
    rule         #newAddr(_,_) <Int pow256 => true   [simplification]

    rule #isPrecompiledAccount(#newAddr(_, _), _) => false [simplification]

  // ########################
  // bool2Word reasoning
  // ########################

    // Range
    rule [b2w-lb]: 0 <=Int bool2Word(_)         => true [simplification, smt-lemma]
    rule [b2w-ub]:         bool2Word(_) <=Int 1 => true [simplification, smt-lemma]

    // Relationship with equality
    rule [b2w-eq-zero]: bool2Word(B) ==Int 0 => notBool B [simplification(30), comm]
    rule [b2w-eq-one]:  bool2Word(B) ==Int 1 => B         [simplification(30), comm]

    // Relationship with other comparators
    rule [b2w-lt-one]:  bool2Word(B) <Int            1 => notBool B           [simplification(30)]
    rule [b2w-gt-zero]:            0 <Int bool2Word(B) => B                   [simplification(30)]

    rule [b2w-lt-true]:  bool2Word(_) <Int X:Int => true  requires 1  <Int X [simplification(30), concrete(X)]
    rule [b2w-gt-false]: X:Int <Int bool2Word(_) => false requires 1 <=Int X [simplification(30), concrete(X)]

    rule [b2w-lt-b2w]:  bool2Word(A)  <Int bool2Word(B) => notBool A andBool         B [simplification(30)]
    rule [b2w-le-b2w]:  bool2Word(A) <=Int bool2Word(B) =>         A  orBool notBool B [simplification(30)]

    // Relationship with `&Int`
    rule [b2w-band-one]:           1  &Int bool2Word(B) => bool2Word(B)           [simplification]
    rule [b2w-band]:     bool2Word(A) &Int bool2Word(B) => bool2Word(A andBool B) [simplification]

    // Relationship with `|Int`
    rule [b2w-bor-one]:           1  |Int bool2Word(_) => 1                     [simplification]
    rule [b2w-bor]:     bool2Word(A) |Int bool2Word(B) => bool2Word(A orBool B) [simplification]

    // Relationship with `xorInt`
    rule [b2w-bxor-zero]:           0  xorInt bool2Word(Y) => bool2Word(Y)                                                     [simplification, comm]
    rule [b2w-bxor-one]:            1  xorInt bool2Word(Y) => bool2Word(notBool Y)                                             [simplification, comm]
    rule [b2w-bxor]:      bool2Word(X) xorInt bool2Word(Y) => bool2Word ( (X andBool notBool Y) orBool (notBool X andBool Y) ) [simplification]

    // Relationship with `#rangeBool`
    rule [b2w-rangeBool-eq-not-zero-l]: bool2Word (notBool (X ==Int 0)) => X requires #rangeBool(X) [simplification]
    rule [b2w-rangeBool-eq-not-zero-r]: bool2Word (notBool (0 ==Int X)) => X requires #rangeBool(X) [simplification]

    // As part of multiplication
    rule [b2w-mul-lt-l]: bool2Word(B) *Int C  <Int A => (B andBool C  <Int A) orBool (notBool B andBool 0  <Int A) [simplification]
    rule [b2w-mul-le-l]: bool2Word(B) *Int C <=Int A => (B andBool C <=Int A) orBool (notBool B andBool 0 <=Int A) [simplification]
    rule [b2w-mul-eq-l]: bool2Word(B) *Int C ==Int A => (B andBool C ==Int A) orBool (notBool B andBool A ==Int 0) [simplification, comm]

    rule [b2w-mul-lt-r]: C *Int bool2Word(B)  <Int A => (B andBool C  <Int A) orBool (notBool B andBool 0  <Int A) [simplification]
    rule [b2w-mul-le-r]: C *Int bool2Word(B) <=Int A => (B andBool C <=Int A) orBool (notBool B andBool 0 <=Int A) [simplification]
    rule [b2w-mul-eq-r]: C *Int bool2Word(B) ==Int A => (B andBool C ==Int A) orBool (notBool B andBool A ==Int 0) [simplification, comm]

    // As part of how the compiler returns a bool from storage
    rule [b2w-storage]: bool2Word(X ==Int 1) => X requires #rangeBool(X) [simplification]

  // ########################
  // Keccak
  // ########################

    // Required for #Ceil(#buf)
    rule 0 <=Int keccak( _ )             => true [simplification]
    rule         keccak( _ ) <Int pow256 => true [simplification]

  // ########################
  // Map Reasoning
  // ########################

    rule 0 <=Int #lookup( _M:Map , _ )             => true [simplification, smt-lemma]
    rule         #lookup( _M:Map , _ ) <Int pow256 => true [simplification, smt-lemma]

    rule #lookup ( _M:Map [ K1 <- V1 ] , K2 )    => #lookup ( K1 |-> V1 , K1 ) requires K1 ==Int  K2 [simplification]
    rule #lookup (  M:Map [ K1 <- _  ] , K2 )    => #lookup ( M         , K2 ) requires notBool ( K1 ==Int K2 ) [simplification]
    rule #lookup ( (K1:Int |-> _) M:Map, K2:Int) => #lookup ( M         , K2 ) requires notBool ( K1 ==Int K2 ) [simplification]

    rule M:Map [ I1:Int <- V1:Int ] [ I2:Int <- V2:Int ] ==K M:Map [ I2 <- V2 ] [ I1 <- V1 ] => true
      requires notBool ( I1 ==Int I2 )
      [simplification]

 // Hardcoded #addrFromPrivateKey simplifications, see: https://github.com/runtimeverification/haskell-backend/issues/3573
    rule #addrFromPrivateKey("0x0000000000000000000000000000000000000000000000000000000000000001") => 721457446580647751014191829380889690493307935711 [priority(40), concrete]

  // ########################
  // Memory
  // ########################

    rule #memoryUsageUpdate(MU, _, WIDTH) => MU requires 0 <=Int MU andBool WIDTH <=Int 0 [simplification]

    rule 0 <=Int #memoryUsageUpdate(MU, START, WIDTH) => true requires 0 <=Int MU orBool ( 0 <=Int START andBool 0 <=Int WIDTH ) [simplification]

    rule #memoryUsageUpdate(#memoryUsageUpdate(MU, START1, WIDTH1), START2, WIDTH2) => #memoryUsageUpdate(MU, START1, WIDTH1)
      requires 0 <Int WIDTH1 andBool 0 <Int WIDTH2 andBool START2 +Int WIDTH2 <=Int START1 +Int WIDTH1
      [simplification]

    rule #memoryUsageUpdate(#memoryUsageUpdate(MU, START1, WIDTH1), START2, WIDTH2) => #memoryUsageUpdate(MU, START2, WIDTH2)
      requires 0 <Int WIDTH1 andBool 0 <Int WIDTH2 andBool START1 +Int WIDTH1 <Int START2 +Int WIDTH2
      [simplification]

  // ########################
  // Gas Costs
  // ########################

    rule 0 <=Int Csload(_, _)                   => true                                       [simplification]
    rule 0 <=Int Cmem(_, N)                     => true requires 0 <=Int N                    [simplification]
    rule 0 <=Int Caddraccess(_, _)              => true                                       [simplification]
    rule 0 <=Int Csstore(_, _, _, _)            => true                                       [simplification]
    rule 0 <=Int Cgascap(_, _:Int, _:Int, _)    => true                                       [simplification]
    rule 0 <=Int #allBut64th(_:Int)             => true                                       [simplification]
    rule 0 <=Int Cextra(_, _, _, _)             => true                                       [simplification]
    rule 0 <=Int _:ScheduleConst < _:Schedule > => true                                       [simplification]
    rule 0 <=Int G up/Int I                     => true requires 0 <=Int G andBool 0 <Int I   [simplification]
    rule Cextra(_, _, _, _) <Int pow256         => true                                       [simplification]

    rule G <Int Csstore(SCHED, _:Int, _:Int, _) => false
      requires Gsload       < SCHED > <=Int G
       andBool Gsstoreset   < SCHED > <=Int G
       andBool Gsstorereset < SCHED > <=Int G
      [simplification]

    rule Csstore(SCHED, _:Int, _:Int, _) <=Int G => true
      requires Gsload       < SCHED > <=Int G
       andBool Gsstoreset   < SCHED > <=Int G
       andBool Gsstorereset < SCHED > <=Int G
      [simplification]

    rule G <=Int Csstore(SCHED, _:Int, _:Int, _) => false
      requires Gsload       < SCHED > <Int G
       andBool Gsstoreset   < SCHED > <Int G
       andBool Gsstorereset < SCHED > <Int G
      [simplification]

    rule Csstore(SCHED, _:Int, _:Int, _) <Int G => true
      requires Gsload       < SCHED > <Int G
       andBool Gsstoreset   < SCHED > <Int G
       andBool Gsstorereset < SCHED > <Int G
      [simplification]

endmodule

module LEMMAS-HASKELL [symbolic]
    imports INT-SYMBOLIC
    imports EVM
    imports BUF

  // ########################
  // Arithmetic
  // ########################

    // ; Z3 version 4.8.12
    // (set-option :smt.mbqi true)
    //
    // ; 2^256
    // (declare-const pow256 Int)
    // (assert (= pow256 115792089237316195423570985008687907853269984665640564039457584007913129639936))
    //
    // (define-fun chop ((x Int)) Int (mod x pow256))
    // (define-fun range256 ((x Int)) Bool (and (>= x 0) (< x pow256)))

    // (push)
    // (assert (forall ((x Int) (y Int)) (=> (and (<= pow256 (+ x y)) (range256 x) (range256 y)) (= (< (chop (+ x y)) x) true))))
    // (check-sat)
    // (pop)
    rule chop ( X +Int Y ) <Int X  => true   requires pow256 <=Int ( X +Int Y ) andBool #rangeUInt(256, X) andBool #rangeUInt(256, Y) [simplification]

    // (push)
    // (assert (forall ((x Int) (y Int)) (=> (and (<= pow256 (+ x y)) (range256 x) (range256 y)) (= (<= x (chop (+ x y))) false))))
    // (check-sat)
    // (pop)
    rule X <=Int chop ( X +Int Y ) => false  requires pow256 <=Int ( X +Int Y ) andBool #rangeUInt(256, X) andBool #rangeUInt(256, Y) [simplification]

  // ########################
  // Map Reasoning
  // ########################

    rule { M:Map [ I1:Int <- V1:Int ] [ I2:Int <- V2:Int ] #Equals M:Map [ I2 <- V2 ] [ I1 <- V1 ] } => #Top
      requires notBool ( I1 ==Int I2 )
      [simplification]

  // ########################
  // Boolean Logic
  // ########################

    rule B ==Bool true  => B         [simplification, comm]
    rule B ==Bool false => notBool B [simplification, comm]

    rule notBool notBool B => B [simplification]

    rule (notBool (A andBool B)) andBool A => (notBool B) andBool A [simplification]

endmodule
