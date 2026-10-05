import os
import torch
import torch.nn as nn  
import pandas as pd
import torch.optim as optim
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, Dataset, random_split
import matplotlib.pyplot as plt
import numpy as np

# 1. Hardware device acceleration verification
device = ("cuda" if torch.cuda.is_available() else "cpu")
print(f"We are on: {device}")

# Define directories and naming systems for saving weights safely
MODEL_SAVE_DIR = "models"
MODEL_NAME = "bangalore_property_model.pth"

os.makedirs(MODEL_SAVE_DIR, exist_ok=True)
MODEL_SAVE_PATH = os.path.join(MODEL_SAVE_DIR, MODEL_NAME)

# Enforce a global system random seed
torch.manual_seed(42)

class DataIngestionModel(Dataset):
    def __init__(self, csv_file, target_column):
        df = pd.read_csv(csv_file)
        
        X_raw = df.drop(columns=[target_column]).values
        y_raw = df[target_column].values

        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X_raw)

        self.scales = StandardScaler()
        y_scaled = self.scales.fit_transform(y_raw.reshape(-1, 1))

        self.X = torch.tensor(X_scaled, dtype=torch.float32)
        self.y = torch.tensor(y_scaled, dtype=torch.float32) 

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X[index], self.y[index]
    
full_dataset = DataIngestionModel(csv_file="Bungalor_cleaned_data.csv", target_column='price')

# Splitting rows (70% Train, 30% Test)
train_split = int(0.7 * len(full_dataset))
test_split = (len(full_dataset) - train_split)

split_generator = torch.Generator().manual_seed(42)

train_data, test_data = random_split(
    dataset=full_dataset,
    lengths=[train_split, test_split],  
    generator=split_generator
)

train_loader = DataLoader(dataset=train_data, batch_size=16, shuffle=True)
test_loader = DataLoader(dataset=test_data, batch_size=16, shuffle=False)

input_features_dimension = full_dataset.X.shape[1]

class TrainingModel(nn.Module):
    def __init__(self, input_dimension):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(in_features=input_dimension, out_features=64),
            nn.ReLU(),
            nn.Linear(in_features=64, out_features=32),
            nn.ReLU(),
            nn.Linear(in_features=32, out_features=1)
        )

    def forward(self, x):
        return self.network(x)

Model = TrainingModel(input_dimension=input_features_dimension).to(device)

Model.eval()
untrained_predictions = []
actual_prices = []

with torch.inference_mode():
    for X_batch, y_batch in test_loader:
        X_batch = X_batch.to(device)
        preds = Model(X_batch)
        untrained_predictions.append(preds.cpu())
        actual_prices.append(y_batch.cpu())

untrained_predictions = torch.cat(untrained_predictions, dim=0).numpy()
actual_prices = torch.cat(actual_prices, dim=0).numpy()

untrained_prices_unscaled = full_dataset.scales.inverse_transform(untrained_predictions)
actual_prices_unscaled = full_dataset.scales.inverse_transform(actual_prices)

loss_function = nn.MSELoss()
optimizer = optim.Adam(Model.parameters(), lr=0.005)

epochs = 180

print("\n--- starting machine learning model training ---".title())

for epoch in range(epochs):
    Model.train()
    train_loss = 0.0

    for X_batch, y_batch in train_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)

        y_pred = Model(X_batch)
        loss = loss_function(y_pred, y_batch)
        train_loss += loss.item() * X_batch.size(0)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    epoch_loss = train_loss / len(train_loader.dataset)
    if (epoch + 1) % 20 == 0 or epoch == 0:
        print(f"Epoch: {epoch+1:03d}/{epochs} | Training Mean Squared Error Loss: {epoch_loss:.5f}")

Model.eval()
total_test_loss = 0.0
trained_predictions = []

with torch.inference_mode():
    for X_batch, y_batch in test_loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)

        test_preds = Model(X_batch)
        trained_predictions.append(test_preds.cpu())

        batch_loss = loss_function(test_preds, y_batch)
        total_test_loss += batch_loss.item() * X_batch.size(0)

final_test_mse = total_test_loss / len(test_loader.dataset)
print("\n--- Final Model Metrics Summary ---")
print(f"Final Scaled Test Set MSE Loss: {final_test_mse:.5f}")

# Unpack and define final predictions array
trained_predictions = torch.cat(trained_predictions, dim=0).numpy()
trained_prices_unscaled = full_dataset.scales.inverse_transform(trained_predictions)

# Calculate R-Squared Accuracy Metric manually
y_test_true = actual_prices_unscaled
y_test_pred = trained_prices_unscaled

residual_sum_of_squares = np.sum((y_test_true - y_test_pred) ** 2)
total_sum_of_squares = np.sum((y_test_true - np.mean(y_test_true)) ** 2)
r2_accuracy = 1 - (residual_sum_of_squares / total_sum_of_squares)

print(f"Model Variance Explanation Accuracy (R2 Score): {r2_accuracy * 100:.2f}%")

if r2_accuracy >= 0.50:
    print(f"\nAccuracy Requirement Passed ({r2_accuracy*100:.2f}% >= 50.00%)")
    print(f"Saving model weights to: {MODEL_SAVE_PATH}...")
    torch.save(obj=Model.state_dict(), f=MODEL_SAVE_PATH)
    print("Model saved successfully!")
else:
    print(f"\n[SKIP SAVE] Accuracy did not clear criteria threshold: {r2_accuracy*100:.2f}% < 50.00%")

slice_size = 50 

plt.figure(figsize=(12, 6))

plt.plot(actual_prices_unscaled[:slice_size], label='Actual Price', color='black', linewidth=2, linestyle='-')
plt.plot(untrained_prices_unscaled[:slice_size], label='Before Training', color='red', alpha=0.6, linestyle='--')
plt.plot(trained_prices_unscaled[:slice_size], label='After Training (Optimized)', color='green', alpha=0.8, linestyle='-.')

plt.title('Bangalore Property Price Predictions: Before vs. After Training', fontsize=14, fontweight='bold')
plt.xlabel('Sample Index (Test Properties)', fontsize=12)
plt.ylabel('Property Price (Original Scale)', fontsize=12)

plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', fontsize=11, shadow=True)
plt.tight_layout()
plt.show()
