from django.contrib import admin
from .models import Profile, ClassSites, Assignment, Message

# Register your models here.
admin.site.register(Profile)
admin.site.register(ClassSites)
admin.site.register(Assignment)
admin.site.register(Message)