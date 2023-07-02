# Laptop Price Predictor

This is a machine learning that predicts the price of a laptop based on various features. The prediction model is trained using the Random Forest algorithm. The application also includes data analysis and feature engineering steps.

## You can check this project at : https://laptop-price-predictor-1gcb.onrender.com/

## Usage

1. Select the laptop brand from the drop-down menu.
2. Choose the laptop type from the available options.
3. Select the RAM size from the drop-down menu.
4. Enter the weight of the laptop in kilograms.
5. Specify if the laptop has a touchscreen feature.
6. Select whether the laptop has an IPS display.
7. Choose the screen resolution from the available options.
8. Enter the screen size in centimeters.
9. Select the processor brand from the drop-down menu.
10. Select the HDD (Hard Disk Drive) size from the drop-down menu.
11. Select the SSD (Solid State Drive) size from the drop-down menu.
12. Choose the GPU (Graphics Processing Unit) brand from the drop-down menu.
13. Select the operating system from the drop-down menu.
14. Click the "Predict Price" button to see the predicted price of the laptop.

## Data Analysis and Feature Engineering

Before training the prediction model, data analysis and feature engineering steps were performed on the dataset. These steps involved exploring the data, handling missing values, encoding categorical variables, and transforming features to make them suitable for the machine learning model.

## Prediction Model

The prediction model is built using the Random Forest algorithm. Random Forest is an ensemble learning method that combines multiple decision trees to make predictions. The model takes the input features provided by the user and predicts the price of the laptop.

## Files

The following files are used in this project:

- `pipe.pkl`: Pickle file containing the trained prediction model.
- `df.pkl`: Pickle file containing the preprocessed dataset.

## How to Run the Project

1. Clone the project repository from GitHub.
2. Make sure you have Python installed on your system.
3. Install the required dependencies by running the command `pip install -r requirements.txt`.
4. Run the Streamlit application by executing the command `streamlit run app.py`.
5. The application will be launched in your browser, and you can interact with it to predict laptop prices.

Feel free to explore and modify the code according to your requirements.
