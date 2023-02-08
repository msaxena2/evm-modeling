Data-Structures over `Word`
===========================

EVM uses bounded 256 bit integer words, and sometimes also bytes (8 bit words).
Here we provide the arithmetic of these words, as well as some data-structures over them.
Both are implemented using K's `Int`.

```k
requires "word.md"

module EVM-TYPES
    imports STRING
    imports COLLECTIONS
    imports K-EQUAL
    imports JSON
    imports WORD
```

Utilities
---------

### Boolean Conversions

Primitives provide the basic conversion from K's sorts `Int` and `Bool` to EVM's words.

-   `bool2Word` interprets a `Bool` as a `Int`.
-   `word2Bool` interprets a `Int` as a `Bool`.

```k
    syntax Int ::= bool2Word ( Bool ) [function, total, smtlib(bool2Word)]
 // ----------------------------------------------------------------------
    rule bool2Word( B:Bool ) => 1 requires B
    rule bool2Word( B:Bool ) => 0 requires notBool B

    syntax Bool ::= word2Bool ( Int ) [function, total]
 // ---------------------------------------------------
    rule word2Bool( W ) => false requires W  ==Int 0
    rule word2Bool( W ) => true  requires W =/=Int 0
```

-   `sgn` gives the twos-complement interperetation of the sign of a word.
-   `abs` gives the twos-complement interperetation of the magnitude of a word.

```k
    syntax Int ::= sgn ( Int ) [function, total]
                 | abs ( Int ) [function, total]
 // --------------------------------------------
    rule sgn(I) => -1 requires pow255 <=Int I andBool I <Int pow256
    rule sgn(I) =>  1 requires 0 <=Int I andBool I <Int pow255
    rule sgn(I) =>  0 requires I <Int 0 orBool pow256 <=Int I

    rule abs(I) => 0 -Word I requires sgn(I) ==Int -1
    rule abs(I) => I         requires sgn(I) ==Int  1
    rule abs(I) => 0         requires sgn(I) ==Int  0
```

Word Operations
---------------

### Low-Level

-   `up/Int` performs integer division but rounds up instead of down.

NOTE: Here, we choose to add `I2 -Int 1` to the numerator beforing doing the division to mimic the C++ implementation.
You could alternatively calculate `I1 modInt I2`, then add one to the normal integer division afterward depending on the result.

```k
    syntax Int ::= Int "up/Int" Int [function, total, smtlib(upDivInt)]
 // -------------------------------------------------------------------
    rule              _I1 up/Int 0  => 0
    rule              _I1 up/Int I2 => 0                             requires I2 <Int 0
    rule               I1 up/Int 1  => I1
    rule [upDivInt] :  I1 up/Int I2 => (I1 +Int (I2 -Int 1)) /Int I2 requires I2 >Int 1
```

-   `log256Int` returns the log base 256 (floored) of an integer.

```k
    syntax Int ::= log256Int ( Int ) [function]
 // -------------------------------------------
    rule log256Int(N) => log2Int(N) /Int 8
```

The corresponding `<op>Word` operations automatically perform the correct modulus for EVM words.
Warning: operands are assumed to be within the range of a 256 bit EVM word. Unbound integers may not return the correct result.

```k
    syntax Int ::= Int "+Word" Int [function, total]
                 | Int "*Word" Int [function, total]
                 | Int "-Word" Int [function, total]
                 | Int "/Word" Int [function, total]
                 | Int "%Word" Int [function, total]
 // ------------------------------------------------
    rule W0 +Word W1 => chop( W0 +Int W1 )
    rule W0 -Word W1 => chop( W0 -Int W1 )
    rule W0 *Word W1 => chop( W0 *Int W1 )
    rule  _ /Word W1 => 0            requires W1  ==Int 0
    rule W0 /Word W1 => W0 /Int W1   requires W1 =/=Int 0
    rule  _ %Word W1 => 0            requires W1  ==Int 0
    rule W0 %Word W1 => W0 modInt W1 requires W1 =/=Int 0
```

Care is needed for `^Word` to avoid big exponentiation.
The helper `powmod` is a totalization of the operator `_^%Int__` (which comes with K).
`_^%Int__` is not defined when the modulus (third argument) is zero, but `powmod` is.

