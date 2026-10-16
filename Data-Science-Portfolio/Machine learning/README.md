# Circle Classification using PyTorch

A deep learning classification model built with PyTorch to separate concentric circles of data using a non-linear neural network. This project demonstrates how to solve a non-linear binary classification problem using multi-layer perceptrons (MLP) equipped with ReLU activation functions and trained via Stochastic Gradient Descent (SGD).

---

## 📊 Dataset Visualization

The dataset consists of two concentric circles generated using Scikit-Learn's `make_circles`. A simple linear model cannot draw a straight decision boundary to separate these classes, making non-linear activation functions necessary.

![Dataset Circles](image_pmw6UZ.png)

---

## 🚀 Results & Decision Boundaries

After training for 20,000 epochs, the network successfully creates a non-linear decision boundary that perfectly isolates the inner circle from the outer ring.

![Decision Boundaries](image_2MM-85.png)

---

## 🧠 Model Architecture

The neural network utilizes three hidden layers with 60 features each, using Rectified Linear Units (ReLU) to handle the geometric complexity of the circular distribution.

* **Input Layer:** 2 features (X₁, X₂)
* **Hidden Layer 1:** 60 neurons + ReLU Activation
* **Hidden Layer 2:** 60 neurons + ReLU Activation
* **Hidden Layer 3:** 60 neurons + ReLU Activation
* **Output Layer:** 1 neuron (Logit for binary classification)

---

## 🛠️ Requirements & Setup

Make sure you have the required Python libraries installed before running the script:

```bash
pip install torch pandas matplotlib scikit-learn
```

> **Note:** This code requires a local helper module named `helper_function.py` containing the `plot_decision_boundary` function to render the classification background shades.

---

## 💻 How to Run

1. Clone this repository to your local machine.
2. Ensure `image_pmw6UZ.png` and `image_2MM-85.png` are saved in the same directory if you want to keep your repository presentation intact.
3. Execute the Python script:

```bash
python Deep_blob.ipynb
```

---

## 📉 Training Configuration

* **Loss Function:** `BCEWithLogitsLoss` (Binary Cross Entropy with built-in Sigmoid)
* **Optimizer:** Stochastic Gradient Descent (SGD)
* **Learning Rate:** 0.01
* **Epochs:** 20,000
