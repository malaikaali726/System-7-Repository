# Q14: single perceptron in NumPy that learns the AND gate
import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

w = np.zeros(2)
b = 0.0
lr = 0.1

for epoch in range(20):
    errors = 0
    for xi, target in zip(X, y):
        pred = int(np.dot(w, xi) + b >= 0)     # step activation
        update = lr * (target - pred)
        w += update * xi
        b += update
        errors += int(update != 0)
    if errors == 0:                           # converged
        break

print("Learned weights:", w, "bias:", round(b, 3), "epochs:", epoch + 1)
for xi in X:
    print(xi, "->", int(np.dot(w, xi) + b >= 0))
