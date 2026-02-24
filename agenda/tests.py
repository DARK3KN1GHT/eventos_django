from django.test import TestCase, Client
from django.utils import timezone
from datetime import timedelta

from .models import Evento, Categoria

class TestPaginaInicial(TestCase):
    def test_lista_eventos_mostra_cabecalhos(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "<th>Nome</th>", html=True)
        self.assertContains(response, "<th>Categoria</th>", html=True)
        self.assertContains(response, "<th>Local ou Link</th>", html=True)
        self.assertContains(response, "<th>Data</th>", html=True)

    def test_eventos_antigos_nao_aparecem(self):
        hoje = timezone.localdate()
        cat = Categoria.objects.create(nome="Aula")

        Evento.objects.create(
            nome="Evento antigo",
            local="X",
            data=hoje - timedelta(days=1),
            categoria=cat,
        )

        Evento.objects.create(
            nome="Evento futuro",
            local="Y",
            data=hoje + timedelta(days=1),
            categoria=cat,
        )

        client = Client()
        response = client.get("/")

        self.assertContains(response, "Evento futuro")
        self.assertNotContains(response, "Evento antigo")