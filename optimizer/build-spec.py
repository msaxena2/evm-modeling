#!/usr/bin/env python3

import pyk
import sys

json_defn        = sys.argv[1]
opcode           = pyk.KToken(sys.argv[2], 'OpCode')
wordstack_number = sys.argv[3]
json_out         = sys.argv[4]

kevm_json = pyk.readKastTerm(json_defn)
kevm_symbols = pyk.buildSymbolTable(kevm_json)
kevm_symbols [ '...'                                           ] = lambda l: l + ' ...'
kevm_symbols [ '_andBool_'                                     ] = lambda b1, b2: b1 + '\nandBool ' + b2
kevm_symbols [ '_+Int_'                                        ] = lambda i1, i2: '( ' + i1 + ' +Int ' + i2 + ' )'
kevm_symbols [ '_*Int_'                                        ] = lambda i1, i2: '( ' + i1 + ' *Int ' + i2 + ' )'
kevm_symbols [ '_-Int_'                                        ] = lambda i1, i2: '( ' + i1 + ' -Int ' + i2 + ' )'
kevm_symbols [ 'infGas'                                        ] = lambda g: '#gas( ' + g + ' )'
kevm_symbols [ 'parens'                                        ] = lambda p: '( ' + p + ' )'
kevm_symbols [ '_[_:=_]_EVM-TYPES_WordStack_WordStack_Int_Int' ] = lambda ws, i, w: '( ' + ws + ' [ ' + i + ' := ' + w + ' ] )'
printKEVM = lambda term: pyk.prettyPrintKast(term, kevm_symbols)

rdots    = lambda l: pyk.KApply('...', [l])
leqInt   = lambda i1, i2: pyk.KApply('_<=Int_', [i1, i2])
plusInt  = lambda i1, i2: pyk.KApply('_+Int_' , [i1, i2])
mulInt   = lambda i1, i2: pyk.KApply('_*Int_' , [i1, i2])
minusInt = lambda i1, i2: pyk.KApply('_-Int_' , [i1, i2])

empt_word = pyk.KConstant('.WordStack_EVM-TYPES_WordStack')
cons_word = lambda w, ws: pyk.KApply('_:__EVM-TYPES_WordStack_Int_WordStack', [w, ws])

infGas = lambda g: pyk.KApply('infGas', [g])

sizeWordStack    = lambda     ws: pyk.KApply('#sizeWordStack(_)_EVM-TYPES_Int_WordStack', [ws])
stackNeeded      = lambda op    : pyk.KApply('#stackNeeded(_)_EVM_Int_OpCode', [op])
stackOverflow    = lambda op, ws: pyk.KApply('#stackOverflow(_,_)_EVM_Bool_WordStack_OpCode',  [ws, op])
stackUnderflow   = lambda op, ws: pyk.KApply('#stackUnderflow(_,_)_EVM_Bool_WordStack_OpCode', [ws, op])

wordstack_before = pyk.KVariable("WS")
for i in range(int(wordstack_number) - 1, -1, -1):
    wordstack_before = cons_word(pyk.KVariable('W' + str(i)), wordstack_before)

final_state  = pyk.readKastTerm(json_out)
final_config = None
final_cond   = pyk.KToken('true', 'Bool')
for conj in pyk.flattenLabel('#And', final_state):
    if pyk.isKApply(conj) and conj['label'] == '<generatedTop>':
        final_config = conj['args'][0]
    else:
        final_cond = pyk.KApply('_andBool_', [final_cond, pyk.unsafeMlPredToBool(conj)])
if final_config is None:
    print('// [ERROR] Could not extract config/cond: ' + printKEVM(opcode))
(empty_config, final_subst) = pyk.splitConfigFrom(final_config)
final_gas       = final_subst['GAS_CELL']
final_wordstack = final_subst['WORDSTACK_CELL']

vi1 = pyk.KVariable('I1')
vi2 = pyk.KVariable('I2')
vi3 = pyk.KVariable('I3')
vi4 = pyk.KVariable('I4')
gas_assoc_rules = [ (plusInt(plusInt(vi1, vi2), vi3)   , plusInt(vi1, plusInt(vi2, vi3)))    # (X + Y) + Z => X + (Y + Z)
                  , (plusInt(minusInt(vi1, vi2), vi3)  , minusInt(vi1, minusInt(vi2, vi3)))  # (X - Y) + Z => X - (Y - Z)
                  , (minusInt(plusInt(vi1, vi2), vi3)  , plusInt(vi1, minusInt(vi2, vi3)))   # (X + Y) - Z => X + (Y - Z)
                  , (minusInt(minusInt(vi1, vi2), vi3) , minusInt(vi1, plusInt(vi2, vi3)))   # (X - Y) - Z => X - (Y + Z)
                  ]

for i in range(3):
    for r in gas_assoc_rules:
        final_gas = pyk.rewriteAnywhereWith(r, final_gas)
gas_pattern = infGas(minusInt(vi1, vi2))
gas_subst   = pyk.match(gas_pattern, final_gas)
if gas_subst is None:
    print('// [ERROR] Could not extract gas expression: ' + printKEVM(opcode))
    sys.exit(1)
gas_used = gas_subst[vi2['name']]
for i in range(3):
    for rule in [(r, l) for (l, r) in gas_assoc_rules]:
        gas_used = pyk.rewriteAnywhereWith(rule, gas_used)

k_claim = { 'K_CELL'          : rdots(pyk.KRewrite(pyk.KApply('#next[_]_EVM_InternalOp_OpCode', [opcode]), pyk.KConstant('#EmptyK')))
          , 'WORDSTACK_CELL'  : pyk.KRewrite(wordstack_before, final_wordstack)
          , 'GAS_CELL'        : pyk.KRewrite(pyk.KVariable('GAVAIL'), minusInt(pyk.KVariable('GAVAIL'), gas_used))
          , 'LOCALMEM_CELL'   : pyk.KRewrite(pyk.KVariable('LM'), final_subst['LOCALMEM_CELL'])
          , 'PC_CELL'         : pyk.KRewrite(pyk.KVariable('PCOUNT'), final_subst['PC_CELL'])
          , 'SCHEDULE_CELL'   : pyk.KRewrite(pyk.KVariable('SCHED'), final_subst['SCHEDULE_CELL'])
          , 'MEMORYUSED_CELL' : pyk.KRewrite(pyk.KVariable('MU'), final_subst['MEMORYUSED_CELL'])
          , 'PROGRAM_CELL'    : pyk.KVariable('PGM')
          }

requires_clauses = [ leqInt(gas_used, pyk.KVariable('GAVAIL'))
                   , leqInt(sizeWordStack(final_wordstack) , pyk.KToken('1024', 'Int'))
                   ]
claim_requires = pyk.KToken('true', 'Bool')
for r in sys.argv[5:]:
    claim_requires = pyk.KApply('_andBool_', [claim_requires, pyk.KToken(r, 'Bool')])
for r in requires_clauses:
    claim_requires = pyk.KApply('_andBool_', [claim_requires, pyk.KApply('parens', [r])])
claim_requires = pyk.simplifyBool(claim_requires)

claim_body = pyk.pushDownRewrites(pyk.substitute(empty_config, k_claim))
new_claim  = pyk.minimizeRule(pyk.KClaim(claim_body, requires = claim_requires))

print(printKEVM(new_claim))
