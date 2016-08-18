# -*- coding:UTF-8 -*-

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
url='http://www.douyu.com/'
guokr =Soup(url).get_soup()
news_list = guokr.find('div',class_="c-items").find_all('li')
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url='http://www.douyu.com/'+news['data-id']
        userid=news['data-id']
        print new_url
        ratingCount=news['data-online']
        print ratingCount
        topzhibo=Soup(new_url).get_soup()
        findpic=topzhibo.find('div',class_="anchor-pic fl")
        if findpic:
            new_icon=findpic.img['src']
        if not findpic:
            findpic1=topzhibo.find('div',class_="room_mes mb15 clearfix js_live_height")
            new_icon=findpic1.img['src']
        print new_icon
        findname=topzhibo.find('div',class_="zb-name-con")
        username=findname.a.get_text(strip=True)
        print username
        imgs =news.img['src']
        print imgs
        title= news.span.get_text(strip=True)
        print title
        getdanmu=get_html(new_url, 17, is_img=True, is_soup=True)
        print getdanmu.find_all('li',class_="jschartli")
        data = {
              "description" : title,
              "platform":"斗鱼",
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : new_url, 
              "starname" : username, 
              "starid":userid,
               "viewernumber":ratingCount,
#               "reviewCount":reviewCount
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
print r