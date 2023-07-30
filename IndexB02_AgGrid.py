"""
Lien : https://www.youtube.com/watch?v=F54ELJwspos
Cours : Using STREAMLIT with AG Grid Table - Interactive Table | Part 1/2

Date : 08-03-23
"""

import pandas as pd
import streamlit as st
# Mise en forme : filtre, trie, déplacement des colonnes
from st_aggrid import AgGrid
# Options complémentaires
from st_aggrid.grid_options_builder import GridOptionsBuilder

@st.cache_data 
def data_upload():
    return pd.read_csv('data/covid-variants.csv')

# Chargement de la DF
df = data_upload()

# st.subheader("This is Streamlit default DF")
# st.dataframe(df)
# st.info(df.shape)

# Sous-titre
st.subheader("This is AgrGrid Table")

############################# Options complémentaires #############################

gd = GridOptionsBuilder.from_dataframe(df) # configuration avec la DF

gd.configure_pagination(enabled=True) # pagination en bas de la DF

gd.configure_default_column(editable=True, # Modification des données 😮 
                            groupable=True # TCD 😮
                            )

# Dans cette option complémentaire :
# En sélectionnant 'sigle', on ne peut sélectionner qu'une ligne dans la DF
# En sélectionnait 'multiple', on peut sélectionner plusieurs lignes dans la DF

sel_mode = st.radio( # Widget radio
    'Selection Type', # Titre du widget radio
    options=['single', 'multiple'] # Options du widget radio
    )

gd.configure_selection(selection_mode=sel_mode, # interaction avec le widget radio
                       use_checkbox=True # coche présente dans la DF
                       )

# Activation des options complémentaires
gridoptions=gd.build()

############################# Mise en page #############################

AgGrid(df, # DF
       gridOptions=gridoptions, # options complémentaires
       )

