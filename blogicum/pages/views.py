from django.http import HttpResponse
from django.shortcuts import render


def about(requets):
    return render(requets, template_name='pages/about.html')


def rules(requets):
    return render(requets, template_name='pages/rules.html')
