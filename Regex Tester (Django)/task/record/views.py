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