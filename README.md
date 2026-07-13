# 🏠 House Price Prediction

A Machine Learning project that predicts house prices using Linear Regression. The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and a Streamlit web application for making predictions.

---

## 📌 Project Overview

This project uses the Ames Housing dataset to predict the selling price of houses based on important property features.

The workflow includes:

- Data Cleaning
- Missing Value Handling
- Duplicate Removal
- Exploratory Data Analysis (EDA)
- Feature Selection
- Categorical Feature Encoding
- Train-Test Split
- Linear Regression Model Training
- Model Evaluation
- Model Saving using Joblib
- Streamlit Web Application

---

## 📂 Project Structure

```
House-Price-Prediction/
│
├── data/
│   └── housing.csv
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── main.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

---

## 📊 Dataset

Dataset used:

**Ames Housing Dataset**

Features include:

- Overall Quality
- Ground Living Area
- Garage Capacity
- Garage Area
- Basement Area
- Full Bathrooms
- Year Built
- Lot Area

Target Variable:

- SalePrice

---

## 📈 Model Performance

Model Used:

**Linear Regression**

Performance Metrics:

| Metric | Value |
|---------|---------|
| MAE | 24,617 |
| RMSE | 39,537 |
| R² Score | 0.796 |

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Manohar5555/House-Price-Prediction.git
```

Go to the project folder

```bash
cd House-Price-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💻 Web Application

The Streamlit application allows users to enter house details and receive a predicted house price instantly.

Inputs:

- Overall Quality
- Living Area
- Garage Capacity
- Garage Area
- Basement Area
- Full Bathrooms
- Year Built
- Lot Area

Output:

- Predicted House Price

---

## 📸 Application Preview

![alt text](<Screenshot 2026-07-13 173849.png>) ![alt text](<Screenshot 2026-07-13 173901.png>)

Example:

```
images/png
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Data preprocessing
- Handling missing values
- Feature selection
- One-Hot Encoding
- Linear Regression
- Model evaluation
- Saving ML models using Joblib
- Building ML web apps with Streamlit
- Using Git and GitHub for version control

---

## 👨‍💻 Author

**Manohar**

GitHub: https://github.com/Manohar5555