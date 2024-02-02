from fastapi import FastAPI
import numpy as np
from train_model import make_model_save
from make_pred import make_prediction
import pandas as pd
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import json

app = FastAPI()

@app.get("/infos")
def read_root():
    return {"message" : "Hello, welcome on my dashboard"}

# lancer uvicorn api_func:app --reload dans un terminal bash

@app.get("/train_model")
def train_model():
    make_model_save()
    print("Training in progress")
    return {"Response" : "Training completed."}

@app.get("/prediction/{tps_liv}/{rtd_liv}")
def get_predict(tps_liv: int, rtd_liv : int):
    p1 =[tps_liv,rtd_liv]
    x = np.array([p1])
    col_headers = ['temps_livraison', 'retard_livraison']
    
    x_df = pd.DataFrame(x, columns = col_headers)

    # Faire des prédictions
    prediction_result = make_prediction(x_df)
    prediction_result_json = jsonable_encoder(prediction_result)

    return { "prediction_result": prediction_result_json}
