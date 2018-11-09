from datetime import datetime
import requests
import json


class DiscordWebhooks:
  def __init__(self, webhook_url, **kwargs):
    # Constructor
    self.webhook_url = webhook_url
    self.content = kwargs.get('content')

    # Generic Embed Data

    # Optional Values
    self.title = None
    self.description = None
    self.url = None
    self.color = None
    self.timestamp = None
    self.author_name = None
    self.author_url = None
    self.author_icon = None
    self.image = None
    self.thumbnail_url = None
    self.footer_text = None
    self.footer_icon = None

    # Fields Array
    self.fields = []

  def set_content(self, **kwargs):
    """
      Sets generic data on the embed object.
    """
    self.content = kwargs.get('content')
    self.title = kwargs.get('title')
    self.description = kwargs.get('description')
    self.url = kwargs.get('url')
    self.color = kwargs.get('color')
    self.timestamp = kwargs.get('timestamp')

  def set_image(self, **kwargs):
    """
      Sets an image on the embed object.
    """
    self.image = kwargs.get('url')

  def set_thumbnail(self, **kwargs):
    """
      Sets a thumbnail on the embed object.
    """
    self.thumbnail_url = kwargs.get('url')

  def set_author(self, **kwargs):
    """
      Sets the author on the embed object.
    """
    self.author_name = kwargs.get('name')
    self.author_url = kwargs.get('url')
    self.author_icon = kwargs.get('icon_url')

  def set_footer(self, **kwargs):
    """
      Sets the footer on the embed object.
    """
    self.footer_text = kwargs.get('text')
    self.footer_icon = kwargs.get('icon_url')

  def add_field(self, **kwargs):
    """
      Adds a field to the embed object.
    """
    field = {
      'name': kwargs.get('name'),
      'value': kwargs.get('value'),
      'inline': kwargs.get('inline', False)
    }

    self.fields.append(field)

  def format_payload(self):
    """
      Formats the data into a JSON object so it can be pushed
      as a payload to Discord.
    """
    # Initializes the default payload structure.
    payload = {}
    embed = {
      'author': {},
      'footer': {},
      'image': {},
      'thumbnail': {},
      'fields': []
    }

    # Attaches data to the payload if provided.
    if self.content:
      payload['content'] = self.content

    if self.title:
      embed['title'] = self.title

    if self.description:
      embed['description'] = self.description

    if self.url:
      embed['url'] = self.url

    if self.color:
      embed['color'] = self.color

    if self.timestamp:
      embed['timestamp'] = self.timestamp

    if self.author_name:
      embed['author']['name'] = self.author_name

    if self.author_url:
      embed['author']['url'] = self.author_url

    if self.author_icon:
      embed['author']['icon_url'] = self.author_icon

    if self.thumbnail_url:
      embed['thumbnail']['url'] = self.thumbnail_url

    if self.image:
      embed['image']['url'] = self.image

    if self.fields:
      embed['fields'] = self.fields

    if self.footer_icon:
      embed['footer']['icon_url'] = self.footer_icon

    if self.footer_text:
      embed['footer']['text'] = self.footer_text

    # If the embed object has content it gets appended to the payload
    if embed:
      payload['embeds'] = []
      payload['embeds'].append(embed)

    return payload

  def send(self):
    """
      Makes a POST request to Discord with the message payload.
    """
    payload = self.format_payload()

    # Makes sure that the required fields are provided before
    # sending the payload.
    if not self.webhook_url:
      print ('Error: Webhook URL is required.')

    elif not payload:
      print ('Error: Message payload cannot be empty.')

    else:
      try:
        request = requests.post(self.webhook_url,
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'})

        request.raise_for_status()

      except requests.exceptions.RequestException as error:
        print('Error: %s' % error)
