"""
Lien : https://www.taipy.io/tips/using-tables/

Avec Taipy, c'est possible de présenter des tables 😲😲😲
https://docs.taipy.io/en/develop/manuals/gui/viselements/table/

Date : 01-08-23
Éditeur : Laurent Reynaud
"""

from taipy.gui import Gui, notify
import pandas as pd

my_df = pd.read_csv('data/weather.csv')

# Selon la température, recourir aux couleurs configurées dans le fichier css
def table_style(state, index, row):
    # Si dans le champ MinTemp la valeur est < à 0...
    if row.MinTemp < 5:
        # Récupérer la configuration de la couleur dans le fichier css
        result = 'brrr'
    elif row.MaxTemp > 30:
        result = 'grrr'
    else:
        result = ''
    return result

# Modification des valeurs dans la DF éditée
def my_df_on_edit(state, var_name, action, payload):
    index = payload["index"] # row index
    col = payload["col"] # column name
    value = payload["value"] # new value cast to the column type
    user_value = payload["user_value"] # new value as entered by the user
 
    old_value = state.my_df.loc[index, col]
    new_my_df = state.my_df.copy()
    new_my_df.loc[index, col] = value
    state.my_df = new_my_df
    notify(state, "I", f"Valeur modifiée de '{old_value}' à '{value}'. (index '{index}', colonne '{col}')")

# Propriétés de la table
table_properties = {
    "filter":True, # Filtre
    "class_name":"rows-bordered rows-similar", # épaisseur des lignes de la DF
    "style":table_style, # Récupération de la fonction ci-avant
    "on_edit": my_df_on_edit,
    }

page = """
<|{my_df}|table|properties=table_properties|>
"""

Gui(page=page).run()
