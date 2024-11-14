# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)

# 打开网站
driver.get('https://www.163.com')

driver.get_window_size()  # 获取窗口大小
driver.set_window_size(1920, 1080)  # 改变窗口大小

# 获取网站标题栏文本
print(driver.title)

# 获取网站地址栏文本
print(driver.current_url)
