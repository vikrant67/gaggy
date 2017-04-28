from django.contrib import admin


from .models import Upload,Comment,Liked

admin.site.register(Upload)
admin.site.register(Comment)
admin.site.register(Liked)

