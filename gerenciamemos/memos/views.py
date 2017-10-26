from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from memos.models import *
from memos.forms import *

def index(request):
	form = MemoForme(request.POST or None)
	if form.is_valid():
		novo_memo = form.save()        
		return redirect('listar')
	return render(request, 'memos/index.html', {'form':form})

def listamemo(request):
	data = {}
	data['lista_memo'] = Memolist.objects.all().order_by('-id')[:1]
	return render(request, 'memos/lista_memo.html', data)


def pegaregistro(request,id):
    memosalvo = Memolist.objects.get(id=id)
    form = MemoForme(request.POST or None, instance=memosalvo)
    if form.is_valid():
        return render(request,'index.html')
    return render(request, 'memos/gerapdf.html', {'objeto':memosalvo, 'form':form})

def criar_table(request):
    form = FormTabela(request.POST or None)
    if form.is_valid():
        nova_tabela = form.save_tabela()        
        return redirect('listar')
    return render(request, 'memos/tabela.html', {'form':form})

def cunsulttabla(request):
    data = {}
    data['tabela'] = Memotabela.objects.all().order_by('-id')[:1]
    return render(request, 'memos/tabela.html', data)