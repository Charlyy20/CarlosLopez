from django.shortcuts import render
from . import models

def home (request): 
    query = models.Comision.objects.all()
    context = {"comisiones": query}
    return render(request, 'PreEntrega/index.html', context)
