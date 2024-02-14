import string
from django.db import connection
from tokenize import String
from django.http import JsonResponse
from django.shortcuts import redirect
from http.client import HTTPResponse
from django.contrib import messages

from django.views.generic import ListView
from django.shortcuts import render
from webapp.forms import ConsultasForm, ConsultasFormCreacionUsuario

from webapp.models import Depto, Entidad,Solicitud, Tipo,PalabrasClaves
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,"index.html")

  

def irbase(request):
    return render(request,"base.html")


def consola_administrativa(request):
    return redirect('/admin/')



class ContactoListar(ListView): 
    model = Depto


def Consulta(request):

    messages.success(request, '')
    form = ConsultasForm()  
    
    if request.method == 'POST':
       
        form = ConsultasForm(request.POST)


        
       # print('POST', request.POST)
      #  print('BODY', request.body)
        
        if(form.is_valid()):

            

            
            
           # form = ConsultasForm() 

            pal = request.POST.getlist('palabrasclaves')
            
            cadena = []


            for p in pal:
                print(p)
                cadena.append(int(p))
            


          #  print(len(cadena)-1)
           # n=len(cadena)-1
          #  cadena=cadena[0:n]    #valores seleccionados en palabras claves

          #  cadena=(cadena.replace("'", ""))

            #print(form.cleaned_data)

            #form.cleaned_data['tipoentidad']

            

            res=Tipo.objects.get(pk=request.POST['tipoentidad'])
            print(res.nombre)

           
            tipo1=Tipo.objects.raw('select * from "TIPO" where nombre= %s', [res.nombre])

            tipov=0
            for p in tipo1:
                print(p.id)
                tipov=p.id

            with connection.cursor() as cursor:
                 consulta_sql = """(select e.nombre,e.acceso,EMP.NOMBRE AS desarrolladopor,dept.depto as administradopor,T.nombre as TIPO,e.ruta,e.rutamanual
                  from  "ENTIDAD"  e JOIN "ENTIDAD_palabrasclaves" ep 
                  on ep.entidad_id=e.id JOIN "EMPRESA" EMP
                  on EMP.ID=E.desarrolladopor_id
                  JOIN "DEPTO" dept
                  on dept.id=e.responsable_id
                  JOIN "TIPO" T
                  on  T.ID= e.tipoentidad_id  where e.tipoentidad_id = %s  and ep.palabrasclaves_id in %s ) """
                 param1=(tipov, tuple(cadena),)
                               
              
                 cursor.execute(consulta_sql, param1)
                 
                 
                 resultados = cursor.fetchall()

                
                 return render(request, 'solicitud.html', {'resultados': resultados,'form':form})

          
            #tipo1=Tipo.objects.raw("select * from ENTIDAD  e where id = %s ", [5])



           
        


            


            




            #b=Entidad.objects.all().prefetch_related("tipoenti","palabrasclav")
           
        
            
            

          

        """
       
            slc=Solicitud()
            slc.tipoConsultao = form.cleaned_data['depto']
            slc.save()-1
            """
    
   
         
         
            
        

    return render(request,'solicitud.html',{'form':form})  



def ConsultaUser(request):


   # messages.SUCCESS('hola')
   # form = ConsultasFormUser()  
    
    if request.method == 'POST':
    
        
        usuario = request.POST.get('username')
        clave=request.POST.get('password') 
        print(usuario)
        print(clave)
        login = authenticate(request=request, username=usuario, password=clave) #valida que el usuario exista en bd
        
        if(login is None):
           mensaje = "Usuario o clave incorrecta"
           return render(request, 'login.html',{'mensaje': mensaje})
          
       
        else:
            mensaje = "Bienvenidos al SGE"
            return render(request, 'index.html',{'mensaje': mensaje})



         
    else:
         print("no entre")

    return render(request,'login.html')  



def ConsultaCreacionUsuario(request):

   
    form = ConsultasFormCreacionUsuario()  

    if request.method == 'POST':

        form = ConsultasFormCreacionUsuario(request.POST)
        print(request.POST.get("usuario"))
        print(request.POST.get("password"))
        print(request.POST.get("primer_nombre"))
        print(request.POST.get("apellido"))
        print(request.POST.get("email"))

        user = User.objects.create_user(username=request.POST.get("usuario"), 
        password=request.POST.get("password"),first_name=request.POST.get("primer_nombre"),
        last_name=request.POST.get("apellido"),email=request.POST.get("email"),is_staff=True)
        user.save()

        mensaje = "Usuario Creado con Éxito!"
        return render(request, 'crearUsuario.html',{'form':form,'mensaje': mensaje})

    
    return render(request,'crearUsuario.html',{'form':form})   
    
def logout_view(request):
    logout(request)
    return redirect('login')


