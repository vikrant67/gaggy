from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [	
    url(r'^admin/', admin.site.urls),
    
    url(r'^gag/', include('gag.urls')),
    url(r'^accounts/', include('allauth.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)