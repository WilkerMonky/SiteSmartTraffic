from typing import Any, Dict
from django.views.generic import TemplateView
from .models import Membro, Registro

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['membros'] = Membro.objects.order_by('?').all()
        context['membro1'] = Membro.objects.get(id=1)
        context['membro2'] = Membro.objects.get(id=2)
        context['membro3'] = Membro.objects.get(id=3)
        context['registros'] = Registro.objects.all()
        print(context['registros'])

        return context
