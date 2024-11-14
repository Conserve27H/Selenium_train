# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

# 点击打开新窗口的链接
link = wd.find_element(By.TAG_NAME, "a")
link.click()

# for handle in wd.window_handles:
#     # 先切换到该窗口
#     wd.switch_to.window(handle)
#     # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
#     if 'Bing' in wd.title:
#         # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
#         break
# mainWindow变量保存当前窗口的句柄
mainWindow = wd.current_window_handle

# 通过前面保存的老窗口的句柄，自己切换到老窗口
# wd.switch_to.window(mainWindow)

# wd.title属性是当前窗口的标题栏 文本
print(wd.title)
