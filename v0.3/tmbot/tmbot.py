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
        # xpath для кнопки Вход
        login_xbutton = "/html/body/div[@class='wrapper']/div[@class='container'][1]/div[@class='header']/div[@class='links f-right']/span[@class='menu-content']/a[@class='ajax-popup']"
        # Нажимаем на кнопку
        driver.find_element_by_xpath(login_xbutton).click()
        time.sleep(1)
        # Xpath Для поля - Имя пользователя
        login_xfield = "/html/body/div[@id='popup-window']/div[@class='inner']/form/input[1]"
        # Вбиваем логин
        driver.find_element_by_xpath(login_xfield).send_keys(self.userlogin)
        time.sleep(1)
        # Xpath Для поля - Пароль
        passwd_xfield = "/html/body/div[@id='popup-window']/div[@class='inner']/form/input[2]"
        # Вбиваем пароль
        driver.find_element_by_xpath(passwd_xfield).send_keys(self.userpassword)
        time.sleep(1)
        # Xpath Для кнопки Войти
        enter_xbutton = "/html/body/div[@id='popup-window']/div[@class='inner']/form/div[@class='center']/div[@class='cool-button form-submitter']"
        # Жмакаем по кнопке
        driver.find_element_by_xpath(enter_xbutton).click()
        time.sleep(5)
