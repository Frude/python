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
url='http://www.douyu.com/directory'
info=Soup(url).get_soup()
live_list = info.find('ul',id="live-list-contentbox").find_all('li')
block=0
for directory in live_list:
        print '*********************************'
        seconds=random()*2
        print seconds
        sleep(seconds)
        biaoji=open("log.txt","r")
        flag=biaoji.readline()
        print flag
        if(int(flag)!=block):
            block=block+1
            continue
        block=block+1
        biaoji=open("log.txt","w")
        biaoji.write(str(block))
#        biaoji.write("\n")
        print block
        directory_url='http://www.douyu.com'+directory.a['href']
        print directory_url
        
        directory_list=Soup(directory_url).get_soup()
        if(directory_url=="http://www.douyu.com/directory/game/xc"):
#            room_list=directory_list.find('div',id="live-list-content").find_all('li')
            continue  
        else:
            room_list=directory_list.find('ul',id="live-list-contentbox").find_all('li')
            if not room_list:
                continue   
        for room in room_list:
             room_url='http://www.douyu.com'+room.a['href']
             print room_url
             findimg=room.find('span',class_="imgbox")
             if not findimg:
                 findimg=room.find('a',class_="s-avatar")
             room_cover= findimg.img['data-original']
             print room_cover
             cover=open("cover.txt","a")
             cover.write(room_cover)
             cover.write("\n")
             userid=room['data-rid']
             if not userid:
                 finduser=room.find('a',class_="s-avatar")
                 userid=finduser['href']
             print userid
             useridtxt=open("userid.txt","a")
             id=str(userid)
             useridtxt.write(id)
             useridtxt.write("\n")
             findviewer=room.find('span',class_="dy-num fr")
             if not findviewer:
                 continue
             viewer=findviewer.get_text()
             print viewer
             viewertxt=open("viewer.txt","a")
             num=str(viewer)
             viewertxt.write(num)
             viewertxt.write("\n")
             
             f=open("test.txt","a")
             f.write(room_url)
             f.write("\n")
f.close()
useridtxt.close()
viewertxt.close()