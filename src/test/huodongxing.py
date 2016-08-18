# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import json
from GetSoup import Soup
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from random import random


def Huodongxing():
    baseURl = 'http://www.huodongxing.com'
    html = get_html('http://www.huodongxing.com/eventlist?orderby=n&city=杭州',1)
    soup = BeautifulSoup(html,"html.parser")
    #print soup
    parents =soup.find('ul',class_='event-horizontal-list-new').find_all('li',limit=10)
    
    for parent in parents:
        print "**************************************"
        seconds=random()*5
        print seconds
        title = parent.h3.a['title']
        imgs = parent.a.img['src']
        newurl =baseURl +parent.h3.a['href']
        print newurl
        soup2=Soup(newurl).get_soup()
        content =soup2.find('div', class_="event-intro tab-content", id="eventContentAreaMain")
        content =str(content)
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : "杭活动行", 
              "url" : newurl, 
              "rela_chan" : '56f8ec1c8cbdb5ce206048ec', 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "simg"
        }   
        upload(data)
        print '*********************************'
# Huodongxing()

