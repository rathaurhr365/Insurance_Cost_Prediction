import pickle
import pandas as pd
from backend.Models.BaseModel import InsuranceInput
from fastapi import APIRouter


with open(r"C:\Users\HARSHIT\OneDrive\Desktop\ml_model\backend\ml_model_file\model_pipeline.pkl", "rb") as file:
    model = pickle.load(file)
router = APIRouter()

@router.post("/predict")
def predict(data: InsuranceInput):
    input_data = pd.DataFrame([{
        "age": data.age,
        "sex": data.sex,
        "bmi": data.bmi,
        "children": data.children,
        "smoker": data.smoker,
        "region": data.region
    }])

    prediction = model.predict(input_data)

    return {
        "predicted_insurance_charges": round(
            float(prediction[0]), 2
        )
    }