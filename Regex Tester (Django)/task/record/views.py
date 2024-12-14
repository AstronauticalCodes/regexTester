from django.shortcuts import render
from django.views import View
from .forms import MainForm
from django.http import HttpResponse
import re
# Create your views here.


class MainView(View):
    template_name = 'record/main.html'
    form = MainForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            match = re.match(request.POST.regex, request.POST.text)
            form.save()
            return HttpResponse(f"<h2>{True if match else False}</h2>")