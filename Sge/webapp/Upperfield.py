from django import forms

class Upperfield(forms.CharField):

    def to_python(self, value):
        return value.upper()


class TipoEntidad(forms.ModelForm):
    nombre = Upperfield()
    