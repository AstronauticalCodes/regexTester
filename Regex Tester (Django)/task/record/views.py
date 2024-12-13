from django.shortcuts import render
from django.views import View
from .forms import MainForm
# Create your views here.


class MainView(View):
    template_name = 'record/main.html'
    form = MainForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})