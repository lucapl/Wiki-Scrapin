from src.wiki_scraper.functions.utils import *
from src.wiki_scraper.functions.data_processing import *
from scipy.spatial.distance import cosine
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def fit_articles(articles):
    urls = [row[0] for row in articles]
    text = [" ".join(row[1:]) for row in articles]
    tfidf = TfidfVectorizer(use_idf=True, smooth_idf=False)
    df = pd.DataFrame(tfidf.fit_transform(text).toarray(),index=urls,columns=tfidf.get_feature_names_out())
    return df,tfidf


def recommend_articles(df,tfidf,queries,n=3):
    recommended = {}
    q_arrays = []

    for query in queries:
        _,url,text = get_title_and_text(query)
        q_stem = " ".join(word_lemmatizer(text))
        q_array = tfidf.transform([q_stem]).toarray()[0]
        q_arrays.append(q_array)
        values = (1-df.apply(lambda x: cosine(x, q_array), axis=1).sort_values())
        recommended[query] = (values[:n])

    return recommended