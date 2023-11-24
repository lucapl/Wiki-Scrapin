from wiki_scraper.utils import *
from scipy.spatial.distance import cosine


def recommend_articles(df,tfidf,queries,n=3):
    recommended = {}
    q_arrays = []

    for query in queries:
        _,url,text = get_title_and_text(query)
        q_stem = " ".join(word_stemmer(text))
        q_array = tfidf.transform([q_stem]).toarray()[0]
        q_arrays.append(q_array)
        values = (1-df.apply(lambda x: cosine(x, q_array), axis=1).sort_values())
        recommended[query] = (values[:n])

    return recommended