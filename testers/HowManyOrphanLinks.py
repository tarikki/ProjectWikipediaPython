__author__ = 'extradikke'

with open("/media/extradikke/UbuntuData/wikipedia_data/wikidump_processed/articles_to_numbers.txt",
          mode='r') as bigFile, open(
        "/media/extradikke/FastFiles/wikidata/articles_processed_no_redirects.txt",
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
                # print(item)
                orphans += 1
            if orphans % 50000 == 0:
                print(links, orphans, 100 * orphans / links)
        print("Total links: %d, orphans: %d, percentage: %.2f" % (links, orphans, 100 * orphans / links))


