# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 根据属性选择元素
element = wd.find_element(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')

# 打印出元素对应的html
print(element.get_attribute('outerHTML'))
