
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    #html = "<html><body>Dados de Fuso Horário %s.</body></html>" % now //Somente para referência
    return render(request,'contas/home.html')