from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from LinearRegression import LinearRegression

def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    feature_idx = 0  # Sepal length
    target_idx = 3  # Petal width

    X_feature = X[:, feature_idx].reshape(-1, 1)
    y_target = X[:, target_idx]

    X_train, X_test, y_train, y_test = train_test_split(X_feature, y_target, test_size=0.1, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    model.save('linear_reg_2_params.npz')

    plt.figure(figsize=(10, 6))
    plt.plot(model.loss_history, label='Validation Loss')
    plt.xlabel('Epoch Number')
    plt.ylabel('Loss')
    plt.title('Validation Loss over Epochs')
    plt.legend()
    plt.savefig('sepal_length_to_petal_width_loss.png')
    plt.show()

    plt.scatter(X_test, y_test, color='blue', label='Actual')
    plt.scatter(X_test, y_pred, color='red', label='Predicted')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Width')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
