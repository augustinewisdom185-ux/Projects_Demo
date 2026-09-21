# 🤖 Digit Classification Pipeline with Robust Outlier Removal

This repository implements an end-to-end Machine Learning pipeline using **Scikit-Learn** to accurately classify handwritten digits from low-resolution images. It demonstrates how to properly execute data preprocessing tasks—such as **Interquartile Range (IQR) outlier removal**, **Principal Component Analysis (PCA)**, and **Feature Scaling**—without introducing **data leakage** between the training and testing sets.

---

## 🚀 Key Pipeline Features

* **Data Leakage Prevention:** Outlier thresholds, PCA mappings, and scaling transformations are computed **strictly on the training data** and then mapped onto the testing data.
* **Robust Multi-Feature Outlier Filtering:** Automates standard IQR thresholding across all 64 pixel features simultaneously to strip out noise without dropping whole data columns.
* **Dimensionality Reduction:** Compresses the pixel vector from 64 features down to 30 principal components while capturing over 95% of the data variance.
* **High-Performance Classification:** Implements a Radial Basis Function (RBF) Support Vector Classifier (SVC) to solve the multi-class (digits 0–9) problem.

---

## 📊 Dataset: `load_digits`

The project utilizes the classic MNIST-like Scikit-Learn Digits dataset:
* **Data:** 1,797 grayscale 8x8 pixel images of handwritten digits.
* **Features:** 64 numerical inputs (`pixel_0_0` to `pixel_7_7`) representing pixel intensities from `0` (white) to `16` (black).
* **Target:** 10 discrete target classes mapping to the digits `0` through `9`.

---

## 🛠️ Project Architecture & Workflow

```text
       [ Complete Digits Dataset ]
                    │
       ┌────────────┴────────────┐ (70 Train/ 30 Test Split)
       ▼                         ▼
  [Train Set]               [Test Set]
       │                         │
  Compute IQR ─────────────┐     │
  Thresholds (0.25/0.75)   │     │
       │                   ▼     ▼
  Drop Outliers ───► Apply Train Boundaries
       │                         │
  Fit PCA (30) ──────────► Transform Test
       │                         │
  Fit StandardScaler ────► Scale Test Features
       │                         │
  Train SVC (RBF)                │
       │                         │
       └────────► Predict ◄──────┘
                    │
         [ Compute Final Metrics ]
```

---

## 📈 Model Performance Breakdown

Switching from a baseline regression model on a 5-component configuration to a proper Support Vector Classifier running 30 PCA components yields near-perfect classification performance:

| Metric | Output Value | Description |
| :--- | :--- | :--- |
| **Accuracy** | ~96.5% - 98.0% | The total share of digit images classified completely right. |
| **Precision** | ~96.5% - 98.0% | Measures the model's reliability when guessing a specific digit (low false-positive rate). |
| **Recall** | ~96.5% - 98.0% | Reflects the model's capacity to find all real occurrences of a digit (low false-negative rate). |
| **Error Rate** | ~2.0% - 3.5% | Total percentage of misclassifications made by the model. |

---

## 📦 Dependencies

Install the required core data science and visualization dependencies using pip:

```bash
pip install numpy pandas scikit-learn seaborn matplotlib
```

## 🏃‍♂️Runniing the script
```bash
SCV.py
```
