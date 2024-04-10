from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            "nome",
            "altura",
            "peso",
            "cor",
            "descricao",
            "possui_os_20_dedos"
        ]