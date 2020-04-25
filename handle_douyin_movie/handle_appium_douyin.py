#!/usr/bin/env python

import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import multiprocessing

def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def handle_douyin(driver):
    while True:
        #定位搜索框
        if WebDriverWait(driver,60).until(lambda x:x.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.EditText[1]")):
            #获取douyin_id进行搜索
            driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.EditText[1]").send_keys('1860719705')
            while driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.EditText[1]").text != '1860719705':
                driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.EditText[1]").send_keys('1860719705')
                time.sleep(0.1)
        #点击搜索
        driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()


        #点击用户标签
        if WebDriverWait(driver,30).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@text='用户']")):
            driver.find_element_by_xpath("//android.widget.TextView[@text='用户']").click()
        #点击头像
        if WebDriverWait(driver,30).until(lambda x:x.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.View[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")):
            driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.View[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        #点击粉丝按钮
        if WebDriverWait(driver,30).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@text='粉丝']")):
            driver.find_element_by_xpath("//android.widget.TextView[@text='粉丝']").click()

            x1 = int(driver.get_window_size()['width']*0.5)
            y1 = int(driver.get_window_size()['height']*0.75)
            y2 = int(driver.get_window_size()['height']*0.25)
            while True:
                time.sleep(3)
                if '没有更多了' in driver.page_source:
                    break
                elif 'TA还没有粉丝' in  driver.page_source:
                    break
                else:
                    driver.swipe(x1,y1,x1,y2)
                    time.sleep(0.5)

            #返回
            driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
            #返回
            driver.find_element_by_id("com.ss.android.ugc.aweme:id/jk").click()
            #重新清空用户id
            driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.EditText[1]").clear()



def handle_appium(device,port):
    cap = {
        "platformName": "Android",
        "platformVersion": "4.4.2",
        "deviceName": device,
        "udid":device,
        # 真机的
        # "platformName": "Android",
        # "platformVersion": "7.1.2",
        # "deviceName": "10d4e4387d74",
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetkeyboard": True
    }

    driver = webdriver.Remote("http://localhost:"+str(port)+"/wd/hub", cap)



    try:
        # 点击搜索
        print('点击搜索')
        if WebDriverWait(driver, 60).until(lambda x: x.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")):
            driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
    except:
        # [26,76][115,165]
        driver.tap([(26, 76), (115, 165)], 500)

    handle_douyin(driver)

if __name__ == '__main__':
    m_list = []
    #定义了2台虚拟设备，夜神模拟器
    devices_list = ["127.0.0.1:62001","127.0.0.1:62025"]
    for device in range(len(devices_list)):
        port = 4723 + 2 * device
        m_list.append(multiprocessing.Process(target=handle_appium,args=(devices_list[device],port,)))

    for m1 in m_list:
        m1.start()

    for m2 in m_list:
        m2.join()