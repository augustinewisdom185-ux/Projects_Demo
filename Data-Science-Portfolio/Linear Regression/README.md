# 🏥 Healthcare Analytics: Systolic Blood Pressure Predictive Modeling

An end-to-end Machine Learning pipeline using **Linear Regression** to predict a patient's **Systolic Blood Pressure** based on demographic markers, medical conditions, and prescribed medications. The project handles categorical data transformation, safeguards against data leakage, evaluates performance over split sets, and features automated serialization gating based on model metrics.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset Architecture](#-dataset-architecture)
- [Pipeline Workflow](#-pipeline-workflow)
- [Performance Criteria & Serialization](#-performance-criteria--serialization)
- [Installation & Setup](#-installation--setup)
- [How to Run](#-how-to-run)

---

## 🔍 Project Overview
Predicting clinical vitals like Systolic Blood Pressure accurately allows healthcare platforms to proactively flag cardiovascular anomalies. This pipeline acts as a script that:
1. Automatically reads and cleans composite clinical text formatting (`Blood Pressure` string arrays).
2. Transmutes categorical profiles (Gender, Diagnosis, and Treatment plans) into model-ready numerical bitmasks.
3. Trains a **Scikit-Learn Linear Regression model** using a 70/30 stratified training split.
4. Generates data visualization charts mapping performance error patterns.
5. Employs a production quality gate to preserve only top-tier models (`R² > 0.96`) as a deployment-ready `.pkl` binary.

---

## 📊 Dataset Architecture
The workflow accepts an initial file named `Healthcare_cleaned_data.csv`. 

### Key Feature Treatments:
* **The Blood Pressure Field:** Originally stored as a string format (e.g., `140/90`), the script automatically tokenizes this string, creating two explicit numeric vectors: `Systolic` and `Diastolic`.
* **Preventing Data Leakage:** To ensure the model remains generalizable for scenarios where real-time patient metrics are unknown, **`Diastolic` data is dropped from the training features (`X`)**. Leaving it in would give the model a mathematical shortcut, inflating accuracy artificially while rendering the model useless in the field.
* **Categorical Handling:** Variables like `Gender` ("Male"/"Female"), `Condition`, and `Medication` are converted to numeric boolean flags using **One-Hot Encoding** (`pd.get_dummies`). `drop_first=True` is utilized to evade multi-collinearity structural failure (the dummy variable trap).

---

## ⚙️ Pipeline Workflow

1. **Ingestion & Text Slicing:** Extracts structural numbers from combined vital fields and casts text elements into `float` parameters.
2. **Dummification:** Maps multi-class categorical arrays to independent binary dimensions.
3. **Data Preservation:** Automatically exports the intermediate structured dataset to `linear_regression_data.csv`.
4. **Train/Test Segregation:** Isolates 30% of data to function as an independent, unseen test set to validate generalizing behavior.
5. **Loss Tracking:** Simultaneously benchmarks both Training Set loss and Testing Set loss to measure overfitting margins.

---

## 🏆 Performance Criteria & Serialization

The script enforces a rigorous quality gate prior to local file exports:
* **Target Metric:** Testing Set R-squared ($R^2$) Score.
* **Acceptance Condition:** $R^2 > 0.96$ (Model explains more than 96% of unseen data variance).

### Outcome Rules:
* **Pass 👍:** Saves model binary directly to disk as `systolic_bp_regression_model.pkl` utilizing standard Python `pickle` streams.
* **Fail ⚠️:** Script cancels file generation and outputs a log detailing performance shortfalls to prevent faulty asset overwrites.

---

## 💻 Installation & Setup

Ensure you have Python 3.8+ installed along with the required analytical dependencies.

```bash
#Install the necessary processing libraries
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## 🚀 How to Run

1. Place your raw data file inside the root repository directory and name it `Healthcare_cleaned_data.csv`.
2. Execute the processing script via your terminal command structure:

```bash
python Linear_reg.py
```

### Generated Outputs
* **`linear_regression_data.csv`:** The fully numerical, encoded dataset.
* **`systolic_bp_regression_model.pkl`:** The compiled model binary (only generated if $R^2 > 0.96$).
* **Diagnostic Windows:** Side-by-side visualization subplots showing the *Actual vs. Predicted Trendline* and the *Residual Error Dispersion Plot*.
