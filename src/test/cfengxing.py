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
url='http://www.fengyunlive.com/'
guokr =Soup(url).get_soup()
news_list = guokr.find('ul',class_="channel-list clear").find_all('li',limit=16)

for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        
        new_url=news.a['href']
        print new_url

        wapurl='http://www.fengyunlive.com/'+news.a['href']
        id=news.a['href']
        
        userid=re.search("[0-9]{5,8}",id).group()
        
        print userid
        imgs=news.a.img['src']
        print imgs
        findtitle=news.find('div',class_="pname")
        title=findtitle.get_text()
        print title
        finduser=news.find('div',class_="cname")
        new_user=finduser.get_text()
        print new_user
        
        findinfo=Soup(new_url).get_soup()
        findauthor=findinfo.find('div',class_="director-logo")
        if not findauthor:
            new_icon=imgs
        if findauthor:
            new_icon=findauthor.img['src']
        print new_icon
        new_user=title
        print new_user
        
        findnum=findinfo.find('span',class_="online-num")
        if not findnum:
            ratingCount=None
        if findnum:
            ratingCount=findnum.get_text()
        print ratingCount
        data = {
              "description" : title,
              "platform":"风行",
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