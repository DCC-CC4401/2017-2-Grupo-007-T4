from django import forms
from municipality.models import Municipality
from .models import Complaint, AnimalType, ComplaintImage


class ComplaintForm(forms.Form):
    COMPLAINT_OPTIONS = (
        (1, "Abandono en la calle"),
        (2, "Exposición a temperaturas extremas"),
        (3, "Falta de agua"),
        (4, "Falta de comida"),
        (5, "Violencia"),
        (6, "Venta ambulante"),
    )

    COMPLAINT_STATUS = (
        (1, "Reportada"),
        (2, "Consolidada"),
        (3, "Verificada"),
        (4, "Cerrada"),
        (5, "Desechada"),
    )
    COLOR_OPTIONS = (
        (1, "Marron"),
        (2, "Amarillo"),
        (3, "Blanco"),
        (4, "Gris"),
        (5, "Manchado"),
    )

    GENDER_OPTIONS = (
        (1, "Macho"),
        (2, "Hembra"),
    )

    WOUND_OPTIONS = (
        (True, "Sí"),
        (False, "No"),
    )

    lat = forms.FloatField(widget=forms.HiddenInput(), required=True)
    lng = forms.FloatField(widget=forms.HiddenInput(), required=True)
    directions = forms.CharField(max_length=200, widget=forms.HiddenInput(), required=True)
    status = forms.ChoiceField(choices=COMPLAINT_STATUS, widget=forms.HiddenInput(), required=True, initial=1)
    animal_type = forms.ModelChoiceField(label="Tipo de animal", queryset=AnimalType.objects,
                                         widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    caso = forms.ChoiceField(label="Caso de maltrato", choices=COMPLAINT_OPTIONS,
                             widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    descripcion = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=True)
    sexo = forms.ChoiceField(choices=GENDER_OPTIONS, widget=forms.Select(attrs={'class': 'form-control'}),
                             required=True)
    color = forms.ChoiceField(choices=COLOR_OPTIONS, widget=forms.Select(attrs={'class': 'form-control'}),
                              required=True)
    herido = forms.ChoiceField(choices=WOUND_OPTIONS, widget=forms.Select(attrs={'class': 'form-control'}),
                               required=True)
    municipalidad = forms.ModelChoiceField(queryset=Municipality.objects,
                                           widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=True)

    def is_valid(self):
        super(ComplaintForm, self).is_valid()

        return self.cleaned_data['status'] is not None

    def save(self):
        complaint = Complaint(description=self.cleaned_data['descripcion'], case=self.cleaned_data['caso'],
                              lat=self.cleaned_data['lat'], lng=self.cleaned_data['lng'],
                              directions=self.cleaned_data['directions'], status=self.cleaned_data['status'],
                              animal_type=self.cleaned_data['animal_type'], gender=self.cleaned_data['sexo'],
                              wounded=self.cleaned_data['herido'], color=self.cleaned_data['color'],
                              municipality=self.cleaned_data['municipalidad'])
        complaint.save()

        image = ComplaintImage(complaint=complaint, image=self.cleaned_data['foto'])
        image.save()


class ImageForm(forms.Form):
    complaint_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={'id': 'image-input', 'class': "form-control", 'placeholder': "Agrega una imagen de tu denuncia"}))
