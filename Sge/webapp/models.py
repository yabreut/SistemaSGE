from ast import Num
from contextlib import nullcontext
import email
from operator import truediv
from pickle import TRUE
from random import choices
from re import VERBOSE
from secrets import choice
from select import select
from sre_parse import Verbose
from tabnanny import verbose
from xml.parsers.expat import model
from django.db import models
from django.forms import model_to_dict
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

from . import opciones
#from .managers import CategoriaBaseDeDatosManager
# Create your models here.



class Estado(models.Model):
    estado = models.CharField(max_length=50,unique=TRUE)

    def save(self) -> None:
        self.estado=self.estado.upper()    #para que se guerde en mayuscula en bd
        return super().save(self)


    class Admin:
        list_display = ('nombre estado')

  
    def __str__(self):
        return  f'''  
            Estado : {self.id} : {self.estado} 
        '''
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'ESTADO'
        ordering = ['estado']


class BaseDeDatos(models.Model):
    nombre = models.CharField(max_length=100,unique=TRUE)
    host = models.CharField(max_length=30,unique=TRUE)            
    puerto = models.IntegerField()
    estado = models.ForeignKey(Estado,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name_plural = "BaseDeDatos"
        db_table = "BASEDEDATOS"
        ordering = ["id"]

    def __str__(self):
        return  f'''  
        Base De Datos: {self.nombre}
        Host: {self.host}
        Puerto: {self.puerto}

        '''

    class Admin:
        list_display = ('nombre', 'host', 'puerto','estado')
        list_filter = ('nombre', 'estado')
        ordering = ('nombre',)
        search_fields = ('title',)



class Direccion(models.Model):
    direccion=models.CharField(max_length=100,unique=TRUE)

    def __str__(self) -> str:
        return f'''  
            Direccion : {self.id} : {self.direccion} 
        '''
    
    def save(self) -> None:
        self.direccion=self.direccion.upper()
        return super().save(self)

    class Meta:
        verbose_name_plural = "Direcciones Administrativas"
        ordering = ["direccion"]
        db_table = "DIRECCION"

class Gerencia(models.Model):
    gerencia=models.CharField(max_length=100,unique=TRUE)
    direccion=models.ForeignKey(Direccion, on_delete=models.SET_NULL,null=True)

    def save(self) -> None:
        self.gerencia=self.gerencia.upper()
        return super().save(self)

    def __str__(self) -> str:
        return f'''  
            gerencia : {self.id} : {self.gerencia} 
        '''
    
    class Meta:
        verbose_name_plural = "Gerencias"
        db_table = "GERENCIA"

class Depto(models.Model):
    depto = models.CharField(max_length=100,unique=TRUE)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.SET_NULL,null=True)
    correogrupal=models.EmailField(default=None,null=True,blank=True) #para que permita valores nulos


    def save(self,*args, **kwargs) -> None:
        self.depto=self.depto.upper()

        if not self.correogrupal:  #si no tiene valor el campo lo guarda vacio
            self.correogrupal= None

        
        return super(Depto, self).save(*args, **kwargs)
        
    def __str__(self):
        return  f'''  
            Depto : {self.id} : {self.depto} 
            Email : {self.correogrupal}
        '''
    class Meta:
        verbose_name_plural = "Departamentos"
        ordering = ["depto"]
        db_table = "DEPTO"
    

class LenguajeProgramacion(models.Model):
    nombre = models.CharField(max_length=50,unique=TRUE)

    def save(self) -> None:
        self.nombre=self.nombre.upper()
        return super().save(self)
   
    def __str__(self):
        return  f'''  
            Lenguaje Programación : {self.id} : {self.nombre} 
           
        '''
    class Meta:
        verbose_name_plural = "Lenguajes De Programación"
        ordering = ["nombre"]
        db_table = "LENGUAJEPROGRAMACION"


