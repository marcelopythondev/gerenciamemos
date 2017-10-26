from django.forms import ModelForm
from memos.models import *
from django import forms


class MemoForme(ModelForm):
    class Meta:
        model = Memolist
        fields = ['Memo', 'Setor', 'Para', 'Assunto']

class FormMemo(forms.Form):	
	"""docstring for FormMemo"""	
	id = models.AutoField(primary_key=True, editable=False)
	Memo = models.CharField(max_length = 20, default = increment_chamado, editable=False)
	Setor = forms.CharField(max_length=50)
	Para = forms.CharField(max_length=50)	
	Assunto = forms.CharField(max_length=500)
	

			
	
class FormTabela(forms.Form):
	coluna = models.CharField(max_length = 50)
	linha = models.CharField(max_length = 50)
		
def save():
	id = self.cleaned_data.get('id')
	Memo = self.cleaned_data.get('Memo')
	Setor = self.cleaned_data.get('Setor')
	Para = self.cleaned_data.get('Para')
	Assunto = self.cleaned_data.get('Assunto')

	novo_memo(
		id = id,
		Memo = Memo,
		Setor = Setor,
		Para = Para,
		Assunto = Assunto,
		
	)
	novo_memo.save()
	return novo_memo

def save_tabela():	
	coluna = self.cleaned_data.get('coluna')
	linha = self.cleaned_data.get('linha')
	nova_tabela(		
		coluna = coluna,
		linha = linha,
	)
	nova_tabela.save_tabela()
	return nova_tabela

def cleaned_Memo(self):
	Memo = self.cleaned_data.get('id')
	if Memolist.object.filter(email = email):
		raise forms.ValidationError('Memo já cadastrado!')
		return Memo