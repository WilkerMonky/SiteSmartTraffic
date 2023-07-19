from typing import Any, Dict
from django.views.generic import TemplateView, FormView
from .models import Membro, Registro, SugestoesModel
from .forms import SugestoesModelForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(FormView):
    model = SugestoesModel
    template_name = 'index.html'
    form_class = SugestoesModelForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['membros'] = Membro.objects.order_by('?').all()
        context['membro1'] = Membro.objects.get(id=1)
        context['membro2'] = Membro.objects.get(id=2)
        context['membro3'] = Membro.objects.get(id=3)
        context['registros'] = Registro.objects.all()
        
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.save()
        messages.success(self.request, 'Mensagem enviado com suceso')
        return super().form_valid(form)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar Mensagem')
        return super().form_invalid(form, *args, **kwargs)
    

