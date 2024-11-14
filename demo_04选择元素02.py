# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 限制 选择元素的范围是 id 为 container 元素的内部。
element = wd.find_element(By.ID, 'container')
spans = element.find_elements(By.TAG_NAME, 'span')
for span in spans:
    print(span.text)
