
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

## 📥 Practice Cleaning This Dataset Yourself!

If you want to practice your own data cleaning skills using this exact messy marketing dataset, you can get it in two easy ways:

### Option 1: Load it directly into Python (No download needed)
Copy and paste this code into your own Jupyter Notebook or Python script to import the messy dataset instantly over the web:

# Direct raw link to the messy dataset
url = "[https://raw.githubusercontent.com/augustinewisdom185-ux/Projects_Demo/refs/heads/main/Data-Science-Portfolio/market_campaign/marketing_campaign_data_messy.csv](https://raw.githubusercontent.com/augustinewisdom185-ux/Projects_Demo/refs/heads/main/Data-Science-Portfolio/market_campaign/marketing_campaign_data_messy.csv)"
file_name = pd.read_csv(url)

# Now you're ready to clean!
print(file_name.head())

### Option 2: Download the CSV file directly
1. Go to the dataset file page on GitHub [here](https://github.com/augustinewisdom185-ux/Projects_Demo/blob/main/Data-Science-Portfolio/market_campaign/marketing_campaign_data_messy.csv).
2. On the top right of the data table, click the **Download raw file** button (it looks like a small down-arrow pointing into a tray, next to the "Raw" button).
3. Save the `marketing_campaign_data_messy.csv` file to your local project folder and start cleaning!
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

*   **Python 3**
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
