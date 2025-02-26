import config
import socket
import heroku3
from AltSpam.logging import LOGGER


HAPP = None


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER("AltSpam").info("™°‌ 𝗕𝗥𝗔𝗠𝗛𝗔𝗦𝗧𝗥𝗔 𝗗𝗘𝗣𝗟𝗢𝗬𝗘𝗗 !")
            except BaseException:
                LOGGER("AltSpam").warning("𝗕𝗛𝗦𝗗𝗞 𝗛𝗘𝗥𝗢𝗞𝗨 𝗜𝗗 𝗦𝗔𝗛𝗜 𝗦𝗘 𝗗𝗔𝗟 𝗟𝗘!")
                
                
