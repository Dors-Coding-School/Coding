import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check the number of command-line arguments provided by the user
    if len(sys.argv) not in [2, 3]:
        # If there aren't 2 or 3 arguments (including the script's name itself), exit the program with a usage message
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Use the load_data function to fetch images and labels from the directory provided as the first command-line argument
    images, labels = load_data(sys.argv[1])

    # Convert label list into one-hot encoded format
    labels = tf.keras.utils.to_categorical(labels)

    # Use sklearn's train_test_split function to divide the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get the compiled neural network model using the get_model function
    model = get_model()

    # Train the model using the training data 
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate the model's performance using the testing data
    model.evaluate(x_test, y_test, verbose=2)

    # If a third command-line argument is provided, assume it's the filename to save the trained model
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        # Save the trained model to the specified filename
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    # Initialize empty lists to store image data and corresponding labels
    images = []
    labels = []

    # Loop through each category folder in the data directory
    for category in range(NUM_CATEGORIES):
        # Construct the path to the category directory using os.path.join for compatibility
        category_directory = os.path.join(data_dir, str(category))
        
        # Check if the path points to a directory
        if os.path.isdir(category_directory):
            
            # Loop through each image file in the category directory
            for filename in os.listdir(category_directory):
                
                # Construct the full path to the image file
                image_path = os.path.join(category_directory, filename)
                
                # Use OpenCV to read the image from the file
                image = cv2.imread(image_path)
                
                # Resize the image to the desired dimensions (aIeMG_WIDTH x IMG_HEIGHT)
                image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
                
                # Append the processed image to the images list
                images.append(image)
                
                # Append the current category number to the labels list
                labels.append(category)

    # Return the lists of images and labels
    return images, labels


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    # Create a new sequential model
    model = tf.keras.models.Sequential([
        
        # First convolutional layer: 
        # 32 filters, each of size (3, 3), ReLU activation function
        # The input shape is defined for the very first layer (it matches the shape of our images)
        tf.keras.layers.Conv2D(
            32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),
        
        # Max-pooling layer: 
        # Reduces spatial dimensions by taking the maximum value in each 2x2 grid
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Second convolutional layer: 
        # 64 filters, each of size (3, 3), ReLU activation function
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        
        # Another max-pooling layer to further reduce spatial dimensions
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Flatten the 3D output of the previous layer to 1D
        tf.keras.layers.Flatten(),
        
        # Fully connected (dense) layer: 
        # 128 units, ReLU activation function
        tf.keras.layers.Dense(128, activation='relu'),
        
        # Dropout layer: 
        # Randomly sets 50% of the input units to 0 during training, which can help prevent overfitting
        tf.keras.layers.Dropout(0.5),

        # Output layer: 
        # One unit for each category, softmax activation function for multi-class classification
        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])

    # Compile the model: 
    # Defines how the model should be trained (optimizer, loss function, metric to monitor)
    model.compile(
        optimizer='adam',                      # Adam optimization algorithm
        loss='categorical_crossentropy',       # Suitable loss function for multi-class classification
        metrics=['accuracy']                   # Monitor accuracy during training
    )

    return model


if __name__ == "__main__":
    main()
