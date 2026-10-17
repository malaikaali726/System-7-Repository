# Day 6: Pandas Series, DataFrames, filtering, sorting, missing values
import pandas as pd
import numpy as np

# Series
marks = pd.Series([85, 72, 90, 64], index=["Ali", "Sara", "Hassan", "Fatima"])
print("Series:\n", marks)
print("Ali's marks:", marks["Ali"])

# DataFrame
data = {
    "name": ["Ali", "Sara", "Hassan", "Fatima", "Usman"],
    "age": [20, 21, 19, 22, 20],
    "marks": [85, 72, 90, np.nan, 65],
    "city": ["Lahore", "Karachi", "Lahore", "Islamabad", None],
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("\nFirst 3 rows:\n", df.head(3))
print("\nInfo:")
df.info()

# Filtering
print("\nStudents from Lahore:\n", df[df["city"] == "Lahore"])
print("\nMarks above 70:\n", df[df["marks"] > 70])

# Sorting
print("\nSorted by marks (high to low):\n", df.sort_values(by="marks", ascending=False))

# Missing values
print("\nMissing values per column:\n", df.isnull().sum())
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["city"] = df["city"].fillna("Unknown")
print("\nAfter filling missing values:\n", df)

# Adding a new column
df["passed"] = df["marks"] >= 70
print("\nWith new column:\n", df)