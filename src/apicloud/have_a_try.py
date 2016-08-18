# -*- coding: UTF-8 -*-
'''
Created on 2016-3-18

@author: Administrator
'''
from dataCloud import DataCloud
appId ='A6902143139612'
appKey = 'AB1B8AFF-E1E4-D552-2979-37313E96D43A'
url ='https://d.apicloud.com/mcm/api'
client = DataCloud(appId, appKey,url);
attr = {'title':'aaaa','brief':'ccccccc'}
client.createObject('channel', attr)
print client.getObject('channel', '000000000000000000000001').get('brief')
