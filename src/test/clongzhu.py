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
url='http://longzhu.com/?from=chindex'
guokr =Soup(url).get_soup()
#print guokr
news_list = guokr.find('div',class_="side").find_all('li',limit=16)
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        
        new_url=news.a['href']
        print new_url
        new_userid=news['data-roomid']
        print new_userid
        
        imgs =news.img['data-image']
        print imgs
        title= news.img['alt']
        print title
        findinfo=Soup(new_url).get_soup()
        findicon=findinfo.find('img',class_="header-avatar-img")
        
        if not findicon:
            new_icon=imgs
            print new_icon
        if findicon:
            new_icon=findicon['data-image']
            print new_icon
        findnum=findinfo.find('span',class_="header-info-online",id="header-info-online")
        if not findnum:
            find2=findinfo.find('span',id="live-online")
            print find2
            
            ratingCount=find2.get_text()
        if findnum:
            print findnum
            ratingCount=findnum.i.get_text()
        print ratingCount 
        finduser=findinfo.find('span',class_="header-info-name")
        if finduser:
            new_user=finduser.get_text()
        if not finduser:
            new_user=title
        print new_user
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