from django.shortcuts import render
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
        print(req_copy)
        print(request.POST)
        print(req_copy)
        if form.is_valid():
            print('hello')
            form.save()
            return HttpResponse(f"<h2>{result}</h2>")