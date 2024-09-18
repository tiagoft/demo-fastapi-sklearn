from fastapi import FastAPI
import uvicorn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib

app = FastAPI()
model = joblib.load('model.joblib')

app.model = model

@app.get("/")
def route_root():
    return {"Hello": "World"}

@app.get("/predict")
def route_predict(query : str):
    prediction = app.model.predict([query])[0]
    print(prediction)
    return {"query": query,
            "prediction": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)