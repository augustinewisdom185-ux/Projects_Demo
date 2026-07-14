# Marketing Campaign Data Cleaning Project 📊🧼

Welcome to my data cleaning repository! This project focuses on the crucial first step of any data science workflow: transforming messy, raw marketing campaign data into a structured, analysis-ready format using **Python** and **Pandas**.

Data cleaning is where the real work happens. Before we can build dashboards or run predictive models, we have to make sure the data is accurate, consistent, and clean.

---

## 🛠️ Key Data Cleaning Steps Implemented

*   **Header Standardization:** Automatically stripped whitespace from column names to prevent indexing errors.
*   **Date Normalization:** Split messy timestamps into clean dates, parsed strings into proper 1D `datetime` objects, and restructured campaign start and end timelines.
*   **Boolean Mapping:** Standardized the `Active` status column (handling variations like `'Y'`, `1`, and `'True'`) into clean `'Yes'` / `'No'` values.
*   **Safety Handling for Numeric Types:** Cleaned up duplicate columns on the fly and handled data-type conversions safely (e.g., forcing invalid text in numeric columns to `NaN`).
*   **Categorical Mapping:** Decoded internal marketing tag abbreviations (`FA`, `IN`, `EM`, `GO`) into human-readable channel names (`Facebook`, `Instagram`, `Email`, `Google Ads`).
*   **Financial Currency Parsing:** Cleaned raw currency formatting by removing negative markers, parentheses, and standardizing the global `$` prefix.
*   **Deduplication:** Dropped duplicate records strictly based on `Campaign_ID` and `Campaign_Name` combinations to preserve dataset integrity.

---

## 🚀 Built With

*   **Python 3.14.5**
*   **Pandas** - For data manipulation and structures
*   **PyCharm / Jupyter Notebooks** - Development environment

---

## 📂 Project Structure

*   `marketing_campaign_data_messy.csv`: The raw, uncleaned input data.
*   `data_cleaning_notebook.ipynb`: The step-by-step Jupyter Notebook containing all the Pandas logic and explanations.
*   `README.md`: Project documentation.

---

## 📈 Next Steps
Now that the dataset is cleanly structured, the next phase of this project will focus on **Exploratory Data Analysis (EDA)** and **Data Visualization** to extract high-level marketing insights!
