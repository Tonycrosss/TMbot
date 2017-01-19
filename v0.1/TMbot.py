from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.get('http://twitchmaster.ru/')  # Коннектимся

