# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1a.html')

# elements = wd.find_elements(By.CSS_SELECTOR, '#t1 > span , #t1 > p') # 组选择
# elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-child(2)') # 父元素第2个元素
# elements = wd.find_elements(By.CSS_SELECTOR, 'p:nth-last-child(1)')  # 父元素倒数第1个元素
# elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-of-type(1)')  # 父元素span类型的第一个元素
# elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-last-of-type(1)')  # 父元素span类型的倒数第一个元素
# elements = wd.find_elements(By.CSS_SELECTOR, 'div:nth-child(odd)')  # 父元素奇数节点
# elements = wd.find_elements(By.CSS_SELECTOR, 'div:nth-child(even)')  # 父元素偶数节点
# elements = wd.find_elements(By.CSS_SELECTOR, 'h3 + span')  # 相邻兄弟节点
elements = wd.find_elements(By.CSS_SELECTOR, 'h3 ~ span')  # 后续所有兄弟节点

for element in elements:
    print(element.text)
