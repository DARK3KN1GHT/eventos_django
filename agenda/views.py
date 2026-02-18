from django.shortcuts import render, get_object_or_404
from .models import Evento

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, "agenda/design/listar_eventos.html", {"eventos": eventos})

def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, "agenda/design/exibir_evento.html", {"evento": evento})
