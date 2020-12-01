from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from PaginaProyecto.forms import ContactoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from pic.models import *

def index(request):
	return render(request, 'index.html')

def prod0(request):
	prods1 = Productos_Medicinales.objects.all();
	prods2 = Semillas.objects.all();
	prods3 = Suplementos.objects.all();
	prods4 = Herramientas.objects.all();
	return render(request, 'prodAll.html', {'prods1': prods1, 'prods2': prods2, 'prods3': prods3, 'prods4': prods4,})

def prod1(request):
	prodsM = Productos_Medicinales.objects.all();
	return render(request, 'prod1.html', {'prodsM': prodsM})

def prod2(request):
	prodsSe = Semillas.objects.all();
	return render(request, 'prod2.html', {'prodsSe': prodsSe})

def prod3(request):
	prodsH = Herramientas.objects.all();
	return render(request, 'prod3.html', {'prodsH': prodsH})

def prod4(request):
	prodsSu = Suplementos.objects.all();
	return render(request, 'prod4.html', {'prodsSu': prodsSu})

def buscar(request):
	if 'busca' in request.GET and request.GET['busca']:
		consulta = request.GET['busca']
		prods1F = Productos_Medicinales.objects.filter(nombre__icontains=consulta);
		prods2F = Semillas.objects.filter(nombre__icontains=consulta);
		prods3F = Suplementos.objects.filter(nombre__icontains=consulta);
		prods4F = Herramientas.objects.filter(nombre__icontains=consulta);
		return render(request, 'resultado.html', {'prods1F': prods1F, 'prods2F': prods2F, 'prods3F': prods3F, 'prods4F': prods4F,})
	else:
		return render(request, 'resultado.html', {'error': True})

def contacto(request):
	if request.method == 'POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Correo de PIC'
			contenido = formulario.cleaned_data['mensaje'] + '\n\n'
			contenido += 'Comunicarse al correo ' + formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to=['inboxPIC2020@gmail.com'])
			try:
				correo.send()
				return render(request, 'correoEnviado.html')
			except:
				return render(request, 'correoNoEnviado.html')
		else:
			return render(request, 'contacto.html', {'error': True, 'formulario':formulario})

	else:
		formulario = ContactoForm()
		return render(request, 'contacto.html', {'formulario': formulario})

def usuarioNuevo(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)
		try:
			formulario.save()
			return render(request, 'usuarioAgregado.html')
		except:
			return render(request, 'usuarioNuevo.html',{'error':True, 'formulario': formulario})
	else:
		formulario = UserCreationForm()
		return render(request, 'usuarioNuevo.html',{'formulario': formulario})

def ingresar(request):
	if not request.user.is_anonymous:
		return HttpResponseRedirect('/privado')
	elif request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/privado')
			else:
				return render(request, 'noUsuario.html')
	else:
		formulario = AuthenticationForm()
		return render(request, 'ingresar.html', {'formulario': formulario})

@login_required(login_url='/ingresar')
def privado(request):
	usuario = request.user
	return render(request, 'privado.html',{'usuario': usuario})

def salir(request):
	if not request.user.is_anonymous:
		logout(request)
		return HttpResponseRedirect('/ingresar')
	else:
		return render(request, 'noLogueado.html')

def error404(request, exception):
	response = render(request, 'error404.html',{})
	return response

def error500(request):
	response = render(request, 'error500.html',{})
	return response