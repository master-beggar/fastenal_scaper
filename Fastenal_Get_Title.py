# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open(r'C:\Users\wnaimi\Desktop\Python\Python Projects\Fastenal Fasteners\Diff.txt') as file:
    list = []
    for line in file:
        line = line.strip()
        list.append(line)

with open(r'C:\Users\wnaimi\Desktop\Python\Python Projects\Fastenal Fasteners\Remaining.txt','w') as file:
    for pn in list:
        url = 'https://www.fastenal.com/products/details/' + pn
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        # Retrieve all of the anchor tags
        tags = soup('title')
        for tag in tags:
            # Look at the parts of a tag
            # print('TAG:', tag)
            # print('URL:', tag.get('href', None))
            the_title = str(tag.contents[0])
            pos = the_title.find('|')
            the_title = the_title[:pos].strip()
            to_write = pn + '|' + the_title + '\n'
            file.write(to_write)
            # print('Attrs:', tag.attrs)
