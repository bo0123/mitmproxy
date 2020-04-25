#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 20:31
# @Author  : Aries
# @Site    : 
# @File    : handle_appium_docker.py
# @Software: PyCharm

import multiprocessing
import time
from appium import webdriver
from selenium.webdriver.support.wait import  WebDriverWait

def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def handle_appium(info):
    cap = {
        "platformName": "Android",
        "platformVersion": "4.4.2",
        "deviceName":info['device'],
        "udid": info['device'],
        "appPackage": info['appPackage'],
        "appActivity": info['appActivity'],
        "noReset": True,
        "unicodeKeyboard": True,
        "resetkeyboard": True
    }
    driver = webdriver.Remote("http://192.168.199.140:" + str(info["port"]) + "/wd/hub", cap)

    l = get_size(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.15)
    y2 = int(l[1] * 0.9)

    #抖音
    if info["appPackage"] == "com.ss.andrpid.ugc.aweme":
        #根据实际的我这里直接写//android，通过
        if WebDriverWait(driver,60).until(lambda x:x.find_element_by_xpath("//android")):
            while True:
                # 初始鼠标位置，从哪里开始，结束时鼠标位置，到哪里结束
                driver.swipe(x1,y1,x1,y2)
                time.sleep(3)

    #快手
    if info["appPackage"] == "com.smile.gifmaker":
        # 根据实际的我这里直接写//android
        if WebDriverWait(driver, 60).until(lambda x: x.find_element_by_xpath("//android")):
            while True:
                # 初始鼠标位置，从哪里开始，结束时鼠标位置，到哪里结束
                driver.swipe(x1, y1, x1, y2)
                time.sleep(3)

    #快手
    if info["appPackage"] == "com.ss.android.article.news":
        # 根据实际的我这里直接写//android
        if WebDriverWait(driver, 60).until(lambda x: x.find_element_by_xpath("//android")):
            while True:
                #初始鼠标位置，从哪里开始，结束时鼠标位置，到哪里结束
                driver.swipe(x1, y1, x1, y2)
                time.sleep(3)

if __name__ =='__main__':
    m_list = []
    devices_list = [
        {
                "device": "192.168.199.133:5555",
                "appPackage": "com.ss.android.ugc.aweme",
                "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
                "port": 4723,
                "key": '抖音'
        },
        {
                "device": "192.168.199.133:5555",
                "appPackage": "com.smile.gifmaker",
                "appActivity": "com.yxcorp.gifshow.HomeActivity",
                "port": 4725,
                "key": '快手'
        },
        {
                "device": "192.168.199.133:5555",
                "appPackage": "com.ss.android.article.news",
                "appActivity": "com.ss.android.article.news.activity.SplashBadgeActivity",
                "port": 4727,
                "key": '今日头条'
        }
    ]

for device in (devices_list):
    m_list.append(multiprocessing.Process(target=handle_appium,args=(device,)))

for m1 in m_list:
    m1.start()