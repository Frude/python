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
url='http://www.panda.tv/'
guokr =Soup(url).get_soup()
#print guokr
news_list = guokr.find('div', class_="suggestion-lists clearfix").find_all('li',limit=20)
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url='http://www.panda.tv'+news.a['href']
        print new_url
        Find1=Soup(new_url).get_soup()
        print Find1
        find2=Find1.find('div',class_="thumb-list-info")
        new_user=find2.span.get_text(strip=True)
        find5=Find1.find('div',class_="room-viewer-num")
        ratingCount=find5.span.get_text(strip=True)
        print ratingCount
        find=news.find('div',class_="room-head-info")
        new_icon=find.img['src']
        new_userid=news.a['href']
        print new_icon
        print new_user
        print new_userid
        
        imgs =news.img['src']
        print imgs
        find4=news.find('div',class_="thumb-title")
        title= find4['title']
        print title
        data = {
              "description" : title,
              "platform":'虎牙',
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : new_url, 
              "starname" : new_user, 
              "starid":new_userid,
              "viewer":ratingCount,
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
        print r