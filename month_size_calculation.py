__author__ = 'extradikke'

import re
with open("/media/extradikke/UbuntuData/programming/python/wikipediaCheckOut/january_files_merged.txt") as f:
    lines = [line.strip('\n').split() for line in f][6:]
    print(lines[:5])

    summ = 0
    for line in lines:
        print(line[3])
        summ += int(line[3])
    print(summ)
    # summ = 0
    # for line in lines:
    #     match = re.match(r'.*size (\d+)M', line)
    #     if match:
    #         summ += int(match.group(1))
    #         print(match.group(1))
    # print(summ)