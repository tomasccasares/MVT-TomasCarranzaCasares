from django.shortcuts import render
from app_desafio.models import Familia

def lista_familiares(request):

    context = {}
    context['familiares'] = Familia.objects.all() # me traigo todos los objetos, que vienen dentro de una lista
    # los elementos de la lista(en donde estan los objetos) seran los valores de la clave: familiares

    return render(request, 'app_desafio/lista_familiares.html', context)
    # y ahora render armara el template con la pagina web(html) y lo trae devuelta para view
    # y view se lo da al servidor y luego el nav me lo va a traer a mi despues de ejecutar runserver
    
