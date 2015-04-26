__author__ = 'extradikke'
import os

with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles_processed_pruned2.txt",
          mode='r') as f:
    counter = 0
    max_length = 0
    longest_line = ""
    for line in f:
        # print(line)
        counter += 1
        if max_length < len(line):
            max_length = len(line)
            longest_line = line
        if counter % 20000 == 0:
            print("Progress:", counter)
    print(max_length)
    print(longest_line)