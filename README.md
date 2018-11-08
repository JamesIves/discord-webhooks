# Discord Webhooks for Python 🔗 🐍
Package for Python which allows for easy sending of webhooks to a Discord server.

## Installation Steps 💽
The `discord-webhooks` package can be installed into your project via Pip.

```
$ pip install discord-webhooks
```

## How It Works 🎬

Import the package into your project and initialize it like so to get started.

```python
import discord-webhooks
import timestamp

# Webhook URL for your Discord channel.
WEBHOOK_URL = ''

# Initialize the webhook class.
webhook = DiscordWebhooks(WEBHOOK_URL)

# Send a basic message.
discord_webhook.send_message('', ts=ts.now())
```

If you'd like to send a message attachment you can do so.


```python
import discord-webhooks
import timestamp

# Webhook URL for your Discord channel.
WEBHOOK_URL = ''

# Initialize the webhook class.
webhook = DiscordWebhooks(WEBHOOK_URL)

# Send a basic message.
discord_webhook.send_message('', ts=ts.now())
```

## API 📡
You can find a list of all available methods below.

