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
url='http://www.9xiu.com/'
guokr =Soup(url).get_soup()
#list = guokr.find('div', class_="indexAhoTabBox")
#news_list=list.find_all_next()
#print news_list
news_list=guokr.find_all('div',class_="moduleImgBox fn_left")
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url='http://www.9xiu.com'+news.a['href']
        print new_url
        imgs=news.img['dataimg']
        print imgs 
        
        new_user=news.a['title']
        print new_user
#        findtitle=news.find('span',class_="moduleTitle moduBig")
        findtitle=news.find('span',class_="moduleTitle")
        title=findtitle.get_text()
        print title
        info=Soup(new_url).get_soup()
        icon=info.find('div',class_="ahoInfoImg")
        new_icon=icon.img['src']
        print new_icon
        id=news.a['href']
        userid=re.search("[0-9]{5,8}",id).group()
        print userid
        num=get_html(new_url,16,is_img=True, is_soup=True)
        number=num.find('div',class_="ahoInfoFans filter1 mpt a_follow")
        ratingCount=number.span.get_text()
        print ratingCount
        data = {
              "description" : title,
              "platform":"九秀",
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : new_url, 
              "starname" : new_user, 
              "starid":userid,
              "viewernumber":ratingCount
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
        print r