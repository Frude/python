# -*- coding:UTF-8 -*-
'''
Created on 2016-2-27

@author: Administrator
'''
import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from random import random
import time
def get_content(contents):
    if contents!=None:
        videos = contents.find_all("iframe" ,class_="video_iframe")
        if videos:
            for video in videos:
                src = video.get("data-src")
                if not src: return ""
                else:
                    #u'''<br />视频地址：<a href="'''+parent.a['href']+u'''">点击这里</a>'''
                    a='''<p data-href ="'''+src+'''" >这是视频</p>'''
                    a=BeautifulSoup(a,"lxml").p
                    video.replace_with(a)
        imgs=contents.find_all("img")
        for img in imgs:
            if img:
                img['height']='100%'
                img['width']='100%'
    else:
        return ""
    return str(contents)
def code(flag=True):
    if flag:
        url='http://182.254.137.53/wx/weixin.php'
        data ={'weixin':"name",
               "key":'a1b4f5e4caae69ddfe50f81f48a33881',
               'page':1}
        postdatastr=urllib.urlencode(data)
        request = urllib2.Request(url,postdatastr)
        response = urllib2.urlopen(request)
        dict = response.read()
        dict = eval(dict)
        print dict#['code']
        if dict['code']==4:
            print "none of message!"
            return {}
        return dict  
    else:
        dict ={'count': 10, 'code': 1, 'name': '\xe7\xa5\x9e\xe5\x90\x90\xe6\xa7\xbd', 'weixin': 'yiqishentucao8', 'content': [{'date': 1461751089, 'link': 'http:\\/\\/mp.weixin.qq.com\\/s?timestamp=1461764423&src=3&ver=1&signature=q6zBqnZRpDGVmaj9UNA20dpcJSY5nHmBwzPLiYnYehh1szS7u9-e6EVq1IkqQsGJT5W0jj3RohfJsp8OrwY02znqAo09ZHAlqQsKgZy2AS5o5*NKoU3P6o7XuvSOfwivhvuIB8Irw5-sNmczjbwRp9vGx6AcrqPM5qoRbQd5PyA=', 'title': '\xe6\x88\x91\xe7\x94\x9f\xe6\xb0\x94\xe6\x98\xaf\xe8\xa6\x81\xe7\x81\xad\xe6\x8e\x89\xe5\x9c\xb0\xe7\x90\x83\xe7\x9a\x84\xef\xbc\x81'}, {'date': 1461672153, 'link': 'http:\\/\\/mp.weixin.qq.com\\/s?timestamp=1461764423&src=3&ver=1&signature=q6zBqnZRpDGVmaj9UNA20dpcJSY5nHmBwzPLiYnYehh1szS7u9-e6EVq1IkqQsGJT5W0jj3RohfJsp8OrwY02-SdH8SwwTuXn6*b2rTNsSM**oK1Q8ZRAYMtRIAiCdVRaHsXjIrUAcDX9NJfBNFOQABu-xx8HZAmffqGVKTBqcc=', 'title': '\xe6\x88\x91\xe5\x9c\xa8\xe9\xab\x98\xe6\xbd\xae\xe4\xb8\xad\xe7\xbb\x93\xe6\x9d\x9f\xe4\xba\x86\xe4\xb8\x80\xe7\x94\x9f'}, {'date': 1461586297, 'link': 'http:\\/\\/mp.weixin.qq.com\\/s?timestamp=1461764423&src=3&ver=1&signature=q6zBqnZRpDGVmaj9UNA20dpcJSY5nHmBwzPLiYnYehh1szS7u9-e6EVq1IkqQsGJT5W0jj3RohfJsp8OrwY024mGbSxFAf7N90dNC7-HuEYWFsl5Mj2aY1ts2LoJlrYD751xpsXInyedEkPdCcRQ4btDZlyfyyPYVOsuWziVYUs=', 'title': '\xe8\x87\xb4\xe6\x8b\x8d\xe5\x8f\x8b\xef\xbc\x9a\xe8\xbf\x99\xe4\xba\x9b\xe5\xb9\xb4\xe6\x88\x91\xe4\xbb\xac\xe7\xbb\x8f\xe5\x8e\x86\xe7\x9a\x84N\xe7\xa7\x8d\xe9\xad\x94\xe6\x80\xa7\xe8\x87\xaa\xe6\x8b\x8d'}, {'date': 1461499283, 'link': 'http:\\/\\/mp.weixin.qq.com\\/s?timestamp=1461764423&src=3&ver=1&signature=q6zBqnZRpDGVmaj9UNA20dpcJSY5nHmBwzPLiYnYehh1szS7u9-e6EVq1IkqQsGJT5W0jj3RohfJsp8OrwY020wLGcfuCBKbdUHQZLKdvXRYSMpVK4TRsrc4*b-fPpfzff8yHO-7D3p1l17U0O8etTX4MHfC1ji5nbuFZp2sj2s=', 'title': '\xe7\xbb\x93\xe5\xa9\x9a\xe5\xbd\x93\xe5\xa4\xa9\xef\xbc\x8c\xe6\x96\xb0\xe9\x83\x8e\xe8\xb7\x9f\xe6\x9f\x90\xe4\xb8\xaa\xe5\xa5\xb3\xe4\xba\xba\xe8\xb5\xb0\xe4\xba\x86...'}, {'date': 1461412990, 'link': 'http:\\/\\/mp.weixin.qq.com\\/s?timestamp=1461764423&src=3&ver=1&signature=q6zBqnZRpDGVmaj9UNA20dpcJSY5nHmBwzPLiYnYehh1szS7u9-e6EVq1IkqQsGJT5W0jj3RohfJsp8OrwY027uXtaWFA2WCMDZto4Jab1DqvUGpyZTbE7fo3ndYXopDW6lDDkk1zvj*OceiMuJYmLTJcH6ol-*2uZw0u9631nY=', 'title': '\xe4\xbd\xa0\xe6\x83\xb3\xe7\xba\xa2\xef\xbc\x9f\xef\xbc\x81\xe8\xbf\x99\xe6\xa0\xb7\xe5\x81\x9a\xe5\xb0\xb1\xe5\x8f\xaf\xe4\xbb\xa5\xe8\xae\xa9\xe4\xbd\xa0\xe7\xba\xa2'}, {'date': 1461326422, 'link': 'http:\\/\\/mp.weixin.qq.com\\/s?timestamp=1461764423&src=3&ver=1&signature=q6zBqnZRpDGVmaj9UNA20dpcJSY5nHmBwzPLiYnYehh1szS7u9-e6EVq1IkqQsGJT5W0jj3RohfJsp8OrwY0260CVQQPpF-GrxgVqWHSHtz0Cq3PYgcGY1o2S*3JICvaveCJo8EPvPNXiR0ktO-mxHlSkewBcXkWB6wg5IOVEJM=', 'title': '\xe6\x89\xab\xe7\xa0\x81\xe6\xaf\x81\xe7\xa5\x9e\xe5\x89\xa7\xef\xbc\x81\xe6\x88\x91\xe5\xb0\xb1\xe6\x98\xaf\xe4\xb8\x8d\xe6\x8c\x89\xe5\xa5\x97\xe8\xb7\xaf\xe5\x87\xba\xe6\x8b\x9b\xef\xbc\x81'}, {'date': 1461240334, 'link': 'http:\\/\\/mp.weixin.qq.com\\/s?timestamp=1461764423&src=3&ver=1&signature=q6zBqnZRpDGVmaj9UNA20dpcJSY5nHmBwzPLiYnYehh1szS7u9-e6EVq1IkqQsGJT5W0jj3RohfJsp8OrwY02w52fWcYHvJELiSHG7PeHBcqNpol3CIb5KPpJ3MJJ89A5V0pZXNsjjAlWrcFU2eyBGcSuux7-P7U9jkrzuzyDIs=', 'title': '\xe9\xa9\xac\xe5\xbb\xba\xe5\x9b\xbd\xe8\x99\x90\xe7\x8b\x97\xe8\x99\x90\xe7\x8c\xab\xef\xbc\x8c\xe5\xa3\xb0\xe5\x8a\xbf\xe7\x9b\x96\xe8\xbf\x87papi\xe9\x85\xb1\xe6\x8b\x9b\xe6\xa0\x87\xe4\xbc\x9a\xef\xbc\x81\xe6\x9c\x80\xe5\x90\x8e\xe7\xbb\x93\xe6\x9e\x9c\xe7\xab\x9f\xe7\x84\xb6\xe6\x98\xaf\xe2\x80\xa6\xe2\x80\xa6'}, {'date': 1461154261, 'link': 'http:\\/\\/mp.weixin.qq.com\\/s?timestamp=1461764423&src=3&ver=1&signature=q6zBqnZRpDGVmaj9UNA20dpcJSY5nHmBwzPLiYnYehh1szS7u9-e6EVq1IkqQsGJT5W0jj3RohfJsp8OrwY027acyYMu1i5KhM6ga7AsiQSf-v8BMwtpkwWX-AtN2U9HAAD8GhhmAsaYT2Z9fAWn8-n8fHs-nN-CfwGa7ktyDVg=', 'title': '\xe8\xa7\x81\xe7\xbd\x91\xe5\x8f\x8b\xe7\xac\xac\xe4\xb8\x80\xe5\xa4\xa9\xe5\xb0\xb1\xe5\x95\xaa\xe5\x95\xaa\xe5\x95\xaa...\xe6\xb2\xa1\xe6\x83\xb3\xe5\x88\xb0...'}, {'date': 1461067219, 'link': 'http:\\/\\/mp.weixin.qq.com\\/s?timestamp=1461764423&src=3&ver=1&signature=q6zBqnZRpDGVmaj9UNA20dpcJSY5nHmBwzPLiYnYehh1szS7u9-e6EVq1IkqQsGJT5W0jj3RohfJsp8OrwY02xnv78TZ9ev88IuJ4K0umifWika-xh0gyIaimU3JZj577Vuu1e7RmyQQ4lrQz-L6cRzgfiBbxxQwTWX7nt-40kE=', 'title': '\xe5\x9b\xa0\xe6\x88\x8f\xe7\xbb\x93\xe7\xbc\x98\xef\xbc\x8c\xe7\x8e\x8b\xe5\xad\x90\xe5\x92\x8c\xe9\xaa\x91\xe5\xa3\xab\xe4\xbb\x8e\xe6\xad\xa4\xe8\xbf\x87\xe4\xb8\x8a\xe4\xba\x86\xe5\xb9\xb8\xe7\xa6\x8f\xe5\xbf\xab\xe4\xb9\x90\xe7\x9a\x84\xe7\x94\x9f\xe6\xb4\xbb'}, {'date': 1460983613, 'link': 'http:\\/\\/mp.weixin.qq.com', 'title': ''}], 'tips': 'success'}
        return  dict
