import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("../day-12-regression-sklearn/house_prices_practice.csv")
print("Summary:\n", df.describe())
print("\nCorrelation matrix:\n", df.corr(numeric_only=True))

X = df[["area_sqft", "bedrooms", "age_years", "location_score"]]
y = df["price"]
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)
print(f"Train: {len(X_train)} rows; validation: {len(X_val)} rows; test: {len(X_test)} rows")
