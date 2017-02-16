from tmbot import tmbot
from tmbot import config

tm = tmbot.TwitchMaster(config.user_login, config.user_password)

tm.login()