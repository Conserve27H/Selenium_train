# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID, '1')
# 获取元素的属性值
print(element.get_attribute('class'))

# 获取整个元素对应的HTML
print(element.get_attribute('outerHTML'))
print('----------------')
# 获取某个元素内部的HTML
print(element.get_attribute('innerHTML'))

element = wd.find_element(By.ID, "kw")
element.send_keys('郑源涵')
# 获取输入框里面的文字
print(element.get_attribute('value'))  # 获取输入框中的文本
