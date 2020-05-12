import random

from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

sns.set()
# barplot z globalnymi przychodami w latach 2011 - 2018
# (2011,32.6) (2012,34.7)
# 		 (2013,35.9) (2014,36.4)
# 		 (2015,38.4) (2016,38.8)
# 		 (2017,40.5) (2018,41.1)

plt.ylabel('Przychody w miliardach dolarów')
#plt.title('Globalne przychody kinowe w latach 2011-2018')

def autolabel(rects, higher=False, rects2=None):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect_num in range(len(rects)):
        if higher and rects2:
            height = rects[rect_num].get_height() + rects2[rect_num].get_height()
        else:
            height = rects[rect_num].get_height()
        plt.annotate('{}'.format(height),
                    xy=(rects[rect_num].get_x() + rects[rect_num].get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')



global_revenue_by_year = (32.6, 34.7, 35.9, 36.4, 38.4, 38.8, 40.5, 41.1)
bars = ('2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018')
inflation_rate = (0, 2.07, 3.56, 5.24, 5.37, 6.70, 8.97, 11.69)
global_revenue_real_by_2011 = []

for i in range(len(bars)):
    revenue = global_revenue_by_year[i]
    denominator = 1 + inflation_rate[i]/100
    real_revenue = revenue / denominator
    global_revenue_real_by_2011.append(real_revenue)

print(global_revenue_by_year)
print(global_revenue_real_by_2011)

y_pos = np.arange(len(bars))

# Create bars
p1 = plt.bar(x=y_pos, height=global_revenue_by_year)
autolabel(p1)
# Create names on the x-axis
plt.xticks(y_pos, bars)

x = range(13)
y = [random.randrange(100) for _ in range(13)]

# Show graphic
plt.show()
