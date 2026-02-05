from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    return HttpResponse('Olá MUNDO!!!')


def exibir_evento(request):
    evento = {
        "nome": "Teste",
        "categoria": "categoria A",
        "local": "Rio de Janeiro",
    }
    # template = loader.get_template('agenda/exibir_evento.html')
    # rendered_templated = template.render(context={'evento': evento}, request=request)
    # return HttpResponse(rendered_templated)
    return render(request=request, context={'evento': evento}, template_name='agenda/exibir_evento.html')