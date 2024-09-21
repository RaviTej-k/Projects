# Import necessary libraries
import numpy as np
import mlxtend
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from mlxtend.plotting import plot_decision_regions

# Define the Logistic Regression class
class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)
        self.bias = 0

        for _ in range(self.num_iterations):
            linear_model_output = np.dot(X, self.weights) + self.bias
            predictions = self.sigmoid(linear_model_output)

            dw = (1 / num_samples) * np.dot(X.T, (predictions - y))
            db = (1 / num_samples) * np.sum(predictions - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        linear_model_output = np.dot(X, self.weights) + self.bias
        predictions = self.sigmoid(linear_model_output)
        return (predictions >= 0.5).astype(int)

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = (iris.target != 0).astype(int)  # Binary classification: setosa (0) vs others (1)

# Define feature combinations for evaluation
feature_combinations = [
    {'features': [0, 1], 'title': 'Sepal Length/Width'},
    {'features': [2, 3], 'title': 'Petal Length/Width'},
    {'features': [0, 1, 2, 3], 'title': 'All Features'}
]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the feature data
scaler = StandardScaler()
X_train_standardized = scaler.fit_transform(X_train)
X_test_standardized = scaler.transform(X_test)

# Train and visualize Logistic Regression models for each feature combination
for combo in feature_combinations:
    # Select features for the current combination
    X_train_combo = X_train_standardized[:, combo['features']]
    X_test_combo = X_test_standardized[:, combo['features']]
    
    # Train Logistic Regression model
    log_reg_model = LogisticRegression()
    log_reg_model.fit(X_train_combo, y_train)

    # Plot decision regions
    plot_decision_regions(X_train_combo, y_train, clf=log_reg_model, filler_feature_values={i: 0 for i in range(len(combo['features']))}, filler_feature_ranges={i: 1 for i in range(len(combo['features']))})
    plt.title(f'Logistic Regression - {combo["title"]} Combination')
    plt.xlabel('Feature 1 (Standardized)')
    plt.ylabel('Feature 2 (Standardized)')
    plt.show()
