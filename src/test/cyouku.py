# -*- coding: UTF-8 -*-

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
url='http://live.youku.com/'
guokr =Soup(url).get_soup()
news_list = guokr.find_all(class_="contentHolderUnit")
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url=news.a['href']
        wapurl=new_url
        userid=news['data-room-id']
        print new_url
        topzhibo=Soup(new_url).get_soup()
        starinfo=topzhibo.find('div',class_="head-info-panel clear-float")
        new_icon=starinfo.a['style']
        print new_icon
        findname=topzhibo.find('div',class_="master-info")
        username=findname.a.get_text(strip=True)
        print username
        Count=starinfo.find('div',class_="dp-inline-block v-middle")
        ratingCount=Count.span.get_text(strip=True)
        print ratingCount
        imgs =news.img['src']
        print imgs
        title= news.img['alt']
        print title
        data = {
              "description" : title,
              "platform":'优酷',
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : wapurl, 
              "starname" : username, 
              "starid":userid,
               "viewernumber":ratingCount,
#               "reviewCount":reviewCount
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
print r