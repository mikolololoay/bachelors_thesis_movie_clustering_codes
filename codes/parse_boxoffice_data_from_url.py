'''
wczytujemy dataframe, który był outputem pliku "urls_parser.py"
dla każdego url wczytujemy tabele i zapisujemy je wszystkie jako plik .pickle.

-----------------------------------------------------------------------------------
OPIS TABEL:
    jest 17 tabel
    [0] ogólne dane ; total earnings
    [1] statystyki takie jak legs, opening weekend, production budget, czy film zarobił, domestic BO inflation adjusted
    [2] miejsce na ważnych rankingach w the-numbers.com
    [3] informacje o gatunkach, długości, franchise, dacie premiery, języku
    [4] pomniejsze rekordy
    [5] główni aktorzy (mało - do star wars tylko driver, ridley i boyega)
    [6] cała obsada chyba
    [7] wszyscy twórcy np abrams, kasdan itp
    [8] pozycje na różnych rankingach domestic
    [9] tygodniowy boxoffice domestic
    [10] MOJA GŁÓWNA TABELA - DZIENNY BOXOFFICE
    [11] tygodniowy boxoffice global
    [12] statystyki dla państw
    [13] miejsca w rankingach international
    [14] miejsca w rankingach worldwide
    [15] tygodniowe ale nie w dolarach tylko w unitsthisWeek (co to jest?); spendingthisWeek, TotalSpending; domstic
    [16] to samo co [15] ale chyba worldwide
    -------------------------------------------------------------------------------
'''
import pandas as pd
from lxml import html
import requests
import numpy as np
from random import randint
from time import sleep
import os
import pickle


def get_dataframes_from_url(movie_url):
    movie_page = requests.get(movie_url)
    movie_dataframes_list = pd.read_html(movie_page.content)
    return movie_dataframes_list

def create_movie_folder(title):
    foldername = title.replace('.','').replace(' ', '_').replace(':','').replace("'",'')
    folder_path = f'raw_data/boxoffice_data/{foldername}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def pickle_dataframes_list(movie_dataframes_list, folder_path):
    with open(folder_path+'/boxoffice_dataframes_list.pickle', 'wb') as f:
        pickle.dump(movie_dataframes_list, f)

df_with_urls = pd.read_csv('raw_data/movie_urls_df.csv')
    

for index, row in df_with_urls.iterrows():
    sleep(randint(4,8))
    movie_url = row['url']
    movie_dataframes_list = get_dataframes_from_url(movie_url)
    title = row['Movie']
    folder_path = create_movie_folder(title)
    pickle_dataframes_list(movie_dataframes_list, folder_path)
    print(index)


    

    

    