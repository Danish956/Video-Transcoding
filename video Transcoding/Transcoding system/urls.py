from django.contrib import admin
from django.urls import path
from Internship_app.views import *
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_internship_video',upload_internship_video,name='upload_internship_video'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
