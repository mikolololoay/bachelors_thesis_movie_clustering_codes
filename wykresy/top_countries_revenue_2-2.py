import random

from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

sns.set()

# stan na rok 2018

countries_dict = {'USA/Kanada': 11.9,
                  'Chiny': 9.0,
                  'Japonia': 2.0,
                  'Wielka Brytania': 1.7,
                  'Korea Południowa': 1.6,
                  'Francja': 1.6,
                  'Indie': 1.5,
                  'Niemcy': 1.0,
                  'Pozostałe państwa': 10.8}

plt.pie(x = countries_dict.values(),
        labels = countries_dict.keys(),
        shadow=False, startangle=90, autopct='%1.0f%%', pctdistance=0.85, labeldistance=1.1)

plt.axis('equal')
plt.show()
