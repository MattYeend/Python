from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict a new value
prediction = model.predict([[5]])
print("Prediction for 5:", prediction[0])
