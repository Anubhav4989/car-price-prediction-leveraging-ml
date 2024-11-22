import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

# Load the pre-trained model
model = pk.load(open('CPP_leveraging_ML.pkl', 'rb'))

# Set up the title and header
st.title('Car Price Prediction Leveraging Machine Learning')
st.header('Enter the details below to predict the car price:')

# Collect user inputs
present_price = st.number_input("Present Price of the Car (in lakhs)", min_value=0.0)
kms_driven = st.number_input("Kms Driven", min_value=0.0)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", [0, 1, 2, 3, 4])  # 0 = First Owner, 1 = Second Owner, etc.
age = st.number_input("Age of the Car (Years)", min_value=0)

# Map categorical variables to numerical values
fuel_type_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_type_map = {"Dealer": 0, "Individual": 1}
transmission_map = {"Manual": 0, "Automatic": 1}

# Convert categorical inputs to numbers
fuel_type_value = fuel_type_map[fuel_type]
seller_type_value = seller_type_map[seller_type]
transmission_value = transmission_map[transmission]

# Prepare the input data for the model
input_data = pd.DataFrame({
    'Present_Price': [present_price],
    'Kms_Driven': [kms_driven],
    'Fuel_Type': [fuel_type_value],
    'Seller_Type': [seller_type_value],
    'Transmission': [transmission_value],
    'Owner': [owner],
    'Age': [age]
})

# Predict the car price
if st.button('Predict'):
    predicted_price = model.predict(input_data)
    st.subheader(f"Predicted Car Price: ₹{predicted_price[0]:.2f} lakhs")