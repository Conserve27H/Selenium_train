# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# 获取当前选中的元素
element = wd.find_element(By.CSS_SELECTOR,
                          '#s_radio input[name="teacher"]:checked')
print('当前选中的是: ' + element.get_attribute('value'))

# 点选 小雷老师
wd.find_element(By.CSS_SELECTOR,
                '#s_radio input[value="小雷老师"]').click()

element = wd.find_element(By.CSS_SELECTOR,
                          '#s_radio input[name="teacher"]:checked')
print('后来选中的是: ' + element.get_attribute('value'))
