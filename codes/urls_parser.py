import pandas as pd
from lxml import html
import requests
from random import randint
from time import sleep
import os
from lxml.etree import XPathEvalError


'''
Tutaj pobieram tytuły wszystkich filmów z top 500 z rankingu All Time Domestic Inflation Adjusted Box Office
Następnie filtruję je tak, by zostały tylko filmy z XXI wieku. (Ponieważ stare filmy często nie mają kompletnej rubryki DAILY BOX OFFICE)
Wyszukuję url do każdego z otrzymanych tytułów, dodaję je do dataframe i zapisuję do pliku.
'''


def read_ranking_url_into_df(page, tree):
    tree_read_html = pd.read_html(page.content)
    df = tree_read_html[0]
    df = df[df['Released']>2000].reset_index(drop=True)
    return df

def add_movies_urls_to_df(df, page, tree):
    list_of_movie_urls = []
    page_string = page.content.decode('utf-8').replace('&hellip;', '…')
    for title in df['Movie']:
        if title not in page_string:
            print(title + 'not in page_string')
            list_of_movie_urls.append(' movie title not found')
        else:
            try:
                if title == '2012':
                    movie_url = 'https://www.the-numbers.com/movie/2012#tab=summary'
                else:
                    movie_url = "https://www.the-numbers.com" + tree.xpath(f"//table//a[text()='{title}']/@href")[0].replace('#tab=box-office', '#tab=summary')
            except XPathEvalError:
                if title == "Ocean's Eleven":
                    movie_url = 'https://www.the-numbers.com/movie/Oceans-Eleven#tab=box-office'
                elif title == "Madagascar 3: Europe's Most Wanted":
                    movie_url = 'https://www.the-numbers.com/movie/Madagascar-3#tab=box-office'
                elif title == "Doctor Seuss' The Lorax":
                    movie_url = 'https://www.the-numbers.com/movie/Lorax-The#tab=box-office'
                else:
                    print(title + ' XPathEvalError')
                    exit()
            list_of_movie_urls.append(movie_url)

    df['url'] = list_of_movie_urls
    return df
            

list_of_urls_with_rankings = ['https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time-inflation-adjusted',
    'https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time-inflation-adjusted/101',
    'https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time-inflation-adjusted/201',
    'https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time-inflation-adjusted/301',
    'https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time-inflation-adjusted/401'
    ]

df_global = pd.DataFrame()

for url in list_of_urls_with_rankings:
    sleep(randint(4,8))
    print('mi sono svegliato')
    page = requests.get(url)
    tree = html.fromstring(page.content)
    df = read_ranking_url_into_df(page, tree)
    df = add_movies_urls_to_df(df, page, tree)
    df_global = df_global.append(df).reset_index(drop=True)

df_global.to_csv('raw_data/movie_urls_df.csv')
    
