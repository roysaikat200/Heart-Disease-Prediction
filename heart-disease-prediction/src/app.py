import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model
def load_model():
    with open('models/model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.title('Heart Disease Prediction App')
    
    # Create input fields
    age = st.number_input('Age', min_value=20, max_value=100, value=40)
    sex = st.selectbox('Sex', ['Male', 'Female'])
    cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    trestbps = st.number_input('Resting Blood Pressure', min_value=90, max_value=200, value=120)
    chol = st.number_input('Cholesterol', min_value=100, max_value=600, value=200)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    restecg = st.selectbox('Resting ECG Results', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
    thalach = st.number_input('Maximum Heart Rate', min_value=60, max_value=220, value=150)
    exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
    oldpeak = st.number_input('ST Depression', min_value=0.0, max_value=6.0, value=0.0)
    slope = st.selectbox('Slope of Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
    ca = st.number_input('Number of Major Vessels', min_value=0, max_value=4, value=0)
    thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])
    
    if st.button('Predict'):
        # Convert categorical inputs
        sex = 1 if sex == 'Male' else 0
        fbs = 1 if fbs == 'Yes' else 0
        exang = 1 if exang == 'Yes' else 0
        
        cp_dict = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
        cp = cp_dict[cp]
        
        restecg_dict = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2}
        restecg = restecg_dict[restecg]
        
        slope_dict = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
        slope = slope_dict[slope]
        
        thal_dict = {'Normal': 1, 'Fixed Defect': 2, 'Reversible Defect': 3}
        thal = thal_dict[thal]
        
        # Make prediction
        model = load_model()
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, 
                            exang, oldpeak, slope, ca, thal]])
        prediction = model.predict(features)
        
        # Display result
        if prediction[0] == 1:
            st.error('High probability of heart disease.')
        else:
            st.success('Low probability of heart disease.')

if __name__ == '__main__':
    main()