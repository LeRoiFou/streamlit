"""
Lien : https://www.youtube.com/watch?v=2u4lKaJ8IOg
Formation Streamlit : Combinaison de Matplotlib, Seaborn et Plotly avec Streamlit (n°8)

Activer l'application web : 
dans la console saisir streamlit run nomfichier.py

Pour arrêter l'application web :
dans la console -> touches CTRL + C

Accéder à la documentation sur streamlit : 
dans la console saisir streamlit hello

markdown avec 1 * : italique
markdown avec 2 * : gras
markdown avec 3 * : gras et italique

Par rapport au précédent cours, on fait appel aux librairies
spécifiques à la dataviz

Date : 01-03-23
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# DF des températures hebdomadaires
temps = pd.DataFrame({
    'day':['Monday', 'Tuesday', 'Wednesday',
           'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'temp':[28, 27, 25, 31, 32 , 35, 36]
})

# DF sur les véhicules
cars = pd.read_csv('data/automobile_dataset.csv')
# Récupération des en-têtes des colonnes qui ne sont pas de type 'object'
# et les mettre dans une liste
numeric_cols = cars.select_dtypes(exclude='object').columns.to_list()
# Récupération des en-têtes des colonnes sont de type 'object'
# et les mettre dans une liste
object_cols = cars.select_dtypes(include='object').columns.to_list()

################## Plotly #################

st.subheader("Plotly")

# Diagramme en barre
fig1 = px.bar(
    data_frame=temps,
    x='day',
    y='temp',
    title="Température moyenne journalière")
st.plotly_chart(fig1)

# Menus déroulants
var_x = st.selectbox(
    "Choisir la variable dans l'axe des abscisses", 
    numeric_cols)
var_y = st.selectbox(
    "Choisir la variable dans l'axe des ordonnées", 
    numeric_cols)
var_col = st.selectbox(
    "Choisir la couleur de la variable", 
    object_cols)

# Nuage de points
fig2 = px.scatter(
    data_frame=cars,
    x=var_x,
    y=var_y,
    title=str(var_x) + ' VS ' + str(var_y),
    color=var_col
)
st.plotly_chart(fig2)
