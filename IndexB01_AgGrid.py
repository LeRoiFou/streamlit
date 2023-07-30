"""
La librairie AgGrid s'utilise pour les DF insérées 
dans une page Web avec la librairie Streamlit

Package installé : pip install streamlit-aggrid

https://towardsdatascience.com/7-reasons-why-you-should-use-the-streamlit-aggrid-component-2d9a2b6e32f0

Cette librairie est similaire aux graphiques générés à partir 
de la librairie Plotly : les DF sont manipulables

Problématique avec cette librairie :
Au-delà de 500 lignes, il y a un problème de chargement de la DF 😭

Date : 08-03-2023
"""

import pandas as pd 
import streamlit as st 
# Mise en forme : filtre, trie, déplacement des colonnes
from st_aggrid import AgGrid
# Options complémentaires : 
# pagination, filtre, colonnes à afficher, TCD
from st_aggrid.grid_options_builder import GridOptionsBuilder
# Couleur des cellules selon des conditions
from st_aggrid.shared import JsCode

# Titres de la fenêtres et plein page
st.set_page_config(page_title="Agrid !!!", layout="wide") 
st.title("Agrid !!! Où est le hibou ???")

# Mettre en cache pour que la DF ne soit chargée qu'une seule fois
@st.cache_data
def load_df():
    return pd.read_csv("data/titanic.csv")

# Chargement de la DF
shows = load_df()

# Options complémentaires (pagination, barre latérale... )
gb = GridOptionsBuilder.from_dataframe(shows)
gb.configure_pagination() # pagination
gb.configure_side_bar() # barre latérale : filtre / colonnes à afficher / TCD

# Couleur des cellules selon des conditions
cellsytle_jscode = JsCode(
    """
function(params) {
    if (params.value.includes('female')) {
        return {
            'color': 'red'}
    } 
};
"""
)
# Colonne concernée selon la condition décrite ci-avant
gb.configure_column("Sex", cellStyle=cellsytle_jscode)

# Mise en place des options complémentaires
gridOptions = gb.build()

# Affichage avec la librairie AgGrid
AgGrid(shows, # DF
    #    height=500, # Taille de la DF
       gridOptions=gridOptions, # Options complémentaires
       enable_enterprise_modules=True, # Couleur de la cellule selon la condition
       allow_unsafe_jscode=True # Couleur de la cellule selon la condition
       )
