from _utils import *
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import sys
from joblib import dump


def main(argv):

    texts = []
    titles = []
    urls = []
    for _ in range(int(argv[1])):
        while True:
            title,url,text = get_title_and_text()
            if len(text) != 0:
                break
            print(f"Article {url} contains no interesting text, getting another...S")
        
        titles.append(title)
        urls.append(url)
        print(f"Adding article: {title}...")
        texts.append(" ".join(word_stemmer(text)))

    tfidf=TfidfVectorizer(use_idf=True, smooth_idf=False)

    print("Transforming the data")
    df = pd.DataFrame(tfidf.fit_transform(texts).toarray(), index=urls, columns=tfidf.get_feature_names_out())

    output = ".\\data\\articles.csv"
    model_output = ".\\model\\tfidf_model.joblib"
    print("Saved the data to",output)
    df.to_csv(output)
    print("Saved model to:",model_output)
    dump(tfidf,model_output)
    
    return 0

if __name__ == '__main__':
    main(sys.argv)