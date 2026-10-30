# Insurance Cost Prediction

A machine learning project that predicts estimated medical insurance charges based on personal details such as age, BMI, smoking habits, number of children, sex, and region.

## Features
- Predicts estimated insurance charges.
- Uses a trained Scikit-learn pipeline.
- Validates user input using Pydantic.
- Provides predictions through a FastAPI backend.
- Includes a simple Streamlit frontend.

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, FastAPI, Pydantic, Streamlit.

## Input Features
- Age
- Sex
- BMI
- Number of Children
- Smoking Status
- Region

## Installation

git clone https://github.com/rathaurhr365/Insurance_Cost_Prediction.git
cd Insurance_Cost_Prediction

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

## Run the Project

Start the FastAPI backend:

python -m uvicorn main:app --reload


Start the Streamlit frontend in another terminal:

python -m streamlit run frontend/app.py


- Frontend: http://localhost:8501
- API Docs: http://127.0.0.1:8000/docs

## Author
**Harshit Rathaur**

GitHub: [rathaurhr365](https://github.com/rathaurhr365)

*Note: The predicted charges are estimates, not actual insurance quotes.*
