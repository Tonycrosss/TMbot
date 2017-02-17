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
        global driver
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

    def bot1(self):
        self.login()
        # Xpath для первого стрима
        first_stream_xpath = "/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div/div[1]/a[2]/img"
        driver.find_element_by_xpath(first_stream_xpath).click()
        time.sleep(5)
        # ____ Вытягиваем кол-во бабла у стримера ____
        self.money_checker1()

    def money_checker1(self):
        try:
            # Xpath для баблишка
            money_xpath = "//*[@id='credits-earned']"
            current_money = driver.find_element_by_xpath(money_xpath).text.replace(',', '')
            print('Bot 1 - Current money: {}'.format(current_money))
            time.sleep(150)
            new_money = driver.find_element_by_xpath(
                money_xpath).text.replace(',', '')
            # summary_money.append(float(new_money))
        except common.exceptions.NoSuchElementException:
            print("Нету денег!")
            print("Всего заработано : {}".format(new_money))
            time.sleep(2)
            driver.close()
            self.bot1()

        if new_money <= current_money:
            driver.close()
            self.bot1()
        else:
            self.money_checker1()


    def bot2(self):
        self.login()
        # Xpath для второго стрима
        second_stream_xpath = "/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div/div[1]/a[2]/img"
        # Переходим на второй стрим
        driver.find_element_by_xpath(second_stream_xpath).click()
        time.sleep(5)
        # ____ Вытягиваем кол-во бабла у стримера ____
        self.money_checker2()

    def money_checker2(self):
        try:
            # Xpath для баблишка
            money_xpath = "//*[@id='credits-earned']"
            current_money = driver.find_element_by_xpath(money_xpath).text.replace(',', '')
            print('Bot 2 - Current money: {}'.format(current_money))
            time.sleep(150)
            new_money = driver.find_element_by_xpath(
                money_xpath).text.replace(',', '')
            # summary_money.append(float(new_money))
        except common.exceptions.NoSuchElementException:
            print("Нету денег!")
            print("Всего заработано : {}".format(new_money))
            time.sleep(2)
            driver.close()
            self.bot2()

        if new_money <= current_money:
            driver.close()
            self.bot2()
        else:
            self.money_checker2()

    def bot3(self):
        self.login()
        # Xpath для первого стрима
        third_stream_xpath = "/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div/div[2]/a"
        # Переходим на третий стрим
        driver.find_element_by_xpath(third_stream_xpath).click()
        time.sleep(5)
        # ____ Вытягиваем кол-во бабла у стримера ____
        self.money_checker3()

    def money_checker3(self):
        try:
            # Xpath для баблишка
            money_xpath = "//*[@id='credits-earned']"
            current_money = driver.find_element_by_xpath(money_xpath).text.replace(',', '')
            print('Bot 3 - Current money: {}'.format(current_money))
            time.sleep(150)
            new_money = driver.find_element_by_xpath(
                money_xpath).text.replace(',', '')
            # summary_money.append(float(new_money))
        except common.exceptions.NoSuchElementException:
            print("Нету денег!")
            print("Всего заработано : {}".format(new_money))
            time.sleep(2)
            driver.close()
            self.bot3()

        if new_money <= current_money:
            driver.close()
            self.bot3()
        else:
            self.money_checker3()





# TODO Переписать все xpath