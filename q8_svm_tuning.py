# Q8: tune an SVM with GridSearchCV and RandomizedSearchCV, compare score and time
import time
from scipy.stats import loguniform
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

pipe = make_pipeline(StandardScaler(), SVC())

param_grid = {
    "svc__C": [0.1, 1, 10, 100],
    "svc__gamma": [0.001, 0.01, 0.1, 1],
    "svc__kernel": ["rbf", "linear"],
}
start = time.time()
grid = GridSearchCV(pipe, param_grid, cv=5, n_jobs=-1).fit(X_train, y_train)
grid_time = time.time() - start

param_dist = {
    "svc__C": loguniform(1e-2, 1e3),
    "svc__gamma": loguniform(1e-4, 1e1),
    "svc__kernel": ["rbf", "linear"],
}
start = time.time()
rand = RandomizedSearchCV(pipe, param_dist, n_iter=20, cv=5,
                          random_state=42, n_jobs=-1).fit(X_train, y_train)
rand_time = time.time() - start

print(f"GridSearchCV      best CV={grid.best_score_:.4f} time={grid_time:.2f}s params={grid.best_params_}")
print(f"RandomizedSearchCV best CV={rand.best_score_:.4f} time={rand_time:.2f}s params={rand.best_params_}")
print("Test accuracy (grid):", round(grid.score(X_test, y_test), 4))
print("Test accuracy (random):", round(rand.score(X_test, y_test), 4))
