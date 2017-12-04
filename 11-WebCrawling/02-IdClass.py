import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("http://www.imdb.com/chart/top")

soup = bs.BeautifulSoup(sauce, 'lxml')

titleColumn = soup.find_all(class_ = 'titleColumn')
ratingColumn = soup.find_all(class_ = 'ratingColumn')
for d in titleColumn:
    print(d.text)
