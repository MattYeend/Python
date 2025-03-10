import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Load the MNIST dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Define the AI model (a simple neural network)
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Input layer (flatten 28x28 images)
    keras.layers.Dense(128, activation='relu'),  # Hidden layer with ReLU activation
    keras.layers.Dropout(0.2),  # Dropout to prevent overfitting
    keras.layers.Dense(10, activation='softmax')  # Output layer (10 classes)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Test accuracy: {test_acc:.4f}")

# Make predictions
predictions = model.predict(x_test)

# Display a test image and the model's predicted label
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {np.argmax(predictions[0])}")
plt.show()
