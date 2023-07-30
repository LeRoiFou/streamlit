"""
Lien : https://www.youtube.com/watch?v=_H_4rb2G59w&list=PLmJWMf9F8euQKADN-mSCpTlp7uYDyCQNF&index=5
Cours : Formation Streamlit : Ajout d'entrées utilisateurs pour la réactivité d'une application web (n°5)

Activer l'application web : 
dans la console saisir streamlit run nomfichier.py

Pour arrêter l'application web :
dans la console -> touches CTRL + C

Accéder à la documentation sur streamlit : 
dans la console saisir streamlit hello

Date : 01-03-23
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(size=1_000)
data = pd.DataFrame(data, columns=['Dist_norm'])

# Affichage de la DF
st.write(data.head())

# Configuration du graphique
fig, ax = plt.subplots()

# Zone de saisie : nombre de bins
n_bins = st.number_input(
    label="Choisir un nombre de bins",
    min_value=10,
    value=20, # valeur par défaut
)

# Adaptation du graphique par rapport au nombre de bins
ax.hist(data.Dist_norm, # graphique à afficher
         bins=n_bins # zone de saisie de l'utilisateur
         )

# Zone de saisie : titre du graphique
graph_title = st.text_input(
    label="Ecrire le titre du graphique"
)

# Titre à ajouter au graphique
plt.title(graph_title)

# Affichage du graphique
st.pyplot(fig)
