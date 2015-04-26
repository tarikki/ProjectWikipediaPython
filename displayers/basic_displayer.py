__author__ = 'extradikke'

with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/dataMaps/wiki_in_numbers.txt") as bigFile:
    for index, line in enumerate(bigFile):
        print(line)
        if index > 500: break
