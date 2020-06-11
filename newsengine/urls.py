from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import settings
from .views import redirect_news

urlpatterns = [
    path('blog/', redirect_news),
    path('news/', include('news.urls')),
    path('weather/', include('weather.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
