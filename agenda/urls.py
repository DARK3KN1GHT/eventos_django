from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_eventos, name="listar_eventos"),
    path("eventos/<int:id>/", views.exibir_evento, name="exibir_evento"),
    path("eventos/<int:id>/participar/", views.participar_evento, name="participar_evento"),
]