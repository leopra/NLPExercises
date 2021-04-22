import nltk
nltk.download("masc_tagged")

from nltk.corpus import masc_tagged
print(masc_tagged.tagged_sents()[0])
print(masc_tagged.tagged_sents()[1])


#Submit the computed p(tag[i+1] = DT | tag[i] = VB) - the probability of a verb being followed by a determiner.
vbdict = {'END': 0}
count = 0

for sent in masc_tagged.tagged_sents():
    #iterate in all except the last one
    for idx,pair in enumerate(sent[:-1]):
        if pair[1] == "VB":
            nextpos = sent[idx+1]
            if nextpos[1] not in vbdict.keys():
                vbdict[nextpos[1]] = 1
            else:
                vbdict[nextpos[1]] = vbdict[nextpos[1]] + 1
            count += 1
    #special case VB is the last tag of sentence
    if sent[-1][1] == 'VB':
        vbdict['END'] = vbdict['END'] + 1
        count += 1


ptagDTafterVB = vbdict['DT'] / count

#######################
#Submit the computed p(word[i] = 'feel' | tag[i] = VB).
vbdict = {}
count = 0

for sent in masc_tagged.tagged_sents():
    #iterate in all except the last one
    for pair in sent:
        if pair[1] == "VB":
            word = pair[0]
            if word not in vbdict.keys():
                vbdict[word] = 1
            else:
                vbdict[word] = vbdict[word] + 1
            count += 1

pwordIfVB = vbdict['feel'] / count


###################################
# train hinner markov model

from nltk.tag import hmm

trainer = hmm.HiddenMarkovModelTrainer()

model = trainer.train_supervised(masc_tagged.tagged_sents())

model.tag('Once we have finished , we will go out .'.split())
model.tag('There is always room for more understanding between warring peoples .'.split())
model.tag('Evidently , this was one of Jud \'s choicest tapestries , for the noble emitted a howl of grief and rage and leaped from his divan .'.split())

model.tag('Misjoggle in a gripty hifnipork .'.split())
model.tag('One fretigy kriptog is always better than several intersplicks .'.split())

####################################
# train unsupervised
import pickle
import dill
import w3utils as w3

with open("radio_planet_tokens.txt") as f:
    nsvdata = f.readlines()

tokendata = [x.split() for x in nsvdata]
model2 = w3.train_unsupervised(masc_tagged.tagged_sents(), tokendata)

model2.tag('Yesterday these fiends operated upon Doggo .'.split())
model2.tag('For a time, his own soul and this brain - maggot struggled for supremacy .'.split())

pickle.dump(model, open("easymodelsaved.pkl", 'wb'))

model2 = pickle.load(open("modelsaved.pkl", "rb"))


#############################################
# Language Model HMM
sent = [("I", None), ("Love", None), ("Potatoes", None)]
fake_sentence = [("Eat", None), ("roof", None), ("forever", None), ("then", None), ("run", None)]

real_sentence = [("The", None), ("President", None), ("gave", None), ("a", None), ("speech", None)]
model.log_probability(fake_sentence)

######################################################
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