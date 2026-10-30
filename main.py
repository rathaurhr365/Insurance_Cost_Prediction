from fastapi import APIRouter, FastAPI
from backend.routers.prediction import router as prediction_router

app = FastAPI(title="Insurance Cost Prediction API")

app.include_router(prediction_router)