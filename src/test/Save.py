# -*- coding:UTF-8 -*-
'''
Created on 2016-2-28

@author: Administrator
'''
import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from datetime import *
import uuid 
class Save():
    #    100000000000000000000009
    def __init__(self):
        self.data = {
          "title" : "",
          "content" :'', 
          "imgs" : '''http://i45.tinypic.com/2w1tg1v.jpg''',
          "cname" : "Business Insider", 
          "url" : "http://www.baidu.com", 
          "rela_chan" : "", 
          "is_hot" : 1, 
          "is_bot" : 1, 
          "type" : "img"
        }  
    def tostring(self):
        return self.data
    def save(self,title,content,imgs,rela_chan,cname="Business Insider",url='http://www.baidu.com',type='img'):
        self.data['title']=title
        self.data['content']=content
        self.data['imgs']=imgs
        self.data['rela_chan']=rela_chan