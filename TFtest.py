import tensorflow as tf

# Create the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Generate some training data
x_train = tf.constant([2, 4, 6, 8, 10, 11, 13, 15, 17, 19], dtype=tf.float32)
y_train = tf.constant([0, 0, 0, 0, 0, 1, 1, 1, 1, 1], dtype=tf.float32)

# Train the model
model.fit(x_train, y_train, epochs=100)

# Test the model
x_test = tf.constant([3, 7, 12, 14, 16], dtype=tf.float32)
y_test = tf.constant([1, 1, 0, 0, 0], dtype=tf.float32)
loss, accuracy = model.evaluate(x_test, y_test)

# Print the results
print('Test accuracy:', accuracy)