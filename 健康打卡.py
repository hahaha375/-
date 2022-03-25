#导入第三方库
from selenium import webdriver as wb
import os
import time
import sys

#打开文本文件读取信息
f = open('.\账号信息.txt', 'r')
学号 = f.readline()
学号 = 学号.rstrip('\n')
密码 = f.readline()
密码 = 密码.rstrip('\n')
try:
    driver = wb.Edge('.\msedgedriver.exe')
    URL = 'http://form.hhu.edu.cn/pdc/form/list'
except:
    print('浏览器打开出错')
    os.system('pause')
try:
    driver.get(URL)

except:
    print('连接出错')
    os.system('pause')
    sys.exit(0)

driver.find_element_by_id('IDToken1').send_keys(学号)#这里填学号
time.sleep(0.5)
driver.find_element_by_id('IDToken2').send_keys(密码)#这里填密码
time.sleep(1)
xpath = "//*[@src='/amserver/images/i01.jpg']"
    
try:
    #通过网页的相对xpath来定位，这个是比较好的办法，想不起来怎么做的时候记得再上百度查一下
    driver.find_element_by_xpath("//*[@src='/amserver/images/i01.jpg']")
except:
    print('登录出错')
    os.system('pause')
    sys.exit(0)
driver.find_element_by_xpath(xpath).click()
time.sleep(0.5)

try:
    driver.find_element_by_class_name('datav-flex')
except:
    print('进入打卡系统出错')
    os.system('pause')
    sys.exit(0)
driver.find_element_by_class_name('datav-flex').click()
time.sleep(0.5)

try:
    driver.find_element_by_id('saveBtn')
except:
    print('保存出错')
    os.system('pause')
    sys.exit(0)
driver.find_element_by_id('saveBtn').click()
os.system('pause')

