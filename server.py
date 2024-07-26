from fastapi import FastAPI
from models import PredictReq
import pickle
import json
import numpy as np

app = FastAPI()

ml_model = None
# Load the XGBoost model
with open('xgb_model.pkl', 'rb') as model_file:
	ml_model = pickle.load(model_file)

# This is just the normal getter api to check if working of the entire backend
@app.get("/")
def foo():
	return {
		"status": "House Price Prediction"
	}

@app.post("/predict_house_price")
def predice_house_price(req: PredictReq):
	inp = np.array([[
				req.medInc,
				req.houseAge,
				req.avgRooms,
				req.avgBdrms,
				req.population,
				req.avgOccup,
				req.latitude,
				req.longitude,
			]])

	prediction = ml_model.predict(inp)[0]

	return {
		'price': str(prediction*100)
	}