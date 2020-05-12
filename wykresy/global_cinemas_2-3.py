import random

from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

sns.set()

# stan na rok 2018

plt.ylabel('Ekrany')
#plt.title('Liczba ekranów kinowych na całym świecie w latach 2011-2018')

number_of_digital_screens = (63825, 89342, 111329, 127466, 142359, 155320, 169198, 182019)
bars = ('2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018')
number_of_analog_screens = (61056, 40123, 22779, 14526, 11092, 8859, 2481, 4840)

def autolabel(rects, higher=False, rects2=None):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect_num in range(len(rects)):
        if higher and rects2:
            height = rects[rect_num].get_height() + rects2[rect_num].get_height()
        else:
            height = rects[rect_num].get_height()
        plt.annotate('{}'.format(rects[rect_num].get_height()),
                    xy=(rects[rect_num].get_x() + rects[rect_num].get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')



y_pos = np.arange(len(bars))

# Create bars
p1 = plt.bar(x=y_pos, height=number_of_analog_screens, color='orange')
p2 = plt.bar(x=y_pos, height=number_of_digital_screens, color='green', bottom=number_of_analog_screens)
print(p1[0].get_height())
autolabel(p1)
autolabel(p2, higher=True, rects2=p1)

plt.legend(['Ekrany analogowe', 'Ekrany cyfrowe'])

# Create names on the x-axis
plt.xticks(y_pos, bars)

x = range(13)
y = [random.randrange(100) for _ in range(13)]

# Show graphic
plt.show()