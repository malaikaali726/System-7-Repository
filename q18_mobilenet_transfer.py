# Q18: MobileNetV2 transfer learning with a frozen base, compared with the CNN from scratch
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

CLASSES = ["airplane", "automobile", "bird", "cat", "deer",
           "dog", "frog", "horse", "ship", "truck"]

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
# Subset for speed on a laptop; use the full data if time allows
x_train, y_train = x_train[:10000], y_train[:10000]
x_test, y_test = x_test[:2000], y_test[:2000]

def prep(x):
    x = tf.image.resize(x, (96, 96)).numpy()
    return preprocess_input(x)

x_train, x_test = prep(x_train), prep(x_test)

base = MobileNetV2(input_shape=(96, 96, 3), include_top=False,
                   weights="imagenet", pooling="avg")
base.trainable = False                       # feature extraction: freeze the base

model = keras.Sequential([
    layers.Input(shape=(96, 96, 3)),
    base,
    layers.Dropout(0.2),
    layers.Dense(10, activation="softmax"),
])
model.compile(optimizer=keras.optimizers.Adam(1e-3),
              loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

_, acc = model.evaluate(x_test, y_test, verbose=0)
print(f"MobileNetV2 (frozen base) test accuracy: {acc:.4f}")
print("Compare with the CNN from scratch in q17_cnn_cifar10.py (full data, 10 epochs).")

# Visualize predictions
probs = model.predict(x_test[:9], verbose=0)
fig, axes = plt.subplots(3, 3, figsize=(7, 7))
for i, ax in enumerate(axes.flat):
    img = (x_test[i] - x_test[i].min()) / (x_test[i].max() - x_test[i].min())
    ax.imshow(img)
    pred = CLASSES[np.argmax(probs[i])]
    true = CLASSES[int(y_test[i])]
    ax.set_title(f"pred: {pred}\ntrue: {true}", fontsize=8)
    ax.axis("off")
plt.tight_layout()
plt.savefig("mobilenet_predictions.png")