```k
    syntax Int ::= Int "^Word" Int       [function]
    syntax Int ::= powmod(Int, Int, Int) [function, total]
 // ------------------------------------------------------
    rule W0 ^Word W1 => powmod(W0, W1, pow256)

    rule [powmod.nonzero]: powmod(W0, W1, W2) => W0 ^%Int W1 W2  requires W2 =/=Int 0
    rule [powmod.zero]:    powmod( _,  _, W2) => 0               requires W2  ==Int 0
```

`/sWord` and `%sWord` give the signed interperetations of `/Word` and `%Word`.

```k
    syntax Int ::= Int "/sWord" Int [function]
                 | Int "%sWord" Int [function]
 // ------------------------------------------
    rule [divSWord.same]: W0 /sWord W1 =>          abs(W0) /Word abs(W1)  requires sgn(W0) *Int sgn(W1) ==Int  1
    rule [divSWord.diff]: W0 /sWord W1 => 0 -Word (abs(W0) /Word abs(W1)) requires sgn(W0) *Int sgn(W1) ==Int -1
    rule [modSWord.pos]:  W0 %sWord W1 =>          abs(W0) %Word abs(W1)  requires sgn(W0) ==Int  1
    rule [modSWord.neg]:  W0 %sWord W1 => 0 -Word (abs(W0) %Word abs(W1)) requires sgn(W0) ==Int -1
```

### Word Comparison

The `<op>Word` comparisons similarly lift K operators to EVM ones:

```k
    syntax Int ::= Int "<Word"  Int [function, total]
                 | Int ">Word"  Int [function, total]
                 | Int "<=Word" Int [function, total]
                 | Int ">=Word" Int [function, total]
                 | Int "==Word" Int [function, total]
 // -------------------------------------------------
    rule W0 <Word  W1 => bool2Word(W0 <Int  W1)
    rule W0 >Word  W1 => bool2Word(W0 >Int  W1)
    rule W0 <=Word W1 => bool2Word(W0 <=Int W1)
    rule W0 >=Word W1 => bool2Word(W0 >=Int W1)
    rule W0 ==Word W1 => bool2Word(W0 ==Int W1)
```

-   `s<Word` implements a less-than for `Word` (with signed interperetation).

```k
    syntax Int ::= Int "s<Word" Int [function, total]
 // -------------------------------------------------
    rule [s<Word.pp]: W0 s<Word W1 => W0 <Word W1           requires sgn(W0) ==K 1  andBool sgn(W1) ==K 1
    rule [s<Word.pn]: W0 s<Word W1 => bool2Word(false)      requires sgn(W0) ==K 1  andBool sgn(W1) ==K -1
    rule [s<Word.np]: W0 s<Word W1 => bool2Word(true)       requires sgn(W0) ==K -1 andBool sgn(W1) ==K 1
    rule [s<Word.nn]: W0 s<Word W1 => abs(W1) <Word abs(W0) requires sgn(W0) ==K -1 andBool sgn(W1) ==K -1
```

### Bitwise Operators

Bitwise logical operators are lifted from the integer versions.

```k
    syntax Int ::= "~Word" Int       [function, total]
                 | Int "|Word"   Int [function, total]
                 | Int "&Word"   Int [function, total]
                 | Int "xorWord" Int [function, total]
                 | Int "<<Word"  Int [function]
                 | Int ">>Word"  Int [function]
                 | Int ">>sWord" Int [function]
 // -------------------------------------------
    rule ~Word W       => W xorInt maxUInt256
    rule W0 |Word   W1 => W0 |Int W1
    rule W0 &Word   W1 => W0 &Int W1
    rule W0 xorWord W1 => W0 xorInt W1
    rule W0 <<Word  W1 => chop( W0 <<Int W1 ) requires W1 <Int 256
    rule  _ <<Word  W1 => 0 requires W1 >=Int 256
    rule W0 >>Word  W1 => W0 >>Int W1
    rule W0 >>sWord W1 => chop( (abs(W0) *Int sgn(W0)) >>Int W1 )
```

-   `bit` gets bit `N` (0 being MSB).
-   `byte` gets byte `N` (0 being the MSB).

```k
    syntax Int ::= bit  ( Int , Int ) [function]
                 | byte ( Int , Int ) [function]
 // --------------------------------------------
    rule bit (N, _) => 0 requires notBool (N >=Int 0 andBool N <Int 256)
    rule byte(N, _) => 0 requires notBool (N >=Int 0 andBool N <Int  32)

    rule bit (N, W) => bitRangeInt(W , (255 -Int N)        , 1) requires N >=Int 0 andBool N <Int 256
    rule byte(N, W) => bitRangeInt(W , ( 31 -Int N) *Int 8 , 8) requires N >=Int 0 andBool N <Int  32
```

