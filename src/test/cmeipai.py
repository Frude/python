
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
url='http://www.meipai.com/'
guokr =Soup(url).get_soup()
#print guokr
pagetitle=guokr.find('img',id="topLogin" )
getpagetitle=pagetitle['alt']
print getpagetitle
news_list = guokr.find('ul', class_="content-l-ul mp-home clearfix").find_all('li',limit=5)
for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_video =news.div['data-video']
        print new_video
        new_url='www.meipai.com'+news.a['href']
        print new_url
        find2=news.find('span',itemprop="ratingCount")
        ratingCount=find2.get_text(strip=True)
        print ratingCount  
        find3=news.find('span',itemprop="reviewCount")
        reviewCount=find3.get_text(strip=True)
        print reviewCount
        find=news.find('div',itemprop="aggregateRating",class_="pr")
        new_icon=find.img['src']
        new_user=find.img['alt']
        new_userid=find.a['href']
        print new_icon
        print new_user
        print new_userid
        imgs =news.img['src']
        print imgs
        title= news.img['alt']
        print title
        data = {
              "description" : title,
              "platform":"美拍",
              "picurl" : imgs,
              "avatarurl" : new_icon,
              "PCurl" : new_url, 
              "WAPurl" : new_url, 
              "starname" : new_user, 
              "starid":new_userid,
              "viewernumber":ratingCount,
              "reviewCount":reviewCount
        }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
        print r