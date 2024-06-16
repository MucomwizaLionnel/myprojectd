from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.exceptions import ValidationError
import datetime



class ProfileForm(forms.Form):
	#____________pour user___________________#
		nom_utilisateur=forms.CharField(max_length=7)
		mots_de_pass=forms.CharField(max_length=20, widget=forms.PasswordInput)
		mots_de_pass1=forms.CharField(max_length=20, widget=forms.PasswordInput)
		nom_prenom=forms.CharField(max_length=20)
		
	#______________champ pou profil___________#
		date_naissance = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
		genre = forms.CharField(max_length=20)
		qualification=forms.CharField(max_length=20)
		telephone = forms.CharField(max_length=20)
		address = forms.CharField(max_length=20)
		date_enre=forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
class ConnexionForm(forms.Form):
	nom_utilisateur= forms.CharField(widget= forms.TextInput(attrs={
    		'placeholder':'nom_utilisateur....',
    		}),label="nom_utilisateur :")
	mots_de_pass = forms.CharField(widget= forms.PasswordInput(attrs={
    		'placeholder':'mots_de_pass....',
    		}),label="mots_de_pass :")
    

class Personnel_form(forms.ModelForm):

    class Meta:
        model=Personnel
        fields='__all__'
            

class Projet_form(forms.ModelForm):

    class Meta:
        model = Projet
        fields = '__all__'
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_field(self):
        date = self.cleaned_data['date_field']
        if date:
            try:
                datetime.datetime.strptime(str(date), '%Y-%m-%d')
            except ValueError:
                raise ValidationError('La date doit être au format AAAA-MM-JJ.')
        return date