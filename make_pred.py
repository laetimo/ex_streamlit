import pickle

def make_prediction(x):
    # Charger le modèle à partir du fichier Pickle
    with open('main_model.pkl', 'rb') as fichier_modele:  # rb read binary
        loaded_model = pickle.load(fichier_modele)

    # Faire la prédiction
    predictions_out = loaded_model.predict(x)

    # retourner la valeur
    return predictions_out
