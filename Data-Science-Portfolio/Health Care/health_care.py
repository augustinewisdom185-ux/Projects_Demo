import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def clean_and_subset_data(file_path, output_path='Healthcare_cleaned_data.csv'):

    df = pd.read_csv(file_path, skipinitialspace=True)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# UNIFY NULLS, RECODE AGE, & FILTER GENDER 
    
    # Convert string-based missing flags into genuine missing types (np.nan)
    df = df.replace(['nan', 'NaN', '', ' ', 'Other'], np.nan)
    
    df['Age'] = df['Age'].replace({'forty': 40})
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)

    #  Replace 'Other' in Gender with either 'Male' or 'Female' randomly
    # Identifying where 'Other' is available iin the Age column
    gender_mask = df['Gender'] == 'Other'
    other_count = gender_mask.sum()
    
    if other_count > 0:
        # Generate a random array of 'Male' and 'Female' for those rows
        random_genders = np.random.choice(['Male', 'Female'], size=other_count)
        # Overwrite only the 'Other' rows with the random binary choices
        df.loc[gender_mask, 'Gender'] = random_genders
        
    # Handle any accidental blank rows remaining in Gender
    df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])


    df['Condition'] = df['Condition'].replace({'None': np.nan})
    valid_conditions = df['Condition'].dropna()
    probabilities = valid_conditions.value_counts(normalize=True)
    
    condition_mask = df['Condition'].isna()
    none_count = condition_mask.sum()
    
    if none_count > 0:
        random_choices = np.random.choice(
            probabilities.index, 
            size=none_count, 
            p=probabilities.values
        )
        df.loc[condition_mask, 'Condition'] = random_choices

# REARRANGE MEDICATION COLUMN BASED ON CONDITION RULE

    # Define the first-choice medication based on your instructions
    medication_mapping = {
        'Heart Disease': 'Atorvastatin',
        'Diabetes': 'Metformin',
        'Hypertension': 'Amlodipine',
        'Asthma': 'Albuterol'
    }
    
    # Apply the mapping directly to dynamically rewrite the entire column
    df['Medication'] = df['Condition'].map(medication_mapping)
    
    # Safe fallback if an unexpected condition remains unmapped
    df['Medication'] = df['Medication'].fillna('Unknown')

# RECOVERY OF OTHER FEATURE COLUMNS

    df['Cholesterol'] = pd.to_numeric(df['Cholesterol'], errors='coerce')
    df['Cholesterol'] = df['Cholesterol'].fillna(df['Cholesterol'].median()).astype(int)
    
    df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
    
    df['Blood Pressure'] = df['Blood Pressure'].fillna('120/80')

# FILTER AND EXPORT REQUESTED COLUMNS

    requested_columns = ['Age', 'Gender', 'Condition', 'Medication', 'Blood Pressure', 'Cholesterol']
    final_df = df[requested_columns].copy()
    
    final_df.to_csv(output_path, index=False)
    
    print("Data cleaning completed successfully!")
    print(f"Columns exported to '{output_path}':\n{list(final_df.columns)}")
    print(f"Total Rows: {final_df.shape[0]}")

# DATA VISUALIZATION
    # Temporarily parse Blood Pressure for numerical plotting
    bp_split = final_df['Blood Pressure'].str.split('/', expand=True)
    final_df['Systolic'] = pd.to_numeric(bp_split[0], errors='coerce').fillna(120).astype(int)
    final_df['Diastolic'] = pd.to_numeric(bp_split[1], errors='coerce').fillna(80).astype(int)

    # Set up standard visual styling parameters
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(3, 1, figsize=(10, 16))
    
    # Plot 1: Age vs Condition (Boxplot)
    sns.boxplot(x='Condition', y='Age', data=final_df, ax=axes[0], palette='Set2')
    axes[0].set_title('Age Distribution by Health Condition', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Condition', fontsize=12)
    axes[0].set_ylabel('Age', fontsize=12)

    # Plot 2: Condition vs Cholesterol (Violin plot to show density)
    sns.violinplot(x='Condition', y='Cholesterol', data=final_df, ax=axes[1], palette='Pastel1', inner="quart")
    axes[1].set_title('Cholesterol Level Distribution by Health Condition', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Condition', fontsize=12)
    axes[1].set_ylabel('Cholesterol', fontsize=12)

    # Plot 3: Condition vs Blood Pressure (Scatter plot showing Systolic and Diastolic ranges)
    axes[2].scatter(final_df['Condition'], final_df['Systolic'], color='crimson', label='Systolic (Top Number)', alpha=0.6, s=100, edgecolors='black')
    axes[2].scatter(final_df['Condition'], final_df['Diastolic'], color='royalblue', label='Diastolic (Bottom Number)', alpha=0.6, s=100, edgecolors='black')
    axes[2].set_title('Blood Pressure Ranges by Health Condition', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('Condition', fontsize=12)
    axes[2].set_ylabel('Blood Pressure (mmHg)', fontsize=12)
    axes[2].legend(loc='upper right')

    # Optimize alignment and layout spacing
    plt.tight_layout()
    
    # Save the plot image locally
    plt.savefig('patient_data_plots.png', dpi=300)
    print("Plots and saved as 'patient_data_plots.png'!")
    
    plt.show()

    return final_df

if __name__ == '__main__':
    
    clean_df = clean_and_subset_data('healthcare_messy_data.csv')
