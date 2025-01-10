KEVM Gas
========

Here is a representation of `Gas`. This sort is used by `<gas>`, `<callGas>`, and `<gasUsed>` cells of the EVM configuration. As is in this file, `Gas` is a super-sort of `Int` with no differing behaviour. However the distinction at this level allows for an extension of infinite gas later, see `infinite-gas.md`.

```k
requires "schedule.md"

module GAS-SYNTAX
    imports INT-SYNTAX

    syntax Gas ::= Int
    syntax Int ::= "gas2Int" "(" Gas ")" [function, total]

    syntax Gas ::= "minGas" "(" Gas "," Gas ")" [function, total]
                 > left:
                   Gas "*Gas" Gas [function, total]
                 | Gas "/Gas" Gas [function]
                 > left:
                   Gas "+Gas" Gas [function, total]
                 | Gas "-Gas" Gas [function, total]

    syntax Bool ::= Gas  "<Gas" Gas [function, total]
                  | Gas "<=Gas" Gas [function, total]
endmodule

module GAS
    imports INT
    imports BOOL
    imports GAS-SYNTAX
    imports GAS-SIMPLIFICATION
    imports GAS-FEES

    rule I1:Int *Gas I2:Int => I1 *Int I2
    rule I1:Int /Gas I2:Int => I1 /Int I2
    rule I1:Int +Gas I2:Int => I1 +Int I2
    rule I1:Int -Gas I2:Int => I1 -Int I2

    rule I1:Int  <Gas I2:Int => I1  <Int I2
    rule I1:Int <=Gas I2:Int => I1 <=Int I2

    rule minGas(I1:Int, I2:Int) => minInt(I1, I2)
    rule gas2Int(G:Int) => G
endmodule
```

KEVM Infinite Gas
=================

Here we use the construct `#gas` to represent positive infinity, while tracking the gas formula through execution.
This allows (i) computing final gas used, and (ii) never stopping because of out-of-gas.
Note that the argument to `#gas(_)` is just metadata tracking the current gas usage, and is not meant to be compared to other values.
As such, any `#gas(G)` and `#gas(G')` are the _same_ positive infinite, regardless of the values `G` and `G'`.
In particular, this means that `#gas(_) <Gas #gas(_) => false`, and `#gas(_) <=Gas #gas(_) => true`, regardless of the values contained in the `#gas(_)`.

```k
module INFINITE-GAS
    imports GAS

    syntax Gas ::= #gas(Int) [symbol(infGas), smtlib(infGas)]
 // ---------------------------------------------------------

    rule #gas(G) +Gas G'       => #gas(G +Int G')
    rule #gas(G) -Gas G'       => #gas(G -Int G')
    rule #gas(G) *Gas G'       => #gas(G *Int G')
    rule #gas(G) /Gas G'       => #gas(G /Int G')  requires G' =/=Int 0
    rule      G  +Gas #gas(G') => #gas(G +Int G')
    rule      G  -Gas #gas(G') => #gas(G -Int G')
    rule      G  *Gas #gas(G') => #gas(G *Int G')
    rule      G  /Gas #gas(G') => #gas(G /Int G')  requires G' =/=Int 0
    rule #gas(G) +Gas #gas(G') => #gas(G +Int G')
    rule #gas(G) -Gas #gas(G') => #gas(G -Int G')
    rule #gas(G) *Gas #gas(G') => #gas(G *Int G')
    rule #gas(G) /Gas #gas(G') => #gas(G /Int G')  requires G' =/=Int 0

    rule _:Int    <Gas #gas(_) => true
    rule #gas(_)  <Gas _       => false [simplification]
    rule #gas(_) <=Gas _:Int   => false
    rule _       <=Gas #gas(_) => true  [simplification]

    rule minGas(#gas(G), #gas(G')) => #gas(minInt(G, G'))
    rule minGas(G:Int  , #gas(G')) => #gas(minInt(G, G'))
    rule minGas(#gas(G), G':Int)   => #gas(minInt(G, G'))

    rule gas2Int(#gas(G)) => G

    rule #allBut64th(#gas(G)) => #gas(#allBut64th(G))
    rule Cgascap(SCHED, #gas(GCAP), #gas(GAVAIL), GEXTRA) => #gas(Cgascap(SCHED, GCAP, GAVAIL, GEXTRA)) [simplification]
    rule Cgascap(SCHED, #gas(GCAP), GAVAIL:Int, GEXTRA)   => #gas(Cgascap(SCHED, GCAP, GAVAIL, GEXTRA)) [simplification]
    rule Cgascap(SCHED, GCAP:Int, #gas(GAVAIL), GEXTRA)   => #gas(Cgascap(SCHED, GCAP, GAVAIL, GEXTRA)) [simplification]

    rule #if B #then #gas(G) #else #gas(G') #fi => #gas(#if B #then G #else G' #fi) [simplification]
endmodule
```

