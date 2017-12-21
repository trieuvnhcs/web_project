from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from project.upload import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^uploads/allfiles/$', views.all_files, name='all_files'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^uploads/login/$', views.login, name='login'),
    url(r'^uploads/register/$', views.register, name='register'),
    url(r'^uploads/report/$', views.report, name='report'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
