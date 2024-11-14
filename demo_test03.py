# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome()

wd.implicitly_wait(100)

wd.get('http://127.0.0.1/mgr/sign.html')

wd.find_element(By.ID, 'username').send_keys('byhy')
wd.find_element(By.ID, 'password').send_keys('88888888')
wd.find_element(By.TAG_NAME, 'button').click()

# 点击菜单栏药品
wd.find_element(By.CLASS_NAME, 'fa-plus').click()
# 点击添加药品
wd.find_element(By.CLASS_NAME, 'btn-md').click()

inputs = wd.find_elements(By.XPATH,
                          '//*[@id="root"]/div/section[2]/div[1]/div[1]/descendant::input | //textarea')

inputs[0].send_keys('阿莫西林')
inputs[1].send_keys('6925014502118')
inputs[2].send_keys('阿莫西林（Amoxicillin）是一种有机化合物，化学式为C16H19N3O5S，是一种抗生素药物，又称之为羟氨苄青霉素，属于青霉素家族的氨基青霉素类。')
# 创建
wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()

time.sleep(1)


spans = wd.find_elements(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div/span[last()]')
information = [i.text for i in spans]
expected = ['阿莫西林', '6925014502118', '阿莫西林（Amoxicillin）是一种有机化合物，化学式为C16H19N3O5S，是一种抗生素药物，又称之为羟氨苄青霉素，属于青霉素家族的氨基青霉素类。']

if information[:3] == expected:
    print(information)
    print('信息都正确')
else:
    print('信息有误')
