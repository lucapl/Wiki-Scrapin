import requests
import bs4

import csv

WIKIPEDIA_RANDOM = 'https://en.wikipedia.org/wiki/Special:Random'

def get_title_and_text(url=WIKIPEDIA_RANDOM):
    response = requests.get(url)
    parsed = bs4.BeautifulSoup(response.text,features="lxml")
    output = ""
    for p in parsed.select('p'):
        output += p.getText()
    return parsed.title.string,response.url,output



def save_csv(to_write,output):
    with open(output,"w",encoding='utf-8') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(to_write)

def read_csv(input):
    articles = []
    with open(input,"r",encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) == 0:
                continue
            articles.append(row)
    return articles