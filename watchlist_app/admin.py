from django.contrib import admin
from watchlist_app.models import Watchlist, StreamPlatform, Review

# Register your models here.
admin.site.register(Watchlist)
admin.site.register(StreamPlatform)
admin.site.register(Review)
