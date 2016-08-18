# -*- coding:UTF-8 -*-
from GetSoup import Soup
import re
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from random import random
from time import ctime,sleep
import sys
import os
'''
Created on 2016-4-17

@author: Administrator
'''
url='http://tieba.baidu.com/p/4614197468'
getcontent=Soup(url).get_soup()
print getcontent
