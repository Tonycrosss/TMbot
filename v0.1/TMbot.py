from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

username = input("Введи логин\n")
mypasswd = input("Введи пароль\n")

driver = webdriver.Chrome()
driver.get('http://twitchmaster.ru/')  # Коннектимся
time.sleep(4)

# ____ Авторизуемся ____

# xpath для кнопки Вход
login_xbutton = "/html/body/div[@class='wrapper']/div[@class='container'][1]/div[@class='header']/div[@class='links f-right']/span[@class='menu-content']/a[@class='ajax-popup']"
# Нажимаем на кнопку
driver.find_element_by_xpath(login_xbutton).click()
time.sleep(2)

# Xpath Для поля - Имя пользователя
login_xfield = "/html/body/div[@id='popup-window']/div[@class='inner']/form/input[1]"
# Вбиваем логин
driver.find_element_by_xpath(login_xfield).send_keys(username)
time.sleep(2)
# Xpath Для поля - Пароль
passwd_xfield = "/html/body/div[@id='popup-window']/div[@class='inner']/form/input[2]"
# Вбиваем пароль
driver.find_element_by_xpath(passwd_xfield).send_keys(mypasswd)
time.sleep(2)
# Xpath Для кнопки Войти
enter_xbutton = "/html/body/div[@id='popup-window']/div[@class='inner']/form/div[@class='center']/div[@class='cool-button form-submitter']"
# Жмакаем по кнопке
driver.find_element_by_xpath(enter_xbutton).click()

time.sleep(5)