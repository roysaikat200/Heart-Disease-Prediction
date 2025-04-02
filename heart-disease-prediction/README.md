# Heart Disease Prediction App

This project is a Streamlit application that predicts the likelihood of heart disease based on user input. The application utilizes a trained machine learning model to provide predictions and insights.

## Project Structure

- `src/app.py`: Main entry point of the Streamlit application.
- `src/models/model.pkl`: Serialized trained machine learning model.
- `src/utils/data_processing.py`: Functions for preprocessing input data.
- `src/utils/prediction.py`: Functions for making predictions using the model.
- `src/data/heart_disease_data.csv`: Dataset used for training the model.

## Requirements

To run this application, you need to install the required Python packages. You can do this by running:

```
pip install -r requirements.txt
```

## Running the Application

To start the Streamlit application, navigate to the `src` directory and run:

```
streamlit run app.py
```

This will open the application in your web browser, where you can input data and receive predictions regarding heart disease.