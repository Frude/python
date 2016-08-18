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
url='http://www.huajiao.com/'
guokr =Soup(url).get_soup()
#print guokr
news_list = guokr.find('div',class_="living-switch").find_all('li',limit=6)
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        
        new_url='http://www.huajiao.com/l/'+news['data-id']
        print new_url
        WAPurl='http://www.huajiao.com/mobile/'+news['data-id']
        new_userid=news['data-id']
        print new_userid
        imgs =news.img['src']
        print imgs
        title= news.p.get_text()  
        print title

        
        Findinfo=Soup(new_url).get_soup()
        Fiodauthor=Findinfo.find('div', id="author-info")
#        findicon=Fiodauthor.find('div',class_="avatar avatar-v personal")
        new_icon=Fiodauthor.img['src']
        findim=Findinfo.find('div',class_="base-info")
        new_user=findim.h3.get_text()
        print new_user
        findwatch=findim.find('p',class_="watches")
        ratingCount=findwatch.strong.get_text()
        print ratingCount  
        print new_icon
        data = {
              "description" : title,
              "platform":"花椒",
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : WAPurl, 
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