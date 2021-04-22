import nltk

cfg_rules = """
S -> NP VP
NP -> Det N | PropN
Det -> PosPro | Art
VP -> Vt NP

Art -> 'the' | 'a'
PropN -> 'Alice'
N -> 'duck' | 'telescope' | 'park'
Vt -> 'saw'
PosPro -> 'my' | 'her'
"""
cfg = nltk.CFG.fromstring(cfg_rules)

print(cfg.is_flexible_chomsky_normal_form())

print(cfg.check_coverage("Alice saw the duck".split()))
##########################################################
rules = """
S -> WHADVP SQ STOP | NP VP STOP | PP NP VP STOP
SQ -> VBD NP VP
WHADVP -> WRB
NP -> DT JJ NN | DT NN
VP -> VB | VBD ADVP | VBD RB VP | VBD IN JJ NN
ADVP -> RB
PP -> IN NP | RB

WRB -> 'how'
DT -> 'the'
JJ -> 'blue' | 'past'
NN -> 'dog' | 'past' | 'experience'
VB -> 'fly'
STOP -> '?' | '.'
VBD -> 'flew' | 'did'
RB -> 'past' | 'not' | 'earlier'
IN -> 'in' | 'without'
"""

cfg = nltk.CFG.fromstring(rules)
#print(cfg.is_flexible_chomsky_normal_form()) not CNF

# Check that all the words of the input sentence are covered
sentences = [
    "how did the blue dog fly ?".split(),
    "the blue dog flew past .".split(),
    "in the past the dog did not fly .".split(),
]
for s in sentences:
    cfg.check_coverage(s)

new_sentences = ["earlier the dog did not fly .".split(),
"the dog flew without past experience .".split()]

for s in new_sentences:
    cfg.check_coverage(s)

###########################################################
cnf_grammar = cfg.chomsky_normal_form()

from nltk.parse.chart import BottomUpChartParser

total = sentences + new_sentences

parser = BottomUpChartParser(cnf_grammar)

chart = parser.chart_parse(total[0])
type(chart)
chart.edges()
chart.pretty_format()

parser.parse(total[0]).draw()

def parse(sent):
    a = []
    for tree in parser.parse(sent):
        a.append(tree)
    return (a[0])

for sent in total:
    parses = parser.parse(sent)
    print(len(list(parses)))

othersentencesthatarederived = ["without the past experience the dog fly .".split(),
"the past experience flew without blue dog .".split(),
]

for sent in othersentencesthatarederived:
    print(parse(sent))

##################################################################################
# TREEBANK PARSER

from nltk.corpus import treebank
print(treebank.parsed_sents()[0])
print(treebank.parsed_sents()[1])

productions = []
for sent in treebank.parsed_sents():
    productions = productions + sent.productions()

cfg = nltk.CFG(nltk.Nonterminal("S"), productions)

parser = BottomUpChartParser(cfg)

sentences = ["Mr. Vinken is chairman .".split(),
"Stocks rose .".split(),
"Alan introduced a plan .".split()]

for sent in sentences:
    print(len(list(parser.parse(sent))))


###########################################################à
# PCFG

from nltk import induce_pcfg, InsideChartParser

pcfg = induce_pcfg(nltk.Nonterminal("S"), productions)

parser = InsideChartParser(pcfg, beam_size=900)

sentences = ["Mr. Vinken is chairman .".split(),
"Stocks rose .".split(),
"Alan introduced a plan .".split()]

next(parser.parse(sentences[1])).draw()


###########################################################à
# PCFG
from nltk import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

s = '''man in New York.'''
#Please buy me\ntwo of them.\nThanks.'''

str = tokenizer.tokenize(s)

x  = parser.parse(str)
