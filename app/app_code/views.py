from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
	template_name='index.html'
class ResultPageView(TemplateView):
    template_name='result.html'
