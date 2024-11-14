# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

# 打开网站
wd.get('https://tinypng.com/')

# 先定位到上传文件的 input 元素
ele = wd.find_element(By.CSS_SELECTOR, 'input[type=file]')

# 再调用 WebElement 对象的 send_keys 方法
ele.send_keys(r'.\1.png')
