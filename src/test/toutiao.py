# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import json
from GetSoup import Soup
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from time import ctime,sleep
from random import random
import time
import threading

def toutiao(cname,url,rela_chan):
    print "in "+cname+"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
    baseURl = 'http://toutiao.com'
    html = get_html(url,3,False,False)
    soup = BeautifulSoup(html,"html.parser")
    #print soup
    parents =soup.find_all('li',class_="item clearfix",limit =10)
    
    for parent in parents:
        print "**************************************"
        seconds=random()*5
        print seconds
        time.sleep(seconds)
        newurl =baseURl+parent.div.div.a['href']
        print newurl
        imgs = parent.find("img")
        title =parent.find("div",class_="title-box")
        title = title.get_text(strip=True)
        if  not imgs : 
            imgs = "http://p3.pstatp.com/large/3410/6931534718"
            #title = parent.div.div.a.get_text(strip=True)
        else : 
            imgs=imgs['src']
            #print parent.div.contents[3]
            #title = parent.div.contents[3].div.div.a.get_text(strip=True)
        print imgs
        
        print title
        soup2=Soup(newurl,"").get_soup()
        #print soup2
        content=  soup2.find('div',class_="article-content")
        content = str(content)
        seconds=random()*5
        print seconds
        time.sleep(seconds)
        #print content
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" :cname, 
              "url" : newurl, 
              "rela_chan" : rela_chan, 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "simg",
            }  
        upload(data)#,True,True)
        print '*********************************'

def Toutiao():
    print "in toutiao. %s"%(ctime())

    list =[
        {"cname":"头条历史","url":'http://toutiao.com/news_history/',        "rela_chan":'56f8ec1c1675c45d431adc5f'},
        {"cname":"头条科技","url":"http://toutiao.com/news_tech/",           "rela_chan":'5720d20999e0668a02ae5e1d'},
        {"cname":"头条养生","url":"http://toutiao.com/news_regimen/",        "rela_chan":'5720d1fb99e0668a02ae5e1a'},
        {"cname":"头条美食","url":"http://toutiao.com/news_food/",           "rela_chan":'5723a0b4f535d0ae542cd9f0'},
        {"cname":"头条游戏","url":"http://toutiao.com/news_game/",           "rela_chan":'5723a086f535d0ae542cd9ef'},
        {"cname":"头条美文","url":"http://toutiao.com/news_essay/",          "rela_chan":'5723a055bba07b0e3f15ab36'},
        {"cname":"头条育儿","url":"http://toutiao.com/news_baby/",           "rela_chan":'57239fc6bba07b0e3f15ab34'},
        {"cname":"头条探索","url":"http://toutiao.com/news_discovery/",      "rela_chan":'57239fc6bba07b0e3f15ab34'},
        {"cname":"头条旅游","url":"http://toutiao.com/news_travel/",         "rela_chan":'57239f62ba2ceb790b2eb572'},
        {"cname":"头条国际","url":"http://toutiao.com/news_world/",          "rela_chan":'57239f62ba2ceb790b2eb572'},
        {"cname":"头条军事","url":"http://toutiao.com/news_military/",       "rela_chan":'57239efcba2ceb790b2eb570'},
        {"cname":"头条财经","url":"http://toutiao.com/news_finance/",        "rela_chan":'57239e9d44eb5c3e0a63b13c'},
        {"cname":"头条体育","url":"http://toutiao.com/news_sports/",         "rela_chan":'57239e46bba07b0e3f15ab33'},
        {"cname":"头条汽车","url":"http://toutiao.com/news_car/",            "rela_chan":'57239d8944eb5c3e0a63b13a'},
        {"cname":"头条娱乐","url":"http://toutiao.com/news_entertainment/",  "rela_chan":'57239d0aba2ceb790b2eb56f'},
        {"cname":"头条热点","url":"http://toutiao.com/news_hot/",            "rela_chan":'57239c9d44eb5c3e0a63b139'},
        {"cname":"头条推荐","url":"http://toutiao.com/",                     "rela_chan":'57239c4ee8f87e8a3f8d9330'},
        {"cname":"头条故事","url":"http://toutiao.com/news_story/",          "rela_chan":'5723a013f0e3bc3d175928b6'},
        {"cname":"头条社会","url":"http://toutiao.com/news_society/",        "rela_chan":'57239ccebba07b0e3f15ab2f'},
           #{"cname":"头条养生","url":"http://toutiao.com/news_regimen/",        "rela_chan":'5720d1fb99e0668a02ae5e1a'},
           #{"cname":"头条养生","url":"http://toutiao.com/news_regimen/",        "rela_chan":'5720d1fb99e0668a02ae5e1a'},
           ]
    threads = []
    for item in list:
        cname =item['cname']
        url =item['url']
        rela_chan =item['rela_chan']
        t = threading.Thread(target=toutiao,args=(cname,url,rela_chan,))#lufuli.Lufuli,args=("zhainafuli/",))
        #toutiao(cname,url,rela_chan)
        threads.append(t) 
    for t in threads:
        t.setDaemon(True)
        t.start()
        tt=20
        time.sleep(tt)
        tt+=2
    for t in threads:
        t.join()
    print "all over %s" %ctime()
    print "out toutiao. %s"%(ctime())
# Toutiao()