
from django.conf.urls import include, url
from .views import *
from django.conf import settings

urlpatterns = (
    url(r'^addAnimal/$', addAnimal, name="addAnimal"),
    url(r'^$', IndexView.as_view(), name='ong-inicio'),
)

