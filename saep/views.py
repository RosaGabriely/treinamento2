from django.shortcuts import render
from .models import Usuario

def cadastroUsuarios(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Usuario.objects.create(name=name, email=email)
    
    return render(request, 'cadastroUsuarios.html')
