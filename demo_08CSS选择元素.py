# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

element = wd.find_element(By.CSS_SELECTOR, '#searchtext')
element.send_keys('你好')
elements = wd.find_elements(By.CSS_SELECTOR, '.animal')

for element in elements:
    print(element.text)
