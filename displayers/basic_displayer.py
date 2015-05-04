__author__ = 'extradikke'

with open("/media/extradikke/UbuntuData/wikipedia_data/wikidump_processed/wiki_in_numbers.txt", mode='r') as bigFile:
    for index, line in enumerate(bigFile):
        print(line)
        if index > 5000: break
