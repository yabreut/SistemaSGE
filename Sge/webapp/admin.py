from django.contrib import admin
from webapp.models import Direccion,Estado,BaseDeDatos,Depto, Gerencia,LenguajeProgramacion,Manejador,PalabrasClaves, Tipo,Tipo,Persona,Entidad,UsuarioLider,SistemaOperativo,Empresa

# Register your models here.
admin.site.register(Estado)
admin.site.register(BaseDeDatos)

admin.site.register(Depto)
admin.site.register(Gerencia)
admin.site.register(Direccion)


admin.site.register(LenguajeProgramacion)
admin.site.register(Manejador)
admin.site.register(PalabrasClaves)
admin.site.register(Tipo)


admin.site.register(Persona)
admin.site.register(Entidad)
admin.site.register(UsuarioLider)
admin.site.register(SistemaOperativo)
admin.site.register(Empresa)