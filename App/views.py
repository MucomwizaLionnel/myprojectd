from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# from .forms import ProfileForm,LoginForm,FormTache
from django.contrib.auth import authenticate,login
from .models import *

from .forms import *


def index(request):
    return render(request, 'index.html')

def register(request):
    profil_form=ProfileForm(request.POST or None, request.FILES)
    if (request.method=='POST'):
        if (profil_form.is_valid()):
            nom_utilisateur=profil_form.cleaned_data['nom_utilisateur']
            mots_de_pass=profil_form.cleaned_data['mots_de_pass']
            mots_de_pass1=profil_form.cleaned_data['mots_de_pass1']
            nom_prenom=profil_form.cleaned_data['nom_prenom']
            
            date_naissance=profil_form.cleaned_data['date_naissance']
            genre=profil_form.cleaned_data['genre']
            qualification=profil_form.cleaned_data['qualification']
            telephone=profil_form.cleaned_data['telephone']
            address=profil_form.cleaned_data['address']
            date_enre=profil_form.cleaned_data['date_enre']
            if (mots_de_pass==mots_de_pass1):
                user=User.objects.create_user(username=nom_utilisateur, password=mots_de_pass)

                user.first_name=nom_prenom
                user.last_name=nom_prenom
                
                user.save()
                group = Group.objects.get_or_create(name= "personnel")
                user.groups.add(group[0])
                profil=Personnel(
                        user=user,
                        nom_prenom=nom_prenom,
                        
						date_naissance=date_naissance,
						genre=genre,
                        qualification=qualification,
						address=address,
						telephone=telephone,
                        date_enre=date_enre).save()
                if user:
                    login(request, user)
                    return redirect(index)
                else:
                    return redirect(login_view)
            else: 
                profil_form=ProfileForm(request.FILES)
                return render(request, 'register.html',locals())
    return render(request, 'register.html',locals())
    

def login_view(request):
    Connexion_form=ConnexionForm(request.POST or None)
    msg=None
    if request.method=='POST':
        if Connexion_form.is_valid():
            nom_utilisateur=Connexion_form.cleaned_data.get('nom_utilisateur')
            mots_de_pass=Connexion_form.cleaned_data.get('mots_de_pass')
            user=authenticate(username=nom_utilisateur,password=mots_de_pass)


            if user:#si l'objet existe 


                login(request, user)
                groups = [group.name for group in user.groups.all()]
                if user.is_superuser or 'personnel' in groups:
                     return redirect(index) #on connecte l'utilisateur
                if user.is_superuser or 'chef' in groups:
                    return redirect(chef) #on connecte l'utilisateur
                if 'responsable' in groups:
                    return redirect(responsables) #on connecte l'utilisateur
                if 'personnel' in groups:
                    return redirect(index) #on connecte l'utilisateur
                
            
            else:
                Connexion_form=ConnexionForm()
        else:
            Connexion_form=ConnexionForm()
            return render(request, 'login.html', locals())
    return render(request, 'login.html', locals())
        
def home(request):
    return render(request,'homepage.html')
def liste_des_personnel(request):
    personnels=Personnel.objects.all()
    return render(request,'liste_personnel.html',{'personnels': personnels})  
def ajouter_personnel(request):
    if request.method=='POST':
        form=Personnel_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('liste_personnel')    
    else:
        form=Personnel_form()
    return render(request,'personnel_form.html',{'form':form})      
def edit_personnel(request,pk):
    personnels=get_object_or_404(Personnel,pk=pk)
    if request.method=='POST':
        form=Personnel_form(request.POST,instance=personnels)
        if form.is_valid():
            form.save()
            return redirect('liste_personnel')
    else:
        form=Personnel_form(instance=personnels)

    return render(request,'projet_form.html',{'form':form})
   


def liste_des_projets(request):
    projets=Projet.objects.all()
    return render(request,'projet.html',{'projets': projets})
def creer_projet(request):
    if request.method=='POST':
        form=Projet_form(request.POST)
        if form.is_valid():
            form.save() 
           
            
        return redirect('listedesprojet')
    else:
        form=Projet_form()

    return render(request,'projet_form.html',{'form':form})    

def edit_projet(request,pk):
    projets=get_object_or_404(Projet,pk=pk)
    if request.method=='POST':
        form=Projet_form(request.POST,instance=projets)
        if form.is_valid():
            form.save()
            return redirect('listedesprojet')
    else:
        form=Projet_form(instance=projets)

    return render(request,'projet_form.html',{'form':form})

def supprimer_projet(request,pk):
    projets=get_object_or_404(Projet,pk=pk)
    if request.method=='POST':
        projets.delete()
        return redirect('listedesprojet')
    return render(request, 'supprimer_projet.html', {'projets': projets})






def chef(request):
    return render(request,'chef.html')
 
def responsables(request):
    return render(request,'chef_equipe.html')    
# def liste_personnel(request):
#     personnels = Personnel.objects.all()
#     return render(request, 'liste_personnel.html', {'personnels': personnels})
    
def transaction(request):
    return render(request,'transaction.html') 
def charge(request):
    return render(request,'charge.html') 
def rapport(request):
    return render(request,'rapport.html') 

