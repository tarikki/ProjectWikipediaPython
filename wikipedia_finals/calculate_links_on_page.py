__author__ = 'extradikke'
import bs4

with open("/media/extradikke/UbuntuData/programming/python/wikipediaCheckOut/wikipedia_finals/letter_a.html") as file:
    soup = bs4.BeautifulSoup(file)
    result = [x for x in soup.find_all('a', href=True)]

    counter = 0
    for tuub in result:
        if tuub['href']:
            print(tuub['href'])
    print(len(result))
    print(len(set(result)))