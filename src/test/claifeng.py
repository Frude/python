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
url='http://www.laifeng.com/'
guokr =Soup(url).get_soup()
#print guokr
news_list = guokr.find_all('div', class_="lf-col1 lf-col-left")
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        finurl=news.find('div',class_="HM-video-move")
        new_url=finurl.a['href']
        print new_url
        finimg=news.find('div',class_="img")
        imgs =finimg.img['src']
        print imgs
        title=finimg.img['alt']+"的直播间"
        print title
        findnum=news.find('p',class_="num")
        ratingCount=findnum.get_text()
        print ratingCount
  
       
        Find1=get_html(new_url,12,is_img=True,is_soup=True)
#        Find1=Soup(new_url).get_soup()
        print Find1
#        finstring=re.compile(" ^DDS.anchorInfo.*?表情字典$",1).match(Find1)
        startStr="DDS.anchorinfo"
        endStr="//表情字典"
        patternStr = r'%s(.+?)%s'%(startStr,endStr) 
        print patternStr
        p = re.compile(patternStr,re.IGNORECASE) 
        finstring= re.match(p,Find1) 

        print finstring
#        find2=Find1.find('img',class_="host_portrait")
#        findicon=Find1.find('div',class_="photoer")
#        print findicon
#        new_icon=findicon.img['src']
#        print new_icon    
#        new_userid=findicon.img['data-id']
        new_user=finimg.img['alt']
        print new_user
        
       
        data = {
              "description" : title,
              "platform":"来疯",
              "picurl" : imgs,
#              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : new_url, 
              "starname" : new_user, 
#              "starid":new_userid,
              "viewer":ratingCount,
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
        print r