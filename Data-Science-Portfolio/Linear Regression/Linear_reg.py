import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle 

# 1. Load the raw data from your CSV file
datas = pd.read_csv("Healthcare_cleaned_data.csv", encoding='utf-8', thousands=',')

#Splitting Blood Pressure column into systolic and diastolic
datas[["Systolic", "Diastolic"]] = datas["Blood Pressure"].str.split('/', expand=True)

#Converting newly split data into float
datas["Systolic"] = datas["Systolic"].astype(float)
datas["Diastolic"] = datas["Diastolic"].astype(float)

datas = datas.drop("Blood Pressure", axis=1)

#Convert all texts in Gender, Condition, Medication into either 0 or 1
datas_clean = pd.get_dummies(datas, columns=["Gender", "Condition", "Medication"], drop_first=True)

datas_clean.to_csv("linear_regression_data.csv", index=False)
print("The dataset has been cleaned, converted to values, and saved successfully!")

#Isolate independent features (X) and the dependent target label (y)
X = datas_clean.drop(["Systolic", "Diastolic"], axis=1)
y = datas_clean["Systolic"]

#Split dataset into 70% training and 30% testing in test_size
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()

#Train the model using the training inputs and expected training targets
model.fit(X_train, y_train)

#Generate predictions for BOTH training and testing data to monitor performance
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

#Calculate performance metrics for the training set (How well it learns)
train_mse = mean_squared_error(y_train, train_predictions)
train_r2 = r2_score(y_train, train_predictions)

#Calculate performance metrics for the testing set (How well it generalises)
test_mse = mean_squared_error(y_test, test_predictions)
test_r2 = r2_score(y_test, test_predictions)

#performance results 
print(f"TRAINING SET:  MSE = {train_mse:.2f}  |  R-squared (R²) = {train_r2:.4f}")
print(f"TESTING SET:   MSE = {test_mse:.2f}  |  R-squared (R²) = {test_r2:.4f}")

#Check accuracy threshold (>0.96) and save using Pickle
accuracy_threshold = 0.96

if test_r2 > accuracy_threshold:
    # Open a file write in 'wb' (write binary) mode
    with open('systolic_bp_regression_model.pkl', 'wb') as file:
        pickle.dump(model, file)
    print(f"\n🎉 Success! Testing R² ({test_r2:.4f}) exceeded threshold ({accuracy_threshold}).")
    print("Model has been saved successfully using Pickle as 'systolic_bp_regression_model.pkl'!")
else:
    print(f"\n⚠️ Model NOT saved. The Testing R² score ({test_r2:.4f}) did not meet the required >{accuracy_threshold} threshold.")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

sns.scatterplot(x=y_test, y=test_predictions, alpha=0.6, color="teal", ax=ax1)
ideal_line = [y_test.min(), y_test.max()]
ax1.plot(ideal_line, ideal_line, color="red", linestyle="--", linewidth=2, label="Perfect Predictions")
ax1.set_title("Actual vs. Predicted Systolic BP (Test Set)")
ax1.set_xlabel("Actual Values")
ax1.set_ylabel("Predicted Values")
ax1.legend()
ax1.grid(True, alpha=0.3)

residuals = y_test - test_predictions
sns.scatterplot(x=test_predictions, y=residuals, alpha=0.6, color="purple", ax=ax2)
ax2.axhline(y=0, color="black", linestyle="--", linewidth=2)
ax2.set_title("Residual Plot (Model Errors)")
ax2.set_xlabel("Predicted Values")
ax2.set_ylabel("Residuals (Actual - Predicted)")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
