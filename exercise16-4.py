import nltk
nltk.download('wordnet')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

strings = "Radio is the technology of signaling and communicating using radio waves. \
Radio waves are used to carry information across space from a transmitter to a receiver, by modulating the radio signal. \
The artificial generation and use of radio waves is strictly regulated by law. \
The purpose of most transmitters is radio communication of information. \
The amplitude of the carrier signal is varied with the amplitude of the modulating signal. \
State-enforced laws can be made by a group legislature. \
The creation of laws themselves may be influenced by a constitution. \
The constitution has supremacy over ordinary statutory law. \
Records are information produced consciously or as by-products."

def process_text(text):
    tokens = word_tokenize(text.lower())
    stopWords = set(stopwords.words('english'))
    return [x for x in tokens if x not in stopWords]

xx = process_text(strings)

dictio = dict([(x, dict()) for x in set(xx)])

