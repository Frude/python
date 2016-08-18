# -*- coding:UTF-8 -*-
from GetSoup import Soup
import re
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from random import random
from time import ctime,sleep
from log.main import m_log
'''
Created on 2016-4-17

@author: Administrator
'''
def qingsongyike(file_name):
    print "in %s. %s"%(file_name,ctime())
    url='http://news.yodao.com/search?q=每日轻松一刻'
    qingsongyike =Soup(url).get_soup()
    #print qingsongyike
    
    news_list = qingsongyike.find('ul', id="results").find_all('li',limit =10)
    for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url =news.div.a['href']
        hh= re.compile("http://news.163.com/")
        if re.match(hh,new_url):
            print new_url
        else:
            print "bu fu he de wangzhi :",new_url
            continue
        title= news.h3.a.get_text().encode('utf-8')
        print title
        soup2=Soup(new_url,'gbk').get_soup()
        content =soup2.find('div', id="endText")
        imgs =content.find("img")
        imgs= imgs['src']
        print imgs
        content= str(content)
        #print content
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : "轻松一刻", 
              "url" : new_url, 
              "rela_chan" : '57133600a578826b4ddd78a8', 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "simg",
        }
        upload(data)
        print '*********************************'
    print "out %s. %s"%(file_name,ctime())
def Qingsongyike():
    file_name="qingsongyike"
#     m_log(file_name)
    qingsongyike(file_name)
# Qingsongyike()