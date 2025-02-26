from django.shortcuts import render
from django.http import HttpResponse
""" from django.forms import modelform_factory """
from picpet.models import Persona




# Create your views here.

def home(request):
    return render(request, 'home.html')

# -- inicio funcion iniciar sesion --
def iniciarSesion(request):
    return render(request, 'login.html')
# -- fin --

# -- inicio funcion validar sesion--
def validarSesion(request):
    if(request.method == 'POST'):
        persona = Persona.objects.get(email=request.POST['email'])
        
        if(persona.contrasenia == request.POST['contrasenia']):
            mensaje = "Inicio de sesion exitoso"
            return render(request, 'validarSesion.html', {'mensaje' : mensaje})
        else:
            mensaje = "Inicio de sesion fracasado"
            return render(request, 'validarSesion.html', {'mensaje' : mensaje})
    else:
        print("error primer if")
        return render(request, 'login.html')
# -- fin --

# -- inicio funcion cuentas--
def cuentas(request):
    return render(request, 'cuentas.html')
# -- fin --

# -- inicio funcion registrar artista--
def registrarArtista(request):
    return render(request, 'registrarArtista.html')
# -- fin --

# -- inicio funcion registrar persona--
def registrarPersona(request):
    return render(request, 'registrarPersona.html')
# -- fin --

# -- inicio funcion insertar persona--
def insertarPersona(request):
    if(request.method == 'POST'):
        
        personaNueva = Persona(nombre=request.POST['nombre'], apellidoPaterno=request.POST['apellidoPaterno'], apellidoMaterno=request.POST['apellidoMaterno'], nombreUsuario=request.POST['nombreUsuario'], email=request.POST['email'], edad=request.POST['edad'], contrasenia=request.POST['contrasenia'])
        if personaNueva.save() == True:
            personaNueva.save()
            return render(request, 'registrarPersona.html')
        else:
            print("NO se guardo")
            return render(request, 'registrarPersona.html')
    else:
        return render(request, 'registrarPersona.html')
# -- fin --

# -- inicio funcion read personas--    
def readPersonas(request):
    personas = Persona.objects.order_by('nombre')

    return render(request, 'readPersonas.html', {'personas' : personas})
# -- fin --