__author__ = 'extradikke'
import time
with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/dataMaps/wiki_in_numbers.txt", mode='r') as wiki_in_numbers:
    wiki = dict()
    start = time.time()
    for line in wiki_in_numbers:
        items = line.split("|")
        wiki[items[0].strip("\n")] = [int(item.strip("\n")) for item in items[1::]]
    print("Loaded in", time.time()-start, "seconds")
    for index, key in enumerate(wiki):
        print(key, wiki[key])
        if index > 5:
            break