# -*- coding:UTF-8 -*-
import urllib
import urllib2
import re
import json
from GetSoup import Soup
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from StringIO import StringIO
import gzip
from upload import upload

url = 'http://note.youdao.com/share/?id=f560fc4c9b4e0f80629160762ce705a3&type=note#/'
html = get_html(url, 2)
print html
# soup =BeautifulSoup(html,"html.parser")
# print soup