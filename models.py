import datetime

from django.db import models
from django.conf import settings
from django.template import loader, Context
from markdown import markdown

blog = __import__(settings.BLOG_APP)
Entry = blog.models.__getattribute__(settings.BLOG_ENTRY_MODEL)

if Entry.objects.count():
    default_blog_entry = Entry.objects.all()[0]
else:
    default_blog_entry = None

class LiveBlogEntry(models.Model):
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True)
    blog_entry = models.ForeignKey(Entry, 
                                   default=(Entry.objects.all()[0].id
                                            if Entry.objects.count() 
                                            else None))

    class Meta:
        verbose_name_plural = "Live Blog Entries"
        ordering = ['-pub_date', ]

    def __unicode__(self):
        self.sample_size = 100 # Used only in admin.
        return '%s: %s %s' % (self.blog_entry.title, 
                              self.body[:self.sample_size],
                              '...' if len(self.body) > self.sample_size else '')

    def save(self, *args, **kwargs):
        self.body_html = markdown(self.body)
        super(LiveBlogEntry, self).save()
