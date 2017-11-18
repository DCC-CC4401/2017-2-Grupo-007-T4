from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import new_animalForm
from ong.models import ONG, ONGUser
from animals.models import Animal
from django.http import HttpResponseRedirect


# Create your views here.
def addAnimal(request):
    if request.POST:
        animal = request.POST.get('animal')
        gender = request.POST.get('gender')
        color = request.POST.get('color')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        description = request.POST.get('description')
        animal_type = request.POST.get('animal_type')
        estimated_age = request.POST.get('estimated_age')
        if request.user.is_authenticated:
            ong = ONGUser.objects.get(ong_id=request.user.id)
            animal_obj = Animal(animal=animal, gender=gender, color=color, name=name, description=description,
                                animal_type=animal_type, estimated_age=estimated_age, ong_responsable=ong)
        else:
            return HttpResponseRedirect('/')
    else:
        form = new_animalForm()
        return render(request, 'ong_addanimal.html', {'form': form})

class IndexView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'ong-estadisticas.html', {})

