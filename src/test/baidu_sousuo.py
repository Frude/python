# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from Save import Save
from GetSoup import Soup
from apicloud.dataCloud import DataCloud
from upload import upload
from time import ctime,sleep
from random import random
import time
from Get_html import get_html

url = 'http://v.baidu.com/v?ct=301989888&rn=20&pn=0&db=0&s=25&ie=utf-8&word=作死'
soup = Soup(url).get_soup()
print soup
# html = get_html(url,0)
# print html