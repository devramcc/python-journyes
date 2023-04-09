import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
import numpy as np

# Define the function that creates the Keras model with the hyperparameters to tune
def create_model(hidden_layer_size=32, learning_rate=0.001):
    model = keras.Sequential([
        keras.layers.Dense(hidden_layer_size, activation='relu', input_shape=(4,)),
        keras.layers.Dense(3, activation='softmax')
    ])
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Define the hyperparameters to tune
param_grid = {
    'hidden_layer_size': [16, 32, 64],
    'learning_rate': [0.01, 0.001, 0.0001]
}

# Create a KerasClassifier model with the create_model function and the hyperparameters to tune
model = KerasClassifier(build_fn=create_model, epochs=20, batch_size=5, verbose=0)

# Create a GridSearchCV object with the hyperparameters to tune and the model to use
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)

# Fit the GridSearchCV object to the data
grid_search.fit(X, y)

# Print the best hyperparameters and the corresponding accuracy score
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")