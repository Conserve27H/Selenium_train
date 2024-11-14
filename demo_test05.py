# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome()
wd.maximize_window()
wd.implicitly_wait(100)

wd.get('http://127.0.0.1/mgr/sign.html')

wd.find_element(By.ID, 'username').send_keys('byhy')
wd.find_element(By.ID, 'password').send_keys('88888888')
wd.find_element(By.TAG_NAME, 'button').click()


# 定义一个函数 执行每次的添加操作
def add(field1, field2, field3):
    # 点击添加
    wd.find_element(By.CLASS_NAME, 'btn-md').click()

    inputs = wd.find_elements(By.XPATH,
                              '//*[@id="root"]/div/section[2]/div[1]/div[1]/descendant::input | //textarea')

    inputs[0].send_keys(field1)
    inputs[1].send_keys(field2)
    inputs[2].send_keys(field3)

    # 创建
    wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()

    # time.sleep(1)


# 点击药品菜单
wd.find_element(By.CLASS_NAME, 'fa-plus').click()
# 添加药品
add('青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装')
add('青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装')
add('青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装')

# 点击客户菜单
wd.find_element(By.XPATH, '//*[@id="root"]/aside/section/ul/li[2]/a').click()
# 添加客户
add('南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501')
add('南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502')
add('南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503')


# 定义一个函数 执行创建订单操作
def Order(field1, field2, field3, field4):
    # 点击订单菜单
    wd.find_element(By.XPATH, '//*[@id="root"]/aside/section/ul/li[4]/a').click()
    # 点击添加订单
    wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/button').click()
    # 订单名称
    wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys(field1)
    # 选择客户
    wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/button').click()

    # 创建Select对象 选中客户框
    select = Select(wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/select'))
    # 通过 Select 对象选中对象
    select.select_by_visible_text(field2)

    # 创建Select对象 选中药品框
    select = Select(wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/select'))
    # 通过 Select 对象选中对象
    select.select_by_visible_text(field3)

    # 输入药品数量
    wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/div/input').send_keys(field4)
    # 点击创建
    wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()


Order('2024', '南京中医院2', '青霉素盒装1', '100')
