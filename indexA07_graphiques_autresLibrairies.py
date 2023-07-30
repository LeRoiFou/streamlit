"""
Lien : https://www.youtube.com/watch?v=xOdMiSeDTeE&list=PLmJWMf9F8euQKADN-mSCpTlp7uYDyCQNF&index=9
Formation Streamlit : Graphiques Matplotlib et Seaborn dans Streamlit (n°9)

Activer l'application web : 
dans la console saisir streamlit run nomfichier.py

Pour arrêter l'application web :
dans la console -> touches CTRL + C

Accéder à la documentation sur streamlit : 
dans la console saisir streamlit hello

markdown avec 1 * : italique
markdown avec 2 * : gras
markdown avec 3 * : gras et italique

Appel aux librairies spécifiques à la dataviz :
plotly, matplotly et seaborn

Avis personnel : plotly !

Date : 04-03-23
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# DF des températures hebdomadaires
temps = pd.DataFrame({
    'day':['Monday', 'Tuesday', 'Wednesday',
           'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'temp':[28, 27, 25, 31, 32 , 35, 36]
})

# DF sur les données des appartements à new-york
airbnb = pd.read_csv('data/new_york.csv')

st.title("Plotly, Seaborn et Matplotlib")

################## Plotly #################

st.subheader("Plotly")

fig_px = px.histogram(
    data_frame=airbnb,
    x=airbnb['availability_365'],
    nbins=50, # Nombre de barres
    labels={"availability_365":"Jour d'occupation"}, # Changement du titre abscisse
    title="Nombre de jours d'occupation de l'appartement")

st.plotly_chart(fig_px)

################## Matplotlib #################

st.subheader("Matplotlib")

fig_mt, ax_mt = plt.subplots()
ax_mt = plt.hist(airbnb['availability_365'])
plt.xlabel("Nombre de jours d'occupation de l'appartement")

st.pyplot(fig_mt)

################## Seaborn #################

st.subheader("Seaborn")

fig_sb, ax_b = plt.subplots()
ax_b = sns.histplot(airbnb['availability_365'])
plt.xlabel("Nombre de jours d'occupation de l'appartement")

st.pyplot(fig_sb)
