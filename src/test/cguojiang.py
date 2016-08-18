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
from test.Get_html import get_html
url='http://www.guojiang.tv/'
guokr =Soup(url).get_soup()
news_list = guokr.find_all('dl',class_="room-item")

for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        imgs=news.img['src']
        print imgs
        new_url='http://www.guojiang.tv'+news.a['href']
        wapurl='http://www.guojiang.tv'+news.a['href']
        userid=news['rid']
        print new_url 
        print userid

 
        findviewer=news.find('span',class_="viewer")
        ratingCount=findviewer.get_text()
        print ratingCount
        finddd=news.find('dd')
       
        new_icon=imgs
        print new_icon
        title=finddd.p.get_text()
        print title
        finduser=news.find('span',class_="list_nickname")
        new_user=finduser.get_text()
        print new_user
        
        
        
       
        data = {
              "description" : title,
              "platform":"果酱",
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : wapurl, 
              "starname" : new_user, 
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