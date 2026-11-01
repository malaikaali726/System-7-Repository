# Q7: scale numeric columns and one-hot encode categorical columns in one step
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

rng = np.random.default_rng(42)
n = 200
df = pd.DataFrame({
    "age": rng.integers(18, 70, n),
    "income": rng.normal(50000, 15000, n).round(0),
    "city": rng.choice(["Lahore", "Karachi", "Islamabad"], n),
})
df["bought"] = ((df["income"] > 50000) ^ (rng.random(n) < 0.2)).astype(int)

X = df.drop(columns="bought")
y = df["bought"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocess = ColumnTransformer([
    ("num", StandardScaler(), ["age", "income"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["city"]),
])
model = make_pipeline(preprocess, LogisticRegression())
model.fit(X_train, y_train)
print("Test accuracy:", round(model.score(X_test, y_test), 4))
print("Transformed feature count:", model[0].transform(X_train).shape[1])
