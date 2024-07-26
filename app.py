import streamlit as st
import requests
import json
from io import BytesIO

st.title('House Price Prediction')

# Text input for label
label_medInc = st.text_input("income in block group:")
label_HouseAge =  st.text_input("house age in block group:")
label_AveRooms = st.text_input("number of rooms per household:")
label_AveBedrms = st.text_input("number of bedrooms per household:")
label_Population = st.text_input("population:")
label_AveOccup = st.text_input("number of household members:")
label_Latitude = st.text_input("Latitude:")
label_Longitude = st.text_input("Longitude:")

if st.button("Predict"):
    if label_medInc:
        # Send the label to the server
        response = requests.post(
            "https://gruhit-patel-deployment-app.hf.space/predict_house_price",  # Replace with your API endpoint
            json={'medInc': label_medInc,'houseAge': label_HouseAge,'avgRooms': label_AveRooms,'avgBdrms': label_AveBedrms,'population': label_Population,'avgOccup': label_AveOccup,'latitude': label_Latitude,'longitude': label_Longitude}
        )

        if response.status_code == 200:
            # Convert the response content to an text
            label = json.loads(response._content)
            # Display the value
            st.write(f"House Price is {label['price']}")
        else:
            st.write("Error: Unable to get the response from the server.")
    else:
        st.write("Please enter a label.")
