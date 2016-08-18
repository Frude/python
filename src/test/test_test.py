# -*- coding:UTF-8 -*-
from GetSoup import Soup
import re
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from random import random
from time import ctime,sleep
# base_url ="http://mp.weixin.qq.com/"
# url="http://mp.weixin.qq.com/profile?src=3&timestamp=1462033207&ver=1&signature=acBkValXwihMvLOJFFdJiNRX1tLQcAz6pIdmJSMo9xnaZ7r41VcOeU-Al9sXbv4f2E2KIdk-doTlG24G3IAlVQ=="
# soup=get_html(url, 6, is_img=True, is_soup=False)#
#print soup

# div='''<div><span class="cmt">转发理由:</span>快过年了，是不是该让他也赢两把过个好年？[思考] //<a href="/n/%E6%9E%97%E6%9B%B4%E6%96%B0">@林更新</a>:小王，请你到时别怂。&nbsp;&nbsp;<a href="http://weibo.cn/attitude/Dgs9T27m0/add?uid=3716310005&amp;rl=0&amp;st=586bc5">赞[64071]</a>&nbsp;<a href="http://weibo.cn/repost/Dgs9T27m0?uid=1826792401&amp;rl=0">转发[3396]</a>&nbsp;<a class="cc" href="http://weibo.cn/comment/Dgs9T27m0?uid=1826792401&amp;rl=0#cmtfrm">评论[27533]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/Dgs9T27m0?rl=0&amp;st=586bc5">收藏</a><!---->&nbsp;<span class="ct">02月05日 17:44&nbsp;来自iPhone 6s</span></div>'''
# div=BeautifulSoup(div,"lxml")
# zan =div.find("a",text=re.compile(u"林"))
# print zan.text

print type(type( 'bs4.element.NavigableString'))