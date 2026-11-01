# Q3: MAE, MSE, RMSE and R2 with NumPy, verified with scikit-learn
# Note: load_diabetes is used as a regression dataset in place of a house-price dataset.
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_pred = LinearRegression().fit(X_train, y_train).predict(X_test)

# NumPy calculations
mae = np.mean(np.abs(y_test - y_pred))
mse = np.mean((y_test - y_pred) ** 2)
rmse = np.sqrt(mse)
r2 = 1 - np.sum((y_test - y_pred) ** 2) / np.sum((y_test - y_test.mean()) ** 2)
print(f"NumPy   -> MAE={mae:.4f} MSE={mse:.4f} RMSE={rmse:.4f} R2={r2:.4f}")

# scikit-learn verification
print(f"sklearn -> MAE={mean_absolute_error(y_test, y_pred):.4f} "
      f"MSE={mean_squared_error(y_test, y_pred):.4f} "
      f"RMSE={np.sqrt(mean_squared_error(y_test, y_pred)):.4f} "
      f"R2={r2_score(y_test, y_pred):.4f}")
