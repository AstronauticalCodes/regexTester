from django.shortcuts import render, redirect
from django.views import View
from .forms import MainForm
from django.http import HttpResponse
import re
from .models import Record
# Create your views here.


class MainView(View):
    template_name = 'record/main.html'
    form = MainForm
    model = Record

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})

    def post(self, request, *args, **kwargs):
        match = re.match(request.POST['regex'], request.POST['text'])
        result = True if match else False
        req_copy = request.POST.copy()
        req_copy['result'] = result
        form = self.form(req_copy)
        if form.is_valid():
            form.save()
            pk = self.model.objects.all().last().id
            print(pk)
            return redirect(f'/result/{pk}/')


class ResultView(View):
    template_name = 'record/result.html'
    model = Record

    def get(self, request, pk, *args, **kwargs):
        pk = self.kwargs['pk']
        record = self.model.objects.filter(id=pk).first()
        return render(request, self.template_name, context={'record': record})


class HistoryView(View):
    template_name = 'record/history.html'
    model = Record

    def get(self, request, *args, **kwargs):
        latest_records = self.model.objects.all().order_by('-id')
        return render(request, self.template_name, context={'records': latest_records})