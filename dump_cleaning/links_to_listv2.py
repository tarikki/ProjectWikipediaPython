from xml.dom import pulldom
import os
import time
import re
import math
from multiprocessing import Queue, Process, Value
import sys


__author__ = 'extradikke'
# xml_file is either a filename or a file

def extract_links(node):
    # global counter
    # global redirect_counter
    redirect_node = False
    texts = node.getElementsByTagName("text")
    if node.getElementsByTagName("redirect"):
        redirect_node = True

    total_links = 0
    title = (node.getElementsByTagName("title")[0].firstChild.data)
    if not reject_non_articles(title):
        # print("rejected", title)
        return None, False
    result_list = [title]
    result_set = set()
    result_list_raw = []
    for whatevah in texts[0].childNodes:

        matches = re.findall(r'\[\[(.+?)\]\]', whatevah.nodeValue)
        if matches:
            total_links += len(matches)
            result_list_raw.extend(
                [group.split("|")[0].strip() for group in matches if reject_non_articles(group.split("|")[0].strip())])
            result_set.update(result_list_raw)

    result_list.extend([remove_hashtag(link) for link in list(result_set)])
    # result += "links on page " + str(total_links) + "\n"
    # print("TITLE ", title)
    # extension_checker(result_set)

    # saveable_list = ",".join(result_list)
    # print(result_list)
    results = "|".join(result_list) + "\n"
    # print(result)
    # counter += 1
    # print(results)
    return results, redirect_node
    # print(result)

def extract_links2(node):
    # global counter
    # global redirect_counter
    result_list_raw = []
    # print(node)
    title, text_list = node
    result_list = [title]
    result_set = set()
    for whatevah in text_list:
        matches = re.findall(r'\[\[(.+?)\]\]', whatevah)
        if matches:
            result_list_raw.extend(
                [group.split("|")[0].strip() for group in matches if reject_non_articles(group.split("|")[0].strip())])
            result_set.update(result_list_raw)

    result_list.extend([remove_hashtag(link) for link in list(result_set)])
    results = "|".join(result_list) + "\n"
    return results


def extract_title_and_text_2(node):
    # global counter
    # global redirect_counter
    title = (node.getElementsByTagName("title")[0].firstChild.data)
    if not reject_non_articles(title):
        # print("rejected", title)
        return None
    redirect_node = False
    texts = node.getElementsByTagName("text")
    if node.getElementsByTagName("redirect"):
        redirect_node = True

    total_links = 0

    result_list_raw = [whatevah.nodeValue for whatevah in texts[0].childNodes]
    return title, result_list_raw, redirect_node


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
    if len(notag) > 1:
        return notag[0]
    else:
        return link


def extension_checker(links):
    for link in links:
        matches = re.match(r'.+:.*', link)
        if matches:
            print(matches.group())


def redirect_saver(q, still_looping):
    with open("/media/extradikke/FastFiles/wikidata/redirects_try.txt", mode='w') as file_redirects:
        while still_looping.value:
            node = q.get()
            file_redirects.write(node)


def link_extractor(rnq, rq, pq, still_looping):
    while still_looping.value:
        node = rnq.get()
        clean_node = extract_links2(node[0:2])
        if clean_node is not None:
            if node[2]:
                # print("redirect")
                rq.put(clean_node)
            else:
                # print("page")
                pq.put(clean_node)


def save_pages(pq, still_looping):
    with open("/media/extradikke/FastFiles/wikidata/articles_processed_try.txt", mode='w') as output:
        while still_looping.value:
            node = pq.get()
            output.write(node)
def opener(rawq, pq, rq):
    with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml",
              mode='r') as big_file:
        fsize = os.stat(
            "/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml").st_size
        stream = pulldom.parse(big_file)
        # sys.setrecursionlimit(10000)
        counter = 1
        redirect_counter = 0

        start = time.time()

        for event, node in stream:
            #
            # print(event, node.nodeName)
            if event == "START_ELEMENT" and node.nodeName == "page":
                stream.expandNode(node)  # node now contains a mini-dom tree
                title_and_text_and_redirect = extract_title_and_text_2(node)
                if title_and_text_and_redirect is not None:
                    if title_and_text_and_redirect[2]:
                        redirect_counter+=1
                    else:
                        counter += 1
                    rawq.put(title_and_text_and_redirect)



            if counter % 1000 == 0:
                completion_ratio = big_file.tell() / fsize
                print(counter, redirect_counter, 100 * completion_ratio)
                print("raw nodes:", rq.qsize(), ", pages queue:", pq.qsize(), ", redirect queue:",
                      rq.qsize())
                elapsed_time = math.floor(time.time() - start)
                print("Time:", elapsed_time)
                seconds_to_finish = math.floor((elapsed_time / completion_ratio)) - elapsed_time
                minutes, seconds = divmod(seconds_to_finish, 60)
                hours, minutes = divmod(minutes, 60)
                print("Estimated time of completion: %d:%02d:%02d" % (hours, minutes, seconds))


def main():
    with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml",
              mode='r') as big_file:
        fsize = os.stat(
            "/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml").st_size
        stream = pulldom.parse(big_file)
        # sys.setrecursionlimit(10000)
        redirect_queue = Queue(100)
        pages_queue = Queue(100)
        rawnodes_queue = Queue(1000)

        counter = 1
        redirect_counter = 0

        running = Value('b', True)

        link_extractor1 = Process(target=link_extractor, args=(rawnodes_queue, redirect_queue, pages_queue, running, ))
        link_extractor2 = Process(target=link_extractor, args=(rawnodes_queue, redirect_queue, pages_queue, running, ))
        # link_extractor3 = Process(target=link_extractor, args=(rawnodes_queue, redirect_queue, pages_queue, running, ))
        # link_extractor4 = Process(target=link_extractor, args=(rawnodes_queue, redirect_queue, pages_queue, running, ))
        xml_openeger = Process(target=opener, args=(rawnodes_queue, pages_queue, redirect_queue))
        redirects = Process(target=redirect_saver, args=(redirect_queue, running,))
        page_saver = Process(target=save_pages, args=(pages_queue, running,))
        #

        xml_openeger.start()
        processes = [link_extractor1, link_extractor2, redirects, page_saver]
        for process in processes:
            process.start()
        xml_openeger.join()
        while True:
            print("here???")
            if redirect_queue.empty() and pages_queue.empty() and rawnodes_queue.empty():
                running.value = False
                for process in processes:
                    process.join()
                break


if __name__ == '__main__':
    main()
