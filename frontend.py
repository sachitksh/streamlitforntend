import streamlit as st
import requests

def get_user_data():
    # Fetch the data from the API
    response = requests.get("https://sachitflask3.vercel.app/getdata")
    
    # Check if the response is successful
    if response.status_code == 200:
        user_data = response.json()  # Assuming the response is in JSON format
    else:
        user_data = {"error": "Failed to fetch data"}

    return user_data

# Fetch the user data from the API
x = get_user_data()

# Display the user data
if "error" in x:
    st.error(x["error"])  # Display error message if the API request fails
else:
    st.subheader("User Information:")
    st.write(f"Name: {x.get('name', 'N/A')}, Age: {x.get('age', 'N/A')}, City: {x.get('city', 'N/A')}")
