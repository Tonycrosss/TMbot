from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess, sys
from selenium import common


class TwitchMaster:
    def __init__(self, userlogin, userpassword):
        self.userlogin = userlogin
        self.userpassword = userpassword

    def bot1(self):
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
        driver.find_element_by_xpath(passwd_xfield).send_keys(
            self.userpassword)
        time.sleep(1)
        # Xpath Для кнопки Войти
        enter_xbutton = "/html/body/div[@id='popup-window']/div[@class='inner']/form/div[@class='center']/div[@class='cool-button form-submitter']"
        # Жмакаем по кнопке
        driver.find_element_by_xpath(enter_xbutton).click()
        time.sleep(5)
        # Xpath для первого стрима
        first_stream_xpath = "/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div/div[1]/a[2]/img"
        if_no_promo_xpath = "/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]/a[2]/img"
        try:
            driver.find_element_by_xpath(first_stream_xpath).click()
        except common.exceptions.NoSuchElementException:
            driver.find_element_by_xpath(if_no_promo_xpath).click()
        time.sleep(5)
        # ____ Вытягиваем кол-во бабла у стримера ____

        def money_checker1():
            try:
                # Xpath для баблишка
                money_xpath = "//*[@id='credits-earned']"
                current_money = round(float(
                    driver.find_element_by_xpath(money_xpath).text.replace(',',
                                                                           '')))
                print('текущие бабки' + ' ' + str(current_money))
                print('Bot 1 - Current money: {}'.format(current_money))
                time.sleep(150)
                new_money = round(float(
                    driver.find_element_by_xpath(money_xpath).text.replace(',',
                                                                           '')))
                print('Новые бабки' + ' ' + str(new_money))
                if new_money == current_money:
                    driver.close()
                    self.bot1()
                else:
                    money_checker1()
            except common.exceptions.NoSuchElementException:
                print("Нету денег!")
                time.sleep(2)
                driver.close()
                time.sleep(600)
                self.bot1()

        money_checker1()


    def bot2(self):
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
        driver.find_element_by_xpath(passwd_xfield).send_keys(
            self.userpassword)
        time.sleep(1)
        # Xpath Для кнопки Войти
        enter_xbutton = "/html/body/div[@id='popup-window']/div[@class='inner']/form/div[@class='center']/div[@class='cool-button form-submitter']"
        # Жмакаем по кнопке
        driver.find_element_by_xpath(enter_xbutton).click()
        time.sleep(5)
        # Xpath для второго стрима
        second_stream_xpath = "/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div/div[1]/a[2]/img"
        if_no_promo_xpath2 = "/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/a[2]/img"
        # Переходим на второй стрим
        try:
            driver.find_element_by_xpath(second_stream_xpath).click()
        except common.exceptions.NoSuchElementException:
            driver.find_element_by_xpath(if_no_promo_xpath2).click()
        time.sleep(5)

        # ____ Вытягиваем кол-во бабла у стримера ____
        def money_checker2():
            try:
                # Xpath для баблишка
                money_xpath = "//*[@id='credits-earned']"
                current_money = round(float(
                    driver.find_element_by_xpath(money_xpath).text.replace(',',
                                                                           '')))
                print('текущие бабки' + ' ' + str(current_money))
                print('Bot 2 - Current money: {}'.format(current_money))
                time.sleep(150)
                new_money = round(float(
                    driver.find_element_by_xpath(money_xpath).text.replace(',',
                                                                           '')))
                print('Новые бабки' + ' ' + str(new_money))
                if new_money == current_money:
                    driver.close()
                    self.bot2()
                else:
                    money_checker2()
            except common.exceptions.NoSuchElementException:
                print("Нету денег!")
                time.sleep(2)
                driver.close()
                time.sleep(600)
                self.bot2()

        money_checker2()

    def bot3(self):
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
        driver.find_element_by_xpath(passwd_xfield).send_keys(
            self.userpassword)
        time.sleep(1)
        # Xpath Для кнопки Войти
        enter_xbutton = "/html/body/div[@id='popup-window']/div[@class='inner']/form/div[@class='center']/div[@class='cool-button form-submitter']"
        # Жмакаем по кнопке
        driver.find_element_by_xpath(enter_xbutton).click()
        time.sleep(5)
        # Xpath для первого стрима
        third_stream_xpath = "/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div/div[1]/a[2]/img"
        if_no_promo_xpath3 = "/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div/div[1]/a[2]/img"
        # Переходим на второй стрим
        try:
            driver.find_element_by_xpath(third_stream_xpath).click()
        except common.exceptions.NoSuchElementException:
            driver.find_element_by_xpath(if_no_promo_xpath3).click()
        time.sleep(5)

        # ____ Вытягиваем кол-во бабла у стримера ____
        def money_checker3():
            try:
                # Xpath для баблишка
                money_xpath = "//*[@id='credits-earned']"
                current_money = round(float(
                    driver.find_element_by_xpath(money_xpath).text.replace(',',
                                                                           '')))
                print('текущие бабки' + ' ' + str(current_money))
                print('Bot 3 - Current money: {}'.format(current_money))
                time.sleep(150)
                new_money = round(float(
                    driver.find_element_by_xpath(money_xpath).text.replace(',',
                                                                           '')))
                print('Новые бабки' + ' ' + str(new_money))
                if new_money == current_money:
                    driver.close()
                    time.sleep(600)
                    self.bot3()
                else:
                    money_checker3()
            except common.exceptions.NoSuchElementException:
                print("Нету денег!")
                time.sleep(2)
                driver.close()
                self.bot3()

        money_checker3()





# TODO Переписать все xpath