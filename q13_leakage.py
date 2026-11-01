# Q13: Pipeline (scaler, PCA, classifier) vs scaling before the split (data leakage)
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Correct: the scaler and PCA are fitted only on each training fold
pipe = make_pipeline(StandardScaler(), PCA(n_components=5), LogisticRegression(max_iter=1000))
good = cross_val_score(pipe, X, y, cv=cv)
print("Pipeline (no leakage) CV mean:", round(good.mean(), 4))

# Leaky: the scaler and PCA see the whole dataset, including the test folds
X_leaky = PCA(n_components=5).fit_transform(StandardScaler().fit_transform(X))
leaky = cross_val_score(LogisticRegression(max_iter=1000), X_leaky, y, cv=cv)
print("Scaled-before-split (leaky) CV mean:", round(leaky.mean(), 4))
print("Note: the leaky score is optimistic because test information leaked into training.")
