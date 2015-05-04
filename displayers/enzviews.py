import time

__author__ = 'extradikke'

start = time.time()
with open("/media/extradikke/UbuntuData/wikipedia_data/random/pagecounts-2014-04-24", "r", encoding='utf-8',
          errors='ignore') as bigAssFile:
        counter = 1
        english_pages = 0
        english_hits = dict()
        for line in bigAssFile:

            # print(elements)

            if counter % 10000 == 0:
                print(counter)
            line_beginning = line[0:4]
            if line_beginning == 'En.z' or line_beginning == 'EN.Z' or line_beginning == 'en.Z' or line_beginning == 'EN.z':
                counter += 1
                print(line)
        print(counter)