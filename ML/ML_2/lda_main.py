import numpy as np
from sklearn.metrics import accuracy_score

from utils import load_and_prepare_data
from models import LDAModel

def main(as_grayscale=False):
    print(f"\nRunning model with {'grayscale' if as_grayscale else 'RGB'} images.")
    
    # Load the data (images and labels) using the utility function
    X_train, y_train, X_test, y_test = load_and_prepare_data(as_grayscale)

    # Convert lists to NumPy arrays if necessary
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    y_test = np.array(y_test)

    print(f"Data loaded. Shapes: X_train: {X_train.shape}, y_train: {y_train.shape}, X_test: {X_test.shape}, y_test: {y_test.shape}")

    # Ensure data is reshaped correctly (flatten the images)
    # This step is necessary for LDA since it expects 2D data (samples x features)
    X_train = X_train.reshape(X_train.shape[0], -1)  # Flatten the training images
    X_test = X_test.reshape(X_test.shape[0], -1)     # Flatten the testing images
    print(f"Data reshaped for {'grayscale' if as_grayscale else 'RGB'} mode. New shape: X_train: {X_train.shape}, X_test: {X_test.shape}")

    # Initialize and fit the LDA model
    print("Initializing and fitting the LDA model...")
    lda = LDAModel()          # Create an instance of the LDA model
    lda.fit(X_train, y_train) # Fit the model to the training data
    print("Model fitting completed.")

    # Predict and evaluate the model
    print("Making predictions...")
    predictions = lda.predict(X_test)  # Predict the labels for the test data
    print("Predictions completed.")

    # Calculate and print accuracy
    accuracy = accuracy_score(y_test, predictions)  # Compute the accuracy of the model
    print(f"Accuracy ({'Grayscale' if as_grayscale else 'RGB'}): {accuracy}")  # Print the accuracy

if __name__ == "__main__":
    print("Starting the script...")
    main(as_grayscale=False)  # Evaluate on RGB data
    main(as_grayscale=True)   # Evaluate on Grayscale data


