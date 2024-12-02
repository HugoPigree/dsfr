from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def index(request):
    return render(request, 'projet_centrale_app/index.html')

def medical(request):
    return render(request, 'projet_centrale_app/medical.html')

def rh(request):
    return render(request, 'projet_centrale_app/rh.html')

def autres(request):
    return render(request, 'projet_centrale_app/autres.html')

def drhfs(request):
    return render(request, 'projet_centrale_app/drhfs.html')

def utilisateurs(request):
    return render(request, 'projet_centrale_app/utilisateurs.html')
