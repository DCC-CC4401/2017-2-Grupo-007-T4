from django.conf.urls import include, url

from .views import *

from django.conf import settings

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='ong-inicio')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
