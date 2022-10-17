#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-10-13
# @Author   :asce.huang
# @File     :BasePage.py
# @Desc     :原始页面

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config.config import *
from config.url import *

class BasePage():
    '''原始页面'''
    chrome_option = Options()
    chrome_option.add_argument(option_headless)
    chrome_option.add_experimental_option(option_enablelog)
    chrome_service = Service(executable_path=chromeDriver_path)
    driver = webdriver.Chrome(options=chrome_option,service=chrome_service)

    def setupDriver(self,url):
        driver = webdriver.Chrome(options=self.chrome_option,service=self.chrome_service)
        driver.get(url)
        