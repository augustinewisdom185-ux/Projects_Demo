# Modular Email Processor 🛠️🤖

A modular Python program demonstrating the clean separation of concerns by combining four core functional design patterns: *Action*, *Orchestration*, *Validation*, and *Transformation* functions. 

This project serves as a foundational architecture showcase for processing, verifying, and logging data components cleanly.

---

## Architectural Breakdown

The program splits logic into four distinct functional layers to maintain clean, scalable code:

* **Orchestrator Function (`processed_email`):** Manages the operational workflow, calling validation, transformation, and action functions in the correct sequence.
* **Validation Function (`check_email`):** Evaluates input data integrity, ensuring incoming strings meet standard email formatting rules before processing.
* **Transformation Function (`clean_split`):** Standardizes data inputs (lowercasing, stripping whitespace) and parses the string into structural components (Username and Domain).
* **Action Function (`write_log`):** Handles side effects outside the local state—specifically, writing session logs directly to a `Sample.log` file in the user's local Documents directory.

---

## 🛠️ Tech Stack & Concepts
* **Language:** Python 3.14.5
* **Core Libraries:** `os` (File-path normalization across systems)
* **Concepts applied:** Input validation, Data parsing, System logging, Functional decoupling.

---

## 🚀 How It Works

1. Run the script in your terminal:
   ```bash
   python main.py
2. Writes to the file **True** if the email passes all test and writes the wrong email as the email e.g **wisdomaugustine** to the file
