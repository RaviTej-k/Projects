import numpy as np
from utils import load_and_prepare_data
from models import QDAModel  # Ensure QDAModel is defined in your models.py to handle QDA

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def main(as_grayscale=False):
    print(f"\nRunning QDA model with {'grayscale' if as_grayscale else 'RGB'} images.")
    
    # Load the data (images and labels) using the utility function
    X_train, y_train, X_test, y_test = load_and_prepare_data(as_grayscale)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Apply scaling to data
    # Convert the data to NumPy arrays, reshape (flatten) the images, and apply scaling
    X_train = scaler.fit_transform(np.array(X_train).reshape(X_train.shape[0], -1))  # Flatten and scale the training images
    X_test = scaler.transform(np.array(X_test).reshape(X_test.shape[0], -1))  # Flatten and scale the testing images

    print(f"Data loaded and scaled. Shapes: X_train: {X_train.shape}, X_test: {X_test.shape}")

    # Initialize and fit the QDA model
    print("Initializing and fitting the QDA model...")
    qda = QDAModel()         # Create an instance of the QDA model
    qda.fit(X_train, y_train)  # Fit the model to the training data
    print("Model fitting completed.")

    # Predict and evaluate the model
    print("Making predictions...")
    predictions = qda.predict(X_test)  # Predict the labels for the test data
    print("Predictions completed.")

    # Calculate and print accuracy
    accuracy = accuracy_score(y_test, predictions)  # Compute the accuracy of the model
    print(f"QDA Accuracy ({'Grayscale' if as_grayscale else 'RGB'}): {accuracy}")  # Print the accuracy

if __name__ == "__main__":
    print("Starting the script...")
    main(as_grayscale=False)  # Evaluate on RGB data
    main(as_grayscale=True)   # Evaluate on Grayscale data
