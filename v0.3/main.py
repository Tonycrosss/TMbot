from tmbot import tmbot
from tmbot import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess, sys
from selenium import common






tm = tmbot.TwitchMaster(config.user_login, config.user_password)

tm.bot1()
