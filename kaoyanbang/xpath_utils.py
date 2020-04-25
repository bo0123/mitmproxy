#需要安装客户端的包
#pip3 install Appium-Python-Client
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


cap = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",cap)

def get_driver():
    return driver
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return(x,y)

def xpath_exist_click(xpath):
    try:
        # 是否跳过
        if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(xpath)):
            driver.find_element_by_xpath(xpath).click()
    except:
        pass

def xpath_sendkeys(key,xpath):
    try:
        if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(xpath)):
            driver.find_element_by_xpath(xpath).send_keys(key)
    except:
        pass
