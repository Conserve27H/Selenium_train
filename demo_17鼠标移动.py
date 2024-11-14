# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('https://www.baidu.com/')

ac = ActionChains(driver)

# 鼠标移动到元素上
ac.move_to_element(
    driver.find_element(By.CSS_SELECTOR, '[name="tj_briicon"]')
).perform()
