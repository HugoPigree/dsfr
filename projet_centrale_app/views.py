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

def delta_medical(request):
    return render(request, 'projet_centrale_app/page_projet_medical/delta_medical.html')

def psycho_trauma(request):
    return render(request, 'projet_centrale_app/page_projet_medical/psycho-trauma.html')

def handicap(request):
    return render(request, 'projet_centrale_app/page_projet_medical/handicap.html')

def pol2as(request):
    return render(request, 'projet_centrale_app/page_projet_medical/POL2AS.html')

def gapv(request):
    return render(request, 'projet_centrale_app/page_projet_medical/GAPV.html')

def sisspo(request):
    return render(request, 'projet_centrale_app/page_projet_medical/sisspo.html')


def asa(request):
    return render(request, 'projet_centrale_app/page_projet_rh/ASA.html')

def nomenclature(request):
    return render(request, 'projet_centrale_app/page_projet_rh/nomenclature.html')

def mobipol2(request):
    return render(request, 'projet_centrale_app/page_projet_rh/MOBIPOL2.html')

def bad(request):
    return render(request, 'projet_centrale_app/page_projet_rh/BAD.html')

def retraite(request):
    return render(request, 'projet_centrale_app/page_projet_rh/retraite.html')

def pep(request):
    return render(request, 'projet_centrale_app/page_projet_rh/PEP.html')

def suivi_contractuel(request):
    return render(request, 'projet_centrale_app/page_projet_rh/suivi_contractuel.html')

def avancement(request):
    return render(request, 'projet_centrale_app/page_projet_rh/avancement.html')

def choix_poste(request):
    return render(request, 'projet_centrale_app/page_projet_rh/choix_poste.html')