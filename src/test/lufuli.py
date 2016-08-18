# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from Save import Save
from GetSoup import Soup
from apicloud.dataCloud import DataCloud
from upload import upload
from time import ctime,sleep
from random import random
import time
from apicloud.mysqldb import insert_db
from MySQLdb.constants.FIELD_TYPE import NULL
import sys
from log import mylog
from log.mylog import   m_log
import logging
import os
# from my_final_log import initLogging
# # from my_final_log import initLogging



def get_content(contents):
    time.sleep(random())
    if contents!=None:
        s=contents.find('p', class_='post-copyright')
        if s:s.extract()
        imgs=contents.find_all("img")
        for img in imgs:
            if img:
                img['height']='100%'
                img['width']='100%'
    else:
        return ""
    #logging.info( contents
    #logging.info( str(contents)
    return str(contents)
# def get_content(contents):
#     time.sleep(random())
#     content = u''
#     if contents!=None:
#         s=contents.find('p', class_='post-copyright')
#     else:
#         return u""
#     for cont in contents:
#         if cont==s:continue  
#         if (cont.string != None):
#             #logging.info( cont.string
#             content += u'<br />' + cont.string
#         elif(cont.img != None):
#             for img in cont.find_all("img"):
#                 # logging.info( img
#                 img['height'] = '100%'
#                 img['width'] = '100%'
#                 content += img.decode()
#             #logging.info( cont.get_text()
#             content += u'<br />' + cont.get_text(strip=True) 
#         elif(cont.strong != None):
#             content +=cont.strong.decode()
#         else:
#             #logging.info( cont.get_text()
#             content += u'<br />' + cont.get_text(strip=True) 
#     return content
def my_lufuli(logging):


    #http://lufuli.net/zhainanfuli/
    #http://lufuli.net/chuchu/
    #http://lufuli.net/author/yang/
    soup = Soup("http://www.lufuli.net/?jdfwkey=n9jzw3").get_soup()
    #logging.info( soup
    parents = soup.find_all("article", class_="excerpt excerpt-one",limit=10)
    for parent in parents:
        logging.info( '*********************************')
        seconds=random()*5
        logging.info( seconds)
        time.sleep(seconds)
        title = parent.header.h2.a.get_text()
        logging.info( title )
        imgs = parent.find("img", class_="thumb").get('data-original')
        #logging.info( imgs))
        new_url = parent.h2.a['href']
        logging.info( new_url)
        soup2 = Soup(new_url).get_soup()
        contents = soup2.find('article', class_='article-content')
        #logging.info( type(contents))
        #logging.info( contents)
        pages =soup2.find('div', class_="article-paging")
        #logging.info( pages)
        content = ''
        if (pages!=None) :
            page_content =soup2.find('div', class_="article-social").find_previous('a')
            page =int(page_content.get_text())
            url_base=str(page_content['href']).replace(page_content.get_text()+'/',"")
            for i in range(1,page+1):
                url=url_base+str(i)+'/'
                #logging.info( url))
                soup3=Soup(url).get_soup()
                contents3 = soup3.find('article', class_='article-content')
                content+=get_content(contents3)
            #logging.info( content)
        else:
            content=get_content(contents)
        cname = '撸福利'
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : "撸福利", 
              "url" : new_url, 
              "rela_chan" : '56f8ec1ced37c342644271e0', 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "img"
            } 
        #insert_db("apicloud", "isouji", data) 
        upload(data)
        logging.info( '*********************************')



def Lufuli():
    #sys.stdout = open('lufuli.log', 'a')
    filename = "lufuli.log";
#     my_l=logging.getLogger(filename)
#     logging=initLogging(filename,my_l)
    logging.info( "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    logging.info( "in lufuli. %s"%(ctime()))
    try:
        l=my_lufuli(logging)
    finally:
        logging.info( "out lufuli. %s"%(ctime()))
        logging.info( "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     for i in  logging.handlers:
#         logging.removeHandler(i)
#     print logging.handlers
    
#     logging.warn(sys.stderr)
# Lufuli()

