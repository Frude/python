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
def baishantansuo(cname,url,rela_chan):
    #url='http://news.yodao.com/search?q=每日轻松一刻'
    baishantansuo =Soup(url).get_soup()
    #print baishantansuo
    
    news_list = baishantansuo.find_all('div', class_="list-item block-item",limit =10)
    for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url =news.span.a['href']
        print new_url
        imgs =news.span.a.img['data-original']
        print imgs
        title= news.span.a.img['alt']
        print title
        content =''
        while(True):
            seconds=random()*5
            print seconds
            sleep(seconds)
            soup2=Soup(new_url).get_soup()
            content+=str(soup2.find('div',id="art_main"))
            page=soup2.find('a',class_="nextpage")
            if page!=None:
                new_url =page['href']
                print new_url
            else:
                break
        #print content
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
        upload(data)
        print '*********************************'
    
print "in baishantansuo. %s"%(ctime())
list =[
       {"cname":"未解之谜","url":"http://www.83133.com/weijiezhimi/","rela_chan":'571340d4975f6bf2044eeea9'},
       {"cname":"科学探索","url":"http://www.83133.com/kexuetansuo/","rela_chan":'571347fc70569bda38cb86f3'},
       ]
for item in list:
    cname =item['cname']
    url =item['url']
    rela_chan =item['rela_chan']
    baishantansuo(cname,url,rela_chan)
print "out baishantansuo. %s"%(ctime())