# -*- coding:UTF-8 -*-
import urllib
import urllib2
import re
import os
import json
from bs4 import BeautifulSoup
from datetime import * 
from test.GetSoup import Soup
from apicloud.dataCloud import DataCloud
from test.upload import upload
from random import random
from time import ctime, sleep
import threading
from test import Get_html
from apicloud.mysqldb import insert_db
import logging
from test.Get_html import get_html
import thread
#block=0
url='http://www.douyu.com/directory'
info=Soup(url).get_soup()
live_list = info.find('ul',id="live-list-contentbox").find_all('li')
for directory in live_list:
        print '*********************************'
        seconds=random()*2
        print seconds
#        sleep(seconds)
#        block=0
#        block=block+1
#        print block
        directory_url='http://www.douyu.com'+directory.a['href']
        print directory_url
        biaoji=open("log.txt","r")
        flag=biaoji.readline()
#        if(int(flag)!=block):
#            block=block+1
#            continue
#        block=block+1
#        print block
#        biaoji=open("log.txt","w")
#        biaoji.write(str(block))
#        biaoji.write("\n")
#        print block
        directory_list=Soup(directory_url).get_soup()
        room_list=directory_list.find('ul',id="live-list-contentbox").find_all('li')
        for room in room_list:
             room_url='http://www.douyu.com'+room.a['href']
             print room_url
#             f=open("test1.txt","w")
#
#             f.write(room_url)
#             f=open("test1.txt","r")
#             geturl=f.readline()
#             f.close()
             room_info=Soup(room_url).get_soup()
             findimg=room.find('span',class_="imgbox")
             room_cover= findimg.img['data-original']
             print room_cover
             userid=room['data-rid']
             print userid
             findviewer=room.find('span',class_="dy-num fr")
             viewer=findviewer.get_text()
             print viewer
             finduser=room.find('span',class_="dy-name ellipsis fl")
             user=finduser.get_text()
             print user
             
             findicon=room_info.find('div',class_="anchor-pic fl")
             if not findicon:
                findicon=room_info.find('div',class_="h_tx fl")
             if not findicon:
                findicon=room_info.find('div',class_="anchor-pic")
             icon=findicon.img['src']
             print icon
             findtitle=room_info.find('div',class_="headline clearfix")
             title=findtitle.h1.get_text()
             print title
             tag="斗鱼"
             findtags=room_info.find('div',class_="tag-fs-con clearfix")
             if not findtags:
                tag="比赛直播"
             if findtags:
                 tag_list=findtags.find_all('a')
                 for tags in tag_list:
                     tag=tag+'，'+tags.get_text()
             print tag
            
           
             data = {
              "description" : title,
              "platform":"斗鱼",
              "picurl" : room_cover,
              "avatarurl" : icon,
              "PCurl" : room_url, 
              "WAPurl" : room_url, 
              "starname" : user, 
              "starid":userid,
               "viewer":viewer,
               "viewernumber":viewer,
               "tags":tag
               }
             appId = "A6925963218522"
             appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
             url ='https://d.apicloud.com/mcm/api'
             client = DataCloud(appId, appKey,url);
             r=client.createObject('topzhibo',data)
             print '*********************************'
             print r

