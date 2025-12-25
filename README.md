# 🦟 Malaria Case Prediction in Kenya Counties

## 🎯 Problem Definition: Why This Project Exists

Malaria transmission in Kenya is highly seasonal, geographically uneven, and climate-driven. Counties experience spikes at different times of the year depending on rainfall, temperature, and historical transmission patterns.

## 📌 Project Overview

**Malaria Case Prediction in Kenya Counties** is a data-driven machine learning project that predicts monthly malaria case counts for each county in Kenya using historical case data and climatic features such as temperature and rainfall.

This project demonstrates:
- Data acquisition, cleaning, and preprocessing  
- Feature engineering for time series and climate data  
- Model training and evaluation

👉 The goal of the project is to aid in prior planning by the stakeholders (MoH: Malaria Response Team). Through case prediction, the stakeholders are aware of areas that could have potential spikes in cases in a give time of the year and hence help in resource allocation to aid prevention.
---

## 📊 Motivation

Malaria remains a major public health challenge in Kenya. Accurate short-term predictions can help:
- Health authorities allocate resources more effectively  
- Counties prepare for expected case surges  
- Non-governmental partners plan targeted interventions

This project focuses on predictive modeling using real case counts and weather data to provide actionable forecasting insights.

---

## 🧠 What This Project Does (At a High Level)

This project builds a county-level, monthly malaria case prediction system using machine learning.

Specifically, it:

 1. Learns patterns from past malaria case counts

 2. Incorporates climatic drivers (rainfall and temperature)

 3. Produces forward-looking predictions for each county

It is a decision-support system.

### 🗂️ Project Structure
C:.
│   .gitignore
│   requirements.txt
│   
├───config
│       config.yaml
│       
├───data
│       malaria_raw.csv
│       nyandarua.csv
│       process_malaria.csv
│       siaya.csv
│
├───models
│       model.pk1
│
├───notebooks
│       charts.ipynb
│       malaria.ipynb
│
├───reports
│       evaluation_report.md
│
├───src
│   │   config.py
│   │   data_cleaning.py
│   │   data_loader.py
│   │   data_split.py
│   │   model_training.py
│   │   pipeline.py
│   │__ __init__.py
│  
│
└───tests
        test_config.py
        test_data_clean.py
        test_data_split.py
        test_load_data.py
        test_model_training.py
        __init__.py

---


## 🧰 Dataset

### 📥 Source
- Historical Malaria Cases obtained from the KNH, Malaria Annex in Upper Hill, Nairobi, Kenya.
- Climate data (Temperature, Rainfall). Obtained from the Accuweather API : https://www.accuweather.com/

##🔍 Data Inputs: What the Model Actually Uses

The model works on county-month observations, where each row represents:

 1. County:	Malaria risk varies drastically by geography
 2. Month:	Captures seasonality (rain cycles, breeding patterns)
 3. Historical case counts:	Strong predictor of future outbreaks. This is our target for our model
 4. Rainfall:	Creates mosquito breeding conditions
 5. Temperature:	Affects mosquito survival and parasite development

## ⚙️ Feature Engineering: Turning Raw Data into Signal

This project engineers features that reflect real malaria dynamics and aid in the model development.

Examples:
Encoded months
→Identify the months in numerical format for training

County identifiers
→Encode the county using code to allow the model to learn region-specific risk profiles.


## 🧪 Modeling Approach: Why Machine Learning
Baseline problem

Traditional forecasting methods assume linear, stable relationships.
Malaria transmission is non-linear and context-dependent.

Solution

The project uses tree-based machine learning models (Random Forest) because they:
Capture non-linear interactions (rainfall × temperature × geographical location)
Provide feature importance for interpretability

The model is trained on:
2022–2023 recorded cases data

Tested on:
2024 recorded cases data

## 📏 Evaluation: How We Know the Model Works

Predictions are evaluated using regression metrics because the model is predicting cases which is a continuous values.

### Primary metrics:
MAE (Mean Absolute Error) – average prediction error
MSE (Mean Squared Error) - average squared difference between predicted values and actual values
RMSE (Root Mean Squared Error) – penalizes large misses

Why this matters:

A model that is “accurate” but off by thousands of cases is useless for planning.

Evaluation is done:
Across all counties
Across multiple months

📈 As a result:

This project enables proactive decision-making, such as:

 1. For County Health Offices
 2. Identify high-risk months in advance
 3. Pre-position supplies before outbreaks peak
 4. Compare risk profiles across counties
 5. Allocate limited resources where impact is highest

### The output is not “a number” — it’s early warning intelligence.

## ⚠️ Limitations

This project explicitly acknowledges limitations:

Climate data is aggregated — micro-climates are not capture
Socio-economic factors (housing, bed net usage) are not included
Predictions are probabilistic, not guarantees

## 🚀 Installation

### 🔧 Requirements  
Make sure Python (3.8+) is installed.

```bash
# Clone repository
git clone https://github.com/WElvis87/Malaria-Case-Prediction-in-Kenya-Counties.git
cd Malaria-Case-Prediction-in-Kenya-Counties

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux & macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run Pipeline
cd src
python pipeline.py
