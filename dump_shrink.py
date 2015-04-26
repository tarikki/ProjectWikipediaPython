from xml.dom import pulldom
import os
import time
__author__ = 'extradikke'
# xml_file is either a filename or a file

def reject_redirects(node):
    global counter
    global redirect_counter
    result=""
    for child_node in node.childNodes:
        if child_node.nodeType == 1:
            if child_node.nodeName == "redirect":
                redirect_counter +=1
                return

            result += child_node.nodeName
            if len(child_node.childNodes) > 0:
                result += " " + child_node.childNodes[0].data + "\n"
            else:
                result += "\n"
    counter+=1
    # print(result)


with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml", mode='r') as big_file:
    fsize = os.stat("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml").st_size
    stream = pulldom.parse(big_file)
    counter = 0
    redirect_counter = 0
    start = time.time()
    for event, node in stream:
        if counter > 1000000:
            break

        # print(event, node.nodeName)
        if event == "START_ELEMENT" and node.nodeName == "page":

            stream.expandNode(node) # node now contains a mini-dom tree
            reject_redirects(node)
        if counter % 1000 == 0:
            print(counter, redirect_counter, 100 * big_file.tell()/fsize)
            if 100 * big_file.tell()/fsize > 1:
                print("Time:", time.time()- start)

            # if node.hasAttribute('title'):
            #     print(node.getAttribute('title'))

                    # print(child_node.nodeName, child_node.childNodes[0], child_node.nodeType)
                # print(attr)
            # print(node.toprettyxml())
            # if node.hasAtribute
            # for child in node.childNodes:
            #     print(child.nodeName)
            #     if child.nodeName == 'title':
            #         print(child)

