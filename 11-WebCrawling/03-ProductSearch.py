import bs4
import urllib.request


userChoice = input("Enter Name of Product : ")

sauce = urllib.request.urlopen("https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+userChoice)

soup = bs4.BeautifulSoup(sauce, 'lxml')

for i in range(5):
    data = soup.find_all('li', id = 'result_'+str(i))
    for d in data:
        print(d.text)
    print("--------------------")
