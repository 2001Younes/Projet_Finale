import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données à partir du DataFrame
df = pd.read_csv("df_joint2.csv")

def visualize_duplicate_actors():
    # Compter le nombre d'apparitions de chaque acteur dans chaque plateforme
    actor_platform_count = df.groupby(["source", "name"]).size().reset_index(name="count")

    # Sélectionner les acteurs qui sont apparus plus d'une fois dans une même plateforme
    duplicate_actors = actor_platform_count.loc[actor_platform_count["count"] > 1]

    # Créer un graphique à barres montrant le nombre d'acteurs qui sont apparus plus d'une fois dans chaque plateforme
    fig, ax = plt.subplots(figsize=(10, 6))
    duplicate_actors.groupby("source")["name"].count().plot(kind="bar", color="blue", ax=ax)

    # Ajouter les étiquettes et les titres
    ax.set_xlabel("Plateforme")
    ax.set_ylabel("Nombre d'acteurs")
    ax.set_title("Acteurs qui sont apparus plus d'une fois dans une même plateforme")

    # Afficher le graphique
    st.pyplot(fig)

def generate_production_countries_stats():
    # Compter le nombre d'occurrences pour chaque pays de production
    country_counts = df["production_countries"].value_counts()

    # Sélectionner les 10 pays les plus représentés
    top_countries = country_counts.head(10)

    # Créer un graphique à barres pour illustrer les pays les plus représentés
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_countries.values, y=top_countries.index, ax=ax)
    ax.set_xlabel("Nombre de films")
    ax.set_ylabel("Pays de production")
    ax.set_title("Pays de production les plus fréquents")
    st.pyplot(fig)

def get_film_info(title):
    film_info = df[df['title'] == title].iloc[0]
    return film_info

def find_top_actors_by_genre(df, genre_input):
    # Filtrer les lignes pour ne conserver que les films du genre spécifié
    genre_films = df[df['genres_name'] == genre_input]
    
    # Vérifier si le genre spécifié est présent dans le DataFrame
    if genre_films.empty:
        st.write("Le genre spécifié n'est pas présent dans le DataFrame.")
        return None
    
    # Compter le nombre d'apparitions de chaque acteur dans les films du genre spécifié
    actor_counts = genre_films['name'].value_counts()
    
    # Obtenir les acteurs ayant le plus grand nombre d'apparitions
    top_actors = actor_counts.head(10)

    # Afficher le DataFrame de genre_input
    st.subheader(f"Top acteurs dans le genre '{genre_input}':")
    st.write(top_actors)

    # Afficher le graphique des acteurs
    fig, ax = plt.subplots(figsize=(10, 6))
    top_actors.plot(kind='bar', ax=ax)
    ax.set_title(f"Top acteurs dans le genre '{genre_input}'")
    ax.set_xlabel("Acteurs")
    ax.set_ylabel("Nombre d'apparitions")
    st.pyplot(fig)

# Interface utilisateur avec Streamlit
st.title("Analyse de films")

# Options des différentes fonctionnalités
options = ["Recherche de films","Visualisation des acteurs", "Statistiques des pays de production", "Top des acteurs par genres"]
selected_option = st.selectbox("Sélectionnez une fonctionnalité :", options)

# Afficher la fonctionnalité sélectionnée
if selected_option == "Recherche de films":
    # Titre de la page de l'application
    st.title("Informations sur les films")
    
    # Options des films disponibles
    film_options = df['title'].unique()
    input_title = st.selectbox("Entrez le titre du film :", film_options)

    # Vérification si un titre est saisi
    if input_title:
        # Recherche des informations sur le film
        film_info = get_film_info(input_title)

        # Vérification si le film existe dans le DataFrame
        if not film_info.empty:
            # Affichage des informations du film
            st.subheader(f"Informations sur le film '{input_title}' :")
            st.write(film_info)
        else:
            st.write("Film non trouvé.")

elif selected_option == "Statistiques des pays de production":
    st.subheader("Statistiques des pays de production")
    st.write("Visualisez les pays de production les plus fréquents.")
    generate_production_countries_stats()

elif selected_option == "Visualisation des acteurs":
    st.subheader("Visualisation des acteurs")
    st.write("Visualisez le nombre d'acteurs qui sont apparus plus d'une fois dans chaque plateforme.")
    visualize_duplicate_actors()

elif selected_option == "Top des acteurs par genres":
    # Interface utilisateur avec Streamlit
    st.title("Analyse de films par genre")

    # Options des genres de films
    genres_options = df['genres_name'].unique()
    selected_genre = st.selectbox("Sélectionnez un genre de film :", genres_options)

    # Vérification si un genre est sélectionné
    if selected_genre:
        # Recherche des acteurs les plus populaires dans le genre sélectionné
        find_top_actors_by_genre(df, selected_genre)