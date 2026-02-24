from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Evento

def listar_eventos(request):
    hoje = timezone.localdate()
    eventos = Evento.objects.filter(data__gte=hoje).order_by("data", "hora")
    return render(request, "agenda/design/listar_eventos.html", {"eventos": eventos})

def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, "agenda/design/exibir_evento.html", {"evento": evento})

def participar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento.quantidade_participantes += 1
    evento.save()
    return redirect("exibir_evento", id=id)