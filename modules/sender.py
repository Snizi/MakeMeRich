from discord_webhook import DiscordWebhook

webhook_url = "https://discord.com/api/webhooks/955574363447525407/3h9u4wOcxM3sHD_ZIjSO0jqlbtJt5yywDfljJRXASbFMczMqrlh3O8lhP_gtGYdjXlIS"

webhook = DiscordWebhook(url=webhook_url, content="testee")
resp = webhook.execute()
