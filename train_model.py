import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, accuracy_score, f1_score
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
import streamlit as st
import pickle
# import numpy as np

def make_model_save():
    df = pd.read_csv("training_dataset.csv")
    imputer = SimpleImputer(strategy='mean')
    
    y = df['score']
    X = df[['temps_livraison','retard_livraison']]
    X = imputer.fit_transform(X)
    print(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

    model = RandomForestClassifier(max_depth=2, random_state=0)
    model.fit(X_train, y_train)

    # Save model
    with open('main_model.pkl', 'wb') as fichier_modele:
        pickle.dump(model, fichier_modele)
        st.success("Modèle entraîné avec succès!")

        predictions = model.predict(X_test)
        print(f"MAE: {str(mean_absolute_error(predictions, y_test))}")

        recall_train = round(recall_score(y_train, model.predict(X_train)), 4)
        acc_train = round(accuracy_score(y_train, model.predict(X_train)), 4)
        f1_train = round(f1_score(y_train, model.predict(X_train)), 4)
        st.text(f"Pour le jeu d'entrainement: \n le recall est de {recall_train}, \n l'accuracy de {acc_train} \n le f1 score de {f1_train}")
        recall_test = round(recall_score(y_test, model.predict(X_test)), 4)
        acc_test = round(accuracy_score(y_test, model.predict(X_test)), 4)
        f1_test = round(f1_score(y_test, model.predict(X_test)), 4)
        st.text(f"Pour le jeu de test: \n le recall est de {recall_test}, \n l'accuracy de {acc_test} \n le f1 score de {f1_test}")

# def make_model_save():
# # Import dataframe
#     df = pd.read_csv("training_dataset.csv")

# # Separate Features and Target : x and y datas
#     y = df['score'].copy()
#     x = df[['produit_recu','score']]

# # Separate Trainset / Testset
#     x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)

# # Train model
#     # model = RandomForestClassifier(max_depth=2, random_state=0)
#     model = LogisticRegression()
#     model.fit(x_train, y_train)

# # Save model
#     with open('main_model.pkl', 'wb') as fichier_modele:
#         pickle.dump(model, fichier_modele)

# # Test model
#     predictions = model.predict(x_test)
#     print(f"MAE: {str(mean_absolute_error(predictions, y_test))}")

make_model_save()