class Manejador(models.Model):
    nombre = models.CharField(max_length=100)
    ipservidor =  models.CharField(max_length=50)
    estado_manejador = models.ForeignKey(Estado,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return  f'''  
            Manejador : {self.id} : {self.nombre} 
            Servidor : {self.ipservidor}
           
        '''

    class Meta:
        verbose_name_plural = "Manejadores"
        ordering = ["nombre"]
        db_table = "MANEJADOR"




class PalabrasClaves(models.Model):
    nombre = models.CharField(max_length=100,unique=TRUE)
    
    def save(self) -> None:
        {self.nombre} 
        return super().save(self)

    def __str__(self):
        return  f'''  
            {self.nombre} 
           
        '''
    class Meta:
        verbose_name_plural = "Palabras Claves"
        ordering = ["nombre"]
        db_table = "PALABRASCLAVES"

    

class SistemaOperativo(models.Model):
    nombre = models.CharField(max_length=100,unique=TRUE)
    
    class Meta:
        verbose_name_plural = "Sistemas Operativos"
        ordering = ["nombre"]   
        db_table = "SISTEMAOPERATIVO"
        
    def __str__(self):
        return  f'''  
            Sistema Operativo : {self.nombre} 
           
        '''
        
class Tipo(models.Model):
  
    nombre = models.CharField(max_length=100,unique=TRUE)
    categoria = models.CharField(choices = opciones.categoria, max_length=50)
    
    class Meta:
        verbose_name_plural = "Tipos"
        ordering = ["nombre"]   
        db_table = "TIPO"
        
    def __str__(self):
        return  f' {self.nombre}'

        #return  f'Tipo : {self.id} : {self.nombre} Categoria : {self.categoria}'


"""
class TipoBaseDeDatos(models.Model):

    objects = CategoriaBaseDeDatosManager()
    
    class Meta:
        abstract = True
       # proxy = True
"""



        


class Empresa(models.Model):
    nombre = models.CharField(max_length=100,unique=TRUE)
    
    class Meta:
        verbose_name_plural = "Empresas"
        ordering = ["nombre"]   
        db_table = "EMPRESA"
        
    def __str__(self):
        return  f'''  
            nombre : {self.nombre}  
           
        '''
    

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
   # flota =  PhoneNumberField()
    
    flotaRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    flota = models.CharField(validators = [flotaRegex], max_length = 16, unique = True)

    email=models.EmailField(unique=True)
       
   

    def __str__(self):
        return  f'''  
            Persona : {self.id} : {self.nombre} {self.apellido}
            Flota : {self.flota}
            email : {self.email} 
        '''
    class Meta:
        verbose_name_plural = "Personas"
        ordering = ["nombre",'apellido']   
        db_table = "PERSONA"


class Entidad(models.Model):
    
    accesos=(
        ("CITRIX", "Citrix"),
        ("CORREO", "Correo"),
        ("DESKTOP","Desktop"),
        ("WEB", "Web"),)

    nombre = models.CharField(max_length=100,unique=True)
    cantidad_usuario = models.IntegerField()
    tiempo_ejecucionsegundo = models.IntegerField()
    bases_de_datos = models.ManyToManyField(BaseDeDatos)
    acceso = models.CharField(max_length=50,choices = accesos,null=True)
    depto_utilizan = models.ManyToManyField(Depto)
    responsable = models.ForeignKey(Depto, on_delete=models.SET_NULL,null=True, related_name='DeptoResponsable')
    manejador = models.ManyToManyField(Manejador)
    palabrasclaves=models.ManyToManyField(PalabrasClaves)
    Objetivo = models.CharField(max_length=200)
    tipoentidad = models.ForeignKey(Tipo,on_delete=models.SET_NULL,null=True)
    ruta = models.CharField(max_length=200,null=True,)
    rutamanual= models.CharField(max_length=300,null=True,blank=True)
    
    #objects = models.Manager() # The default manager.
      
  # tipoentidad = CategoriaBaseDeDatosManager()
    #tipoentidad = models.ForeignKey(TipoBaseDeDatos,on_delete=models.SET_NULL,null=True)
 

    sistemaoperativo = models.ForeignKey(SistemaOperativo,on_delete=models.SET_NULL,null=True)
    desarrolladopor = models.ForeignKey(Empresa,on_delete=models.SET_NULL,null=True)
#.objects.get(categoria="ENTIDAD")

    """
     
    def save(self): 
        self.Objetivo=self.Objetivo.upper()
        return super().save(self)
      """  

    class Meta:
        db_table ='ENTIDAD'  #nombre que tendra en base de datos
        verbose_name_plural = "Entidades"       #como se va a mostrar cuando hayan varios elementos
        db_table = "ENTIDAD"             #el nombre como se va a crear la tabla en bd
        ordering = ["id", "nombre"]



    def __str__(self):
        return  f'''  
            Entidad : {self.id} : {self.nombre} 
            cantidad_usuario : {self.cantidad_usuario}
            tiempo_ejecucionsegundo : {self.tiempo_ejecucionsegundo}
            manejador : {self.manejador}
            objetivo : {self.Objetivo}
                        
        '''
    """
    class Admin:
        list_display = ('nombre', 'cantidad_usuario', 'bases_de_datos')
        list_filter = ('publisher', 'publication_date')
        ordering = ('nombre',)
        search_fields = ('tipoentidad',)
    """
    


class UsuarioLider(models.Model):
  
    persona = models.ForeignKey(Persona,on_delete=models.SET_NULL,null=True)
    entidad = models.ManyToManyField(Entidad)

    def __str__(self):

        cadena=self.persona.nombre+","+self.persona.apellido+","+self.persona.flota+","+self.persona.email
        #+","+self.entidad.nombre+","+self.entidad.tipoentidad
       
       
        return cadena

    
    class Meta:
        verbose_name_plural = "Usuarios Lideres"       #como se va a mostrar cuando hayan varios elementos
        db_table ='USUARIOLIDER'  #nombre que tendra en base de datos
        ordering = ["persona"]
   
    
    
 

class HBasededatos(models.Model):
    bd = models.ForeignKey(BaseDeDatos,on_delete=models.SET_NULL,null=True) 
    Estado = models.ForeignKey(Estado,on_delete=models.SET_NULL,null=True)
    fecha = models.DateField()

    class Meta:
        verbose_name_plural = "Historial Base de Datos"       #como se va a mostrar cuando hayan varios elementos
        db_table ='HBASEDEDATOS'  #nombre que tendra en base de datos
        ordering = ["bd"]

class HManejador(models.Model):
    manejador = models.ForeignKey(Manejador,on_delete=models.SET_NULL,null=True) 
    Estado = models.ForeignKey(Estado,on_delete=models.SET_NULL,null=True)
    fecha = models.DateField()

    class Meta:
        verbose_name_plural = "Historial Manejadores"       #como se va a mostrar cuando hayan varios elementos
        db_table ='HMANEJADOR'  #nombre que tendra en base de datos
        ordering = ["manejador"]

class Solicitud(models.Model):
    tipoentidad = models.ForeignKey(Tipo,on_delete=models.SET_NULL,null=True)
    nombre = models.CharField(max_length=200,null=True)
    ticketenkace = models.IntegerField()
    objetivo_solicitud = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now=False) 
    nombre_solicitante = models.CharField(max_length=100)
    extension = models.IntegerField()
    email_solicitante = models.EmailField()
    depto = models.ForeignKey(Depto,on_delete=models.SET_NULL,null=True)

    flotaRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    flota_solicitante = models.CharField(validators = [flotaRegex], max_length = 16, unique = False)

    class Meta:
        verbose_name_plural = "Solicitudes"       #como se va a mostrar cuando hayan varios elementos
        db_table ='SOLICITUD'  #nombre que tendra en base de datos
        ordering = ["nombre","-fecha"]



"""

  )
  LOGGING ;

"""
