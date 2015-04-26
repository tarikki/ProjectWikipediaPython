__author__ = 'extradikke'

with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/dataMaps/article_name_to_number.txt",
          mode="r") as file:
    flines = [f for f in file]
    word_to_number = dict()
    number_to_word = dict()
    # print(flines[14])
    for line in flines:
        # print(line)
        key, entry = line.split("---")
        try:
            integer_entry = int(entry.strip("\n"))
            word_to_number[key] = integer_entry
            number_to_word[integer_entry] = key
        except ValueError:
            print(line)
    print(word_to_number["A Trap"])
    print(len(word_to_number))
    print(max([value for value in word_to_number.values()]))
    print(number_to_word[6000000])
    template_counter = 0
    for key in word_to_number:
        if key.startswith("Template"):
            template_counter +=1
            print(key)
    print(template_counter)
    # for i in range(len(lines)-1, len(lines)-100, -1):
    #     print(lines[i])
