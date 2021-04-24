import nltk
import sklearn

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

doc_matrix_1 = []
for i, doc in enumerate(a):
	temp = [y for (x,y) in sorted(a[i].items(), key= lambda x: x[0])]
	doc_matrix_1.append(temp)

####################################################################################
#2.2
class LemmaAndTokenizer(object):
    def __init__(self):
        lemmatizer = WordNetLemmatizer()

    def __call__(self, articles):
		lemmatizer = WordNetLemmatizer()
		tokens = word_tokenize(articles.lower())
		return [lemmatizer.lemmatize(x) for x in tokens]

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(lowercase=True, stop_words="english", tokenizer=LemmaAndTokenizer())
X = vectorizer.fit_transform(documents)
counts = X.toarray()  # Get the doc-term count matrix
dt = counts > 0       # Convert to a binary matrix
doc_term_mat = dt * 1 # If you prefer, represent as 1s and 0s

stop_words = sklearn.feature_extraction.text.ENGLISH_STOP_WORDS
####################################################################################
#3.1

import numpy as np
words = vectorizer.get_feature_names()
query = ["retail wages"]

vecquery = vectorizer.transform(query).toarray()
res = vecquery.dot(doc_term_mat.T)
res_norm = res / np.sum(doc_term_mat, axis=1)

#result normalized === array([[0.4 , 0.25, 0.25, 0.  , 0.  ]])


####################################################################################
#3.2

from sklearn.feature_extraction.text import TfidfVectorizer

vecIdf = TfidfVectorizer(lowercase=True, stop_words="english", tokenizer=LemmaAndTokenizer())
X = vecIdf.fit_transform(documents)
counts = X.toarray()

idfquery = vecIdf.transform(query).toarray()

res2 = idfquery.dot(counts.T)

#### results = array([[0.570629  , 0.20067738, 0.20067738, 0.        , 0.        ]])

####################################################################################
#4.1

from sklearn.metrics.pairwise import cosine_similarity

for i,doc in enumerate(counts):
	print("DOC", i)
	for doc1 in counts:
		print(cosine_similarity(doc.reshape(1,-1),doc1.reshape(1,-1)))

####################################################################################
#4.2

new_docs = [
    'Plane crash in Baden-Wuerttemberg',      # Doc 4a
	'The weather'                             # Doc 4b
]

new_X = vecIdf.transform(new_docs).toarray()
for i,doc in enumerate(counts):
	print(cosine_similarity(doc.reshape(1, -1), new_X[0].reshape(1,-1)))