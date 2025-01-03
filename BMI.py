import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in cm."""
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return round(bmi, 2)

# Streamlit app
st.title("BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1, format="%.1f")
height = st.number_input("Enter your height (cm):", min_value=0.0, step=0.1, format="%.1f")

# Calculate BMI
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: **{bmi}**")

        # BMI classification
        if bmi < 18.5:
            st.write("You are classified as: **Underweight**")
        elif 18.5 <= bmi < 24.9:
            st.write("You are classified as: **Normal weight**")
        elif 25 <= bmi < 29.9:
            st.write("You are classified as: **Overweight**")
        else:
            st.write("You are classified as: **Obesity**")
    else:
        st.error("Please enter valid weight and height values.")
