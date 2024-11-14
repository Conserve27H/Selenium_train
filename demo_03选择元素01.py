# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 根据 class name 选择元素，返回的是 一个列表

# elements = wd.find_elements(By.CLASS_NAME, 'animal')  # 里面都是class 属性值为 animal的元素对应的 WebElement对象
#
# # 取出列表中的每个 WebElement对象，打印出其text属性的值
#
# for element in elements:  # text属性就是该 WebElement对象对应的元素在网页中的文本内容
#     print(element.text)

# 根据 tag name 选择元素，返回的是 一个列表

elements = wd.find_elements(By.TAG_NAME, 'span')  # 里面 都是 tag 名为 div 的元素对应的 WebElement对象

# 取出列表中的每个 WebElement对象，打印出其text属性的值

for element in elements:  # text属性就是该 WebElement对象对应的元素在网页中的文本内容
    print(element.text)

