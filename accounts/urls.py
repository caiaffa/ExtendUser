# coding=utf-8

from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^create$', views.account_create, name='account_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.account_edit, name='account_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
