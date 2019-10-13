from django.contrib import admin
from .models import Categories, News, Reviews, Images, Videos, Cms, Contacted

# Register your models here.
admin.site.register(Categories)
admin.site.register(News)
admin.site.register(Reviews)
admin.site.register(Images)
admin.site.register(Videos)
admin.site.register(Cms)
admin.site.register(Contacted)