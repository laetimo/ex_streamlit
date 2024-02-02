import streamlit as st
import numpy as np
# from make_pred import make_prediction
import json
import pandas as pd
import plotly.express as px
import requests

df = pd.read_csv("training_dataset.csv")

# Setup title page
st.set_page_config(page_title="Prediction")
st.header("Prediction - Olist Dataset")

# st.sidebar.markdown('Choisir les paramètres')
# colonne_selected = st.sidebar.multiselect('Choisir les colonnes',
#                                         options=['produit_recu',
#                                                 'retard_livraison',
#                                                 'temps_livraison',
#                                                 'order_status',
#                                                 'product_photos_qty',
#                                                 'product_description_lenght'])
tps_liv = st.sidebar.text_input("Temps de livraison")
rtd_liv = st.sidebar.text_input("Retard de livraison")
make_pred_API = st.sidebar.button("Lancer la prédiction")

if make_pred_API:
    url = f"http://localhost:8000/prediction/{tps_liv}/{rtd_liv}"

    # Envoyer la requête à FastAPI
    response = requests.get(url)

    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        prediction_result = response.json()['prediction_result']
        st.success(f'Résultat de la prédiction : {prediction_result}')
    else:
        st.error('Erreur dans la requête de prédiction.')
