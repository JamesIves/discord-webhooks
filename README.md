# Discord Webhooks for Python 🔗 🐍

[![Build Status](https://travis-ci.org/JamesIves/discord-webhooks.svg?branch=master)](https://travis-ci.org/JamesIves/discord-webhooks) [![Issues](https://img.shields.io/github/issues/JamesIves/discord-webhooks.svg)](https://github.com/JamesIves/discord-webhooks/issues)

Easy to use module for Python which allows for sending of webhooks to a [Discord server](https://discordapp.com/).

## Installation Steps 💽
The `Discord-Webhooks` module can be installed into your project via Pip.

```
$ pip install Discord-Webhooks
```

## Getting Started :airplane:

Import the package into your project and initialize it to get started. You must pass the [webhook URL you obtained from your Discord channel in as the argument](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks). 

```python
from discord_webhooks import DiscordWebhooks

# Webhook URL for your Discord channel.
WEBHOOK_URL = 'http://discord.gg/...'

# Initialize the webhook class and attaches data.
webhook = DiscordWebhooks(WEBHOOK_URL)

# Sets some content
webhook.set_content(content='Montezuma!')

# Triggers the payload to be sent to Discord.
webhook.send()

```

If you'd like to send a message attachment you can do so.


```python
from discord_webhooks import DiscordWebhooks

# Webhook URL for your Discord channel.
WEBHOOK_URL = 'http://discord.gg/...'

webhook = DiscordWebhooks(WEBHOOK_URL)

webhook.set_content(content='The best cat ever is...', title='Montezuma!', description='Seriously!', \
  url='http://github.com/JamesIves', color=0xF58CBA, timestamp='2018-11-09T04:10:42.039Z')

# Attaches an image
webhook.set_image(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

# Attaches a thumbnail
webhook.set_thumbnail(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

# Attaches an author
webhook.set_author(name='James Ives', url='https://jamesiv.es', icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

# Attaches a footer
webhook.set_footer(text='Footer', icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

# Appends a field
webhook.add_field(name='Field', value='Value!')

webhook.send()
```

## Methods 📡
You can find an explanation of all available methods below. 

---

#### `set_content`
The `set_content` method can be used to send basic messages to Discord.

| Argument  | Description | Type |
| ------------- | ------------- | ------------- |
| `content`  | Content represents a standard message on Discord. | `String` |
| `title`  | Displays a title on an message attachment. | `String` |
| `description`  | Displays a description on an message attachment. | `String` |
| `url`  | Creates a link on the title. | String|
| `color`  | Displays a colored strip on the left side of an message attachment. This should be a hexademical value, for example `0xF58CBA`. | `Integer` |
| `timestamp`  | Displays a timestamp beneath the message attachment. Must be a valid timestamp, consider using Python's `datetime` to achieve localtime.  | `String` |

---

#### `set_author`
Using `set_author` you're able to attach an author to an message attachment.

| Argument  | Description | Type |
| ------------- | ------------- | ------------- |
| `name`  | The name of the author. | `String` |
| `url`  | Creates a link on the author name. | `String` |
| `icon_url`  | Displays an author icon, must resolve to a valid image path. | `String` |

---

#### `set_footer`
Using `set_footer` you're able to attach a footer to an message attachment.

| Argument  | Description | Type |
| ------------- | ------------- | ------------- |
| `text`  | The text that should display in the footer. | `String` |
| `icon_url`  | Displays a footer icon, must resolve to a valid image path. | `String` |


---

#### `set_thumbnail`
Using `set_thumbnail` you're able to attach a thumbnail to a message attachment.

| Argument  | Description | Type |
| ------------- | ------------- | ------------- |
| `url`  | Displays a thumbnail image in the message attachment | `String` |

---

##### `set_image`
Using `set_image` you're able to attach an image to a message attachment.

| Argument  | Description | Type |
| ------------- | ------------- | ------------- |
| `url`  | Displays an image in the message attachment | `String` |

---

#### `add_field`
Using `add_field` you're able to attach a field to a message attachment. You can add as many fields as you want.

| Argument  | Description | Type |
| ------------- | ------------- | ------------- |
| `name`  | The name of the field. | `String` |
| `value`  | The value of the field. | `String` |
| `inline`  | Determines if the field should display inline or not, this is primarily used for formatting when you have multiple fields. | `Boolean` |

---

#### `send`
When you're done formatting your message attachment you can use the `send` method to dispatch it to Discord.
