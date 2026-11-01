# Q16: resize to 64x64, normalize, apply augmentation layers, show 9 augmented samples
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

(x_train, _), _ = keras.datasets.cifar10.load_data()
images = tf.image.resize(x_train[:9], (64, 64)) / 255.0   # resize and normalize

augment = keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])
augmented = augment(images, training=True)

fig, axes = plt.subplots(3, 3, figsize=(6, 6))
for i, ax in enumerate(axes.flat):
    ax.imshow(augmented[i].numpy())
    ax.axis("off")
plt.suptitle("9 augmented samples")
plt.savefig("augmented_samples.png")
