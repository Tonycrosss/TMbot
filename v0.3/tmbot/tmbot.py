from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess, sys
from selenium import common

class TwitchMaster:
    def __init__(self, userlogin, userpassword):
        self.userlogin = userlogin
        self.userpassword = userpassword

    def login(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        driver = webdriver.Chrome(chrome_options=chrome_options)

        driver.get('http://twitchmaster.ru/')  # Коннектимся
        time.sleep(4)

