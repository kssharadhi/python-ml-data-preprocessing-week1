# Week 1 Task Report
## Python for Machine Learning & Data Preprocessing
### Project: Student Performance Data Preprocessing

### Introduction
This report presents a practical implementation of Python-based data preprocessing using a sample Student Performance dataset. The task focuses on preparing raw data for future exploratory analysis and machine learning.

### Objectives
The objectives are to understand Python for machine learning data preparation, load and inspect a dataset, handle missing values, encode categorical variables, select relevant features, normalize numerical data, and document the preprocessing workflow.

### Dataset
The sample contains 20 student records with Student ID, Age, Gender, Department, CGPA, Attendance Percentage, Final Score, and Absences. Several numerical values are intentionally missing so that missing-value handling can be demonstrated. Gender and Department are categorical variables.

### Methodology
The CSV file is loaded with Pandas. Missing numerical values are replaced with their column median, while missing categorical values are replaced with the mode. Gender and Department are converted to numerical indicator columns using one-hot encoding. Student_ID is excluded from the learning features because it is an identifier. Age, CGPA, Attendance Percentage, Final Score, and Absences are normalized to the 0-to-1 range using Min-Max scaling. The processed data is saved as `student_performance_processed.csv`.

### Results
After preprocessing, the numerical missing values are filled, categorical data is machine-readable, and numerical features are on a common scale. The processed dataset is therefore suitable for further exploratory data analysis or use as input to a machine learning model.

### Tools
Python, Pandas, Scikit-learn, CSV, VS Code or Jupyter Notebook, and GitHub.

### Conclusion
This task provided practical experience with core data preprocessing techniques and produced a reproducible software project. The workflow can later be extended with outlier detection, correlation analysis, train-test splitting, and machine learning model training.

### Submission Note
The internship portal requires a Word document report. The exact DOCX report is supplied separately for portal upload. This Markdown copy is included in the GitHub repository so the report content is also version-controlled with the project.
