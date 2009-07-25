import unittest

from django.conf import settings
from django.contrib.auth.models import User

from liveblog.models import LiveBlogEntry
#from blog.models import Entry

from markdown import markdown

blog = __import__(settings.BLOG_APP)
Entry = blog.models.__getattribute__(settings.BLOG_ENTRY_MODEL)

class LiveBlogTestCase(unittest.TestCase):

    text = 'This is a test liveblog entry **with bold text**'

    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'test@test.com',
            'testpassword'
        )
        self.blog_entry = Entry.objects.create(
            author=self.user,
            title='Main blog post',
            slug='main-blog-post',
            body='This is a test blog entry with **bold** text'
        )
        self.liveblog_entry = LiveBlogEntry.objects.create(
            body=self.text,
            blog_entry=self.blog_entry
        )

    def testEntry(self):
        self.assertEquals(self.liveblog_entry.body, self.text)
        self.assertEquals(self.liveblog_entry.body_html, markdown(self.text))

