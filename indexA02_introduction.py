"""
Lien : https://www.youtube.com/watch?v=f-XpmMnF2Lk&list=PLmJWMf9F8euQKADN-mSCpTlp7uYDyCQNF&index=4
Cours : Formation Streamlit : Affichage d'une dataframe pandas et d'un graphique dans Streamlit (n°4)

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

# Affichage du graphique
fig, ax = plt.subplots()
ax.hist(data.Dist_norm)
st.pyplot(fig)
