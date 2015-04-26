__author__ = 'extradikke'

with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/dataMaps/article_name_to_number.txt") as bigFile, open(
        "/media/extradikke/UbuntuData/wikipedia_data/data_dump/articles_processed_pruned3.txt",
        mode='r') as articles:
    names_to_numbers = dict()
    for line in bigFile:
        items = line.split("|")
        names_to_numbers[items[0]] = items[1]
    links = 0
    orphans = 0
    for index, line in enumerate(articles):
        items = line.split("|")[1::]
        for item in items:
            links += 1
            if item.lower() not in names_to_numbers:
                print(item)
                orphans += 1
            if orphans % 500 == 0:
                break
                print(links, orphans, 100*orphans/links)
        print(links, orphans, 100*orphans/links)


