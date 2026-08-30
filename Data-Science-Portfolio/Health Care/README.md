# 👨‍⚕️Healthcare Data Cleaning & Imputation Pipeline

An automated, end-to-end Python pipeline engineered to ingest chaotic, structural clinical logs and output clean, filtered datasets optimized for distance-based machine learning classifications (such as K-Nearest Neighbors).

## Production Pipeline Architecture

The pipeline processes messy text-based data frames natively using a modular script execution footprint:

1. **Cell-Level Stripping**: Eradicates inconsistent string whitespaces globally across text records.
2. **Global Typo Mapping**: Normalizes typographical irregularities (e.g., converting structural textual descriptors like `'forty'` to integer `40`).
3. **Binary Demographics Optimization**: Flags text markers like `'Other'` within patient demographics and randomly maps them to binary clinical indicators (`'Male'`, `'Female'`) to maintain downstream classifier consistency.
4. **Proportional Label Balancing**: Safely extracts class distributions across existing labels (`Heart Disease`, `Diabetes`, `Asthma`, `Hypertension`) to proportionally fill categorical strings labeled `'None'`.
5. **Distance Metrics Reconstruction**: Unifies raw strings mapping composite clinical vitals (e.g., `Blood Pressure` formatted as `'120/80'`) so they can be processed and plotted via discrete numerical vectors.

## Installation & Deployment

Ensure your local configuration meets the standard analytics suite thresholds:

```bash
pip install pandas numpy matplotlib seaborn
```

Execute the cleaning pipeline across your raw healthcare asset matrix directly from your terminal interface:

```bash
python health_care.py
```

## Exploratory Data Analysis Output

The execution generates an high-fidelity visual dashboard saved directly as `patient_data_plots.png`, featuring:
- **Age Prototyping Distribution**: Grouped structural boxplots parsing patient age profiles.
- **Cholesterol Density Outlines**: Statistical quartiles mapped using kernel-density violin arrays.
- **Vitals Scatter Boundary Diagrams**: Continuous coordinates visualizing overlapping tracking gaps for Systolic and Diastolic categories simultaneously.
