from django.conf import settings
from django.conf.urls import url

from django_pyinfo.views import PyInfoView

if settings.DEBUG:
    urlpatterns = [url(r'^pyinfo/$', PyInfoView.as_view(), name='pyinfo'),]