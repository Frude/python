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
url='http://www.zhanqi.tv/'
guokr =Soup(url).get_soup()
#print guokr
news_list = guokr.find('div', class_="modular-area").find_all('li',limit=7)
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)  
        new_url='http://www.zhanqi.com'+news.a['href']
        print new_url
        find1=Soup(new_url).get_soup()
        find=find1.find('div',class_="live-anchor-info clearfix")
        new_icon=find.img['src']
        new_user=find.span.get_text()
        userid=find.a['href']
        new_userid=re.search(pattern, string)
        find2=find.find('span',class_="dv js-onlines-txt")
        ratingCount=find2.get_text()
        print find2
        print ratingCount  
        print new_icon
        print new_user
        print new_userid
        
        imgs =news.img['src']
        print imgs
        title= news.a['title']
        print title
        data = {
              "description" : title,
              "platform":"战旗",
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : new_url, 
              "starname" : new_user, 
              "starid":new_userid,
              "viewernumber":ratingCount,
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
        print r