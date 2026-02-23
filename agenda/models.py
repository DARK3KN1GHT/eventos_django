from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.id} <{self.nome}"


class Evento(models.Model):
    nome = models.CharField(max_length=256)
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)

    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    quantidade_participantes = models.PositiveIntegerField(default=0)
    
    categoria = models.ForeignKey(
        Categoria,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.id} <{self.nome}>"
