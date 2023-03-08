"""
LIEN ENTRE LA DATA SCIENCE ET LE SAAS

Pour une facilité du recours à un SAAS avec des données de Pandas, Numpy, 
le plus simple est de recours au package Streamlit

Documentation
Présentation : https://datascientest.com/streamlit-ou-loutil-pour-presenter-votre-travail-de-machine-learning
Exemples : https://www.datacamp.com/tutorial/streamlit
Librairie des widgets : https://docs.streamlit.io/library/api-reference/data

https://youtu.be/0ESc1bh3eIg

-------------------------------------------------------------------------

Les étapes suivantes ont été appliquées pour lancer le package Streamlit

ETAPE 1 : Création de l'environnement virtuel à partir de la console
-> Création d'un environnement virtuel : python -m venv .venv
-> Travaux sur l'environnement virtuel : .venv/Scripts/activate

ETAPE 2 : Package Streamlit installé
pip install streamlit

ETAPE 3 : lancer le script suivant dans la console
python -m streamlit run NomFichier.py

-------------------------------------------------------------------------

Pour arrêter le navigateur, il faut appuyer sur les touches suivantes :
CTRL + MAJ + P
Puis sélectionner "Terminal : Relancer le terminal actif"
(Raccourci clavier créé : ALT + D)

Pour relancer le navigateur internet :
-> relancer à nouveau le terminal pour être dans l'environnement virtuel
-> puis saisir dans la console : streamlit run NomFichier.py

-------------------------------------------------------------------------

Il n'est pas possible d'intégrer automatiquement dans la page web
une DF issue de la librairie Polars
https://github.com/streamlit/streamlit/issues/4212
Pour ce faire, il faut convertir la DF sous format 'Pandas',
avec l'instruction suivante : my_df.to_pandas()

Date : 05-01-23
"""

import pandas as pd
import streamlit as st


st.header(":green[Présentation sous la forme d'une SAAS] :sunglasses:")
st.text('\n')

my_file = st.file_uploader("Sélectionnez un fichier à charger")

if st.button("Afficher les données"):
    if my_file is not None:
        # Traitement du fichier
        my_df = pd.read_csv(my_file)
        st.write(my_df)
    else:
        st.write("Aucun fichier sélectionné")

if st.button("Liste des villes"):
    if my_file is not None:
        my_df = pd.read_csv(my_file)
        group_df = my_df.groupby('city').sum().reset_index()
        st.dataframe(group_df['city'])
    else:
        st.write("Aucun fichier sélectionné")
        
st.markdown("# C'est qui le boss ?!? #")

st.text("À gauche c'est débit et à droite c'est crédit 🤣😆")

