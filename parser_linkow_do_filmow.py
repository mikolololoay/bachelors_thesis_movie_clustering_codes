# ten skrypt bierze linki wszystkich filmow z rankingu na tej stronie

from lxml import html
import requests


page = requests.get('https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time')
tree = html.fromstring(page.content)

print(page.text)