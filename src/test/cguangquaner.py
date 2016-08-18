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
url='http://www.guangquaner.com/'
guokr =Soup(url).get_soup()
news_list = guokr.find('ul',class_="liverow").find_all('li',limit=16)

for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        
        new_url='http://www.guangquaner.com'+news.a['href']
        wapurl='http://www.guangquaner.com'+news.a['href']
        id=news.a['href']

        userid=re.search("[0-9]{6,8}",id).group()
        print new_url
        print userid
        imgs=news.a.img['src']
        print imgs
        
        
        findauthor=news.find('div',class_="live-user")
        new_icon=findauthor.img['src']
        print new_icon
        new_user=findauthor.span.get_text()
        print new_user
        
        
        
        title=new_user
        print title
        data = {
              "description" : title,
              "platform":"光圈",
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : wapurl, 
              "starname" : new_user, 
              "starid":userid,
#               "viewer":ratingCount,
#               "reviewCount":reviewCount
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
print r