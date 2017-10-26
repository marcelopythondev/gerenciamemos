from django.conf.urls import *
from memos.views import *


urlpatterns = [
	url(r'^$', index, name='inicio'),
	url(r'^listar', listamemo, name='listar'),
	#url(r'^pdfview/', reportlab_teste, name='pdfview'),
	url(r'^tabela', criar_table, name='tabela'),
	url(r'^mostraultimoid/(?P<id>\d+)/', pegaregistro, name='mostraultimoid'),
]