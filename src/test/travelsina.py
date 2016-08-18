# -*- coding:UTF-8 -*-
from GetSoup import Soup
import re
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from random import random
from time import ctime,sleep
'''
Created on 2016-4-17

@author: Administrator
'''
def fix_img(content):
    if(content==None):return ''
    if type(content)==str: return content
    imgs=content.find_all('img')
    if imgs!=None:
        for img in imgs:
            if img:
                img['height']='100%'
                img['width']='100%'
    return str(content)
def travelsina(cname,url,rela_chan):
    #url='http://news.yodao.com/search?q=每日轻松一刻'
    #travelsina =get_html(url, -1, False)
    #print travelsina
    #sina_1 = get_html(url,5,is_img=True,is_soup=True)
    travelsina =Soup(url,"").get_soup()
    #print travelsina
    
    #news_list = sina_1.find_all("li" ,class_="clearfix",limit=1)
    news_list = travelsina.find_all("dl" ,class_="carditems_list" ,limit=1)
    #print news_list
    for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        img=news.find('img')
        new_url =news.parent['href']
        print new_url
        imgs = img['src']
        print imgs
        h3=news.find('h3')
        title= h3.get_text(strip=True)
        print title
        html2=get_html(new_url,0,False,False)
        soup2=BeautifulSoup(html2,"lxml")
        #soup2=Soup(new_url,"").get_soup()
        #print soup2.body
        content =soup2.find("div" ,class_="wrapper")
        content= fix_img(content)
        print content
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : cname, 
              "url" : new_url, 
              "rela_chan" : rela_chan, 
              #571340d4975f6bf2044eeea9#weijiezhimi
              #56f93be7508421125656a612#caijin
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "simg"
        }
        upload(data,True,True)
        print '*********************************'
    
print "in travelsina. %s"%(ctime())
def Travelsina():
    list =[
           {"cname":"新浪旅游","url":"http://gonglue.travel.sina.cn/?vt=4","rela_chan":'5720ce493e4ef78002c67c61'},
           #{"cname":"新浪健康","url":"http://health.sina.cn/healthcare/index.d.html?vt=4&pos=42","rela_chan":'57173f3d5fefa0ce23755183'},
           ]
    for item in list:
        cname =item['cname']
        url =item['url']
        rela_chan =item['rela_chan']
        travelsina(cname,url,rela_chan)
    print "out travelsina. %s"%(ctime())
# Travelsina()