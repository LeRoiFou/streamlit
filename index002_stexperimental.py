"""
Lien 1 : https://blog.streamlit.io/editable-dataframes-are-here/?_hsmi=248366074&_hsenc=p2ANqtz-_Np9-xNa2pHrjVVQoOr9udV-EszgaxWQEqw0T3yuxr--P89rslYH62mgu2C5ahwnpSOvK9871DmjS2Bwg3jRzG6qzI8A
Lien 2 : https://docs.streamlit.io/library/api-reference/widgets/st.experimental_data_editor?ref=streamlit

Nouveauté sur streamlit : possibilité de modifier la DF directement sur @ 😮😮😮
Vraiment à titre expérimental, car pour l'instant il n'y a que la possibilité de modifier les cellules

Éditeur : Laurent Reynaud
Date : 02-03-23
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

my_df = pd.read_csv('data/titanic.csv').head(20)
my_df = my_df[['Name', 'Age']]

edited_df = st.experimental_data_editor(my_df, num_rows='dynamic')
