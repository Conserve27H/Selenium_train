# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# 创建Select对象
select = Select(wd.find_element(By.ID, "ss_single"))

# 通过 Select 对象选中小雷老师
select.select_by_visible_text("小凯老师")