-   `#nBits` shifts in `N` ones from the right.
-   `#nBytes` shifts in `N` bytes of ones from the right.

```k
    syntax Int ::= #nBits  ( Int )  [function]
                 | #nBytes ( Int )  [function]
 // ------------------------------------------
    rule #nBits(N)  => (1 <<Int N) -Int 1 requires N >=Int 0
    rule #nBytes(N) => #nBits(N *Int 8)   requires N >=Int 0
```

-   `signextend(N, W)` sign-extends from byte `N` of `W` (0 being MSB).

```k
    syntax Int ::= signextend( Int , Int ) [function, total]
 // --------------------------------------------------------
    rule [signextend.invalid]:  signextend(N, W) => W requires N >=Int 32 orBool N <Int 0
    rule [signextend.negative]: signextend(N, W) => chop( (#nBytes(31 -Int N) <<Byte (N +Int 1)) |Int W ) requires N <Int 32 andBool N >=Int 0 andBool         word2Bool(bit(256 -Int (8 *Int (N +Int 1)), W))
    rule [signextend.positive]: signextend(N, W) => chop( #nBytes(N +Int 1)                      &Int W ) requires N <Int 32 andBool N >=Int 0 andBool notBool word2Bool(bit(256 -Int (8 *Int (N +Int 1)), W))
```


A WordStack for EVM
-------------------

### As a cons-list

A cons-list is used for the EVM wordstack.

-   `.WordStack` serves as the empty worstack, and
-   `_:_` serves as the "cons" operator.

```k
    syntax WordStack ::= ".WordStack"      [smtlib(_dotWS)]
                       | Int ":" WordStack [klabel(_:_WS), smtlib(_WS_)]
 // --------------------------------------------------------------------
```

```{.k .bytes}
    syntax Bytes ::= Int ":" Bytes [function]
 // -----------------------------------------
    rule I : BS => Int2Bytes(1, I, BE) ++ BS requires I <Int 256
```

-   `#take(N , WS)` keeps the first `N` elements of a `WordStack` (passing with zeros as needed).
-   `#drop(N , WS)` removes the first `N` elements of a `WordStack`.

```k
    syntax WordStack ::= #take ( Int , WordStack ) [klabel(takeWordStack), function, total]
 // ---------------------------------------------------------------------------------------
    rule [#take.base]:      #take(N, _WS)                => .WordStack                      requires notBool N >Int 0
    rule [#take.zero-pad]:  #take(N, .WordStack)         => 0 : #take(N -Int 1, .WordStack) requires N >Int 0
    rule [#take.recursive]: #take(N, (W : WS):WordStack) => W : #take(N -Int 1, WS)         requires N >Int 0

    syntax WordStack ::= #drop ( Int , WordStack ) [klabel(dropWordStack), function, total]
 // ---------------------------------------------------------------------------------------
    rule #drop(N, WS:WordStack)       => WS                                  requires notBool N >Int 0
    rule #drop(N, .WordStack)         => .WordStack                          requires         N >Int 0
    rule #drop(N, (W : WS):WordStack) => #drop(1, #drop(N -Int 1, (W : WS))) requires         N >Int 1
    rule #drop(1, (_ : WS):WordStack) => WS
```

```{.k .bytes}
    syntax Bytes ::= #take ( Int , Bytes ) [klabel(takeBytes), function, total]
 // ---------------------------------------------------------------------------
    rule #take(N, _BS:Bytes) => .Bytes                                      requires                                        notBool N >Int 0
    rule #take(N,  BS:Bytes) => #padRightToWidth(N, .Bytes)                 requires notBool lengthBytes(BS) >Int 0 andBool         N >Int 0
    rule #take(N,  BS:Bytes) => BS ++ #take(N -Int lengthBytes(BS), .Bytes) requires         lengthBytes(BS) >Int 0 andBool notBool N >Int lengthBytes(BS)
    rule #take(N,  BS:Bytes) => BS [ 0 .. N ]                               requires         lengthBytes(BS) >Int 0 andBool         N >Int lengthBytes(BS)

    syntax Bytes ::= #drop ( Int , Bytes ) [klabel(dropBytes), function, total]
 // ---------------------------------------------------------------------------
    rule #drop(N, BS:Bytes) => BS                                  requires                                        notBool N >Int 0
    rule #drop(N, BS:Bytes) => .Bytes                              requires notBool lengthBytes(BS) >Int 0 andBool         N >Int 0
    rule #drop(N, BS:Bytes) => .Bytes                              requires         lengthBytes(BS) >Int 0 andBool         N >Int lengthBytes(BS)
    rule #drop(N, BS:Bytes) => substrBytes(BS, N, lengthBytes(BS)) requires         lengthBytes(BS) >Int 0 andBool notBool N >Int lengthBytes(BS)
```

