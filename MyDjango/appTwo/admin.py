from django.contrib import admin
from appTwo.models import AccessRecord, Topic, WebPage, User
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(User)