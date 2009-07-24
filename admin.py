from django.contrib import admin
from liveblog.models import LiveBlogEntry


class LiveBlogEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(LiveBlogEntry, LiveBlogEntryAdmin)