### Element Access

-   `WS [ N ]` accesses element `N` of `WS`.
-   `WS [ N := W ]` sets element `N` of `WS` to `W` (padding with zeros as needed).

```k
    syntax Int ::= WordStack "[" Int "]" [function, total]
 // ------------------------------------------------------
    rule (W : _):WordStack [ N ] => W                  requires N ==Int 0
    rule WS:WordStack      [ N ] => #drop(N, WS) [ 0 ] requires N  >Int 0
    rule  _:WordStack      [ N ] => 0                  requires N  <Int 0

    syntax WordStack ::= WordStack "[" Int ":=" Int "]" [function, total]
 // ---------------------------------------------------------------------
    rule (_W0 : WS):WordStack [ N := W ] => W  : WS                     requires N ==Int 0
    rule ( W0 : WS):WordStack [ N := W ] => W0 : (WS [ N -Int 1 := W ]) requires N  >Int 0
    rule        WS :WordStack [ N := _ ] => WS                          requires N  <Int 0
    rule .WordStack           [ N := W ] => (0 : .WordStack) [ N := W ]
```

-   `#sizeWordStack` calculates the size of a `WordStack`.
-   `_in_` determines if a `Int` occurs in a `WordStack`.

```k
    syntax Int ::= #sizeWordStack ( WordStack )       [function, total, smtlib(sizeWordStack)]
                 | #sizeWordStack ( WordStack , Int ) [function, total, klabel(sizeWordStackAux), smtlib(sizeWordStackAux)]
 // -----------------------------------------------------------------------------------------------------------------------
    rule #sizeWordStack ( WS ) => #sizeWordStack(WS, 0)
    rule #sizeWordStack ( .WordStack, SIZE ) => SIZE
    rule #sizeWordStack ( _ : WS, SIZE )     => #sizeWordStack(WS, SIZE +Int 1)

    syntax Bool ::= Int "in" WordStack [function]
 // ---------------------------------------------
    rule _ in .WordStack => false
    rule W in (W' : WS)  => (W ==K W') orElseBool (W in WS)
```

-   `#replicateAux` pushes `N` copies of `A` onto a `WordStack`.
-   `#replicate` is a `WordStack` of length `N` with `A` the value of every element.

```k
    syntax WordStack ::= #replicate    ( Int, Int )            [function, total]
                       | #replicateAux ( Int, Int, WordStack ) [function, total]
 // ----------------------------------------------------------------------------
    rule #replicate   ( N,  A )     => #replicateAux(N, A, .WordStack)
    rule #replicateAux( N,  A, WS ) => #replicateAux(N -Int 1, A, A : WS) requires         N >Int 0
    rule #replicateAux( N, _A, WS ) => WS                                 requires notBool N >Int 0
```

-   `WordStack2List` converts a term of sort `WordStack` to a term of sort `List`.

```k
    syntax List ::= WordStack2List ( WordStack ) [function, total]
 // --------------------------------------------------------------
    rule WordStack2List(.WordStack) => .List
    rule WordStack2List(W : WS) => ListItem(W) WordStack2List(WS)
```

Local Memory
------------

Most of EVM data is held in local memory.

-   `WM [ N := WS ]` assigns a contiguous chunk of `WM` to `WS` starting at position `W`.
-   `#range(WM, START, WIDTH)` reads off `WIDTH` elements from `WM` beginning at position `START` (padding with zeros as needed).

