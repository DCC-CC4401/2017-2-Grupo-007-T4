from django.conf.urls import url

from animals.views import AnimalRenderView, AdoptView

urlpatterns = [
    url(r'^(?P<animal_id>[0-9]+)/$', AnimalRenderView.as_view(), name='verAnimal'),
    url(r'^adopt/$', AdoptView.as_view(), name='adopt')
]
