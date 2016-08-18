# -*- coding:UTF-8 -*-
from GetSoup import Soup
import re
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from random import random
from time import ctime,sleep
import os
from log.mylog import m_log
'''
Created on 2016-4-17

@author: Administrator
'''
# base_path=os.getcwd()
# #print base_path
# base_path=re.sub("test", '''text''', base_path)
# print base_path
# path=base_path+"\\"+"test2.txt"
# f=open(path,"w")
# filename ="test"
# my_log="aaaaaaaaaaaaaaaaaa"
# m_log(filename, my_log)

# imgs ="http://wallstreetcn.com/node/235686"
# # imgs =re.sub('''http://s(.?*)img=''',"",str(imgs))
# # imgs =re.sub("&size=130_87","", str(imgs))
# print re.search('http(.*)wall', imgs).group()
# soup=Soup('http://video.youdao.com/search?q=狗狗搞笑&ue=utf8&lq=狗狗&keyfrom=video.album.top').get_soup()
# print soup
# filename = r"E:/eclipse/workspace/TrinityCore/src/text/1.txt"
# f =open(filename,"w")
# print os.getcwd()
# content='''<video id="video001"  autoplay src="http://player.youku.com/player.php/sid/XMTUzMTg4MjE3Ng==/v.swf"></video><button>play</button>
#         <script type="text/javascript">
#         function play(){
#                 var myVideo=document.getElementById("video1");;
#                 myVideo.play();
#         }</script> '''
# print content
# 
data = {
      "id":"576a34beb2cd668a0d4add1c",
      "title" : '134',
      "content" :"content"
}
 
upload(data,is_update=True)
