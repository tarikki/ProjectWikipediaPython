__author__ = 'extradikke'

with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/articles_processed_pruned3.txt",
          mode='r') as file, open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/dataMaps/article_name_to_number.txt", mode='w') as destination:
    article_names = []
    count = 0
    for line in file:
        name = line.split("|")[0].strip("\n").lower()
        count += 1
        article_names.append(name)
        if count % 50000 == 0:
            print("%dM %d articles done" % (divmod(count, 100000)))
    article_names.sort()
    name_counter = 1
    name_and_number = []
    for name in article_names:
        mapping = name.strip("\n") + "|" + str(name_counter) + "\n"
        name_and_number.append(mapping)
        destination.write(mapping)
        name_counter += 1

    for x in range(len(name_and_number) - 1, len(name_and_number) - 100, -1):
        print(x, article_names[x])

