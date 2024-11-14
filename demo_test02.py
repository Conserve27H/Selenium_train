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

wd.find_element(By.CLASS_NAME, 'btn-md').click()
inputs = wd.find_elements(By.XPATH,
                          '//*[@id="root"]/div/section[2]/div[1]/div[1]/descendant::input | //textarea')

inputs[0].send_keys('南京市中医院')
inputs[1].send_keys('02552276666')
inputs[2].send_keys('南京市大明路157号')
# 创建
wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()

time.sleep(1)
# 编辑
wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[1]').click()

nameInput = wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div[1]/div[1]/input')
nameInput.clear()
nameInput.send_keys('南京省中医院')
wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div[2]/div/label[1]').click()

spans = wd.find_elements(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div/span[last()]')
information = [i.text for i in spans]
expected = ['南京省中医院', '02552276666', '南京市大明路157号']

if information[:3] == expected:
    print(information)
    print('信息都正确')
else:
    print('信息有误')
