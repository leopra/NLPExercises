import nltk
nltk.download('wordnet')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def process_text(text):
    lemmatizer = WordNetLemmatizer() # used to lemmatize words.

    sentences = sent_tokenize(text)

    splitsent = []
    for sent in sentences:
        splitsent.append(word_tokenize(sent))

    pos = []
    for s in splitsent:
        pos.append(pos_tag(s))

    #print(pos)
    lemm = []
    for s in pos:
        lemm.append([(w[0],lemmatizer.lemmatize(w[0]), w[1]) for w in s])

    #print(lemm)
    return lemm


def filter_text(text):
    stopWords = set(stopwords.words('english'))
    print(stopWords)
    out = []
    sentences = process_text(text)
    for s in sentences:
        out.append([x for x in s if x[0] not in stopWords])

    out1 = []
    POSTOREMOVE = ["VB","VBD","VBG","VBN","VBP","VBZ","JJ","JJR","JJS","NN","NNS","NNP","NNPS"]
    for ou in out:
        out1.append([x for x in ou if x[2] not in POSTOREMOVE])


    return out1

#stringa = "I have a dog"
stringa  = "One morning I shot an elephant in my pajamas. How he got into my pajamas I’ll never know."

print(process_text(stringa))



###########################
# 3. spaCy

import spacy # import the spaCy module
nlp = spacy.load("en_core_web_sm") # load the English model

doc = nlp(stringa) # process the text (which is defined in the previous code)

for sent in doc.sents:
  for token in sent: # iterate over every token
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
  print()

for chunk in doc.noun_chunks:
    print(chunk.text)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)