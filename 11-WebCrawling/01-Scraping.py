import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("http://www.imdb.com/chart/top")

soup = bs.BeautifulSoup(sauce, 'lxml')

# data = soup.find('p')
data = soup.find_all('p')
# print(data)
for d in data:
    print(d.text)
