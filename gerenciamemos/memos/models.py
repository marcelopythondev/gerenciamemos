from django.db import models
from tinymce import models as tinymce_models
from tinymce.models import HTMLField

def increment_chamado():
    _model = Memolist.objects.filter().order_by('-Memo')[:1]
    if _model.count() > 0:
        return int(_model[0].Memo) + 1
    return 0

class Memolist(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	Memo = models.CharField(max_length = 20, default = increment_chamado)
	Setor = models.CharField(max_length=50)
	Para = models.CharField(max_length=50)
	Assunto = tinymce_models.HTMLField('')	
	def __str__(self):		
		return '%s ' % (self.Assunto)