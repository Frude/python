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
url='http://www.showself.com/'
guokr =Soup(url).get_soup()
#print guokr
news_list = guokr.find('div',class_="recommend").find_all('li',limit=16)
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        
        new_url='http://www.showself.com/'+news.a['href']
        print new_url
        new_userid=news.a['href']
        print new_userid
        
        imgs =news.img['src']
        print imgs
        title= news.img['alt']
        print title
        findinfo=news.find('div',class_="zhezhao_top_x bg3_h")
        new_user=findinfo.get_text()
        print new_user
        
        findrating=news.find('div',class_="recommend_b")
        ratingCount=findrating.span.get_text()
        print ratingCount 
#        findicon=Soup(new_url).get_soup()
#        print findicon
#        icon=findicon.find('a',class_="info_l1") 
#        print icon
#        new_icon=icon.img['src']
        new_icon=imgs
        print new_icon
        data = {
              "description" : title,
              "platform":"秀色",
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