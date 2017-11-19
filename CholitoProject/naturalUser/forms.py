from django import forms
from django.contrib.auth.models import User
from naturalUser.models import NaturalUser


class PersonRegisterForm(forms.Form):
    tipo = forms.CharField(widget=forms.HiddenInput(), initial='Persona')
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    def is_valid(self):
        super(PersonRegisterForm, self).is_valid()

        return self.cleaned_data['tipo'] == 'Persona'

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        user.first_name = self.cleaned_data['nombre']
        user.last_name = self.cleaned_data['apellido']

        person = NaturalUser(user= user, avatar=self.cleaned_data['foto'], email=self.cleaned_data['email'])
        person.save()