KEVM Gas Fees
=============

Here are some internal helper functions for calculating gas. Most of these functions are specified in the YellowPaper.

```k
module GAS-FEES
    imports GAS-SYNTAX
    imports SCHEDULE

    syntax Gas ::= Cgascap        ( Schedule , Gas , Gas , Int ) [symbol(Cgascap_Gas), overload(Cgascap), function, total, smtlib(gas_Cgascap_Gas)]
    syntax Int ::= Cgascap        ( Schedule , Int , Int , Int ) [symbol(Cgascap_Int), overload(Cgascap), function, total, smtlib(gas_Cgascap_Int)]

    syntax Int ::= Csstore        ( Schedule , Int , Int , Int )         [symbol(Csstore),        function, total, smtlib(gas_Csstore)       ]
                 | Rsstore        ( Schedule , Int , Int , Int )         [symbol(Rsstore),        function, total, smtlib(gas_Rsstore)       ]
                 | Cextra         ( Schedule , Bool , Int , Bool )       [symbol(Cextra),         function, total, smtlib(gas_Cextra)        ]
                 | Cnew           ( Schedule , Bool , Int )              [symbol(Cnew),           function, total, smtlib(gas_Cnew)          ]
                 | Cxfer          ( Schedule , Int )                     [symbol(Cxfer),          function, total, smtlib(gas_Cxfer)         ]
                 | Cmem           ( Schedule , Int )                     [symbol(Cmem),           function, total, smtlib(gas_Cmem), memo    ]
                 | Caddraccess    ( Schedule , Bool )                    [symbol(Caddraccess),    function, total, smtlib(gas_Caddraccess)   ]
                 | Cstorageaccess ( Schedule , Bool )                    [symbol(Cstorageaccess), function, total, smtlib(gas_Cstorageaccess)]
                 | Csload         ( Schedule , Bool )                    [symbol(Csload),         function, total, smtlib(gas_Csload)        ]
                 | Cextcodesize   ( Schedule )                           [symbol(Cextcodesize),   function, total, smtlib(gas_Cextcodesize)  ]
                 | Cextcodecopy   ( Schedule , Int )                     [symbol(Cextcodecopy),   function, total, smtlib(gas_Cextcodecopy)  ]
                 | Cextcodehash   ( Schedule )                           [symbol(Cextcodehash),   function, total, smtlib(gas_Cextcodehash)  ]
                 | Cbalance       ( Schedule )                           [symbol(Cbalance),       function, total, smtlib(gas_Cbalance)      ]
                 | Cmodexp        ( Schedule , Bytes , Int , Int , Int ) [symbol(Cmodexp),        function, total, smtlib(gas_Cmodexp)       ]
                 | Cinitcode      ( Schedule , Int )                     [symbol(Cinitcode),      function, total, smtlib(gas_Cinitcode)     ]
 // ------------------------------------------------------------------------------------------------------------------------------------------
    rule [Cgascap]:
         Cgascap(SCHED, GCAP:Int, GAVAIL:Int, GEXTRA)
      => #if GAVAIL <Int GEXTRA orBool Gstaticcalldepth << SCHED >> #then GCAP #else minInt(#allBut64th(GAVAIL -Int GEXTRA), GCAP) #fi
      requires 0 <=Int GCAP
      [concrete]

    rule Cgascap(_, GCAP, _, _) => 0 requires GCAP <Gas 0 [concrete]

    rule [Csstore.new]:
         Csstore(SCHED, NEW, CURR, ORIG)
      => #if CURR ==Int NEW orBool ORIG =/=Int CURR #then Gsload < SCHED > #else #if ORIG ==Int 0 #then Gsstoreset < SCHED > #else Gsstorereset < SCHED > #fi #fi
      requires Ghasdirtysstore << SCHED >>
      [concrete]

    rule [Csstore.old]:
         Csstore(SCHED, NEW, CURR, _ORIG)
      => #if CURR ==Int 0 andBool NEW =/=Int 0 #then Gsstoreset < SCHED > #else Gsstorereset < SCHED > #fi
      requires notBool Ghasdirtysstore << SCHED >>
      [concrete]

    rule [Rsstore.new]:
         Rsstore(SCHED, NEW, CURR, ORIG)
      => #if CURR =/=Int NEW andBool ORIG ==Int CURR andBool NEW ==Int 0 #then
             Rsstoreclear < SCHED >
         #else
             #if CURR =/=Int NEW andBool ORIG =/=Int CURR andBool ORIG =/=Int 0 #then
                 #if CURR ==Int 0 #then 0 -Int Rsstoreclear < SCHED > #else #if NEW ==Int 0 #then Rsstoreclear < SCHED > #else 0 #fi #fi
             #else
                 0
             #fi +Int
             #if CURR =/=Int NEW andBool ORIG ==Int NEW #then
                 #if ORIG ==Int 0 #then Gsstoreset < SCHED > #else Gsstorereset < SCHED > #fi -Int Gsload < SCHED >
             #else
                 0
             #fi
         #fi
      requires Ghasdirtysstore << SCHED >>
      [concrete]

    rule [Rsstore.old]:
         Rsstore(SCHED, NEW, CURR, _ORIG)
      => #if CURR =/=Int 0 andBool NEW ==Int 0 #then Rsstoreclear < SCHED > #else 0 #fi
      requires notBool Ghasdirtysstore << SCHED >>
      [concrete]

    rule [Cextra.new]: Cextra(SCHED, ISEMPTY, VALUE, ISWARM)  => Caddraccess(SCHED, ISWARM) +Int Cnew(SCHED, ISEMPTY, VALUE) +Int Cxfer(SCHED, VALUE) requires         Ghasaccesslist << SCHED >>
    rule [Cextra.old]: Cextra(SCHED, ISEMPTY, VALUE, _ISWARM) => Gcall < SCHED > +Int Cnew(SCHED, ISEMPTY, VALUE) +Int Cxfer(SCHED, VALUE)            requires notBool Ghasaccesslist << SCHED >>

    rule [Cnew]:
         Cnew(SCHED, ISEMPTY:Bool, VALUE)
      => #if ISEMPTY andBool (VALUE =/=Int 0 orBool Gzerovaluenewaccountgas << SCHED >>) #then Gnewaccount < SCHED > #else 0 #fi

    rule [Cxfer.none]: Cxfer(_SCHED, 0) => 0
    rule [Cxfer.some]: Cxfer( SCHED, N) => Gcallvalue < SCHED > requires N =/=Int 0

    rule [Cmem]: Cmem(SCHED, N) => (N *Int Gmemory < SCHED >) +Int ((N *Int N) /Int Gquadcoeff < SCHED >) [concrete]

    rule [Caddraccess]:    Caddraccess(SCHED, ISWARM)    => #if ISWARM #then Gwarmstorageread < SCHED > #else Gcoldaccountaccess < SCHED > #fi
    rule [Cstorageaccess]: Cstorageaccess(SCHED, ISWARM) => #if ISWARM #then Gwarmstorageread < SCHED > #else Gcoldsload < SCHED >         #fi

    rule [Csload.new]: Csload(SCHED, ISWARM)  => Cstorageaccess(SCHED, ISWARM) requires         Ghasaccesslist << SCHED >>
    rule [Csload.old]: Csload(SCHED, _ISWARM) => Gsload < SCHED >              requires notBool Ghasaccesslist << SCHED >>

    rule [Cextcodesize.new]: Cextcodesize(SCHED) => 0                      requires         Ghasaccesslist << SCHED >>
    rule [Cextcodesize.old]: Cextcodesize(SCHED) => Gextcodesize < SCHED > requires notBool Ghasaccesslist << SCHED >>

    rule [Cextcodehash.new]: Cextcodehash(SCHED) => 0                  requires         Ghasaccesslist << SCHED >>
    rule [Cextcodehash.old]: Cextcodehash(SCHED) => Gbalance < SCHED > requires notBool Ghasaccesslist << SCHED >>

    rule [Cbalance.new]: Cbalance(SCHED) => 0                  requires         Ghasaccesslist << SCHED >>
    rule [Cbalance.old]: Cbalance(SCHED) => Gbalance < SCHED > requires notBool Ghasaccesslist << SCHED >>

    rule [Cextcodecopy.new]: Cextcodecopy(SCHED, WIDTH) => Gcopy < SCHED > *Int (WIDTH up/Int 32)                               requires         Ghasaccesslist << SCHED >> [concrete]
    rule [Cextcodecopy.old]: Cextcodecopy(SCHED, WIDTH) => Gextcodecopy < SCHED > +Int (Gcopy < SCHED > *Int (WIDTH up/Int 32)) requires notBool Ghasaccesslist << SCHED >> [concrete]

    rule [Cmodexp.old]: Cmodexp(SCHED, DATA, BASELEN, EXPLEN, MODLEN) => #multComplexity(maxInt(BASELEN, MODLEN)) *Int maxInt(#adjustedExpLength(BASELEN, EXPLEN, DATA), 1) /Int Gquaddivisor < SCHED >
      requires notBool Ghasaccesslist << SCHED >>
      [concrete]

    rule [Cmodexp.new]: Cmodexp(SCHED, DATA, BASELEN, EXPLEN, MODLEN) => maxInt(200, (#newMultComplexity(maxInt(BASELEN, MODLEN)) *Int maxInt(#adjustedExpLength(BASELEN, EXPLEN, DATA), 1)) /Int Gquaddivisor < SCHED > )
      requires Ghasaccesslist << SCHED >>
      [concrete]

    rule [Cinitcode.new]: Cinitcode(SCHED, INITCODELEN) => Ginitcodewordcost < SCHED > *Int ( INITCODELEN up/Int 32 ) requires         Ghasmaxinitcodesize << SCHED >> [concrete]
    rule [Cinitcode.old]: Cinitcode(SCHED, _)           => 0                                                          requires notBool Ghasmaxinitcodesize << SCHED >> [concrete]

    syntax Bool ::= #accountEmpty ( AccountCode , Int , Int ) [function, total, symbol(accountEmpty)]
 // -------------------------------------------------------------------------------------------------
    rule #accountEmpty(CODE, NONCE, BAL) => CODE ==K .Bytes andBool NONCE ==Int 0 andBool BAL ==Int 0

    syntax Gas ::= #allBut64th ( Gas ) [symbol(#allBut64th_Gas), overload(#allBut64th), function, total, smtlib(gas_allBut64th_Gas)]
    syntax Int ::= #allBut64th ( Int ) [symbol(#allBut64th_Int), overload(#allBut64th), function, total, smtlib(gas_allBut64th_Int)]
 // --------------------------------------------------------------------------------------------------------------------------------
    rule [allBut64th.pos]: #allBut64th(N) => N -Int (N /Int 64) requires 0 <=Int N
    rule [allBut64th.neg]: #allBut64th(N) => 0                  requires N  <Int 0

    syntax Int ::= G0 ( Schedule , Bytes , Bool )           [function, symbol(G0base)]
                 | G0 ( Schedule , Bytes , Int , Int, Int ) [function, symbol(G0data)]
 // ----------------------------------------------------------------------------------
    rule G0(SCHED, WS, false) => G0(SCHED, WS, 0, lengthBytes(WS), 0) +Int Gtransaction < SCHED >
    rule G0(SCHED, WS, true)  => G0(SCHED, WS, 0, lengthBytes(WS), 0) +Int Gtxcreate < SCHED > +Int Cinitcode(SCHED, lengthBytes(WS))

    rule G0(    _,  _, I, I, R) => R
    rule G0(SCHED, WS, I, J, R) => G0(SCHED, WS, I +Int 1, J, R +Int #if WS[I] ==Int 0 #then Gtxdatazero < SCHED > #else Gtxdatanonzero < SCHED > #fi) [owise]

    syntax Gas ::= "G*" "(" Gas "," Int "," Int "," Schedule ")" [function]
 // -----------------------------------------------------------------------
    rule G*(GAVAIL, GLIMIT, REFUND, SCHED) => GAVAIL +Gas minGas((GLIMIT -Gas GAVAIL) /Gas Rmaxquotient < SCHED >, REFUND)

    syntax Int ::= #multComplexity(Int)    [symbol(#multComplexity),    function]
                 | #newMultComplexity(Int) [symbol(#newMultComplexity), function]
 // -----------------------------------------------------------------------------
    rule #multComplexity(X) => X *Int X                                     requires X <=Int 64
    rule #multComplexity(X) => X *Int X /Int 4 +Int 96 *Int X -Int 3072     requires X >Int 64 andBool X <=Int 1024
    rule #multComplexity(X) => X *Int X /Int 16 +Int 480 *Int X -Int 199680 requires X >Int 1024

    rule #newMultComplexity(X) => (X up/Int 8) ^Int 2

    syntax Int ::= #adjustedExpLength(Int, Int, Bytes) [symbol(#adjustedExpLength),    function]
                 | #adjustedExpLength(Int)             [symbol(#adjustedExpLengthAux), function]
 // --------------------------------------------------------------------------------------------
    rule #adjustedExpLength(BASELEN, EXPLEN, DATA) => #if EXPLEN <=Int 32 #then 0 #else 8 *Int (EXPLEN -Int 32) #fi +Int #adjustedExpLength(#asInteger(#range(DATA, 96 +Int BASELEN, minInt(EXPLEN, 32))))

    rule #adjustedExpLength(0) => 0
    rule #adjustedExpLength(1) => 0
    rule #adjustedExpLength(N) => 1 +Int #adjustedExpLength(N /Int 2) requires N >Int 1
endmodule
```

KEVM Gas Simplifications
========================

Here are simplification rules related to gas that the haskell backend uses.

```k
module GAS-SIMPLIFICATION [symbolic]
    imports GAS-SYNTAX
    imports INT
    imports BOOL

    rule A <Gas B => false requires B <=Gas A [simplification]
    rule notBool (A <=Gas B) => B <Gas A [simplification]
    rule notBool (A <Gas B) => B <=Gas A [simplification]
endmodule
```

