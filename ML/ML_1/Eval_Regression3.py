import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from LinearRegression import LinearRegression

def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    feature_indices = [0, 1]  # Sepal length and width
    target_idx = 2  # Petal length

    X_feature = X[:, feature_indices]
    y_target = X[:, target_idx]

    X_train, X_test, y_train, y_test = train_test_split(X_feature, y_target, test_size=0.1, random_state=42)

    model = LinearRegression()
    model.load('linear_reg_3_params.npz')

    # Evaluate on the test set
    mse = model.score(X_test, y_test)
    print(f"Mean Squared Error for Sepal Length and Width to Petal Length: {mse}")

if __name__ == "__main__":
    main()
