from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
from . import firebaseconfig

database = firebaseconfig.database()

import pandas as pd




@api_view(['GET'])
def getAllusers(request):
  
    channel_data = database.child('users') 
    return Response(channel_data.get().val())


@api_view(['POST'])
def addUser(request):
  print("****************************************")

  print(request.data)
  channel_data = database.child('users') 
  data = {"name": "John", "age": 30,"region":"ariana"}
  
  return Response( channel_data.push(data))

#fichier_csv = 'figurs_ruls.csv'
#df = pd.read_csv(fichier_csv)
#data_dict = df.to_dict(orient='records')
#for data in data_dict:
 #   database.child('figure').push(data)

#print("Données stockées avec succès dans la base de données Firebase.")


@api_view(['GET'])
def lire_csv(request):
    # Remplacez 'votre_fichier.csv' par le nom de votre fichier CSV
    fichier_csv = 'figurs_ruls.csv'
    try:
        # Lire le fichier CSV avec pandas
        df = pd.read_csv(fichier_csv)

        # Convertir le DataFrame en format JSON
        data_json = df.to_json(orient='records')

        return Response({"data": data_json})
    except Exception as e:
        return Response({"error": f"Erreur lors de la lecture du fichier CSV : {str(e)}"}, status=500)

@api_view(['GET'])
def chercher_url_par_nom(request, nom):
    fichier_csv = 'figurs_ruls.csv'
    df_images=pd.read_csv(fichier_csv)
    try:
        # Rechercher l'URL par le nom dans le DataFrame
        url = df_images.loc[df_images['titre'] == nom, 'image_url'].values[0]
        return Response({"url": url})
    except IndexError:
        return Response({"error": "Figure non trouvée"}, status=404)
 
@api_view(['GET'])
def chercher_nom_par_url(request, url):
    fichier_csv = 'figurs_ruls.csv'
    df_images=pd.read_csv(fichier_csv)
    try:
        # Rechercher le nom par l'URL dans le DataFrame
        nom = df_images.loc[df_images['image_url'] == url, 'titre'].values[0]
        return Response({"nom": nom})
    except IndexError:
        return Response({"error": "URL non trouvée"}, status=404)


     

