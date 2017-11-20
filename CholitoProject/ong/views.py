from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import new_animalForm
from ong.models import ONG, ONGUser
from animals.models import Animal, AnimalImage
from django.http import HttpResponseRedirect
from CholitoProject.userManager import get_user_index


# Create your views here.
def addAnimal(request):
    if request.POST:
        form = new_animalForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

    else:
        if request.user.is_authenticated():
            ong = ONGUser.objects.get(user=request.user)
            form = new_animalForm(initial={'ong': ong.ong.id})
        else:
            ong = None
            form = None
        return render(request, 'ong_addanimal.html', {'form': form, 'ONG': ong.ong})


class IndexView(TemplateView):
    def get(self, request, **kwargs):
        if request.user.is_authenticated():
            animals = []
            ong = ONGUser.objects.get(user=request.user)
            animals_ong = Animal.objects.filter(ong_responsable=ong.ong)

            for animal in animals_ong:
                try:
                    animal_image = AnimalImage.objects.get(animal=animal)
                except:
                    animal_image = None

                animals.append({'animal': animal, 'image': animal_image})

            return render(request, 'ong-landing.html', {'ONG': ong.ong, 'animals': animals})
        else:
            return render(request, 'ong-landing.html', {})


def VistaExterna(request, ong_id):
    animals = []
    ong = ONG.objects.get(id=ong_id)

    animals_ong = Animal.objects.filter(ong_responsable=ong)

    if request.user.is_authenticated():
        c_user = get_user_index(request.user)

    for animal in animals_ong:
        try:
            animal_image = AnimalImage.objects.get(animal=animal)
        except:
            animal_image = None

        animals.append({'animal': animal, 'image': animal_image})

    return render(request, 'ong-landing-not-in.html', {'ONG': ong, 'animals': animals, 'c_user': c_user})

