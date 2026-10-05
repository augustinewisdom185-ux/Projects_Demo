# 🏠 Bangalore Property Price Prediction Pipeline

An end-to-end **Deep Learning Regression Pipeline** built with **PyTorch** and **Scikit-Learn** to predict housing prices in Bangalore. The pipeline ingests preprocessed property attributes, normalizes features/targets, splits data reproducibly, trains a Multi-Layer Perceptron (MLP) neural network, evaluates it using regression metrics (R² score), conditionally saves model checkpoints based on accuracy thresholds, and visualizes predictions.

## 🚀 Key Features

* **Device-Agnostic Setup:** Auto-detects and fully utilizes **NVIDIA CUDA GPUs** for computation, seamlessly falling back to CPU if unavailable.
* **Dual-Axis Scaling:** Standardizes both the high-dimensional feature matrix (X) and the target vector (y) using `StandardScaler` to prevent exploding gradients and guarantee smooth, stable training convergence.
* **Strict Reproducibility:** Enforces global random seeds across PyTorch and data split generators to ensure completely identical data splits and weight initializations across platform runs.
* **Unbiased Baseline Verification:** Captures raw predictions *before training* to visually prove learning progression against ground truth.
* **Conditional Weight Serialization:** Implements a gatekeeper check that only exports and saves the model's learned weights (`.pth` file) if the validation accuracy surpasses a strict target threshold (e.g., R² ≥ 97%).

---

## 🛠️ Requirements & Installation

Make sure you have Python 3.8+ installed. You can install all necessary engineering packages using `pip`:

```bash
pip install torch pandas scikit-learn matplotlib numpy
```

### File Hierarchy Setup
Before running the script, ensure your working directory matches the structure below:

```text
📂 bangalore-house-prediction/
├── 📄 Bungalor_cleaned_data.csv       # Your cleaned dataset
├── 📄 deep_learning.py               # The main script code
└── 📂 models/                         # Created automatically on save
    └── 📄 bangalore_property_model.pth 
```

---

## 📐 Project Pipeline Architecture

```text
  [Bungalor_cleaned_data.csv]
              │
              ▼
    [DataIngestionModel] ──► (StandardScaler applied to X and y)
              │
              ▼
       [random_split]    ──► (70% Train / 30% Test with explicit Generator seed)
              │
      ┌───────┴───────┐
      ▼               ▼
 [train_loader]  [test_loader]
 (batch_size=16) (batch_size=16)
```

1. **Data Ingestion & Transformation:** Drops the target column `price` to build features. Applies standard normal z-score transformations to features and target matrices, converting them into optimized PyTorch `float32` tensors.
2. **Data Streaming:** Packages indices using custom `Dataset` double-underscore methods (`__len__`, `__getitem__`) into a mini-batch size of 16.
3. **Neural Network Architecture:**
   * **Input Layer:** Dynamically scales to match your dataset feature size (e.g., handling one-hot encoded geographic arrays smoothly).
   * **Hidden Layer 1:** Linear (Input → 64 nodes) + non-linear Rectified Linear Unit (`ReLU`) activation function.
   * **Hidden Layer 2:** Linear (64 → 32 nodes) + `ReLU` activation function.
   * **Output Layer:** Linear (32 → 1 node), producing a single continuous price value estimation matrix.
4. **Optimization Loop:** Employs Mean Squared Error Loss (`nn.MSELoss`) paired with an `Adam` optimization optimizer running at a learning rate velocity of `0.005` across `180` training blocks (`epochs`).

---

## 💻 Script Pipeline Workflow

To train, evaluate, and output the tracking analytics visualizer graph, simply open your terminal environment and run:

```bash
python deep_learning.py
```

### Expected Output Console Logs

```text
We are on: cpu
--- Starting Machine Learning Model Training ---
Epoch: 001/180 | Training Mean Squared Error Loss: 0.14582
Epoch: 020/180 | Training Mean Squared Error Loss: 0.04218
Epoch: 040/180 | Training Mean Squared Error Loss: 0.02104
...
Epoch: 180/180 | Training Mean Squared Error Loss: 0.00841

--- Final Model Metrics Summary ---
Final Scaled Test Set MSE Loss: 0.01254
Model Variance Explanation Accuracy (R2 Score): 97.84%

Accuracy Requirement Passed (97.84<img width="1190" height="590" alt="15c83bc7-3bac-4269-95e4-a8f50c3b9da6" src="https://github.com/user-attachments/assets/1e53e9d7-c18b-4ef5-9679-06ebd3b076f3" />
% >= 96.00%)
Saving model weights to: models/bangalore_property_model.pth...
Model saved successfully!
```

---

## 📈 Metric Evaluation & Visual Analytics

Instead of testing accuracy as a raw decimal, the pipeline evaluates performance using the R² Score (Coefficient of Determination) calculated directly on unscaled prices:

\[R^{2}=1-\frac{\sum (y_{true}-y_{pred})^{2}}{\sum (y_{true}-\bar{y}_{true})^{2}}\]

### The Visualization Output Graph
The pipeline utilizes `matplotlib` to render a detailed line graph window showing the first 50 property samples from the test set:
* **Black Line (`-`):** Ground truth property values (`Actual Price`).
* **Red Dashed Line (`--`):** Initial completely random predictions (`Before Training`).
* **Green Dash-Dot Line (`-.`):** The model's final, learned price predictions (`After Training (Optimized)`).

---

## 📥 Loading the Model in External Projects

To use your saved checkpoint weight file (`bangalore_property_model.pth`) inside external files like VS Code, Google Colab, or Kaggle, implement this boilerplate pattern:

```python
import torch
import torch.nn as nn

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
    def forward(self, x): return self.network(x)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = TrainingModel(input_dimension=245).to(device)
model.load_state_dict(torch.load("models/bangalore_property_model.pth", map_location=device))
model.eval()

print("Model successfully restored for downstream inference tasks!")
```
