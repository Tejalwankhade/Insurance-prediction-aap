import streamlit as st
import pandas as pd
import pickle

# Load the saved model
with open("Best_model_insurance.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Medical Insurance Cost Prediction App")

st.write("Enter the details below to predict medical insurance charges.")

# Taking inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=22.5)
smoker = st.selectbox("Smoker?", ("No", "Yes"))

# Convert smoker input to model format
smoker_yes = 1 if smoker == "Yes" else 0

# Prepare input data for model
input_data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'smoker_yes': [smoker_yes]
})

if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Medical Insurance Cost: ₹{prediction:,.2f}")
