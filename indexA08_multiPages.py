"""
Lien : https://www.youtube.com/watch?v=bybdfk3UVT0&list=PLmJWMf9F8euQKADN-mSCpTlp7uYDyCQNF&index=15
Cours : Comment créer une application multi-pages avec Streamlit | Python ?

Création d'une application web avec plusieurs pages (menu) 🫢

Il suffit tout simplement de créer un sous-dossier dans le repértoire 
où se trouve le fichier principal .py 🤣🤣🤣

... si on veut partager le fichier, il faut recourir à GitHub
-> il faut donc savoir créer des sous-répertoires dans GitHub 🤔

Création également d'un sous-menu

Date : 04-03-23
"""

import streamlit as st

my_var = "C'est une variable du module 'Page'"

def main():
    
    st.header("PAGE D'ACCUEIL")
    st.title("Tuto sur Streamlit multi-pages 🫢")
    st.write(my_var)
    
    choix = st.sidebar.radio("Sous-menu", ["Description", "Documentation"])
    if choix == "Description":
        st.subheader("Voici la description de l'application web")
    if choix == "Documentation":
        st.subheader("Voici la documentation de l'application web")
    
if __name__ == '__main__':
    main()