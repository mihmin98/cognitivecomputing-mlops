from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

class PredictRequest(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    def get_as_array(self):
        # arr = np.array([self.SepalLengthCm, self.SepalWidthCm, self.PetalLengthCm, self.PetalWidthCm])
        arr = np.array([self.SepalLengthCm, self.SepalWidthCm])
        return arr.reshape(1, -1)

app = FastAPI()

@app.get("/test")
async def test_get():
    return {'message': 'Hatz gionule'}

@app.get("/predict")
async def get_prediction(request: PredictRequest):
    model = None
    with open('../model/model.pickle', 'rb') as f:
        model = pickle.load(f)

    label_encoder = None
    with open('../model/label_encoder.pickle', 'rb') as f:
        label_encoder = pickle.load(f)

    prediction = model.predict(request.get_as_array())
    return label_encoder.inverse_transform(prediction)[0]

    
