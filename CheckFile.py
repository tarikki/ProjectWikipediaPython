__author__ = 'extradikke'
import urllib.parse
with open("/media/extradikke/UbuntuData/wikipedia_data/january/pagecounts-2014-01-01-english", "r") as smaller_file:
    entries = [line for line in smaller_file]
    for entry in entries:

        thing = entry.split()
        # print()
        if urllib.parse.unquote(thing[0]) == "Main_Page":
            print(entry)
            print(urllib.parse.unquote(thing[0]), thing[1:])

