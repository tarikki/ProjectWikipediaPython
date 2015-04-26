import time

__author__ = 'extradikke'

start = time.time()
with open("/media/extradikke/UbuntuData/wikipedia_data/january/pagecounts-2014-01-01", "r", encoding='utf-8',
          errors='ignore') as bigAssFile:
    with open("/media/extradikke/UbuntuData/wikipedia_data/january/pagecounts-2014-01-01-english", "w", encoding='utf-8') as saveHere:
        # everything = [line.strip().split('\n') for line in f]
        # print(everything[0:5])
        # print(len(everything))
        counter = 0
        english_pages = 0
        english_hits = dict()
        for line in bigAssFile:

            # print(elements)
            counter += 1
            if counter % 10000 == 0:
                print(counter)
            line_beginning = line[0:4]
            if line_beginning.lower() == 'en.z':
                reducted = line[5::]
                if not "upload.wikimedia.org" in reducted:
                    saveHere.write(reducted)
                    english_pages +=1
                    if line_beginning in english_hits:
                        hits = english_hits.get(line_beginning)
                        english_hits[line_beginning] = hits + 1
                    else:
                        english_hits[line_beginning] = 1
        print(counter)
        print(time.time() - start)
        print("English pages", english_pages)
        for element in english_hits:
            print(element, english_hits.get(element))
            # if counter > 50:
            #     break

            # if line.startswith('en.z'):
            #     counter += 1
            #     print(line)
            #     if counter > 100:
            #         break