
# 🏠 House Price Prediction Project

## 📌 Overview

This project is an end-to-end **Machine Learning system** for predicting house prices based on multiple features such as location, area, number of rooms, and more.

It includes:

* Data Cleaning & Preprocessing
* Feature Engineering
* Model Training & Evaluation
* Hyperparameter Tuning
* Interactive Web App (Streamlit)
* EDA Dashboard

---

## 🚀 Features

- ✅ Predict house prices instantly  
- ✅ Interactive UI built with Streamlit  
- ✅ Multiple ML models comparison  
- ✅ XGBoost best-performing model  
- ✅ Outlier handling (IQR + Skewness logic)  
- ✅ Feature engineering (Views, Encoding, etc.)  
- ✅ EDA Dashboard with Plotly  
- ✅ Clean UI with custom styling  

---

## 📊 Dataset

* **Source:** [Kaggle - House Price Dataset](https://www.kaggle.com/datasets/juhibhojani/house-price) (Download the raw dataset from this link).
* Country: 🇮🇳 India
* Contains features like:

  * Location
  * BHK
  * Bathroom
  * Balcony
  * Super Area
  * Furnishing
  * Ownership
  * Facing
  * Floors
  * Views

---

## 🧠 Machine Learning Workflow

### 1. Data Cleaning

* Removed missing values
* Standardized column names

### 2. Outlier Handling

* Used **skewness-based logic**

  * Normal distribution → Mean ± 2*Std
  * Skewed → IQR method

### 3. Feature Engineering

* View encoding (Garden, Road, Pool)
* Location grouping
* Scaling numerical features

### 4. Models Tested

* Linear Regression
* Decision Tree
* Random Forest
* KNN
* XGBoost (Best)

---

## 🏆 Best Model

**XGBoost Regressor**

* Test R² ≈ 0.85
* Optimized using GridSearchCV
* Improved further using outlier capping

---

## 💻 Web Application

Built using **Streamlit**

### Features:

* Clean UI design
* Multi-select views
* Input validation
* Real-time prediction
* Styled components

---

## 📊 EDA Dashboard

Interactive dashboard using **Plotly**

Includes:

* Univariate analysis
* Bivariate relationships
* Multivariate insights
* Correlation matrix
* Location-based analysis

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* XGBoost
* Plotly
* Streamlit
* Joblib

---

## 📂 Project Structure

```
House_Price_Prediction/
│
├── dataset/
│   └── clean_house_prices_df.csv
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
│   └── EDA & Training
│
├── Deployment/
│   ├── Home_Page.py
│   └── pages/
│       └── prediction.py
│       └── Dashboard.py 
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

```bash
# Clone repo
git clone <your-repo-link>

# Go to project
cd House_Price_Prediction

# Install requirements
pip install -r requirements.txt

# Run app
streamlit run Home_Page.py
```

---


## ⭐ Future Improvements

* Add model explainability (SHAP)
* Deploy on cloud (Streamlit / Render)
* Add map visualization
* Improve accuracy with advanced feature engineering

---

## ❤️ Final Note

This project demonstrates a complete ML pipeline from data to deployment with a clean UI and strong model performance.

