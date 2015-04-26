__author__ = 'extradikke'


def colon_test(link):
    if "[" in link or "]" in link:
        # if "[" in link or "]" in link:
        # if link.startswith(":"):
        return 1
    else:
        return 0


def link_contains(list_of_links, text):
    for item in list_of_links:
        if text in link:
        # if "[" in link or "]" in link:
        # if link.startswith(":"):
            return 1
        else:
            return 0


def start_counter(line):
    if line.startswith("Wikipedia:"):
        print(line)
        return 1
    else:
        return 0


def start_counter_2(line, start):
    if line.startswith(start):
        return 1
    else:
        return 0


with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/articles_processed_pruned3.txt",
          mode="r") as source:
    counter = 0
    counter2 = 1
    for line in source:


        # if "[" in line or "]" in line:
        # print(line)
        links = line.split("|")
        for link in links:
            counter += 1
            counter2 += link_contains()
            if counter % 500000 == 0:
                print(counter, counter2)
                break
print(counter, counter2, 100 * counter2 / counter)
