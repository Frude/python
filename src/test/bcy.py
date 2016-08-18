# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import json
import cookielib
import time
from bs4 import BeautifulSoup
from Save import Save
from GetSoup import Soup
from apicloud.dataCloud import DataCloud
from upload import upload
from random import random
import datetime
from time import ctime,sleep
from apicloud.mysqldb import insert_db
import logging
# from my_final_log import initLogging

'''
Created on 2016-3-19

@author: Administrator
'''
def bcy(logging):
    baseURL = 'http://bcy.net'
    url= "http://bcy.net/coser/toppost100?type=lastday"
    soup= Soup(url).get_soup()
    #logging.info( soup
    
    
    contents = soup.find_all('li', class_="l-work-thumbnail",limit=10)
    for cont in contents:
        logging.info( "******************************************")
        seconds=random()*5
        logging.info( seconds)
        time.sleep(seconds)
        today = datetime.date.today()
        #logging.info( today.strftime("%m月%d日 ")
        title = str(today.month).decode()+u'月'+str(today.day).decode()+u'日第'+cont.span.get_text()+u' : '+cont.div.div.a['title']
        logging.info( title)
        new_url = baseURL+cont.div.div.a['href']
        logging.info( new_url)
        soup2= Soup(new_url).get_soup()
        content = soup2.find('div',class_="post__content js-content-img-wrap js-fullimg js-maincontent mb20")
        content =str(content)
        imgs= cont.div.div.a.img['src']
        imgs=str(imgs)
        #imgs =re.sub("/2X3","",str(imgs))
        logging.info( imgs)
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : "半次元", 
              "url" : new_url, 
              "rela_chan" : '56f8ec1627b94d9119fcecef', 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "img",
            } 
        #insert_db("apicloud", "isouji", data) 
        upload(data)
        logging.info( "*********************************************************")
def Bcy():
    #sys.stdout = open('lufuli.log', 'a')
    filename = "bcy.log";
#     my_l=logging.getLogger(filename)
#     logging=initLogging(filename,my_l)
    logging.info( "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    logging.info( "in bcy. %s"%(ctime()))
    try:
        b=bcy(logging)
    finally:
        logging.info( "out bcy. %s"%(ctime()))
        logging.info( "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     for i in  logging.handlers:
#         logging.removeHandler(i)
#     logging.warn(sys.stderr)
# Bcy()