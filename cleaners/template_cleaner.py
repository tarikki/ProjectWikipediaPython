__author__ = 'extradikke'

with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles_processed_pruned4.txt",
          mode='r') as file, open(
        "/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles_processed_pruned5.txt",
        mode="w") as destination:
    good_articles = 0
    total = 9228239
    count = 0
    for line in file:
        name = line.split("---")[0]
        if not name.startswith("Template:"):
            destination.write(line)
            good_articles +=1
        count +=1
        if count % 50000 == 0:
            print("%0.2f percent complete" % (100*count/total))
    print("%f percent templates" % (100*(count-good_articles)/count))
    print((count-good_articles), count)