```{.k .bytes}
    syntax Memory = Bytes
    syntax Memory ::= Memory "[" Int ":=" ByteArray "]" [function, total, klabel(mapWriteBytes)]
 // --------------------------------------------------------------------------------------------
    rule WS [ START := WS' ] => replaceAtBytes(padRightBytes(WS, START +Int #sizeByteArray(WS'), 0), START, WS') requires START >=Int 0  [concrete]
    rule  _ [ START := _:ByteArray ] => .Memory                                                                  requires START  <Int 0  [concrete]

    syntax ByteArray ::= #range ( Memory , Int , Int ) [function, total]
 // --------------------------------------------------------------------
    rule #range(LM, START, WIDTH) => LM [ START .. WIDTH ] [concrete]

    syntax Memory ::= ".Memory" [macro]
 // -----------------------------------
    rule .Memory => .Bytes

    syntax Memory ::= Memory "[" Int ":=" Int "]" [function]
 // --------------------------------------------------------
    rule WM [ IDX := VAL ] => padRightBytes(WM, IDX +Int 1, 0) [ IDX <- VAL ]
```

```{.k .nobytes}
    syntax Memory = Map
    syntax Memory ::= Memory "[" Int ":=" ByteArray "]" [function, total]
 // ---------------------------------------------------------------------
    rule [mapWriteBytes.base]:      WM[ _N := .WordStack ] => WM
    rule [mapWriteBytes.recursive]: WM[  N := W : WS     ] => (WM[N <- W])[N +Int 1 := WS]

    syntax ByteArray ::= #range ( Memory , Int , Int )             [function, total]
    syntax ByteArray ::= #range ( Memory , Int , Int , ByteArray ) [function, total, klabel(#rangeAux)]
 // ---------------------------------------------------------------------------------------------------
    rule [#range]:         #range(WM, START, WIDTH) => #range(WM, START +Int WIDTH -Int 1, WIDTH, .WordStack)
    rule [#rangeAux.base]: #range( _,  _END, WIDTH, WS) => WS requires notBool 0 <Int WIDTH
    rule [#rangeAux.rec]:  #range(WM,   END => END -Int 1, WIDTH => WIDTH -Int 1, WS => #lookupMemory(WM, END) : WS) requires 0 <Int WIDTH

    syntax Memory ::= ".Memory" [macro]
 // -----------------------------------
    rule .Memory => .Map

    syntax Memory ::= Memory "[" Int ":=" Int "]" [function]
 // --------------------------------------------------------
    rule WM [ IDX := VAL:Int ] => WM [ IDX <- VAL ]
```

Byte Arrays
-----------

The local memory of execution is a byte-array (instead of a word-array).

-   `#asWord` will interperet a stack of bytes as a single word (with MSB first).
-   `#asInteger` will interperet a stack of bytes as a single arbitrary-precision integer (with MSB first).
-   `#asAccount` will interpret a stack of bytes as a single account id (with MSB first).
    Differs from `#asWord` only in that an empty stack represents the empty account, not account zero.
-   `#asByteStack` will split a single word up into a `ByteArray`.
-   `_++_` acts as `ByteArray` append.
-   `WS [ N .. W ]` access the range of `WS` beginning with `N` of width `W`.
-   `#sizeByteArray` calculates the size of a `ByteArray`.
-   `#padToWidth(N, WS)` and `#padRightToWidth` make sure that a `WordStack` is the correct size.

