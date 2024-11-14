# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# 先把 已经选中的选项全部点击一下
elements = wd.find_elements(By.CSS_SELECTOR,
                            '#s_checkbox input[name="teacher"]:checked')

for element in elements:
    element.click()

# 再点击 小雷老师
wd.find_element(By.CSS_SELECTOR,
                "#s_checkbox input[value='小雷老师']").click()
