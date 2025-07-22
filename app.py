import streamlit as st
import joblib
import numpy as np

st.title("Employee Salary Prediction")

st.divider()

st.write("with this app, you can get estimations for the salariess of the company employees")

years = st.number_input("What is your total duration of employment with this company",value = 1, step = 1, min_value = 0)
jobrate = st.number_input("Enter the job rate",value=3.5, step = 0.5, min_value = 0.0 )

x = [years, jobrate]

model = joblib.load("linearmodel.pkl")

st.divider()

predict = st.button("press the button for salary prediction")

st.divider()

if predict:
    
    st.balloons()

    X1 = np.array([x])

    prediction = model.predict(X1)

    st.write(f"Salary prediction is <h2> {prediction[0]} </h2>", unsafe_allow_html=True)

else:
    "Please press the button for app to make the prediction"