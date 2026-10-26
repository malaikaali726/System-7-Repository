import pandas as pd
import numpy as np

df = pd.read_csv("practice_housing_data.csv")
print("First five rows:\n", df.head())
print("\nShape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())

# Fill numeric missing values with each column's median for this exercise.
prepared = df.copy()
for col in prepared.select_dtypes(include="number").columns:
    prepared[col] = prepared[col].fillna(prepared[col].median())

print("\nMean:\n", prepared.mean(numeric_only=True))
print("\nMedian:\n", prepared.median(numeric_only=True))
print("\nMode (first mode per column):\n", prepared.mode(numeric_only=True).iloc[0])
print("\nVariance:\n", prepared.var(numeric_only=True))
print("\nStandard deviation:\n", prepared.std(numeric_only=True))
prepared.to_csv("prepared_housing_data.csv", index=False)
print("\nSaved prepared_housing_data.csv")
