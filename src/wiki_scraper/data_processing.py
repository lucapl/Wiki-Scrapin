from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def word_cutter(string,method):
    stops = stopwords.words('english')
    return list(filter(lambda s: not s in stops,map(method,word_tokenize(string))))

def word_stemmer(string):
    return word_cutter(string,LancasterStemmer().stem)

def word_lemmatizer(string):
    return word_cutter(string,WordNetLemmatizer().lemmatize)