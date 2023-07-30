"""
Lien : https://www.youtube.com/watch?v=HNoF9dU_vrU&list=PLmJWMf9F8euQKADN-mSCpTlp7uYDyCQNF&index=3
Cours : Formation Streamlit : Création d'une application Hello World dans Streamlit (n°3)

Activer l'application web : 
dans la console saisir streamlit run nomfichier.py

Pour arrêter l'application web :
dans la console -> touches CTRL + C

Accéder à la documentation sur streamlit : 
dans la console saisir streamlit hello

Pour partager le fichier sur @ :
https://share.streamlit.io/
Puis récupérer le fichier .py mis sur GitHub
Dans le cas où l'application ne se lancerait pas, cela peut provenir de packages
non reconnus dans streamlit, tel que matplotlib.
Pour cela, crééer dans la même répertoire que le fichier .py un fichier .txt 
avec le nom "requirements" : dans ce mettre le package à recourir ainsi que sa version
Exemple : matplotlib==3.6.3

Date : 01-03-23
"""

import streamlit as st

st.write('Hello World! My name is John Gerald 😎')
