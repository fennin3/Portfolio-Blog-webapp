from django.contrib import admin

# Register your models here.

from .models import Post, Tag, Technologies, Portfolio, Port_Project, SkillCat, EmailList

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Technologies)
admin.site.register(Portfolio)
admin.site.register(Port_Project)
admin.site.register(SkillCat)
admin.site.register(EmailList)