# Student Performance Data Preprocessing

Week 1 task: **Python for Machine Learning & Data Preprocessing**.

## What this project demonstrates

- Loading a CSV dataset with Pandas
- Inspecting dataset shape and missing values
- Handling missing numerical values with median imputation
- Handling categorical values with mode imputation
- One-hot encoding categorical variables
- Feature selection
- Min-Max normalization
- Saving the processed dataset

## Run

```bash
pip install -r requirements.txt
python preprocess.py
```

## Files

- `student_performance_raw.csv` — raw sample data
- `student_performance_processed.csv` — cleaned and transformed data
- `preprocess.py` — complete preprocessing code
- `requirements.txt` — Python dependencies
- `Week1_Python_ML_Data_Preprocessing_Report.docx` — submission report

## Workflow

1. Load the raw CSV dataset.
2. Inspect the shape and missing values.
3. Fill missing numerical values using the column median.
4. Fill missing categorical values using the column mode.
5. Convert categorical values to numerical features using one-hot encoding.
6. Select relevant features and exclude the student identifier.
7. Normalize numerical features to a 0–1 range with Min-Max scaling.
8. Save the final processed dataset as a new CSV file.

## Purpose

The project provides a small, reproducible software implementation of common data preprocessing steps required before exploratory analysis or machine learning model development.
