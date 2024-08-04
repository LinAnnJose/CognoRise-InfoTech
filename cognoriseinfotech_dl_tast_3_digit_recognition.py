# -*- coding: utf-8 -*-
"""CognoRiseInfoTech_DL:Tast_3 Digit Recognition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14cr88AZvtmOVD86ixVOCmsE3LTMXBOq6
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten,Dense

import matplotlib.pyplot as plt
import numpy as np

(x_train,y_train),(x_test,y_test) =keras.datasets.mnist.load_data()

len(x_train)

len(x_test)

x_train[0].shape

x_train[0]

# Plot the first training image
plt.matshow(x_train[0])

# Print the label of the first training image
y_train[0]

#Normalising the dataset
x_train=x_train/255
x_test=x_test/255

x_train[0]

# Reshape the data to add a channel dimension (since MNIST images are grayscale)
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

x_train.shape

x_test.shape

#Building the CNN Model with Dropout
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),  # Dropout layer with 25% dropout rate

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),  # Dropout layer with 25% dropout rate

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),

    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),  # Dropout layer with 50% dropout rate

    layers.Dense(10, activation='softmax')
])

model.summary()

#Compile the model using the Adam optimizer and sparse categorical crossentropy loss.
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

history = model.fit(x_train,y_train,batch_size=6000,epochs=10, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}')

# Visualize training results
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

# Make predictions
y_pred = model.predict(x_test)
y_pred[0]

# Plot the first test image
plt.matshow(x_test[0])

# Print the predicted label for the first test image
np.argmax(y_pred[0])

#For first 5 image predictions
y_pred_labels=[np.argmax(i) for i in y_pred]
y_pred_labels[:5]

#Plotting Confusion matrix using tensorflow
cm=tf.math.confusion_matrix(labels=y_test,predictions=y_pred_labels)
cm

import seaborn as sns
plt.figure(figsize=(10,10))
sns.heatmap(cm,annot=True,fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')