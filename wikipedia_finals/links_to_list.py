from xml.dom import pulldom
import os
import time
import re
import math

__author__ = 'extradikke'
# xml_file is either a filename or a file

def extract_links(node):
    global counter
    global redirect_counter
    texts = node.getElementsByTagName("text")
    if node.getElementsByTagName("redirect"):
        # print(node.getElementsByTagName("redirect"))
        redirect_counter += 1
        return
    # print("tagname", texts[0].childNodes)
    total_links = 0
    title = (node.getElementsByTagName("title")[0].firstChild.data)
    if title.endswith("(disambiguation)"):
        # print(title)
        return
    # print(title)
    result_list = [title]
    result_set = set()
    result_list_raw = []
    for dikke in texts[0].childNodes:
        # matches = re.search(r'\[\[.*?\]\]',dikke.nodeValue)
        # if title == "Answer":
        # print(dikke.nodeValue)
        matches = re.findall(r'\[\[(.+?)\]\]', dikke.nodeValue)
        # if title == "Answer":
        # print(len(matches))
        if matches:
            total_links += len(matches)
            # if title == "Answer":
            # for group in matches:
            #         print(group)
            # print("***")
            # print(dikke.nodeValue)
            result_list_raw.extend(
                [group.split("|")[0].strip() for group in matches if reject_non_articles(group.split("|")[0].strip())])
            result_set.update(result_list_raw)
            # print(title, "list", len(result_list_raw), "set", len(result_set))
            # if title == "Allah":
            #     for link in result_list_raw:
            #         print(link)
            # print(node.toprettyxml())
    result_list.extend(list(result_set))
    # result += "links on page " + str(total_links) + "\n"
    # print("TITLE ", title)
    # extension_checker(result_set)

    # saveable_list = ",".join(result_list)
    results = "|".join(result_list) + "\n"
    # print(result)
    counter += 1
    # print(results)
    return results
    # print(result)


def reject_non_articles(possible_link):
    matches = re.match(
        r'^(?!(File|Category|Wikipedia|wikt|Image|Media|s|n|q|commons|User|file|Special|BibleWiki|Book|wiktionary|wikiquote|Wikt):).+',
        possible_link)
    if matches:
        return True


def extension_checker(links):
    for link in links:
        matches = re.match(r'.+:.*', link)
        if matches:
            print(matches.group())


with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml",
          mode='r') as big_file, open(
        "/media/extradikke/FastFiles/wikidata/articles_processed.txtttt", #changed name so no overwrite
        mode='w') as output:
    fsize = os.stat("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml").st_size

    stream = pulldom.parse(big_file)
    counter = 1
    redirect_counter = 0
    start = time.time()
    nodes_to_save = list()
    for event, node in stream:


        # print(event, node.nodeName)
        if event == "START_ELEMENT" and node.nodeName == "page":

            stream.expandNode(node)  # node now contains a mini-dom tree
            nodes_to_save.append(node)

            if len(nodes_to_save) > 1000:
                for saved_node in nodes_to_save:
                    result = extract_links(saved_node)
                    if result is not None:
                        # print(result)
                        output.write(result)
                nodes_to_save = list()
        counter +=1
        if counter % 1000 == 0:
            completion_ratio = big_file.tell() / fsize
            print(counter, redirect_counter, 100 * completion_ratio)

            elapsed_time = math.floor(time.time() - start)
            print("Time:", elapsed_time)
            seconds_to_finish = math.floor((elapsed_time / completion_ratio)) - elapsed_time
            minutes, seconds = divmod(seconds_to_finish, 60)
            hours, minutes = divmod(minutes, 60)
            print("Estimated time of completion: %d:%02d:%02d" % (hours, minutes, seconds))


