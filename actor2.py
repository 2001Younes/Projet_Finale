import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Interface utilisateur avec Streamlit
st.title("Visualisation des acteurs")
st.write("Visualiser le nombre d'acteurs qui sont apparus plus d'une fois dans chaque plateforme.")

visualize_duplicate_actors()
