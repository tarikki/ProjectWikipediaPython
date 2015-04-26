__author__ = 'extradikke'


with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml", mode='r') as big_file:
    counter = 0
    for line in big_file:
        print(line)
        counter +=1
        if counter > 1000:
            break