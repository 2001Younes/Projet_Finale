# Projet_Finale
DATA
# Analyse des films - Application Streamlit
Cette application Streamlit permet d'analyser des données de films et d'explorer différentes fonctionnalités telles que la visualisation des acteurs, les statistiques des pays de production, la recherche de films et le classement des acteurs par genres.
## Installation:
Pour exécuter cette application en local, vous devez suivre les étapes ci-dessous :
1.	Assurez-vous d'avoir Python 3 installé sur votre système.
2.	Clonez ou téléchargez ce repository sur votre machine.
3.	Ouvrez un terminal et accédez au répertoire du projet.
4.	Installez les dépendances en exécutant la commande suivante :
pip install -r requirements.txt 
Assurez-vous d'avoir une connexion Internet active pour télécharger les packages nécessaires.

## Utilisation:
1.	Assurez-vous d'être dans le répertoire du projet dans votre terminal.
2.	Exécutez l'application Streamlit en utilisant la commande suivante :
streamlit run app_final.py 
L'application devrait se lancer et ouvrir dans votre navigateur par défaut.
3.	Sur la page d'accueil de l'application, vous trouverez différentes fonctionnalités que vous pouvez sélectionner à partir de la liste déroulante.
4.	Choisissez une fonctionnalité et explorez les différentes analyses de films disponibles.

## Fonctionnalités:
__Visualisation des acteurs:__
Cette fonctionnalité vous permet de visualiser le nombre d'acteurs qui sont apparus plus d'une fois dans chaque plateforme.
Statistiques des pays de production
Cette fonctionnalité affiche les pays de production les plus fréquents, en vous montrant le nombre de films produits dans chaque pays.
__Recherche de films:__
Vous pouvez rechercher des informations sur un film spécifique en sélectionnant son titre dans la liste déroulante. Les informations affichées incluent le titre, les acteurs, la plateforme, le genre, etc.
__Top des acteurs par genres:__
Cette fonctionnalité vous permet de rechercher les acteurs les plus populaires dans un genre de film spécifique. Sélectionnez un genre dans la liste déroulante pour afficher les acteurs et le nombre d'apparitions pour chaque acteur.

## Données:
Les données utilisées par cette application sont stockées dans un fichier CSV nommé "df_joint2.csv". Assurez-vous que ce fichier est présent dans le même répertoire que le script "app_final.py".
Les données du fichier CSV sont structurées avec les colonnes suivantes : "title", "name", "source", "genres_name", "production_countries", et d'autres informations sur les films.
