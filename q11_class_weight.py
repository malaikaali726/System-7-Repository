# Q11: imbalanced dataset, compare recall before and after class_weight='balanced'
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.9, 0.1], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

plain = LogisticRegression(max_iter=1000).fit(X_train, y_train)
weighted = LogisticRegression(max_iter=1000, class_weight="balanced").fit(X_train, y_train)

print("Recall before (no weights):", round(recall_score(y_test, plain.predict(X_test)), 4))
print("Recall after (balanced):   ", round(recall_score(y_test, weighted.predict(X_test)), 4))
