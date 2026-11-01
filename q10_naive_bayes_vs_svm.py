# Q10: Naive Bayes and SVM on the same data, compare precision and recall
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

models = {
    "Naive Bayes": GaussianNB(),
    "SVM": make_pipeline(StandardScaler(), SVC()),
}
for name, model in models.items():
    y_pred = model.fit(X_train, y_train).predict(X_test)
    print(f"{name:12s} precision={precision_score(y_test, y_pred):.4f} "
          f"recall={recall_score(y_test, y_pred):.4f}")
