# -*- coding:UTF-8 -*-
from apicloud.dataCloud import DataCloud
import os
from apicloud.mysqldb import insert_db
import re
import logging
def my_update(data,appId,appKey):
    url ='https://d.apicloud.com/mcm/api'
    client = DataCloud(appId, appKey,url);
    id=data['id']
    bodyParm= {"$set":data,"_method":"PUT","fields":["id","title"]}
    result= client.updateObject("article",id,bodyParm)
#     for i,j in result[0].items():
#         print "***************"
#         print i
#         print j
#         print "&&&&&&&&&&&&&&&"
def shujuku_quchong(data):
    return insert_db("apicloud", "isouji", data)
def quchong(data,is_url):
    flag = True
    m=0
    base_path=os.getcwd()
    #print( base_path
    base_path=re.sub("test", "text", base_path)
    base_path=re.sub("thread", "text", base_path)
    file_name =base_path+"\\"+data['rela_chan']+".txt"
    #print file_name
    if os.path.exists(file_name)== False:
        print( "document not exists")
        f = open(file_name,"w")
#         f.write(str(data['cname'])+':')
        f.close()
    f= open(file_name)
    article_url=data['url']
    article_title=data['title']
    if is_url:
        url_list=f.readlines()
        for url in url_list:
            if url[-1] == '\n':
                url = url[0:-1]
            #print( url#qu chu huan hang)
            if article_url == url:
#                 print( "already exits")
                flag = False
                break
        f.close()
        with open(file_name, 'a') as handle:
            if flag == True:
                handle.write('\n')
#                 print( "add this one = "+article_url)
                handle.writelines(article_url)
    else:
        title_list=f.readlines()
        for title in title_list:
            if title[-1] == '\n':
                title = title[0:-1]
            #print( url#qu chu huan hang
            if article_title == title:
#                 print( "already exits")
                flag = False
                break
        f.close()
        with open(file_name, 'a') as handle:
            if flag == True:
                handle.write('\n')
#                 print( "add this one = "+article_title)
                handle.writelines(article_title)
            handle.close()
    
    return flag
def is_empty(data):
    #print( "############"
    flag =True
    #print( type(data['content'])
    #print( data['content']
    if data['content']==None:
        print "content is empty!"
        flag=False
        return flag   
    if data['content'].strip()=="None":
        print "content is empty!"
        flag=False
    if data['content'].strip()=="":
        print "content is empty!"
        flag=False
    return flag
    print( "################")
def fix_yw_url(data):
    newurl=data["url"]
    if data["cname"]=="虎牙lol视频":
        return data
    if data["cname"]=="天下3荒火论坛" or data["cname"]=="杭活动行" or data["cname"]=="炉石动态":
        #return data
        yw_url ='''<br />原文地址：<a href="'''+str(newurl)+'''">点击这里</a>'''
    else:
        yw_url ='''<br />原文地址：<a href="'''+str(newurl)+'''">点击这里</a>'''
    print type(data["content"])
    print type(yw_url)
    if type(data["content"])==type(yw_url):
        data["content"]+=yw_url
    else:
        data["content"]+=u'''<br />原文地址：<a href="'''+str(newurl)+u'''">点击这里</a>'''
    return data
def upload(data,is_url=True,is_test=False,is_update=False):
#     global logging
#     logging=my_log
    print "DATA_length :"+str(len(data["content"]) )
    flag=True
    flag = flag and is_empty(data)
    if flag==False:
        print "uploading is cancel!"
        return
    if is_test:
        appId ='A6904605533915'
        appKey = 'D3198CC8-C0F4-1CCF-68F2-4ED8797F6C24'
        #zhe shi demo alpha
    else:
        appId = "A6916673745899"
        appKey = "C87DDCD6-A28E-D6B3-2DE9-0538F414FC57"
# zhe shi isouji
#         appId = "A6918925738115"
#         appKey = "81D55EB9-D55E-11D8-5602-5CBA0DCAE7DA"
#         zheshi xinban isouji
        if is_update:
            my_update(data,appId,appKey)
            return
        flag=flag and quchong(data,is_url) 
        flag=flag and shujuku_quchong(data)
#         print "Falg2",flag
        if flag==False:
            print "already exits!"
            print "uploading is cancel!"
            return
        # zhengshi ban 
#     print "106"+flag 
    if flag==False:
        print "uploading is cancel!"
        return
    else:
        print "add this one : "+data["title"]
    url ='https://d.apicloud.com/mcm/api'
    client = DataCloud(appId, appKey,url);
    client.createObject('article', fix_yw_url(data))
    