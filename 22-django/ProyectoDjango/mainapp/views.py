from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def register_page(request):
    return render(request, 'users/register.html',{
        'title': 'Registro'
    })