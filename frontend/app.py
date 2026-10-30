
import streamlit as st
import requests

st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="🏥",
    layout="centered"
)

API_URL = "http://127.0.0.1:8000/predict"

st.title("Insurance Cost Prediction")
st.write("Enter your details to estimate insurance charges.")

with st.form("insurance_form"):

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    sex = st.selectbox(
        "Sex",
        ["male", "female"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.1,
        max_value=100.0,
        value=28.5,
        step=0.1
    )

    children = st.selectbox(
        "Number of Children",
        [0, 1, 2, 3, 4, 5]
    )

    smoker = st.selectbox(
        "Smoker",
        ["no", "yes"]
    )

    region = st.selectbox(
        "Region",
        [
            "southwest",
            "southeast",
            "northwest",
            "northeast"
        ]
    )

    submitted = st.form_submit_button(
        "Predict Insurance Cost"
    )

if submitted:

    input_data = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }

    try:
        response = requests.post(
            API_URL,
            json=input_data,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()

            st.success("Prediction Successful!")

            st.metric(
                "Estimated Insurance Charges",
                f"${result['predicted_insurance_charges']:,.2f}"
            )

        else:
            st.error(f"API Error: {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Unable to connect to FastAPI: {e}")
