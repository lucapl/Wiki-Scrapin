import requests
import bs4
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

WIKIPEDIA_RANDOM = 'https://en.wikipedia.org/wiki/Special:Random'

def get_title_and_text(url=WIKIPEDIA_RANDOM):
    response = requests.get(url)
    parsed = bs4.BeautifulSoup(response.text)
    output = ""
    for p in parsed.select('p'):
        output += p.getText()
    return parsed.title.string,output

def word_stemmer(string):
    stops = stopwords.words('english')
    return list(filter(lambda s: not s in stops,map(WordNetLemmatizer().lemmatize,word_tokenize(string))))