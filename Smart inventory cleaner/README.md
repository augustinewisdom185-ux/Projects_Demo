# 📦 Smart Inventory Data Engineering Pipeline

A Python command-line utility built to ingest, clean, and standardize irregular JSON data payloads. This project focuses on data preprocessing and pipeline building, which are fundamental milestones in my learning journey toward becoming an AI developer.

## 🚀 Key Pipeline Features

- **Dynamic State Management:** Maintains a unified data state (`current_inventory`) across multiple terminal processing tasks.
- **Key Normalization:** Safely standardizes erratic properties by transforming inconsistent properties like uppercase `Price` into a unified `price` schema.
- **Data Validation & Transformation:** Loops through dataset elements to detect anomalous negative stock metrics and dynamically resets them to `0`.
- **Cross-Platform Serialization:** Uses `utf-8` text streams paired with `ensure_ascii=False` to preserve emojis and complex symbols securely across Windows, Mac, and Linux.

## 🛠️ Technology Stack

- **Language:** Python 3.x
- **Core Engine Modules:** `json`, `json.JSONDecodeError`

## 📋 Architectural Workflow

1. **Option 1 (Load):** Stream-reads data fragments from `raw_inventory.json` through a file context manager.
2. **Option 2 (Clean):** Traverses the collection schema to fill in empty tags or titles and repair structural casing variations.
3. **Option 3 (Change):** Implements localized logic tests to neutralize data noise, shifting negative numbers to standard baseline floors.
4. **Option 4 (Save):** Commits the memory matrix back into a formatted, human-readable file named `Cleaned Inventory.json`.

## 📈 My Roadmap to AI Development

Data engineers often say that 80% of machine learning is simply collecting and preparing data. By writing defensive, crash-resistant Python code to filter and transform unstructured data feeds, I am mastering the exact ingestion pipelines required to feed data safely into neural networks and machine learning models.

---
⭐ *Feel free to fork this project, star the repo, or drop feedback as I continue mapping out my path to AI systems engineering!*
