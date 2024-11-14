# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/test3.html')

element = wd.find_element(By.ID, "input1")

element.clear()  # 清除输入框已有的字符串
element.send_keys('郑源涵')  # 输入新字符串
