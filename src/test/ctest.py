
import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from datetime import * 
from GetSoup import Soup
from apicloud.dataCloud import DataCloud
from upload import upload
from random import random
from time import ctime, sleep
import threading
from test import Get_html
from apicloud.mysqldb import insert_db
import logging
url='http://www.huya.com/'
guokr =Soup(url).get_soup()
guokrscript=guokr.find('script').get_text()
#guokrscript1=re.search('(?<=\d)uid', guokrscript).group()
print guokrscript