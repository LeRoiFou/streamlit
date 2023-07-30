"""
Lien : https://www.youtube.com/watch?v=hKTI4d9RU8I&list=PLmJWMf9F8euQKADN-mSCpTlp7uYDyCQNF&index=7
Formation Streamlit : Fonctions intrinsèques de Streamlit pour la visualisation des données (n°7)

Activer l'application web : 
dans la console saisir streamlit run nomfichier.py

Pour arrêter l'application web :
dans la console -> touches CTRL + C

Accéder à la documentation sur streamlit : 
dans la console saisir streamlit hello

markdown avec 1 * : italique
markdown avec 2 * : gras
markdown avec 3 * : gras et italique

Dans ce cours on apprend à faire des graphiques directement avec
Streamlit sans recourir à Matplotlib, Seaborn...

Date : 01-03-23
"""

import streamlit as st
import pandas as pd
import numpy as np

# Affichage d'un titre
st.title("Initialisation à la Data Viz avec Streamlit")

# Sous-titre
st.subheader("Auteur : Josué")

# Texte
st.markdown(
    ("***Cette application affiche différents types "
     "de graphiques***"))

# Tracé linéaire
data = np.random.normal(size=1_000)
st.line_chart(data)

# Diagramme à barre
bar_data = pd.DataFrame(
    [100, 19, 88, 54],
    ['A', 'B', 'C', 'D'])
st.bar_chart(bar_data)

# Carte
df = pd.read_csv('data/new_york.csv').head(100)
st.write(df.head(10))
st.map(df[['longitude', 'latitude']])
