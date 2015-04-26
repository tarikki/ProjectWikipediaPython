__author__ = 'extradikke'
import re
import os


def filter_colon(link):
    global wikipedia_counter
    if link.startswith(":"):
        colon_counter +=1
        return False
    return True


if __name__ == '__main__':
    with open("/media/extradikke/FastFiles/wikidata/articles_processed.txt",
              mode="r") as source, open(
            "/media/extradikke/UbuntuData/wikipedia_data/data_dump/articles_processed_pruned1.txt",
            mode="w") as destination:
        counter = 0
        wikipedia_counter = 0
        for line in source:
            counter += 1
            if counter % 50000 == 0:
                print(counter, wikipedia_counter)
            links = line.split("|")

            pruned_links = []
            pruned_links.append(links[0])
            pruned_links.extend([link for link in links[1::] if filter_colon(link)])
            final_pruned = "|".join(pruned_links)
            destination.write(final_pruned)



            # for link in links[1::]:
            # if link.startswith(":"):
            #         print(links[0], link)
            #         break
            # if colon_counter > 10:
            # break
            # colon_counter +=1


