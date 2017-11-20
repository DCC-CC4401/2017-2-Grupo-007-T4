from animals.models import Animal, AnimalType, AnimalImage
from django import forms
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ong.models import ONG, ONGUser
from geolocation.main import GoogleMaps


class new_animalForm(forms.Form):
    GENDER_OPTIONS = (
        (1, "Macho"),
        (2, "Hembra"),
    )
    COLOR_OPTIONS = (
        (1, "Marron"),
        (2, "Amarillo"),
        (3, "Blanco"),
        (4, "Gris"),
        (5, "Manchado"),
    )
    ong = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    sexo = forms.ChoiceField(choices=GENDER_OPTIONS, widget=forms.Select(attrs={'class': 'form-control'}),
                             required=True)
    descripcion = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=True)
    animal_type = forms.ModelChoiceField(label="Tipo de animal", queryset=AnimalType.objects,
                                         widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    color = forms.ChoiceField(choices=COLOR_OPTIONS, widget=forms.Select(attrs={'class': 'form-control'}),
                              required=True)
    estimated_age = forms.IntegerField(label="Edad estimada", widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                       required=True)
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=True)

    def is_valid(self):
        super(new_animalForm, self).is_valid()

        return self.cleaned_data['ong'] is not None

    def save(self):
        animal = Animal(name=self.cleaned_data['name'], gender=self.cleaned_data['sexo'],
                        description=self.cleaned_data['descripcion'], animal_type=self.cleaned_data['animal_type'],
                        color=self.cleaned_data['color'], estimated_age=self.cleaned_data['estimated_age'],
                        ong_responsable_id=self.cleaned_data['ong'])

        animal.save()

        image = AnimalImage(animal=animal, image=self.cleaned_data['foto'])

        image.save()


class ONGRegisterForm(forms.Form):
    tipo = forms.CharField(widget=forms.HiddenInput(), initial='ONG')
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               required=True)
    direccion = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=True)

    def is_valid(self):
        super(ONGRegisterForm, self).is_valid()

        return self.cleaned_data['tipo'] == 'ONG'

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

        googleMaps = GoogleMaps(api_key=settings.GOOGLE_API_KEY)
        location = googleMaps.search(location=self.cleaned_data['direccion'])
        ong_loc = location.first()

        ong = ONG(name=self.cleaned_data['nombre'], lat=ong_loc.lat, lng=ong_loc.lng,
                  directions=self.cleaned_data['direccion'], avatar=self.cleaned_data['foto'])

        ong.save()

        ong_user = ONGUser(user=user, ong=ong)
        ong_user.save()
