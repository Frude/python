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
url='http://www.yy.com/'
guokr =Soup(url).get_soup()
#print guokr
news_list = guokr.find('div',class_="star-wrap").find_all('li',limit=20)
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url='http://www.yy.com/'+news['data-sid']
        print new_url
        
        
        background=news.find('div',class_="pic-real")
        imgs =background.img['data-original']
        print imgs
#        
        Find1=get_html(new_url,9,is_img=True,is_soup=True)
        findicon=Find1.find('div',class_="w-liveplayer-userinfo")
        viewer=Find1.find('div',class_="audience-count")
        new_icon=findicon.img['src']
        print new_icon
        finduser=Find1.find('div',class_="intro")
        new_userid=finduser.span.get_text()

        print new_userid
        
        print viewer
        ratingCount=viewer.get_text()
        title= news.a['title']
        print title
        new_user=title
        print new_user
        data = {
              "description" : title,
              "platform":"yy直播",
              "picurl" : imgs,
#              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : new_url, 
              "starname" : new_user, 
#              "starid":new_userid,
              "viewernumber":ratingCount,
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
        print r