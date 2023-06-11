import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données à partir du DataFrame
df= pd.read_csv("df_joint2.csv")


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
st.title("Analyse de films par genre")

# Options des genres de films
genres_options = df['genres_name'].unique()
selected_genre = st.selectbox("Sélectionnez un genre de film :", genres_options)

# Vérification si un genre est sélectionné
if selected_genre:
    # Recherche des acteurs les plus populaires dans le genre sélectionné
    find_top_actors_by_genre(df, selected_genre)