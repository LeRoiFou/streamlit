"""
Lien : https://www.youtube.com/watch?v=Zs9-8trPadU
Cours : Using STREAMLIT with AG Grid Table - Interactive Table | Part 2/2

L'insertion d'une barre latérale et filtrer une donnée puis annuler le filtre,
permet d'avoir la hauteur de la DF ajustée à l'écran et d'obtenir la pagination
en bas de la DF sans recourir à l'instruction 'height' lors de l'exécution
de la mise en page des scripts effectués avec la librairie aggrid

Date : 09-03-23
"""

import pandas as pd
import streamlit as st
# Mise en forme : filtre, trie, déplacement des colonnes
from st_aggrid import AgGrid
# Options complémentaires : pagination, barre latérale...
from st_aggrid.grid_options_builder import GridOptionsBuilder
# Saisies en JavaScript : condition sur cellule et suppression ligne
from st_aggrid.shared import JsCode

@st.cache_data 
def data_upload():
    return pd.read_csv('data/covid-variants.csv')

# Chargement de la DF
df = data_upload()

# Sous-menu (fenêtre de gauche de la fenêtre principale)
_funct = st.sidebar.radio('Selection type', options=['Display', 'Activate'])

# Sous-titre
st.subheader("This is AgrGrid Table")


############################# Options avec AgGrid #############################

gd = GridOptionsBuilder.from_dataframe(df) # configuration avec la DF

gd.configure_pagination(enabled=True) # pagination en bas de la DF

gd.configure_side_bar() # barre latérale : filtre / colonnes à afficher / TCD

gd.configure_default_column(editable=True, # Modification des données 😮 
                            groupable=True # TCD 😮
                            )

# Dans cette option complémentaire :
# En sélectionnant 'single', on ne peut sélectionner qu'une ligne dans la DF
# En sélectionnait 'multiple', on peut sélectionner plusieurs lignes dans la DF

sel_mode = st.radio( # Widget radio
    'Selection Type', # Titre du widget radio
    options=['single', 'multiple'] # Options du widget radio
    )

gd.configure_selection(selection_mode=sel_mode, # interaction avec le widget radio
                       use_checkbox=True # coche présente dans la DF
                       )


####################### JavaScript : condition cellule #######################

cellstyle_jscode = JsCode(
    """
    function(params) {
        if (params.value == 'Alpha') {
        return {
            'color': 'black',
            'backgroundColor': 'orange'
        }   
        }
        if (params.value == 'Beta') {
        return {
            'color': 'black',
            'backgroundColor': 'red'
        }   
        }
        else{
        return {
            'color': 'black',
            'backgroundColor': 'lightpink'
        }    
        }
    };   
    """
)

# Activation du script de JS
gd.configure_column("variant", cellStyle=cellstyle_jscode)


####################### JavaScript : suppression de lignes #######################

# Si l'option 'Activate' est selectionnée...
if _funct == 'Activate':
    
    js = JsCode(
        """
        function(e) {
            let api = e.api;
            let sel = api.getSelectedRows();
            api.applyTransaction({remove: sel})   
        };
        """
    )

    # Activation du script de JS
    gd.configure_grid_options(onRowSelected=js)


########################## Activation et mise en page ##########################

gridoptions=gd.build()

AgGrid(df, # DF
       gridOptions=gridoptions, # options complémentaires
       fit_columns_on_grid_load=True, # ajustement automatique des colonnes
    #    height=500, # en mettant une taille, la pagination disparaît...
       enable_enterprise_modules=True, # Script JS
       allow_unsafe_jscode=True, # Script JS
       )
