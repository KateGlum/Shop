from django import forms
from .models import Zakaz, Annotation


class ZakazForm(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = ('name', 'phone', 'data_zakaza', 'zakaz', 'total')


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = ('author', 'text')