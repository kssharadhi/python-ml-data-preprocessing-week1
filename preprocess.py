import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("student_performance_raw.csv")
print("Shape:", df.shape)
print("Missing values before cleaning:\n", df.isnull().sum())

numeric_cols = ["CGPA", "Attendance_Percent", "Final_Score", "Absences"]
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

categorical_cols = ["Gender", "Department"]
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df = pd.get_dummies(df, columns=categorical_cols, dtype=int)

selected_features = [
    "Age", "CGPA", "Attendance_Percent", "Final_Score", "Absences",
    "Gender_Female", "Gender_Male",
    "Department_CSE", "Department_ECE", "Department_ISE"
]
X = df[selected_features].copy()

scale_cols = ["Age", "CGPA", "Attendance_Percent", "Final_Score", "Absences"]
scaler = MinMaxScaler()
X[scale_cols] = scaler.fit_transform(X[scale_cols])

X.to_csv("student_performance_processed.csv", index=False)
print("Missing values after cleaning:\n", X.isnull().sum())
print(X.head())
