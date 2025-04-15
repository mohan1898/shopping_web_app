
from django.contrib import admin
from django.urls import path,include
from accountapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homeapp.urls')),
    path('accounts/',include('accountapp.urls')),
]
urlpatterns += staticfiles_urlpatterns()

# Serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)