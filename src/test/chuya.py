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
url='http://www.huya.com/'
guokr =Soup(url).get_soup()
#print guokr
news_list = guokr.find('div', class_="mod-game-type clearfix").find_all('li',limit=20)
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url=news.a['href']
        print new_url
        room =Soup(new_url).get_soup()
        find=room.find('div',class_="room-hd clearfix")
        new_icon=find.img['src']
        user=room.find('span',class_="host-name")
        new_user=user.get_text()
        new_userid=news['uid']
        print new_icon
        print new_user
        print new_userid
        imgs =news.img['src']
        print imgs
        title= find.h1.get_text()
        print title
        renshu=room.find('em', class_="host-spl")
        ratingCount=renshu.get_text()
        print ratingCount
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