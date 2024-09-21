import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from LinearRegression import LinearRegression

def main():
    iris = load_iris()
    X = iris.data
    y = X[:, 2]  # Petal length

    feature_indices = [0, 1]  # Sepal length and width
    X_feature = X[:, feature_indices]

    X_train, X_test, y_train, y_test = train_test_split(X_feature, y, test_size=0.1, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train_standardized = scaler.fit_transform(X_train)
    X_test_standardized = scaler.transform(X_test)

    model = LinearRegression(max_epochs=1000, batch_size=32)
    model.fit(X_train_standardized, y_train)

    y_pred = model.predict(X_test_standardized)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error for Sepal Length and Width to Petal Length: {mse}")

    plt.figure(figsize=(10, 6))
    plt.plot(model.loss_history, label='Validation Loss')
    plt.xlabel('Epoch Number')
    plt.ylabel('Loss')
    plt.title('Validation Loss over Epochs')
    plt.legend()
    plt.savefig('sepal_length_width_to_petal_length_loss.png')
    plt.show()

    # For plotting predicted vs actual values, use a scatter plot without x feature
    plt.scatter(X_test_standardized[:, 0], y_test, color='blue', label='Actual')
    plt.scatter(X_test_standardized[:, 0], y_pred, color='red', label='Predicted')
    plt.xlabel('Standardized Sepal Length')
    plt.ylabel('Petal Length')
    plt.legend()
    plt.show()

    # Alternative plot to show influence of both features using first feature on x-axis
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test_standardized[:, 1], y_test, color='blue', label='Actual')
    plt.scatter(X_test_standardized[:, 1], y_pred, color='red', label='Predicted')
    plt.xlabel('Standardized Sepal Width')
    plt.ylabel('Petal Length')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()