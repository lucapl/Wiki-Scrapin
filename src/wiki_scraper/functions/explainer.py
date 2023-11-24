import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from src.wiki_scraper.functions.data_processing import *
from src.wiki_scraper.functions.utils import get_title_and_text

def explain(df,tfidf,recommendation):

    color_palette = [
    'blue', 'green', 'red', 'purple', 'orange',
    'cyan', 'magenta', 'yellow', 'brown', 'pink',
    'lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightgray',
    (0.2, 0.8, 0.4), (0.8, 0.2, 0.4), (0.4, 0.4, 0.8), (0.8, 0.8, 0.2), (0.2, 0.6, 0.8)
    ]

    for url,recommends in recommendation.items():
        _,_,text = get_title_and_text(url)
        q_array = tfidf.transform([" ".join(word_stemmer(text))]).toarray()[0]
        
        full_q_values = pd.Series(q_array, index=df.columns).sort_values()[::-1]
        q_values = full_q_values[:20]
        x,y = q_values.index,q_values
        colors = dict([(a,color_palette[i]) for i,a in enumerate(x)])
        fig, ax = plt.subplots(len(recommends)+1,1,figsize = (10,10))
        fig.tight_layout(pad=5.0)
        ax[0].title.set_text(url)
        ax[0].bar(x,y,
                  color=[colors.get(color,"gray") for color in x])
        ax[0].tick_params(labelrotation=45)
        for i in range(0,len(recommends)):
            r_url = recommends.index[i]
            #values = df.loc[r_url,full_q_values.index][:20]
            values = df.loc[r_url].sort_values()[::-1][:20]
            x,y = values.index,values
            ax[i+1].bar(x,y,
                        color=[colors.get(color,"gray") for color in x])
            ax[i+1].tick_params(labelrotation=45)
            ax[i+1].title.set_text(r_url)
        plt.show()
