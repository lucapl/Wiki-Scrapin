from src.wiki_scraper.functions.utils import *
from src.wiki_scraper.functions.data_processing import *
import sys
import csv


def main(argv):

    texts = []
    titles = []
    urls = []
    for _ in range(int(argv[1])):
        while True:
            title,url,text = get_title_and_text()
            if len(text) > 2000:
                break
            print(f"Article {url} low amount of text, getting another...")
        
        titles.append(title)
        urls.append(url)
        print(f"Adding article: {title}...")
        texts.append(word_lemmatizer(text))

    to_write = tuple(map(lambda row: [row[0]]+row[1],zip(urls,texts)))
    del texts
    del urls

    output = ".\\data\\articles.csv"
    print("Writing the data...")
    save_csv(to_write,output)
    print("Saved the data to",output)

    return 0

if __name__ == '__main__':
    main(sys.argv)