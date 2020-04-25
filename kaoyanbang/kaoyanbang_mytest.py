#需要安装客户端的包
#pip3 install Appium-Python-Client
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from kaoyanbang.xpath_utils import *

xpath_exist_click("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']")
xpath_exist_click("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")

xpath_sendkeys("15172113801","//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")
xpath_sendkeys("bb915802070","//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']")
xpath_exist_click("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/login_login_btn']")



#点击研讯
xpath_exist_click("//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")


l = get_size()

x1 = int(l[0]*0.5)
y1 = int(l[1]*0.75)
y2 = int(l[1]*0.25)

#滑动操作
while True:
    get_driver().swipe(x1,y1,x1,y2)
    time.sleep(0.5)
