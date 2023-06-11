import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données à partir du DataFrame
data = pd.read_csv("df_joint2.csv")

def generate_production_countries_stats(data):
    # Compter le nombre d'occurrences pour chaque pays de production
    country_counts = data["production_countries"].value_counts()

    # Sélectionner les 10 pays les plus représentés
    top_countries = country_counts.head(10)

    # Créer un graphique à barres pour illustrer les pays les plus représentés
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_countries.values, y=top_countries.index, ax=ax)
    ax.set_xlabel("Nombre de films")
    ax.set_ylabel("Pays de production")
    ax.set_title("Pays de production les plus fréquents")
    st.pyplot(fig)

# Interface utilisateur avec Streamlit
st.title("Statistiques des pays de production")
st.write("Créez une visualisation des pays de production les plus fréquents dans le DataFrame.")

# Afficher les statistiques des pays de production lorsque le bouton est cliqué
if st.button("Afficher les statistiques"):
    generate_production_countries_stats(data)