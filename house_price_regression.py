import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = pd.read_csv("house_prices_practice.csv")
features = ["area_sqft", "bedrooms", "age_years", "location_score"]
X, y = df[features], df["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Intercept:", round(model.intercept_, 2))
print("Coefficients:")
for name, value in zip(features, model.coef_):
    print(f"  {name}: {value:.2f}")
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, predictions)), 2))
print("R²:", round(r2_score(y_test, predictions), 3))

example = pd.DataFrame([{"area_sqft": 1500, "bedrooms": 3, "age_years": 10, "location_score": 7}])
print("Example predicted price:", round(model.predict(example)[0], 2))
