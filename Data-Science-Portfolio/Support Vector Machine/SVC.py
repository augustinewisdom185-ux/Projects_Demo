import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC 

# Loading the digits dataset
digits = load_digits()

df_digits = pd.DataFrame(digits.data, columns=digits.feature_names)
df_long = df_digits.melt(var_name="Pixel", value_name="Intensity")

# Ploting columns side-by-side
plt.figure(figsize=(18, 6))
sns.boxplot(x="Pixel", y="Intensity", data=df_long)
plt.xticks(rotation=90, fontsize=8)  # Rotate labels to make them readable
plt.title("Intensity Distribution Across All Pixel Columns")
plt.tight_layout()
plt.show()

X = pd.DataFrame(digits.data, columns=digits.feature_names)
y = pd.Series(digits.target)

# Train/Test Split train(70) /test (30)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Calculating the  IQR thresholds strictly on training data
Q1 = X_train.quantile(0.25)
Q3 = X_train.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Removing outliers from Train
train_inlier_mask = (X_train >= lower_bound) & (X_train <= upper_bound)
train_clean_rows = train_inlier_mask.all(axis=1)
X_train_clean = X_train[train_clean_rows]
y_train_clean = y_train[train_clean_rows]

# Removing outliers from Test using Train boundaries
test_inlier_mask = (X_test >= lower_bound) & (X_test <= upper_bound)
test_clean_rows = test_inlier_mask.all(axis=1)
X_test_clean = X_test[test_clean_rows]
y_test_clean = y_test[test_clean_rows]

# PCA Dimensionality Reduction
pca = PCA(n_components=30, random_state=42)
x_train_reduced = pca.fit_transform(X_train_clean)
x_test_reduced = pca.transform(X_test_clean)

# Scaling features 
scaler_x = StandardScaler()
x_train_scale = scaler_x.fit_transform(x_train_reduced)
x_test_scale = scaler_x.transform(x_test_reduced)

# Training the Classifier
model = SVC(kernel="rbf", C=1.0, random_state=42)
model.fit(x_train_scale, y_train_clean)

# Predictions
y_pred = model.predict(x_test_scale)
y_true = y_test_clean.values

# Calculated Metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average="macro")
recall = recall_score(y_true, y_pred, average="macro")

print(f"New Classification Accuracy:  {accuracy * 100:.2f}%")
print(f"New Classification Precision: {precision * 100:.2f}%")
print(f"New Classification Recall:    {recall * 100:.2f}%")
print(f"Error Rate:                   {(1 - accuracy) * 100:.2f}%")
