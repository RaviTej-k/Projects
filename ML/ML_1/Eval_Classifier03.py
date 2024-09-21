import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from LogisticRegression import LogisticRegression

def main():
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = (iris.target != 0).astype(int)  # Binary classification: setosa (0) vs others (1)

    # Define input features for the third variant
    feature_indices = [0, 1, 2, 3]  # All Features

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train_standardized = scaler.fit_transform(X_train)
    X_test_standardized = scaler.transform(X_test)

    # Select features for the current variant
    X_train_variant = X_train_standardized[:, feature_indices]
    X_test_variant = X_test_standardized[:, feature_indices]
    
    # Train Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train_variant, y_train)

    # Evaluate on the test set
    y_pred = model.predict(X_test_variant)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy for All Features: {accuracy}")

if __name__ == "__main__":
    main()
