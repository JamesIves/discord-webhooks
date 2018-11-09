# Discord Webhooks for Python 🔗 🐍
Python package which allows for easy sending of webhooks to a [Discord server](https://discordapp.com/).

## Installation Steps 💽
The `DiscordWebhooks` package can be installed into your project via Pip.

```
$ pip install discord-webhooks
```

## How It Works 🎬

Import the package into your project and initialize it like so to get started.

```python
import discord-webhooks

# Webhook URL for your Discord channel.
WEBHOOK_URL = 'http://discord.gg/...'

# Initialize the webhook class and attaches data.
webhook = DiscordWebhooks(WEBHOOK_URL, content='Montezuma!')

# Triggers the payload to be sent to Discord.
webhook.send()

```

If you'd like to send a message attachment you can do so.


```python
import discord-webhooks

# Webhook URL for your Discord channel.
WEBHOOK_URL = 'http://discord.gg/...'

# Initialize the webhook class.
webhook = DiscordWebhooks('webhook_url', content='The best cat ever is...', title='Montezuma!', description='Seriously!', \
  url='http://github.com/JamesIves', color=0xF58CBA, timestamp='2018-11-09T04:10:42.039Z')

webhook.set_author(name='James Ives', url='https://jamesiv.es', author_icon='https://jamesiv.es/montezuma.png')

webhook.send()
```

## Methods 📡
You can find a list of all available methods below.

#### `set_author`

---

#### `set_footer`

---

#### `set_thumbnail`

---

### `set_image`

---

#### `add_field`
