# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.implicitly_wait(10)

wd.get('http://127.0.0.1/mgr/sign.html')

wd.find_element(By.ID, 'username').send_keys('byhy')  # 输入账号
wd.find_element(By.ID, 'password').send_keys('88888888')  # 输入密码
wd.find_element(By.TAG_NAME, 'button').click()  # 点击登录按钮

# 获取左侧菜单栏
ul = wd.find_element(By.CLASS_NAME, 'sidebar-menu')
spans = ul.find_elements(By.TAG_NAME, 'span')

menuTitles = [i.text for i in spans]
for text in menuTitles:
    print(text)

# 检查前三项是否分别是'客户', '药品', '订单'
if menuTitles[:3] == ['客户', '药品', '订单']:
    print('测试通过')
else:
    print('测试不同')

