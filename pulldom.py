from xml.dom import pulldom
import os
import time
import re
__author__ = 'extradikke'
# xml_file is either a filename or a file

def reject_redirects(node):
    global counter
    global redirect_counter
    result=""
    texts = node.getElementsByTagName("text")
    # print("tagname", texts[0].childNodes)
    total_links = 0
    for dikke in texts[0].childNodes:
        # matches = re.search(r'\[\[.*?\]\]',dikke.nodeValue)
        matches = re.findall(r'\[\[.+?\]\]',dikke.nodeValue)

        # [^\]^\]]
        if matches:
            total_links += len(matches)
            # print("***")
            # print(dikke.nodeValue)
            # for group in matches:
            #     print(group)

    for child_node in node.childNodes:
        if child_node.nodeName == "title" and child_node.firstChild.data == "Abyssinia":
            print(node.toprettyxml())
            pass

        # if child_node.nodeType == 3:
            # print("text, baby", len(child_node.data))
            # for i in range(0, len(child_node.data)):
            #     print(child_node[i])
        # else:
            # print(child_node.nodeType)
            # print(child_node.nodeName, child_node.textContent)
        if child_node.nodeType == 1:
            if child_node.nodeName == "redirect":
                redirect_counter +=1
                return
            # if child_node.nodeName == 'revision':
            #     for child in child_node.childNodes:
            #         print("nodeName",child.nodeName)
            #         if child.nodeName == "text":
            #             print("textChildren", len(child.childNodes),child.firstChild.nodeValue)
            #             for child2 in child.childNodes:
            #                 print(child2.nodeType)
            #                 print(child2.nodeValue)
            #                 print("************8")
            result += child_node.nodeName
            if len(child_node.childNodes) > 0:
                result += " " + child_node.firstChild.data + "\n"
            else:
                result += "\n"
    counter+=1
    result += "links on page " + str(total_links) + "\n"
    # print(result)


with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml", mode='r') as big_file:
    fsize = os.stat("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml").st_size
    stream = pulldom.parse(big_file)
    counter = 1
    redirect_counter = 0
    start = time.time()
    for event, node in stream:
        if counter > 1000:
            break

        # print(event, node.nodeName)
        if event == "START_ELEMENT" and node.nodeName == "page":

            stream.expandNode(node) # node now contains a mini-dom tree
            reject_redirects(node)
        if counter % 1000 == 0:
            print(counter, redirect_counter, 100 * big_file.tell()/fsize)
            if 100 * big_file.tell()/fsize > 1:
                print("Time:", time.time()- start)

                    # print(child_node.nodeName, child_node.childNodes[0], child_node.nodeType)
                # print(attr)
            # print(node.toprettyxml())
            # if node.hasAtribute
            # for child in node.childNodes:
            #     print(child.nodeName)
            #     if child.nodeName == 'title':
            #         print(child)

