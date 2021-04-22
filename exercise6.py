import nltk
nltk.download('wordnet')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()  # used to lemmatize words.

documents = ['Wage conflict in retail business grows',
			 'Higher wages for cafeteria employees',
			 'Retailing Wage Dispute Expands',
			 'Train Crash Near Petershausen',
			 'Five Deaths in Crash of Police Helicopter']

def process_text(text):
    tokens = word_tokenize(text.lower())
    stopWords = set(stopwords.words('english'))
    return [lemmatizer.lemmatize(x) for x in tokens if x not in stopWords]


xx = [process_text(doc) for doc in documents]

uniquewords = set([item for sublist in xx for item in sublist])

#make a dictionary of dictionaries
a = dict()
for i,doc in enumerate(documents):
		a[i] = dict.fromkeys(uniquewords, 0)

for i,doc in enumerate(xx):
	for tok in doc:
		a[i][tok] = a[i][tok] + 1

MATRIX = 5 * 19

####################################################################################
#2.2

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
counts = X.toarray()  # Get the doc-term count matrix
dt = counts > 0       # Convert to a binary matrix
doc_term_mat = dt * 1 # If you prefer, represent as 1s and 0s

####################################################################################
#3.1

import numpy as np
words = vectorizer.get_feature_names()
query = ["retail, wages"]

vecquery = vectorizer.transform(query).toarray()