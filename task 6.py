# Task 6: Clean a dataset with missing values and plot before and after
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load raw data
df_raw = pd.read_csv("students_missing.csv")
print("Missing values BEFORE cleaning:\n", df_raw.isnull().sum())

# Clean the data
df = df_raw.copy()
numeric_cols = ["age", "math", "english", "science"]

# Numeric columns: fill with median (median is less affected by outliers)
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Text column: fill with the most common value (mode)
df["city"] = df["city"].fillna(df["city"].mode()[0])

# Make age a whole number
df["age"] = df["age"].astype(int)

print("\nMissing values AFTER cleaning:\n", df.isnull().sum())
print("\nCleaned data:\n", df)

# Save cleaned data
df.to_csv("students_cleaned.csv", index=False)

# Plot 1: Heatmap of missing values before and after
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.heatmap(df_raw.isnull(), cbar=False, cmap="magma", ax=axes[0])
axes[0].set_title("Before Cleaning: Missing Values (yellow = missing)")
sns.heatmap(df.isnull(), cbar=False, cmap="magma", ax=axes[1])
axes[1].set_title("After Cleaning: Missing Values")
plt.tight_layout()
plt.savefig("missing_before_after.png")
plt.show()

# Plot 2: Math marks distribution before and after (boxplot)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(y=df_raw["math"], ax=axes[0], color="salmon")
axes[0].set_title("Math Marks BEFORE Cleaning")
sns.boxplot(y=df["math"], ax=axes[1], color="lightgreen")
axes[1].set_title("Math Marks AFTER Cleaning")
plt.tight_layout()
plt.savefig("math_before_after.png")
plt.show()

print("\nDone. Cleaned file: students_cleaned.csv, charts saved.")