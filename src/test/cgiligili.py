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
url='http://live.bilibili.com/'
guokr =Soup(url).get_soup()
getpagetitle=guokr.title.get_text(strip=True)
print getpagetitle
news_list = guokr.find_all(class_="aside-item tv-cover")

for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url='http://live.bilibili.com/'+news['data-room-id']
        wapurl='http://live.bilibili.com/h5/'+news['data-room-id']
        userid=news['data-room-id']
        print new_url
        topzhibo=Soup(new_url).get_soup()
        starinfo=topzhibo.find('div',class_="head-info-panel clear-float")
        new_icon=starinfo.a['style']
        icon=re.search("http:(.*)jpg",new_icon).group()
        print icon
        findname=topzhibo.find('div',class_="master-info")
        username=findname.a.get_text(strip=True)
        print username
        Count=starinfo.find('span',class_="v-bottom dp-none")
        ratingCount=Count.get_text(strip=True)
        print ratingCount
        finbackground=guokr.find('div',class_="aside-item tv-cover")
        imgssource =news['style']
        imgs = re.search("http:(.*)jpg",imgssource).group()
        print imgs
        title= news['title']
        print title
        data = {
              "description" : title,
              "platform":"B站",
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : wapurl, 
              "starname" : username, 
              "starid":userid,
               "viewer":ratingCount,
#               "reviewCount":reviewCount
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
print r