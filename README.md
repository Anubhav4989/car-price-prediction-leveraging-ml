# Car Price Prediction Leveraging Machine Learning

## Overview
This project uses machine learning to predict car prices based on various features such as the car's present price, kilometers driven, fuel type, seller type, transmission type, and age. A Random Forest model was trained using historical car data, and this model is deployed via a web application using Streamlit.

## Dataset
The dataset used in this project is sourced from [Kaggle - Vehicle Dataset from Cardekho](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho?select=car+data.csv).

It contains details of cars, including:
- Car's Present Price
- Kms Driven
- Fuel Type (Petrol, Diesel, CNG)
- Seller Type (Dealer, Individual)
- Transmission (Manual, Automatic)
- Owner
- Age of the Car
- Selling Price (target variable)

## Project Files

1. **`car data.csv`**: The raw data used for model training.
2. **`DSP08.ipynb`**: Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.
3. **`app.py`**: Streamlit application file for deploying the model as a web app.
4. **`CPP_leveraging_ML.pkl`**: Pickled Random Forest model, which is used for making predictions in the deployed web app.

## How to Run the Project

### Step 1: Clone the Repository
You can clone the repository to your local machine by running the following command in your terminal:

```bash
git clone https://github.com/Anubhav4989/car-price-prediction-leveraging-ml.git
```

### Step 2: Install Dependencies
Make sure to install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can manually install the necessary libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost streamlit
```

### Step 3: Run the Streamlit App
To run the web application, navigate to the directory where `app.py` is located and run:

```bash
streamlit run app.py
```

This will start the web application and open it in your browser.

### Step 4: Make Predictions
Once the app is running, you can enter the car details such as present price, kilometers driven, fuel type, seller type, transmission, owner, and age of the car. The app will use the trained model to predict the car's selling price.

## Model Training

In the Jupyter notebook (`DSP08.ipynb`), the following steps are performed:

1. **Data Preprocessing**:
   - Load the dataset.
   - Handle missing values and outliers.
   - Encode categorical variables (fuel type, seller type, transmission).
   - Drop unnecessary columns (e.g., "Car_Name" and "Year").

2. **Model Selection**:
   - Train multiple models: Linear Regression (LR), Random Forest (RF), Gradient Boosting (GB), and XGBoost (XG).
   - Evaluate models using the R² score.
   - Select the best-performing model (Random Forest) for saving and deployment.

3. **Model Saving**:
   - The final Random Forest model is saved using `joblib` as `CPP_leveraging_ML.pkl`.

## Model Deployment

- The trained model (`CPP_leveraging_ML.pkl`) is loaded in the `app.py` file.
- The user inputs are processed, and the corresponding car price prediction is shown.

## Example Prediction

You can input the following values to predict the car's price:
- **Present Price**: 11.0 (in lakhs)
- **Kms Driven**: 87934
- **Fuel Type**: Petrol
- **Seller Type**: Dealer
- **Transmission**: Manual
- **Owner**: 0 (First Owner)
- **Age**: 8 years

Click on the "Predict" button, and the predicted car price will be displayed.

## Evaluation Results

The following models were evaluated with the respective R² scores:
- **Linear Regression**: R² Score: 0.886571
- **Random Forest**: R² Score: 0.962735 (Best performing model)
- **Gradient Boosting**: R² Score: 0.961776
- **XGBoost**: R² Score: 0.957629

Random Forest provided the best results and was chosen for final deployment.

## Contributing
Feel free to fork this repository, open issues, or submit pull requests with improvements.

## License
This project is open-source, and you can freely use it for educational and research purposes.

**Author**: Anubhav Kumar Tiwary
