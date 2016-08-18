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
from random import random
from time import ctime, sleep
import threading
from apicloud.mysqldb import insert_db
import logging
import thread
#while True:
ftxt=open("flag.txt","r")
flag=ftxt.readline()

f=open("test.txt","r")
#    geturl=f.readline()
#    if geturl:
for geturl in f.readlines()[int(flag):len(f.readlines())-1]:
        flag=int(flag)+1
        ftxt=open("flag.txt","w")
        ftxt.write(str(flag))
        room_url=geturl
        print room_url
        print flag
        room_info=Soup(room_url).get_soup()
        
        findicon=room_info.find('div',class_="anchor-pic fl")
#        print findicon
        if not findicon:
            findicon=room_info.find('div',class_="h_tx fl")
        if not findicon:
            findicon=room_info.find('div',class_="anchor-pic")
        icon=findicon.img['src']
        print icon
        findtitle=room_info.find('div',class_="headline clearfix")
        roomtitle=findtitle.h1.get_text()
        print roomtitle
        tag="斗鱼"
        findtags=room_info.find('div',class_="tag-fs-con clearfix")
        if not findtags:
            tag="比赛直播"
        if findtags:
            tag_list=findtags.find_all('a')
            if not tag_list:
                continue
            for tags in tag_list:
                tag=tag+'，'+tags.get_text()
        print tag
        idt=open("userid.txt","r")
        for id in idt.readlines()[flag:len(idt.readlines())-1]:
            userid=id
        cover=open("cover.txt","r")
        for id1 in cover.readlines()[flag:len(cover.readlines())-1]:
            room_cover=id1
        viewer=open("viewer.txt","r")
        for id2 in viewer.readlines()[flag:len(viewer.readlines())-1]:
            viewernumber=id2  
        finduser=room_info.find('div',class_="zb-name-con")
        if finduser:
            user=finduser.a.get_text()
        if not finduser:
            finduser=room_info.find('i',class_="zb-name")
            user=finduser.get_text()
        print user
#        finduserid=room_info.find('a',class_="feedback-report-button fl")
#        id=finduserid['href']
#        if not id:
#            continue
#        userid=re.search("[0-9]{5,8}",id).group()
#        print userid
#        
#        finduser=room_info.find('div',class_="zb-name-con")
#        user=finduser.a.get_text()
#        print user
#        findup=room_info.find('a',class_="head-room-tag fl second")
#        directory_url='http://www.douyu.com'+findup['href']
#        directory_list=Soup(directory_url).get_soup()
##        room_list=directory_list.find('ul',id="live-list-contentbox").find_all('li')
#       
#       
#        
#        findinfo=directory_list.find('ul',id="live-list-contentbox")
#        findimg=findinfo.find('span',class_="imgbox")
#        room_cover= findimg.img['data-original']
#        print room_cover
#
#        findviewer=findinfo.find('span',class_="dy-num fr")
#        viewer=findviewer.get_text()
#        print viewer
       
        data = {
                "description" : roomtitle,
                "platform":"斗鱼",
                "picurl" : room_cover,
                "avatarurl" : icon,
                "PCurl" : room_url, 
                "WAPurl" : room_url, 
                "starname" : user, 
                "starid":userid,
                "viewer":viewernumber,
                "viewernumber":viewernumber,
                "tags":tag
                }
        appId = "A6925963218522"
        appKey = "2748C88B-36F4-BD41-72B0-5EE7847DD1FE"
        url ='https://d.apicloud.com/mcm/api'
        client = DataCloud(appId, appKey,url);
        r=client.createObject('topzhibo',data)
        print '*********************************'
        print r
        f.close()
    
