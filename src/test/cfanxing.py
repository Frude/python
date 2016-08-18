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
url='http://fanxing.kugou.com/'
guokr =get_html(url, 13, is_img=True, is_soup=True)
news_list = guokr.find('div',class_="cols").find_all('li',limit=16)

for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        
        new_url='http://fanxing.kugou.com'+news.a['href']
        wapurl='http://fanxing.kugou.com'+news.a['href']
        id=news.a['href']
        userid=re.search("[0-9]{6,8}",id).group()
        print new_url
        print userid
        imgs=news.a.img['src']
        print imgs
        title=news.a.p.get_text()
        print title
        
        findinfo=get_html(new_url, 14, is_img=True, is_soup=True)
        findauthor=findinfo.find('img',class_="anchorHeader")
        if not findauthor:
            new_icon=findauthor['src']
        if findauthor:
            new_icon=imgs
        print new_icon
        new_user=title
        print new_user
        
        
        
       
        data = {
              "description" : title,
              "platform":"繁星",
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