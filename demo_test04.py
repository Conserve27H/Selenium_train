# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

import time, check

wd = webdriver.Chrome()
wd.implicitly_wait(100)


wd.get('http://127.0.0.1/mgr/sign.html')

wd.find_element(By.ID, 'username').send_keys('byhy')
wd.find_element(By.ID, 'password').send_keys('88888888')
wd.find_element(By.TAG_NAME, 'button').click()

# 点击右下角链接
wd.find_element(By.XPATH, '//*[@id="root"]/footer/div/a').click()

# mainWindow变量保存当前窗口的句柄
byhyWindow = wd.current_window_handle

for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是要操作的那个窗口
    if '白月黑羽' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

wd.maximize_window()

tabs = wd.find_elements(By.XPATH, '/html/body/header/nav/nav/div/ul/li')
titles = [i.text for i in tabs]
print(titles)

expected = [
    'Python基础',
    'Python进阶',
    'Qt图形界面',
    'Django',
    '自动化测试',
    '性能测试',
    'JS语言',
    'JS前端',
]

check.CHECK_POINT('菜单栏和预期一致', titles == expected)

# 通过前面保存的老窗口的句柄，自己切换到老窗口
wd.switch_to.window(byhyWindow)

wd.find_element(By.XPATH, '//*[@id="root"]/header/nav/div/ul/li[2]/a').click()
wd.find_element(By.XPATH, '//*[@id="root"]/header/nav/div/ul/li[2]/ul/li[3]/div[2]/a').click()
time.sleep(2)

check.CHECK_POINT('进入登录页面', '/mgr/sign.html' in wd.current_url)
