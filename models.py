from pydantic import BaseModel

class PredictReq(BaseModel):
	medInc: float
	houseAge: float
	avgRooms: float
	avgBdrms: float
	population: float
	avgOccup: float
	latitude: float
	longitude: float