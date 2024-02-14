

from dataclasses import field
from pyexpat import model
from xml.dom.minidom import Attr
from django import forms
from webapp.models import Depto, Entidad, Tipo
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class ConsultasForm(forms.ModelForm):
#Depto

          
          class Meta:
                    model = Entidad 
                    fields = ['tipoentidad','palabrasclaves']
                    

                    widgets = {
                              'tipoentidad':forms.Select(attrs={'class':'form-control'}),
                               }


                     
          '''


          def formfield_for_foreignkey(self, db_field, request, **kwargs):
                    if db_field.name == 'tipoentidad':
                              return self.tipoentidadchoice.__name__          

        '''      

          """                   
                    

`
           
         # tipoentidad=forms.ModelChoiceField(label="Tipoentidad", queryset=TipoEntidad.objects.all()) 
          tipoentidad=forms.ChoiceField(choices=[(TipoEntidad.id,TipoEntidad.nombre) for TipoEntidad in TipoEntidad.objects.all()]) 
          ticket=forms.IntegerField(max_value=10)
          objetivo=forms.CharField(max_length=200)
          fecha=forms.DateField(required=False)
          nombre=forms.CharField(max_length=100)
          flota=forms.CharField(max_length=128)
          extension=forms.IntegerField()
          email=forms.EmailField()
          depto=forms.ChoiceField(choices=[(Depto.id,Depto.depto) for Depto in Depto.objects.all()]) 
"""



class ConsultasFormCreacionUsuario(forms.Form):
  usuario=forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)
  primer_nombre=forms.CharField(max_length=100)
  apellido= forms.CharField(max_length=100)
  email = forms.EmailField()
         
