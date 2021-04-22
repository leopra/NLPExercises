# 6 EVALUATE LANGUAGE MODEL
import nltk
import pickle
nltk.download('treebank')
from nltk.corpus import treebank

model2 = pickle.load(open("modelsaved.pkl", "rb"))
# Remove tags from sentences: we just want to use it as a LM over the words
# The model will sum over possible tags
unlabelled_test_set = [(t[0], None) for s in treebank.tagged_sents() for t in s]

#convert text to sentences
converted = []
sent = []
for x in unlabelled_test_set:
    if x[0] == '.':
        sent.append(x)
        converted.append(sent)
        sent = []
    else:
        sent.append(x)

res = []
#get perplexities for first 4 sentences
for sent in converted[:4]:
    val = model2.log_probability(sent)
    res.append(pow(2, -1/len(sent)*val))