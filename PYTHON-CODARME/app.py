from evento import Evento
from evento_online import EventoOnline

ev_online = EventoOnline('Live de Python')
ev2_online = EventoOnline('Live de JavaScript')
# ev_online.imprime_informacoes()
# ev2_online.imprime_informacoes()
print(ev_online.to_json())
print(ev2_online.to_json())

ev = Evento('Aula de Python', 'Rio de Janeiro')
ev.imprime_informacoes()
