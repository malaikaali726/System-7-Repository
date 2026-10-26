import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("student_success_practice.csv")
X = df[["study_hours", "attendance_pct", "assignments_completed"]]
y = df["passed"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

models = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "KNN": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"\n{name} accuracy: {accuracy_score(y_test, pred):.3f}")
    print(classification_report(y_test, pred, zero_division=0))

tree = models["Random Forest"]
print("Random forest feature importance:")
for feature, importance in sorted(zip(X.columns, tree.feature_importances_), key=lambda x: x[1], reverse=True):
    print(f"  {feature}: {importance:.3f}")
