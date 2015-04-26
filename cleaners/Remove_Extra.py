__author__ = 'extradikke'
import re
import os


def filter_colon(link):
    global colon_counter
    if link.startswith(":"):
        colon_counter += 1
        return False
    return True


if __name__ == '__main__':
    with open(
            "/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles_processed_pruned.txt",
            mode="r") as source, open(
            "/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles_processed_pruned2.txt",
            mode="w") as destination:

        counter = 0
        good_counter = 0
        for line in source:
            counter += 1
            if not line.startswith("Wikipedia:"):
                destination.write(line)

            if counter % 50000 == 0:
                print(counter, counter - good_counter)


                # links = line.split("---")
                #
                # pruned_links = []
                # pruned_links.append(links[0])
                # pruned_links.extend([link for link in links if filter_colon(link)])
                # final_pruned = "---".join(pruned_links)
                # destination.write(final_pruned)



                # for link in links[1::]:
                # if link.startswith(":"):
                # print(links[0], link)
                # break
                # if colon_counter > 10:
                # break
                # colon_counter +=1


