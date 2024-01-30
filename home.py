import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

st.set_page_config(
    page_title="[Maximilien] Streamlit : build and share data apps",
    page_icon="📈",
)

st.write("# Quest Streamlit Wild Code School !")




st.markdown(
    """
    ### Challenge
    A partir du dataset des voitures, tu afficheras :

    - Une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires.
    - Des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon).
    - L'application doit être disponible sur la plateforme de partage.

    ### Critères de validation

    - L'application est accessible en ligne
    - L'analyse est effectuée, avec des commentaires explicatifs
    - Des boutons sont présents pour filtrer par région

    ### Présentation du Dataframe
    Voici les dix premières lignes :

    """
)

st.dataframe(df_cars.head(10))
