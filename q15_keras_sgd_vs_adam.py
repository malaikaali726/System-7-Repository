# Q15: Keras Sequential model on tabular data, compare SGD and Adam
# For the student results task, replace the dataset below with your student data
# (numeric features as X, pass/fail or grade as y).
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_breast_cancer(return_X_y=True)
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

def build_model():
    return keras.Sequential([
        keras.Input(shape=(X.shape[1],)),
        keras.layers.Dense(16, activation="relu"),
        keras.layers.Dense(1, activation="sigmoid"),
    ])

optimizers = {
    "SGD": keras.optimizers.SGD(learning_rate=0.01),
    "Adam": keras.optimizers.Adam(learning_rate=0.001),
}
histories = {}
for name, opt in optimizers.items():
    model = build_model()
    model.compile(optimizer=opt, loss="binary_crossentropy", metrics=["accuracy"])
    h = model.fit(X_train, y_train, epochs=50, batch_size=16,
                  validation_split=0.2, verbose=0)
    histories[name] = h.history
    _, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"{name} test accuracy: {acc:.4f}")

for name, hist in histories.items():
    plt.plot(hist["loss"], label=f"{name} train")
    plt.plot(hist["val_loss"], "--", label=f"{name} validation")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.title("Loss curves: SGD vs Adam")
plt.savefig("loss_curves.png")