```{.k .bytes}
    syntax ByteArray = Bytes
    syntax ByteArray ::= ".ByteArray" [macro]
 // -----------------------------------------
    rule .ByteArray => .Bytes

    syntax Int ::= #asWord ( ByteArray ) [function, total, smtlib(asWord)]
 // ----------------------------------------------------------------------
    rule #asWord(WS) => chop(Bytes2Int(WS, BE, Unsigned)) [concrete]

    syntax Int ::= #asInteger ( ByteArray ) [function, total]
 // ---------------------------------------------------------
    rule #asInteger(WS) => Bytes2Int(WS, BE, Unsigned) [concrete]

    syntax Account ::= #asAccount ( ByteArray ) [function]
 // ------------------------------------------------------
    rule #asAccount(BS) => .Account    requires lengthBytes(BS) ==Int 0
    rule #asAccount(BS) => #asWord(BS) [owise]

    syntax ByteArray ::= #asByteStack ( Int ) [function, total]
 // -----------------------------------------------------------
    rule #asByteStack(W) => Int2Bytes(W, BE, Unsigned) [concrete]

    syntax ByteArray ::= ByteArray "++" ByteArray [function, total, right, klabel(_++_WS), smtlib(_plusWS_)]
 // --------------------------------------------------------------------------------------------------------
    rule WS ++ WS' => WS +Bytes WS' [concrete]

    syntax ByteArray ::= ByteArray "[" Int ".." Int "]" [function, total]
 // ---------------------------------------------------------------------
    rule                 _ [ START .. WIDTH ] => .ByteArray                      requires notBool (WIDTH >=Int 0 andBool START >=Int 0)
    rule [bytesRange] : WS [ START .. WIDTH ] => substrBytes(padRightBytes(WS, START +Int WIDTH, 0), START, START +Int WIDTH)
      requires WIDTH >=Int 0 andBool START >=Int 0 andBool START <Int #sizeByteArray(WS)
    rule                 _ [ _     .. WIDTH ] => padRightBytes(.Bytes, WIDTH, 0) [owise]

    syntax Int ::= #sizeByteArray ( ByteArray ) [function, total, klabel(sizeByteArray), smtlib(sizeByteArray)]
 // -----------------------------------------------------------------------------------------------------------
    rule #sizeByteArray ( WS ) => lengthBytes(WS) [concrete]

    syntax ByteArray ::= #padToWidth      ( Int , ByteArray ) [function, total]
                       | #padRightToWidth ( Int , ByteArray ) [function, total]
 // ---------------------------------------------------------------------------
    rule                            #padToWidth(N, BS)      =>               BS        requires notBool (N >=Int 0)
    rule [padToWidthNonEmpty]:      #padToWidth(N, BS)      =>  padLeftBytes(BS, N, 0) requires          N >=Int 0
    rule                            #padRightToWidth(N, BS) =>               BS        requires notBool (N >=Int 0)
    rule [padRightToWidthNonEmpty]: #padRightToWidth(N, BS) => padRightBytes(BS, N, 0) requires          N >=Int 0
```

```{.k .nobytes}
    syntax ByteArray = WordStack
    syntax ByteArray ::= ".ByteArray" [macro]
 // -----------------------------------------
    rule .ByteArray => .WordStack

    syntax Int ::= #asWord ( ByteArray ) [function, total, smtlib(asWord)]
 // ----------------------------------------------------------------------
    rule [#asWord.base-empty]:  #asWord( .WordStack     ) => 0
    rule [#asWord.base-single]: #asWord( W : .WordStack ) => W
    rule [#asWord.recursive]:   #asWord( W0 : W1 : WS   ) => #asWord(((W0 *Word 256) +Word W1) : WS)

    syntax Int ::= #asInteger ( ByteArray ) [function]
 // --------------------------------------------------
    rule #asInteger( .WordStack     ) => 0
    rule #asInteger( W : .WordStack ) => W
    rule #asInteger( W0 : W1 : WS   ) => #asInteger(((W0 *Int 256) +Int W1) : WS)

    syntax Account ::= #asAccount ( ByteArray ) [function]
 // ------------------------------------------------------
    rule #asAccount( .WordStack ) => .Account
    rule #asAccount( W : WS     ) => #asWord(W : WS)

    syntax ByteArray ::= #asByteStack ( Int )             [function, total]
                       | #asByteStack ( Int , ByteArray ) [function, klabel(#asByteStackAux), smtlib(asByteStack)]
 // --------------------------------------------------------------------------------------------------------------
    rule [#asByteStack]:              #asByteStack( W )      => #asByteStack( W , .WordStack )
    rule [#asByteStackAux.base]:      #asByteStack( 0 , WS ) => WS
    rule [#asByteStackAux.recursive]: #asByteStack( W , WS ) => #asByteStack( W /Int 256 , W modInt 256 : WS ) requires W =/=K 0

    syntax ByteArray ::= ByteArray "++" ByteArray [function, memo, right, klabel(_++_WS), smtlib(_plusWS_)]
 // -------------------------------------------------------------------------------------------------------
    rule .WordStack ++ WS' => WS'
    rule (W : WS)   ++ WS' => W : (WS ++ WS')

    syntax ByteArray ::= ByteArray "[" Int ".." Int "]" [function, total, memo]
 // ---------------------------------------------------------------------------
    rule [ByteArray.range]: WS [ START .. WIDTH ] => #take(WIDTH, #drop(START, WS))

    syntax Int ::= #sizeByteArray ( ByteArray ) [function, total, smtlib(sizeByteArray), memo]
 // ------------------------------------------------------------------------------------------
    rule #sizeByteArray ( WS ) => #sizeWordStack(WS) [concrete]

    syntax ByteArray ::= #padToWidth      ( Int , ByteArray ) [function, total, memo]
                       | #padRightToWidth ( Int , ByteArray ) [function, memo]
 // ---------------------------------------------------------------------------------
    rule [#padToWidth]:      #padToWidth(N, WS)      => #replicateAux(N -Int #sizeByteArray(WS), 0, WS)
    rule [#padRightToWidth]: #padRightToWidth(N, WS) => WS ++ #replicate(N -Int #sizeByteArray(WS), 0)
```

