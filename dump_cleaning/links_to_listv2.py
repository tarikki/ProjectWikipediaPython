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
    redirect_node = False
    texts = node.getElementsByTagName("text")
    if node.getElementsByTagName("redirect"):
        # print(node.toprettyxml())
        redirect_counter += 1
        redirect_node = True

    total_links = 0
    title = (node.getElementsByTagName("title")[0].firstChild.data)
    if not reject_non_articles(title):
        print("rejected", title)
        return None, False
    result_list = [title]
    result_set = set()
    result_list_raw = []
    for whatevah in texts[0].childNodes:
        # matches = re.search(r'\[\[.*?\]\]',dikke.nodeValue)
        # if title == "Answer":
        # print(dikke.nodeValue)
        matches = re.findall(r'\[\[(.+?)\]\]', whatevah.nodeValue)
        # if title == "Answer":
        # print(len(matches))
        if matches:
            total_links += len(matches)
            # if title == "Answer":
            # for group in matches:
            # print(group)
            # print("***")
            # print(dikke.nodeValue)

            result_list_raw.extend(
                [group.split("|")[0].strip() for group in matches if reject_non_articles(group.split("|")[0].strip())])

            result_set.update(result_list_raw)
            # print(title, "list", len(result_list_raw), "set", len(result_set))
            # if title == "Allah":
            # for link in result_list_raw:
            # print(link)
            # print(node.toprettyxml())
    result_list.extend([remove_hashtag(link) for link in list(result_set)])
    # result += "links on page " + str(total_links) + "\n"
    # print("TITLE ", title)
    # extension_checker(result_set)

    # saveable_list = ",".join(result_list)
    # print(result_list)
    results = "|".join(result_list) + "\n"
    # print(result)
    counter += 1
    # print(results)
    return results, redirect_node
    # print(result)


def reject_non_articles(possible_link):
    temp = possible_link.lower()
    if temp.startswith((
            "file:", "category:", "wikipedia:", "wikt:", "image:", "media:", "s:", "n:", "commons:", "user:",
            "special:",
            "biblewiki:", "book:", "wiktionary:", "wikiquote:")) or temp.endswith("(disambiguation)"):
        return False
    else:
        return True


def remove_hashtag(link):
    notag = link.split("#")
    if notag > 1:
        return notag[0]
    else:
        return link


def extension_checker(links):
    for link in links:
        matches = re.match(r'.+:.*', link)
        if matches:
            print(matches.group())


with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml",
          mode='r') as big_file, open(
        "/media/extradikke/FastFiles/wikidata/articles_processed.txtttt", mode='w') as output, open(
        "/media/extradikke/FastFiles/wikidata/redirects.txt", mode='w') as file_redirects:
    fsize = os.stat("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml").st_size

    stream = pulldom.parse(big_file)
    counter = 1
    redirect_counter = 0
    start = time.time()
    nodes_to_save = list()
    for event, node in stream:

        if redirect_counter > 2:
            break
        # print(event, node.nodeName)
        if event == "START_ELEMENT" and node.nodeName == "page":

            stream.expandNode(node)  # node now contains a mini-dom tree
            nodes_to_save.append(node)

            if len(nodes_to_save) > 1000:
                for saved_node in nodes_to_save:
                    result, redirect = extract_links(saved_node)
                    if redirect:
                        print(result)
                        file_redirects.write(result)
                    if result is not None:
                        # print(result)
                        output.write(result)
                nodes_to_save = list()
        counter += 1
        if counter % 1000 == 0:
            completion_ratio = big_file.tell() / fsize
            print(counter, redirect_counter, 100 * completion_ratio)

            elapsed_time = math.floor(time.time() - start)
            print("Time:", elapsed_time)
            seconds_to_finish = math.floor((elapsed_time / completion_ratio)) - elapsed_time
            minutes, seconds = divmod(seconds_to_finish, 60)
            hours, minutes = divmod(minutes, 60)
            print("Estimated time of completion: %d:%02d:%02d" % (hours, minutes, seconds))


