from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('Home.urls')),
    path ('', include('Blog.urls'))
]

from django.conf.urls.static import static
from django.conf import settings

url_patterns_for_media= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + url_patterns_for_media