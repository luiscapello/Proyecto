from cgitb import html
from django.shortcuts import render, HttpResponse

layout = """
<h1>Sitio web con Django</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de Prueba</a>
    </li>
</ul>
<hr/>
"""

# Create your views here.

def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    """
    year = 2022
    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"

    return HttpResponse(layout + html)

def hola_mundo(request):
    return HttpResponse(layout +"""
        <h1>Hola mundo con Django !!</h1>
        <h3> Creado por Capello </h3>
    """)

def pagina(request):
    return HttpResponse(layout +"""
        <h1>Pagina de mi Web</h1>
        <p>Creado por Capello</p>
    """)

def contacto(request):
    return HttpResponse(layout + "<h2>Contactos</h2>")