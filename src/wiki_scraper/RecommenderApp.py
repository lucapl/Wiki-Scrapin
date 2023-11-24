import argparse
import re
import os

from src.wiki_scraper.functions.recommender import *
from src.wiki_scraper.functions.explainer import *
from src.wiki_scraper.functions.utils import read_csv

class RecommenderApp:

    def __init__(self):

        self.parser = argparse.ArgumentParser(
            prog='Wikipedia Article Recommender',
            description='Recommends articles from the database',
            epilog='Wiki scraping')
        self.parser.add_argument("articles",
                                 action="extend",
                                 help="articles urls to query",
                                 nargs="+",
                                 type=str)
        self.parser.add_argument("-n","--number_of_recommendations",
                                 help="number of articles to recommend per query",
                                 default=3,
                                 type=int)
        self.parser.add_argument("-v", "--verbose",
                                 action="store_true",
                                 help="be more verbose")
        self.parser.add_argument("-d","--data",
                                 help = "database to read from",
                                 default=".\\data\\articles.csv")
        self.parser.add_argument("-e","--explain",
                                 action="store_true",
                                 help = "show graph that explains the decision")

    def launch(self):
        args = self.parser.parse_args()

        data = read_csv(args.data)

        df,tfidf = fit_articles(data)

        recommendations = recommend_articles(df,tfidf,args.articles,args.number_of_recommendations)

        for query,recommends in recommendations.items():
            print("Query:",query)
            print("Recommended article:\tScore:")
            print(recommends)
            print()

        if args.explain:
            explain(df,tfidf,recommendations)

        return 0