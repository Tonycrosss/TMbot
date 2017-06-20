from tmbot import tmbot
from tmbot import config
import time
import threading


if __name__ == '__main__':

    tm = tmbot.TwitchMaster(config.user_login, config.user_password)
    b1 = tm.bot1
    b2 = tm.bot2
    b3 = tm.bot3

    th1 = threading.Thread(target=b1)
    th2 = threading.Thread(target=b2)
    th3 = threading.Thread(target=b3)
    th1.setDaemon(True)
    th2.setDaemon(True)
    th3.setDaemon(True)
    th1.start()
    time.sleep(35)
    th2.start()
    time.sleep(35)
    th3.start()
    while True: pass


