from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID, 'kw')

element.send_keys('通讯\n')

# 返回页面 ID为1 的元素
element = wd.find_element(By.ID, '1')

print(element.text)
