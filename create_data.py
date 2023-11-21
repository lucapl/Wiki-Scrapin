from _utils import *
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

texts = []
titles = []
for _ in range(100):
    title,text = get_title_and_text()
    titles.append(title)
    texts.append(" ".join(word_stemmer(text)))

tfidf=TfidfVectorizer(use_idf=True, smooth_idf=False)

df = pd.DataFrame(tfidf.fit_transform(texts).toarray(), index=titles, columns=tfidf.get_feature_names_out())
df.to_csv(".\\data\\articles.csv")