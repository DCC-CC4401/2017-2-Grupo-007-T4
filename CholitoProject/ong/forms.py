from animals.models import Animal, AnimalType
from django import forms
from django.db import models

class new_animalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = (
            'name',
            'gender',
            'description',
            'animal_type',
            'color',
            'estimated_age',

        )
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name-input'}),
            'gender': forms.RadioSelect(attrs={'id': "gender-input"}),
            'description': forms.TextInput(attrs={'id': "description-input"}),
            'animal_type': forms.Select(attrs={'id': 'animal_type-input'}),
            'color': forms.TextInput(attrs={'id': 'color-input'}),
        }

        def __init__(self, *args, **kwargs):
            super(new_animalForm, self).__init__(*args, **kwargs)
            self.fields['animal_type'] = forms.ModelChoiceField(queryset=AnimalType.objects)
            self.field['estimated_age']=models.PositiveSmallIntegerField()