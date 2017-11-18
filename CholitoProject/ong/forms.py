from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from ong.models import ONG, ONGUser
from geolocation.main import GoogleMaps


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
