# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://cdn2.byhy.net/files/selenium/test4.html')


# --- alert ---
driver.find_element(By.ID, 'b1').click()

# 打印 弹出框 提示信息
print(driver.switch_to.alert.text)

# 点击 OK 按钮
driver.switch_to.alert.accept()
