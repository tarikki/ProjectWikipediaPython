__author__ = 'extradikke'
import re
import os


def filter_colon(link):
    global wikipedia_counter
    if link.startswith(":"):
        colon_counter += 1
        return False
    return True


if __name__ == '__main__':
    with open(
            "/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles_processed_pruned2.txt",
            mode="r") as source:

        counter = 0
        wikipedia_counter = 0
        for line in source:
            counter += 1
            if counter % 50000 == 0:
                print(counter)
            links = line.split("---")
            for link in links:
                if link.startswith(":"):
                    print(link)




                    # for link in links[1::]:
                    # if link.startswith(":"):
                    # print(links[0], link)
                    # break
                    # if colon_counter > 10:
                    # break
                    # colon_counter +=1


