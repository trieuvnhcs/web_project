from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from project.upload import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^all_files/$', views.all_files, name='all_files'),
    url(r'^upload/$', views.model_form_upload, name='model_form_upload'),    
    url(r'^report/(?P<document_id>[0-9]+)/$', views.report, name='report'),
    url(r'^doc/(?P<document_id>[0-9]+)/$', views.one_file, name='one_file'),   
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
