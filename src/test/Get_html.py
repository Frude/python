# -*- coding:UTF-8 -*-
from selenium import webdriver
import selenium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # available since 
from bs4 import BeautifulSoup
import requests
import logging
import re
import time
import urllib
from urllib import urlopen
import random

UA = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"

def get_html(url, flag, is_img=True, is_soup=False):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        UA
    )
    dcap["takesScreenshot"] = (False)
    #t0 = time.time()
    try:
        if is_img == True:
            driver = webdriver.PhantomJS(desired_capabilities=dcap)#, service_args=['--load-images=no'])
        else:
            driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=no'])
        driver.set_page_load_timeout(240)
    except NoSuchElementException:#selenium.common.exceptions.WebDriverException:
        return None
    try:
        driver.get(url)
        driver.get_screenshot_as_file('show' + str(flag) + '.png')
        if flag == 6:
            new_url = get_target_url(driver)
            print "new_url:", new_url
            #return #get_html(new_url,0,is_img=True,is_soup=True)
        if flag == 1:
            driver.find_element_by_xpath('//*[@id="filterByCity"]/li[6]/a').click()
        if flag == 3:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="pagelet-nfeedlist"]/ul/li[1]/div''').is_displayed())
        if flag == 2:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="main-container"]/div[2]''').is_displayed())
        if flag == 4:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="artibody"]''').is_displayed())
        #/html/body/div[8]/div[7]/div[1]/div[2]/ul[1]/li[1]
        if flag == 5:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''/html/body/div[8]/div[7]/div[1]/div[2]/ul[1]/li[1]''').is_displayed())
        
        if flag == 7:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="container"]/div[1]/div[2]/div[1]''').is_displayed())
        
        if flag == 8:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="container"]/div[1]/div[2]/div[2]/div[1]/ul/li[1]''').is_displayed())
        
        if flag == 9:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="wLiveplayerUserInfo"]/a[1]''').is_displayed())
        if flag == 10:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="ng-app"]/div/div[2]/div[3]/ul/li[3]/div/div/a[1]/img''').is_displayed())
        if flag == 11:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="play-user-avatar"]''').is_displayed())
        if flag == 12:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="LF-area-video"]/div[2]/dl/dt/div/img''').is_displayed())
        if flag == 13:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath(''' //*[@id="pic_wall"]/div/ul/li[1]''').is_displayed())
        if flag == 14:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath(''' //*[@id="anchorHeader"]''').is_displayed())
        if flag == 15:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath(''' /html/body/div[8]/div/div[2]/div[6]/div[3]/h3/span[1]/em''').is_displayed())
        if flag == 16:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''/html/body/div[8]/div/div[2]/div[3]/div[1]/div[2]/span''').is_displayed())
        
        if flag == 17:
            WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="js-chat-cont"]/div[2]/ul/li[187]''').is_displayed())
        
     
        html = driver.page_source

    except Exception as e:
        html = None
        logging.error(e)
    finally:
        driver.get_screenshot_as_file('show.png')
        #print driver.title
        #print driver.page_source
        html = driver.page_source
        driver.quit()
    if is_soup:
        return BeautifulSoup(html, "lxml")
    return html
def get_target_url(driver, box_a):
        """
        get real url(without encryption) of target page
        :param no: NO.
        :return target_url:
        :Usage:
        """
        #box_a = driver.find_element_by_xpath(path)       # 找到标题元素并点击
        #print driver.find_element_by_tag_name("div").get_attribute("class")
        current_handle = driver.current_window_handle#保留当前窗口句柄
        box_a.click()
#         for handle in driver.window_handles:
#             if handle == current_handle:
        target_url = driver.current_url
        #print "target_url",target_url
        
#         driver.forward()
#         driver.forward()
        #print driver.title
#                 continue
#             else:
#                 #   切换到文章正文窗口，获取url后关闭，并回到主窗口
#                 driver.switch_to_window(handle)
#                 target_url = driver.current_url
#                 driver.close()
#                 driver.switch_to_window(current_handle)
#                 driver.get_screenshot_as_file('wodetian.png')
#                 print "wode tian!!"
        return target_url    
def weixin(url, flag, is_img=False):
#     data={"url":"",
#           "title:":"",
#           }
    w_dict = {"title":"", "url":""}
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        UA
    )
    dcap["takesScreenshot"] = (False)
    #t0 = time.time()
    try:
        if is_img == True:
            driver = webdriver.PhantomJS(desired_capabilities=dcap)#, service_args=['--load-images=no'])
        else:
            driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=no'])
        driver.set_page_load_timeout(240)
    except NoSuchElementException:#selenium.common.exceptions.WebDriverException:
        return None
    try:
        driver.get(url)
        driver.get_screenshot_as_file('show.png')
        list = driver.find_elements_by_class_name("weui_media_title")
        m = 0
        for item in list:
            m += 1
            if not m == flag:    
                continue
            path = item
            #print path
            new_url = get_target_url(driver, path)
            w_dict["url"] = new_url
        #driver.forward()
        w_dict["title"] = driver.title
        #print "new_url:",new_url
        #html = driver.page_source
    except Exception as e:
        #html = None
        logging.error(e)
    finally:
        driver.get_screenshot_as_file('show.png')
        #print driver.title
        #print driver.page_source
        #html = driver.page_source
        driver.quit()
    return w_dict
def weibo():
    UA1 = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4"
    is_img = True
    is_soup = True
    url = "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F"
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        UA1
    )
    dcap["takesScreenshot"] = (False)
    #t0 = time.time()
    try:
        if is_img == True:
            driver = webdriver.PhantomJS(desired_capabilities=dcap)#, service_args=['--load-images=no'])
        else:
            driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=no'])
        driver.set_page_load_timeout(240)
    except NoSuchElementException:#selenium.common.exceptions.WebDriverException:
        return None
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="loginName"]''').is_displayed())
        driver.find_element_by_xpath('''//*[@id="loginName"]''').send_keys("961373747@qq.com")
        driver.find_element_by_xpath('''//*[@id="loginPassword"]''').send_keys("961373747")
        driver.find_element_by_xpath('''//*[@id="loginAction"]''').click()
        driver.get('http://m.weibo.cn/d/fbb0916')
        WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="boxId_1463836806971_17"]''').is_displayed())
        #//*[@id="loginname"]
        #//*[@id="loginAction"]
        #driver.find_element_by_xpath('''//*[@id="loginname"]''').text="961373747"
        
        
        driver.get_screenshot_as_file('show.png')
       
            #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('''/html/body/div[8]/div[7]/div[1]/div[2]/ul[1]/li[1]''').is_displayed())
        html = driver.page_source

    except Exception as e:
        html = None
        logging.error(e)
    finally:
        driver.get_screenshot_as_file('show.png')
        #print driver.title
        #print driver.page_source
        html = driver.page_source
        driver.quit()
    if is_soup:
        return BeautifulSoup(html, "lxml")
    return driver.current_url
# print weibo()
