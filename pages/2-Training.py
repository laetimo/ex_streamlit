import streamlit as st
import requests

# Make page
st.set_page_config(page_title="Training")
st.header("Olist Dataset")
st.markdown("Entrainer le modèle pour faire de prédictions.")
st.sidebar.header("Modèle d'entrainement")

launch_training = st.sidebar.button("Lancer l'entrainement")

if launch_training:
    # Welcome message
    url = f"http://localhost:8000/train_model"
    
    # envoyer la requête à FastAPI
    response = requests.get(url)

    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        response = response.json()["Response"]
        st.success(f"Model training message : {response}")
    else:
        st.error("Error in training request")

else:
    url = f"http://127.0.0.1:8000/infos"

    # envoyer la requête à FastAPI
    response = requests.get(url)

    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        message = response.json()["message"]
        st.success(f"API welcome message: {message}")
    else:
        st.error("Error in welcome request")