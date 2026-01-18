from django.shortcuts import render , redirect
from .models import Employe
from .forms import EmployeForm

# Create your views here.

def liste_employes(request):
    employes = Employe.objects.all()
    return render(request , 'employe/list.html' , {'employes' : employes}) 

def ajouter_employe (request):
    form = EmployeForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return redirect('liste_employes')
    return render(request , 'employe/formulaire.html' , {'form' : form})