Accounts
--------

### Empty Account

-   `.Account` represents the case when an account ID is referenced in the yellowpaper, but
    the actual value of the account ID is the empty set. This is used, for example, when
    referring to the destination of a message which creates a new contract.

```k
    syntax Account ::= ".Account" | Int
 // -----------------------------------
```

### Addresses

-   `#addr` turns an Ethereum word into the corresponding Ethereum address (160 LSB).

```k
    syntax Int ::= #addr ( Int ) [function]
 // ---------------------------------------
    rule #addr(W) => W %Word pow160
```

Storage/Memory Lookup
---------------------

`#lookup*` looks up a key in a map and returns 0 if the key doesn't exist, otherwise returning its value.

```k
    syntax Int ::= #lookup        ( Map , Int ) [function, total, smtlib(lookup)]
                 | #lookupMemory  ( Map , Int ) [function, total, smtlib(lookupMemory)]
 // -----------------------------------------------------------------------------------
    rule [#lookup.some]:         #lookup(       (KEY |-> VAL:Int) _M, KEY ) => VAL modInt pow256
    rule [#lookup.none]:         #lookup(                          M, KEY ) => 0                 requires notBool KEY in_keys(M)
    //Impossible case, for completeness
    rule [#lookup.notInt]:       #lookup(       (KEY |-> VAL    ) _M, KEY ) => 0                 requires notBool isInt(VAL)

    rule [#lookupMemory.some]:   #lookupMemory( (KEY |-> VAL:Int) _M, KEY ) => VAL modInt 256
    rule [#lookupMemory.none]:   #lookupMemory(                    M, KEY ) => 0                 requires notBool KEY in_keys(M)
    //Impossible case, for completeness
    rule [#lookupMemory.notInt]: #lookupMemory( (KEY |-> VAL    ) _M, KEY ) => 0                 requires notBool isInt(VAL)
```

Substate Log
------------

During execution of a transaction some things are recorded in the substate log (Section 6.1 in YellowPaper).
This is a right cons-list of `SubstateLogEntry` (which contains the account ID along with the specified portions of the `wordStack` and `localMem`).

```k
    syntax SubstateLogEntry ::= "{" Int "|" List "|" ByteArray "}" [klabel(logEntry)]
 // ---------------------------------------------------------------------------------
```

Transactions
------------

Productions related to transactions

```k
    syntax TxType ::= ".TxType"
                    | "Legacy"
                    | "AccessList"
                    | "DynamicFee"
 // ------------------------------

    syntax Int ::= #dasmTxPrefix ( TxType ) [function]
 // --------------------------------------------------
    rule #dasmTxPrefix (Legacy)     => 0
    rule #dasmTxPrefix (AccessList) => 1
    rule #dasmTxPrefix (DynamicFee) => 2

    syntax TxType ::= #asmTxPrefix ( Int ) [function]
 // -------------------------------------------------
    rule #asmTxPrefix (0) => Legacy
    rule #asmTxPrefix (1) => AccessList
    rule #asmTxPrefix (2) => DynamicFee

    syntax TxData ::= LegacyTx | AccessListTx | DynamicFeeTx
 // --------------------------------------------------------

    syntax LegacyTx     ::= LegacyTxData         ( nonce: Int, gasPrice: Int, gasLimit: Int, to: Account, value: Int, data: ByteArray )
                          | LegacyProtectedTxData( nonce: Int, gasPrice: Int, gasLimit: Int, to: Account, value: Int, data: ByteArray, chainId: Int )
    syntax AccessListTx ::= AccessListTxData     ( nonce: Int, gasPrice: Int, gasLimit: Int, to: Account, value: Int, data: ByteArray, chainId: Int, accessLists: JSONs )
    syntax DynamicFeeTx ::= DynamicFeeTxData     ( nonce : Int , priorityGasFee : Int       , maxGasFee : Int ,    gasLimit :   Int , to : Account
                                                 , value : Int , data :           ByteArray , chainId   : Int , accessLists : JSONs
                                                 )
 // ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

endmodule
```
