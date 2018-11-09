import unittest
import json
from webhooks import DiscordWebhooks

class BaseTest(unittest.TestCase):

  def test_standard_message(self):
    """
      Tests a standard messgae payload with nothing but content.
    """
    webhook = DiscordWebhooks('webhook_url', content='Montezuma')

    expected_payload = {
        'content': 'Montezuma', 
          'embeds': [
            {
              'fields': [], 
              'image': {}, 
              'author': {}, 
              'thumbnail': {}, 
              'footer': {},
            }
          ]
        }
    
    self.assertEqual(webhook.format_payload(), expected_payload)


  def test_generic_embed_message(self):
    """
      Tests a generic messgae payload.
    """
    webhook = DiscordWebhooks('webhook_url', content='Montezuma', title='Best Cat Ever', description='Seriously', \
      url='http://github.com/JamesIves', color=0xF58CBA, timestamp='2018-11-09T04:10:42.039Z')

    expected_payload = \
      {
        'content': 'Montezuma',
        'embeds': [
            {
              'title': 'Best Cat Ever',
              'description': 'Seriously',
              'url': 'http://github.com/JamesIves',
              'color': 16092346,
              'timestamp': '2018-11-09T04:10:42.039Z',
              'fields': [],
              'image': {},
              'author': {},
              'thumbnail': {},
              'footer': {},
            }
          ]
        }
      
    self.assertEquals(webhook.format_payload(), expected_payload)

  def test_set_image(self):
    """
      Tests the set_image method and ensures the data gets added to the payload.
    """
    webhook = DiscordWebhooks('webhook_url', content='Montezuma')
    webhook.set_image(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

    expected_payload = \
      {
        'content': 'Montezuma',
        'embeds': [
            {
              'fields': [],
              'image': {
                'url': 'https://avatars1.githubusercontent.com/u/10888441?s=460&v=4'
              },
              'author': {},
              'thumbnail': {},
              'footer': {},
            }
          ]
        }
      
    self.assertEquals(webhook.format_payload(), expected_payload)

  def test_set_thumbnail(self):
    """
      Tests the set_thumbnailk method and ensures the data gets added to the payload.
    """
    webhook = DiscordWebhooks('webhook_url', content='Montezuma')
    webhook.set_thumbnail(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

    expected_payload = \
      {
        'content': 'Montezuma',
        'embeds': [
            {
              'fields': [],
              'image': {},
              'author': {},
              'thumbnail': {
                'url': 'https://avatars1.githubusercontent.com/u/10888441?s=460&v=4'
              },
              'footer': {},
            }
          ]
        }
      
    self.assertEquals(webhook.format_payload(), expected_payload)

  def test_set_author(self):
    """
      Tests the set_author method and ensures the data gets added to the payload.
    """
    webhook = DiscordWebhooks('webhook_url', content='Montezuma')
    webhook.set_author(name='James Ives', url='https://jamesiv.es', icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

    expected_payload = \
      {
        'content': 'Montezuma',
        'embeds': [
            {
              'fields': [],
              'image': {},
              'author': {
                'name': 'James Ives',
                'url': 'https://jamesiv.es',
                'icon_url': 'https://avatars1.githubusercontent.com/u/10888441?s=460&v=4'
              },
              'thumbnail': {},
              'footer': {},
            }
          ]
        }
      
    self.assertEquals(webhook.format_payload(), expected_payload)

  def test_set_footer(self):
    """
      Tests the set_footer method and ensures the data gets added to the payload.
    """
    webhook = DiscordWebhooks('webhook_url', content='Montezuma')
    webhook.set_footer(text='Footer', icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

    expected_payload = \
      {
        'content': 'Montezuma',
        'embeds': [
            {
              'fields': [],
              'image': {},
              'author': {},
              'thumbnail': {},
              'footer': {
                'text': 'Footer',
                'icon_url': 'https://avatars1.githubusercontent.com/u/10888441?s=460&v=4'
              },
            }
          ]
        }
      
    self.assertEquals(webhook.format_payload(), expected_payload)

  def test_add_field(self):
    """
      Tests the set_field method and ensures the data gets added to the payload.
    """
    webhook = DiscordWebhooks('webhook_url', content='Montezuma')
    webhook.add_field(name='Field1', value='Value1', inline=True)
    webhook.add_field(name='Field2', value='Value2', inline=True)
    webhook.add_field(name='Field3', value='Value3', inline=False)

    # Inline should default to false
    webhook.add_field(name='Field4', value='Value4')

    expected_payload = \
      {
        'content': 'Montezuma',
        'embeds': [
            {
              'fields': [
                {
                  'name': 'Field1',
                  'value': 'Value1',
                  'inline': True
                },
                {
                  'name': 'Field2',
                  'value': 'Value2',
                  'inline': True
                },
                {
                  'name': 'Field3',
                  'value': 'Value3',
                  'inline': False
                },
                {
                  'name': 'Field4',
                  'value': 'Value4',
                  'inline': False
                },
              ],
              'image': {},
              'author': {},
              'thumbnail': {},
              'footer': {},
            }
          ]
        }
      
    self.assertEquals(webhook.format_payload(), expected_payload)

  def test_complex_embed(self):
    """
      Tests a combination of all methods to form a complex payload object.
    """
    webhook = DiscordWebhooks('webhook_url', content='Montezuma', title='Best Cat Ever', description='Seriously', \
      url='http://github.com/JamesIves', color=0xF58CBA, timestamp='2018-11-09T04:10:42.039Z')
    webhook.set_image(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')
    webhook.set_thumbnail(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')
    webhook.set_author(name='James Ives', url='https://jamesiv.es', icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')
    webhook.set_footer(text='Footer', icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')
    webhook.add_field(name='Field', value='Value!')

    self.maxDiff = None
    expected_payload = \
      {
        'content': 'Montezuma',
        'embeds': [
            {
              'title': 'Best Cat Ever',
              'description': 'Seriously',
              'url': 'http://github.com/JamesIves',
              'color': 16092346,
              'timestamp': '2018-11-09T04:10:42.039Z',
              'fields': [
                {
                  'name': 'Field',
                  'value': 'Value!',
                  'inline': False
                }
              ],
              'image': {
                'url': 'https://avatars1.githubusercontent.com/u/10888441?s=460&v=4'
              },
              'author': {
                'name': 'James Ives',
                'url': 'https://jamesiv.es',
                'icon_url': 'https://avatars1.githubusercontent.com/u/10888441?s=460&v=4'
              },
              'thumbnail': {
                'url': 'https://avatars1.githubusercontent.com/u/10888441?s=460&v=4'
              },
              'footer': {
                'text': 'Footer',
                'icon_url': 'https://avatars1.githubusercontent.com/u/10888441?s=460&v=4'
              },
            }
          ]
        }
      
    self.assertEquals(webhook.format_payload(), expected_payload)



if __name__ == '__main__':
    unittest.main()