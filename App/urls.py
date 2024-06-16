
from django.urls import path
from .import views 



urlpatterns = [

    path('',views.index ,name="index" ),
    path('login/',views.login_view ,name='login_view' ),
    path('register/',views.register ,name='register' ),
    path('home/',views.home,name='home' ),
   
    path('chef/',views.chef,name='chef' ),
    path('chef_equipe/',views.responsables,name='responsables' ),
  
    path('projet/',views.liste_des_projets,name='listedesprojet'),
    path('personnel/',views.liste_des_personnel,name='liste_personnel' ),
    path('Ajouter_personnel/',views.ajouter_personnel,name='AjouterPersonnel' ),
    path('editer_personnel<int:pk>/',views.edit_personnel,name='editerpersonnel'),
    path('creer_projet',views.creer_projet,name='creer' ),
    path('editer_projet<int:pk>/',views.edit_projet,name='editer'),
    path('supprimer_projet<int:pk>/',views.supprimer_projet,name='effacer'),
    

    
   
]