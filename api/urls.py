from django.urls import path 
from . import views 

urlpatterns = [
    path('add/',views.addUser),
    path('figures/',views.lire_csv),
    path('search_figure/<str:nom>/',views.chercher_nom_par_url),
    path('search_url/<str:nom>/',views.chercher_url_par_nom,name='chercher_nom_par_url'),
    #path('deletedata/', Models.deleteAllMachines, name='predict')







]
