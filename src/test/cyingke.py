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
url='http://video.inke.com/pc/app/hotlive_list.html'
guokr =get_html(url,7,is_img=True,is_soup=True)
#print guokr
news_list = guokr.find_all('div', class_="list_box")
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        
        new_url='http://video.inke.com'+news.a['href']
        print new_url
        imgs =news.img['src']
        print imgs
        findtitle=news.find('div',"list_intro")
        title= findtitle.p.get_text()  
        print title
        new_user=news.img['alt']
        print new_user
        
        find=news.find('p',class_="num")
        ratingCount=find.get_text()
        print ratingCount  
      
       
        Find1=get_html(new_url,8,is_img=True,is_soup=True)
        find2=Find1.find('img',class_="host_portrait")
        new_icon=find2['src']
        print new_icon
        findid=Find1.find('p',class_="host_code")
        new_userid=findid.span.get_text()
        print new_userid
        
        data = {
              "description" : title,
              "platform":"映客",
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