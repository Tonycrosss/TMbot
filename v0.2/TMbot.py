from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess, sys

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

# ___ Открываем первый стрим ____

# Xpath для первого стрима
first_stream_xpath = "/html/body/div[@class='wrapper']/div[@class='container'][2]/div[@class='content-left']/div[@class='block'][1]/div[@class='streams-list']/div[@class='item vip super-vip']/div[@class='inner']/div[@class='status']/a"
# Переходим на первый стрим
driver.find_element_by_xpath(first_stream_xpath).click()
time.sleep(5)

# ____ Вытягиваем кол-во просмотров у стримера ____

# Xpath для баблишка
money_xpath = "/html/body/div[@class='wrapper']/div[@class='container']/div[@class='content-left']/div[@class='block'][2]/div[@class='time-is-money']/div[@class='money f-right']/div[@class='center bc-cont']/div[@id='credits-earned']"
# Получаем видимый текст =)
print(driver.find_element_by_xpath(money_xpath).text)
current_money = driver.find_element_by_xpath(money_xpath).text
time.sleep(65)
new_money = driver.find_element_by_xpath(money_xpath).text
if new_money <= current_money:
    driver.close()
    subprocess.call(['python3.5', '/mnt/3EA24E96A24E5297/Python/TMbot/v0.2/TMbot.py'])


# TODO Отсутствие элемента чтоб преезапускало скрипт