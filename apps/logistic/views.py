from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from apps.logistic.components.LogisticForm import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from apps.logistic.models import *


# Create your views here.


# Customers
class LoadsView(ListView):
    model = Load
    template_name = 'logistic/load/loadViews.html'

class LoadsCreate(CreateView):
     model = Load
     form_class = LoadsForm
     template_name = 'logistic/load/loadForm.html'

     def get(self, request, *args, **kwargs):
         form = self.form_class(initial=self.initial)
         return render(request, self.template_name, {'form': form, 'title': 'Create new Load'})

     def post(self, request, *args, **kwargs):
         user = request.user
         form = self.form_class(request.POST)
         if form.is_valid():
             load = form.save(commit=False)
             load.users_id = user.id
             load.save()
             return HttpResponse(reverse_lazy('logistic:loads'))

class LoadsEdit(UpdateView):
    model = Load
    form_class = LoadsForm
    template_name = 'logistic/load/loadForm.html'
    success_url = reverse_lazy('logistic:loads')


class LoadsDelete(DeleteView):
    model = Load
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('logistic:loads')

class LoadPDF(View):
    def get(self, request, *args, **kwargs):
        receipt = Load.objects.get(id_lod=self.pk)
        data = {
            'date': '27/5/2017',
            'description': 'Prueba de recibo',
            'total': '50,00',
        }
        pdf = render('accounting/receipts/receiptsPrint.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