def fix_dict(w_dict,rela_chan,imgs,type):
    #w_dict=final_weixin(name)
    cname=w_dict["cname"]
    #print cname
    title=w_dict["title"]
    print title
    url=w_dict["url"]
    print url
    my_funtion(cname,title,url,rela_chan,imgs,type)
def my_funtion(cname,title,url,rela_chan,imgs,type):
#     dict =code(False)
#     cname = dict['name']
#     count = 9
#     for i in range(0,count):
    seconds=random()*5
    print seconds
    time.sleep(seconds)
    #title = dict['content'][i]['title']
    #dict={"code":1, "tips":"success", "weixin":"withoutdistance", "name":"不要异地恋", "count":10, "content":[{"title":"【一百零三期】是谁来自五湖四海", "date":["1458741285"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=403018221&idx=1&sn=fbbed78c1b6a96380be35b63506a2a1b&3rd=MzA3MDU4NTYzMw==&scene=6"}, {"title":"【一百零三期】你是彩色照片,而我是幻灯机", "date":["1458741284"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=403018221&idx=2&sn=3185f5052124b98b71f482c30e606483&3rd=MzA3MDU4NTYzMw==&scene=6"}, {"title":"像动物一样地去爱", "date":["1458570917"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=402971328&idx=1&sn=055fdb5e2f34641d66abc68dfc5a7f77&3rd=MzA3MDU4NTYzMw==&scene=6"}, {"title":"【第一百一十二期】听到音乐就要动的帅帅的Poppin boy", "date":["1458570916"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=402971328&idx=2&sn=a3804e1b4038007f895d75c42b6ed4de&3rd=MzA3MDU4NTYzMw==&scene=6"}, {"title":"【微鸡汤,慎入】关于新栏目“众里寻她千百度”", "date":["1458399335"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=402925970&idx=1&sn=e594cfdba0d8b7478325c80ef446e7a2&3rd=MzA3MDU4NTYzMw==&scene=6"}, {"title":"这么送礼,难怪你单身!", "date":["1458399334"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=402925970&idx=2&sn=449c36cdcc537a9f84418cc6a6629282&3rd=MzA3MDU4NTYzMw==&scene=6"}, {"title":"失恋——这件难闻的事情", "date":["1458306584"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=402904059&idx=1&sn=bcc3ed0518d49ac0879cb7824d2398be&3rd=MzA3MDU4NTYzMw==&scene=6"}, {"title":"【一百零一期】你就是那么独一无二", "date":["1458306583"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=402904059&idx=2&sn=9611c7d71283e05c8d1d6134e7dc2d39&3rd=MzA3MDU4NTYzMw==&scene=6"}, {"title":"嘿,前面的女生,你掉了一封情书", "date":["1457962847"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=402831097&idx=1&sn=41c1746ec7f609790babfe53ca7c4238&3rd=MzA3MDU4NTYzMw==&scene=6"}, {"title":"【第一百期】在爱你这件事上,我会一心一意", "date":["1457962846"], "link":"http:\/\/mp.weixin.qq.com\/s?__biz=MzAwNDA0MTQyMQ==&mid=402831097&idx=3&sn=0d958e1d9706d8edd45ee7376af9ad6a&3rd=MzA3MDU4NTYzMw==&scene=6"}]}
    #url =  dict['content'][i]['link'].replace('\/', "/")
    #print url
    html = get_html(url,0,True)
    #print html
    soup=BeautifulSoup(html,"lxml")
    if type==1:
        content = soup.find('section' ,class_="article135")#.encode('utf8')
    elif type==2:
        content =soup.find('div', class_="rich_media_content")
    elif type==3:
        content =soup.find('div', class_="rich_media_area_primary")
    content =get_content(content)
    replaceBR = re.compile('data-src')
    text = re.sub(replaceBR,"img src",content)    
    data = {
              "title" : title,
              "content" :text, 
              "imgs" : imgs,
              "cname" : cname, 
              "url" : url, 
              "rela_chan" :rela_chan,
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "simg"
            }  
    upload(data)
# 5704f63c5ca8b98636298932     不要异地恋   withoutdistance
# 5704f63b36d809ac0ada467f     美剧百科      mjbkshare
# 5704f63b5ca8b98636298931     河北交广      hbjtgb992  yokacom

