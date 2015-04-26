__author__ = 'extradikke'
from lxml import etree
# with open("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml",
#           mode='r') as big_file:
context = etree.iterparse("/media/extradikke/UbuntuData/wikipedia_data/data_dump/enwiki-20150112-pages-articles.xml", events=('end',), tag='Title')

for event, elem in context:
    print('%s\n' % elem.text.encode('utf-8'))