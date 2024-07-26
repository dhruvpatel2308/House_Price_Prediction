from fastapi.testclient import TestClient
import json

from server import app

client = TestClient(app)

def test_read_app():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "House Price Prediction"}

def test_predict_house_price():
	response = client.post(
			"/predict_house_price",
			json={
				'medInc': 8.3252,
				'houseAge': 41,
				'avgRooms': 6.0,
				'avgBdrms': 1.0,
				'population': 1.0,
				'avgOccup': 2.5,
				'latitude': 37.88,
				'longitude': -122.23,
			}
		)

	assert response.status_code == 200