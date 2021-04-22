import spacy
nlp = spacy.load('en_core_web_sm')
strin = "President Obama said to reporters from the Washington Post that the Federal Reserve had overstepped in its decision to decrease the margins on inter-bank loans last Wednesday"

out  = nlp(strin).ents

strin2 = "Obama said to reporters from the Washington Post that the Federal Reserve had overstepped in its decision to decrease the margins on inter-bank loans last Wednesday"

out2  = nlp(strin2).ents
