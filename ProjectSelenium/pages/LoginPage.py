#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-10-13
# @Author   :asce.huang
# @File     :LoginPage.py
# @Desc     :登录页面

import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from config.url import *
from config.config import *

class LoginPage(BasePage):
    '''CMS用户登录页'''
    # 定位器
    username_input_loc = (By.XPATH,'//*[@id="email"]')
    password_input_loc = (By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/form/div[2]/div/div/span/span')
    submit_button_loc = (By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/form/div[3]/div/div/span/button')
    login_url = baseurl_console + login_postfix #登录链接

    def openPage(self):
        self.setupDriver(self.login_url)

    def input_username(self,username):
        self.find_element(self.username_input_loc).clear()
        self.find_element(self.username_input_loc).click()
        self.find_element(self.username_input_loc).send_keys(username)

    def input_password(self,password):
        self.find_element(self.password_input_loc).clear()
        self.find_element(self.password_input_loc).click()
        self.find_element(self.password_input_loc).send_keys(password)

    def click_login(self):
        self.find_element(self.submit_button_loc).click()

    def user_login(self,username,password):
        self.input_username(username)
        self.input_password(password)
        time.sleep(1)
        self.click_login()
        time.sleep(2)
        self.driver.get_screenshot_as_file(screenshot_dir +'login.png')

if __name__ == "main":
    login = LoginPage()
    login.openPage()
    login.input_username(login_name)
    login.input_password(login_password)
    login.click_login()
