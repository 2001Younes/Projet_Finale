import streamlit as st
import pandas as pd

df = pd.read_csv('df_joint2.csv')

def get_film_info(df, title):
    film_info = df[df['title'] == title].iloc[0]
    return film_info

# Titre de la page de l'application
st.title("Informations sur les films")

# Options des films les plus vus
film_options = df['title'].unique()
input_title = st.selectbox("Entrez le titre du film :", film_options)

# Vérification si un titre est saisi
if input_title:
        # Recherche des informations sur le film
        film_info = get_film_info(df, input_title)

        # Vérification si le film existe dans le DataFrame
        if not film_info.empty:
            # Affichage des informations du film
            st.subheader(f"Informations sur le film '{input_title}' :")
            st.write(film_info)
        else:
            st.write("Film non trouvé.")