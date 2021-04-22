import nltk
nltk.download('inaugural')
nltk.download('averaged_perceptron_tagger')
from collections import Counter
from nltk.corpus import inaugural
import spacy
nlp = spacy.load('en_core_web_sm')

#longest sentence
xx = inaugural.fileids()

sents = inaugural.sents('1961-Kennedy.txt')

longest_sents = [(speech, max(inaugural.sents(speech), key=len)) for speech in inaugural.fileids()]

longest = max(longest_sents, key = lambda item: len(item[1]))


#pos distribution
postags = nltk.pos_tag(longest[1])
res = Counter(postags)
res.most_common(3)

#spacy entities
strin = "President Obama said to reporters from the Washington Post that the Federal Reserve had overstepped in its decision to decrease the margins on inter-bank loans last Wednesday"

out  = nlp(strin).ents

strin2 = "Obama said to reporters from the Washington Post that the Federal Reserve had overstepped in its decision to decrease the margins on inter-bank loans last Wednesday"

out2  = nlp(strin2).ents
