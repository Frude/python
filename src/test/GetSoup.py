# -*- coding:UTF-8 -*-
'''
Created on 2016-3-8

@author: Administrator
'''

import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from datetime import *
import time
class Soup():
    def __init__(self,url,encoding='utf-8'):
        self.url = url
        #self.sleep_download_time = 10
        self.soup = BeautifulSoup("","html.parser")
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        #    'Host': "pinghot.qq.com",
            'Referer': "http://lol.qq.com/v/index.shtml",
            'X-Requested-With': "XMLHttpRequest"
        }
        try:
            #time.sleep(self.sleep_download_time)
            request = urllib2.Request(self.url,headers = headers)
            response = urllib2.urlopen(request)
            if encoding =='':
                contents =response.read()
            else:
                contents = response.read().decode(encoding)
            #contents2 = UnicodeDammit(contents)
            #print contents2.unicode_markup
            
            self.soup = BeautifulSoup(contents,"html.parser")
            #request.close()
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
    def get_soup(self):
        return self.soup 

#soup = Soup('http://lufuli.net/chuchu/').get_soup()
#print soup