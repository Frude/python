# -*- coding:UTF-8 -*-
from GetSoup import Soup
import re
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from Get_html import weixin
from upload import upload
from random import random
from time import ctime, sleep
import time
from pymongo.message import update
from test.gikrleyuan import fix_dict
import threading
def final_weixin(name, rela_chan, imgs, type):
    # name ="withoutdistance"
    BASE_URL = 'http://weixin.sogou.com'
    url = BASE_URL + '/weixin?query=' + name
    soup = Soup(url).get_soup()
    time.sleep(random() * 5)
    url_1 = soup.find("div", id=re.compile("sogou_vr"))['href']
    # print url_1
    cname = soup.find("div", class_="txt-box").h3.get_text(strip=True)
    print cname
    w_dict = {"cname":cname}
    for i in range(1, 5):
        print "***************************************"
        time.sleep(random() * 10)
        w_dict.update(weixin(url_1, i, False))
        # print w_dict
        fix_dict(w_dict, rela_chan, imgs, type)
        print "***************************************"
def Weixin():
#     list =[
#         {'name':'withoutdistance',  'rela_chan':'5704f63c5ca8b98636298932','imgs':'http://img01.sogoucdn.com/app/a/100520090/oIWsFt0MtPG7hhf4-EOcTAZ02TaI',"type":1},
#         {'name':'mjbkshare',        'rela_chan':'5704f63b36d809ac0ada467f','imgs':'http://img01.sogoucdn.com/app/a/100520090/oIWsFt9l5G3Hr-gkVJotAagXf7g8',"type":2},
#         {'name':'hbjtgb992',        'rela_chan':'5704f63b5ca8b98636298931','imgs':'http://img01.sogoucdn.com/app/a/100520090/oIWsFtzDuH6UaIIfT0YiOcxwiiLA',"type":2},
#         {'name':'yokacom',          'rela_chan':'5720d1a486813d7602d560ab','imgs':'http://wx.qlogo.cn/mmhead/Q3auHgzwzM7jCMTw97iaII15ytzfeH1kXB20A5kVOvo75LnftUTFgRg/0',"type":2},
#         {'name':'v_night',          'rela_chan':'5720d1c4f6d296e7796745be','imgs':'http://wx.qlogo.cn/mmhead/Q3auHgzwzM6Yia0MOq0katSuIaaWSOrR3nFRA8eib9c8QFC3dH0ppLnA/0',"type":2},
#         {'name':'yiqishentucao8',   'rela_chan':'5720d14699e0668a02ae5e13','imgs':'http://wx.qlogo.cn/mmhead/Q3auHgzwzM4Uub7DXIzhebp9ajP3LrrKMQAVrCbbr0DbBTcmbJILWw/0',"type":3},
#     #demoalpha       {'name':'hbjtgb992','rela_chan':'5720ce493e4ef78002c67c61','imgs':'http://img01.sogoucdn.com/app/a/100520090/oIWsFtzDuH6UaIIfT0YiOcxwiiLA',"type":2},
#            ]
    list = [
        {'name':'withoutdistance',      'rela_chan':'5704f63c5ca8b98636298932', 'imgs':'http://img01.sogoucdn.com/app/a/100520090/oIWsFt0MtPG7hhf4-EOcTAZ02TaI', "type":2},
        {'name':'biaoqingcangku',       'rela_chan':'573b52dd8e269a8943b3d43a', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E8%A1%A8%E6%83%85%E4%BB%93%E5%BA%93.jpg', "type":2},
        {'name':'ghostimes',            'rela_chan':'573b526982f8d0a63fb896d1', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E9%83%AD%E6%96%AF%E7%89%B9.jpg', "type":3},
        {'name':'YesFakeshion',         'rela_chan':'573b477586db98572b95f7ae', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/Fakeshion.jpg', "type":3},
        {'name':'witheating',           'rela_chan':'573b470e8e269a8943b3d3e0', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E9%A3%9F%E5%B8%96.jpg', "type":3},
        {'name':'voicer_me',            'rela_chan':'573b46bf379de6bc2a45753d', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/Voicer.jpg', "type":3},
        {'name':'sixiangjujiao-weixin', 'rela_chan':'573b465ee473acba20ca784a', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%80%9D%E6%83%B3%E8%81%9A%E7%84%A6.jpg', "type":3},
        {'name':'xwcbxy',               'rela_chan':'573b45fa19cdb68f2dc726f6', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%96%B0%E9%97%BB%E4%BC%A0%E6%92%AD%E5%AD%A6%E7%A0%94.jpg', "type":3},
        {'name':'ijiaboshi',            'rela_chan':'573b459b19cdb68f2dc726f3', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%81%87%E5%8D%9A%E5%A3%AB.jpg', "type":3},
        {'name':'shenyefachi',          'rela_chan':'573b453de473acba20ca783e', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B7%B1%E5%A4%9C%E5%8F%91%E5%AA%B8.jpg', "type":2},
        {'name':'weiguanggao',          'rela_chan':'573b44d486db98572b95f797', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/4A%E5%B9%BF%E5%91%8A%E6%8F%90%E6%A1%88.jpg', "type":3},
        {'name':'TDCADS',               'rela_chan':'573b441386db98572b95f792', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/3D%E5%88%9B%E6%84%8F%E5%B9%BF%E5%91%8A.jpg', "type":3},
        {'name':'land-2013',            'rela_chan':'573b439382f8d0a63fb8965c', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%BE%AE%E8%AE%BE%E8%AE%A1.jpg', "type":2},
        {'name':'haibaofugu',           'rela_chan':'573b4334c1b95f7434de4e2c', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%A4%8D%E5%8F%A4%E6%B5%B7%E6%8A%A5.jpg', "type":2},
        {'name':'Lensmagazine',         'rela_chan':'573b42d186db98572b95f788', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/Lens%E6%9D%82%E5%BF%97.jpg', "type":2},
        {'name':'ziti2015',             'rela_chan':'573b425fe473acba20ca7830', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%88%98%E5%85%B5%E5%85%8B%E5%AD%97%E4%BD%93.jpg', "type":3},
        {'name':'thecity2015',          'rela_chan':'573b15cd19cdb68f2dc724de', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E9%82%A3%E4%B8%80%E5%BA%A7%E5%9F%8E.jpg', "type":3},
        {'name':'yyetsustv',            'rela_chan':'573b14d18e269a8943b3d1bf', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/YYeTs%E7%BE%8E%E5%89%A7.jpg', "type":3},
        {'name':'duliyumovie',          'rela_chan':'573b14588e269a8943b3d1b6', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E7%8B%AC%E7%AB%8B%E9%B1%BC%E7%94%B5%E5%BD%B1.jpg', "type":3},
        {'name':'huangcanranstation',   'rela_chan':'573b13d28e269a8943b3d1b0', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E9%BB%84%E7%81%BF%E7%84%B6%E5%B0%8F%E7%AB%99.jpg', "type":3},
        {'name':'unipus',               'rela_chan':'573b131f379de6bc2a457263', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%A4%96%E7%A0%94%E7%A4%BEUnipus.jpg', "type":3},
        {'name':'tianluo_hhhaze',       'rela_chan':'573b12a75f401b53347166c8', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E7%94%B0%E8%9E%BA%E5%A7%91%E5%A8%98.jpg', "type":3},
        {'name':'Chinadaily_Mobile',    'rela_chan':'573b12075f401b53347166bc', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%8F%8C%E8%AF%AD%E6%96%B0%E9%97%BB.jpg', "type":3},
        {'name':'ilove-eat',            'rela_chan':'573b11848e269a8943b3d191', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%9D%AD%E5%B7%9E%E5%90%83%E8%B4%A7.jpg', "type":3},
        {'name':'fanyiluntan',          'rela_chan':'573b10f05f401b53347166a9', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E7%BF%BB%E8%AF%91%E6%95%99%E7%A0%94.jpg', "type":3},
        {'name':'withniyining',         'rela_chan':'573b1046b33292991f8d3f82', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%98%8E%E7%88%B1%E6%9A%97%E6%81%8B.jpg', "type":3},
        {'name':'v_danshen',            'rela_chan':'573b0669379de6bc2a457131', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%8D%95%E8%BA%AB%E7%8B%97.jpg', "type":3},
        {'name':'zuiheikeji',           'rela_chan':'573b05da86db98572b95f3cf', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%9C%80%E9%BB%91%E7%A7%91%E6%8A%80.jpg', "type":3},
        {'name':'newWhatYouNeed',       'rela_chan':'573aeb92b33292991f8d3b5c', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%88%91%E8%A6%81wyn.jpg', "type":3},
        {'name':'zgdfxy15j',            'rela_chan':'572504a24ad28a570b166395', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/GiveM1Five.jpg', "type":3},
        {'name':'falvboke',             'rela_chan':'5725042b639ee5cf7be0c82a', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B3%95%E5%BE%8B%E5%8D%9A%E5%AE%A2.jpg', "type":3},
        {'name':'ZJUTXYH',              'rela_chan':'572503c6e3be9d7b08f65082', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B5%99%E5%B7%A5%E6%A0%A1%E5%8F%8B%E4%BC%9A.jpg', "type":3},
        {'name':'yunfalvshitong',       'rela_chan':'5724ffa0b674b4937b82e818', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%BE%8B%E4%BA%8B%E9%80%9A.jpg', "type":3},
        {'name':'zjutweixin',           'rela_chan':'5724ff44639ee5cf7be0c825', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B5%99%E5%B7%A5%E5%AD%A6%E7%94%9F%E4%BC%9A.jpg', "type":3},
        {'name':'zhihedongfang',        'rela_chan':'5724feba6cf5b5517253a6a5', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%99%BA%E5%90%88%E6%B3%95%E5%AA%92%E4%BD%93.jpg', "type":3},
        {'name':'way2en',               'rela_chan':'5724fe3d017625777c9d9f7f', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%94%AF%E9%80%94%E8%8B%B1%E8%AF%AD.jpg', "type":3},
        {'name':'xdf-cet46',            'rela_chan':'5724fde3f12ca6ab7a863fdc', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%9C%A8%E7%BA%BF%E5%9B%9B%E5%85%AD%E7%BA%A7.jpg', "type":3},
        {'name':'zjut_tw',              'rela_chan':'5724fd8be3be9d7b08f65077', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B5%99%E5%B7%A5%E5%A4%A7%E5%9B%A2%E5%A7%94.jpg', "type":3},
        {'name':'shajiabang8',          'rela_chan':'5724fd1f017625777c9d9f7d', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%8F%A3%E7%90%B4.jpg', "type":3},
        {'name':'hzlongre',             'rela_chan':'5724fcc914e6550f7e0d4878', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%9D%AD%E5%B7%9E%E6%9C%97%E9%98%81.jpg', "type":3},
        {'name':'tttangH5',             'rela_chan':'5724fc6c639ee5cf7be0c821', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E8%B7%B3%E8%B7%B3%E7%B3%96.jpg', "type":2},
        {'name':'xingfacaiyaqi',        'rela_chan':'5724fc18b674b4937b82e813', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%88%91%E6%B3%95%E5%A4%A9%E4%B8%8B.jpg', "type":3},
        {'name':'gcdyweixin',           'rela_chan':'5724fb51639ee5cf7be0c81f', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%85%B1%E4%BA%A7%E5%85%9A%E5%91%98.jpg', "type":3},
        {'name':'imwrdy',               'rela_chan':'5724faf0017625777c9d9f79', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B8%A9%E6%9F%94%E7%9A%84%E5%A4%9C.jpg', "type":3},
        {'name':'ddy98com',             'rela_chan':'5724fa8fe3be9d7b08f65070', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E7%82%B9%E7%82%B9%E7%9B%88.jpg', "type":3},
        {'name':'yyjq9988',             'rela_chan':'5724fa1ae3be9d7b08f6506e', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E7%B2%A4%E8%AF%AD%E9%87%91%E6%9B%B2.jpg', "type":3},
        {'name':'fygc20140416',         'rela_chan':'5724f992639ee5cf7be0c81b', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B3%95%E7%9C%BC%E8%A7%82%E5%AF%9F.jpg', "type":3},
        {'name':'faxuexinqingnian',     'rela_chan':'5724f924b674b4937b82e80b', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B3%95%E5%AD%A6%E6%96%B0%E9%9D%92%E5%B9%B4.jpg', "type":3},
        {'name':'hangzhou8090',         'rela_chan':'5724f8bc4ad28a570b16637f', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%9D%AD%E5%B7%9E%E5%A4%B4%E6%9D%A1.jpg', "type":3},
        {'name':'zjuthelp',             'rela_chan':'5724f7f14ad28a570b16637e', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E5%B7%A5%E5%A4%A7%E5%8A%A9%E6%89%8B.jpg', "type":2},
        {'name':'gh_06237f6e7d40',      'rela_chan':'5724f770f12ca6ab7a863fce', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%BD%AE%E6%B5%81Pa.jpg', "type":2},
        {'name':'chinazuel',            'rela_chan':'5724f6cfe3be9d7b08f65068', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%AF%8F%E5%A4%A9%E6%B3%95%E5%BE%8B.jpg', "type":2},
        {'name':'frontiers-of-law',     'rela_chan':'5724f66ab674b4937b82e807', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B3%95%E5%AD%A6%E5%AD%A6%E6%9C%AF%E5%89%8D%E6%B2%BF.jpg', "type":3},
        {'name':'lawreaders',           'rela_chan':'5724f5c114e6550f7e0d4870', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B3%95%E5%BE%8B%E8%AF%BB%E5%BA%93.jpg', "type":2},
        {'name':'OSCAR-Cinema',         'rela_chan':'5724f543639ee5cf7be0c818', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E4%B9%90%E6%B8%85%E5%A5%A5%E5%BD%B1.jpg', "type":2},
        {'name':'zhshy06',              'rela_chan':'5724f4854ad28a570b16637d', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E8%89%BA%E6%9C%AF%E4%B9%A6%E7%94%BB%E7%A0%94%E7%A9%B6%E9%99%A2.jpg', "type":3},
        {'name':'v_night',              'rela_chan':'5720d1c4f6d296e7796745be', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%99%9A%E5%AE%89%E5%B0%91%E5%B9%B4.jpg', "type":2},
        {'name':'yokacom',              'rela_chan':'5720d1a486813d7602d560ab', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B5%99%E5%B7%A5%E5%A4%A7%E5%9B%A2%E5%A7%94.jpg', "type":2},
        {'name':'yiqishentucao8',       'rela_chan':'5720d14699e0668a02ae5e13', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E7%A5%9E%E5%90%90%E6%A7%BD.jpg', "type":3},
        #{'name':'withoutdistance',      'rela_chan':'5704f63c5ca8b98636298932', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E4%B8%8D%E8%A6%81%E5%BC%82%E5%9C%B0%E6%81%8B.jpg', "type":3},
        {'name':'mjbkshare',            'rela_chan':'5704f63b36d809ac0ada467f', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E7%BE%8E%E5%89%A7%E7%99%BE%E7%A7%91.jpg', "type":2},
        {'name':'hbjtgb992',            'rela_chan':'5704f63b5ca8b98636298931', 'imgs':'http://7xrk3y.com1.z0.glb.clouddn.com/%E6%B2%B3%E5%8C%97%E4%BA%A4%E5%B9%BF.jpg', "type":2},
    ]
    print "in weixin. %s" % (ctime())
    threads = []
    for item in list:
        name = item['name']
        rela_chan = item['rela_chan']
        imgs = item['imgs']
        type = item["type"]
#         t = threading.Thread(target=final_weixin, args=(name, rela_chan, imgs, type,))  # lufuli.Lufuli,args=("zhainafuli/",))
#         # toutiao(cname,url,rela_chan)
#         threads.append(t) 
        final_weixin(name, rela_chan, imgs,type)
        time.sleep(5)
#     for t in threads:
# #         t.append()
#         t.setDaemon(True)
#         t.start()
#     for t in threads:
#         t.join()
#     print "all over %s" % ctime()
    print "out weixin. %s" % (ctime())
Weixin()
