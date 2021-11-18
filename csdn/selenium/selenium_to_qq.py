#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/17 9:32 
# @Author : keke618
# @File : selenium_to_qq.py
# @Software: PyCharm
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 用get打开 qq空间
driver.get("https://i.qq.com/")
# 定位到账号密码登录
# 先选择到 ifname 嵌套的子页面
driver.switch_to.frame("login_frame")
driver.find_element("id", "switcher_plogin").click()       # 执行点击
sleep(1)
driver.find_element("id", "u").send_keys("1627061758")      # 键入账号
driver.find_element("id", "p").send_keys("")                # 键入密码
sleep(1)
driver.find_element("id", "login_button").click()            # 点击登录
sleep(10)
driver.quit()












# 找到 b站 搜索框 查询 美食
# driver.find_element_by_class_name('nav-search-input').send_keys('美食')
# # driver.execute_script('alert("123")')
# sleep(2)
# driver.find_element_by_class_name('nav-search-btn').click()
# sleep(10)
# 用get打开百度页面
# driver.get("http://www.baidu.com")
# # 找到百度的输入框，并输入 CSDN
# driver.find_element_by_id('kw').send_keys('CSDN')
# sleep(2)
# # 点击搜索按钮
# driver.find_element_by_id('su').click()
# sleep(2)
# # 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
# driver.find_elements_by_link_text('CSDN - 专业开发者社区')[0].click()
# sleep(10)
# # 关闭浏览器
