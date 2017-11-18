from ong.views import addAnimal
from django.conf.urls import url
urlpatterns = (
    url(r'^addAnimal/$', addAnimal, name="addAnimal"),
)