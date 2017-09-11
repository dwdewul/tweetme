from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        random_user = User.objects.create(username='lilybell')

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            text='Random content'
        )
        self.assertTrue(obj.text == 'Random content')
