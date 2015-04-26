__author__ = 'extradikke'
import time

with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/articles_processed_pruned3.txt",
          mode="r") as source, open(
        "/media/extradikke/UbuntuData/wikipedia_data/data_dump/dataMaps/article_name_to_number.txt",
        mode="r") as mapping, open(
        "/media/extradikke/UbuntuData/wikipedia_data/data_dump/dataMaps/wiki_in_numbers.txt", mode="w") as entire_wiki:
    start = time.time()
    name_number = {key.strip("\n"): value.strip("\n") for (key, value) in [line.split("|") for line in mapping]}
    print("Time to load mappings", time.time() - start)
    start = time.time()
    for index, line in enumerate(source):
        entries = line.split("|")
        savable = []
        for entry in entries:
            item = entry.strip("\n").lower()
            if item in name_number:
                savable.append(name_number[item])
            else:
                savable.append("0")
        final_savable = "|".join(savable)+"\n"
        entire_wiki.write(final_savable)
        if index % 50000 == 0:
            print(index)


    # for index, key in enumerate(name_number):
    #     print(key, name_number[key])
    #     if index > 5:
    #         break
