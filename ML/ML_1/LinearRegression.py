import numpy as np

class LinearRegression:
    def __init__(self, batch_size=32, regularization=0, max_epochs=100, patience=3):
        self.batch_size = batch_size
        self.regularization = regularization
        self.max_epochs = max_epochs
        self.patience = patience
        self.weights = None
        self.bias = None
        self.loss_history = []

    def fit(self, X, y):
        # Initialize weights and bias with random values
        self.weights = np.random.randn(X.shape[1])
        self.bias = np.random.randn()

        # Create validation and training splits
        validation_split_ratio = 0.1
        num_val_samples = int(validation_split_ratio * len(X))
        X_train, y_train = X[:-num_val_samples], y[:-num_val_samples]
        X_val, y_val = X[-num_val_samples:], y[-num_val_samples:]

        best_loss = float('inf')
        epochs_without_improvement = 0
        optimal_weights = None
        optimal_bias = None

        for epoch in range(self.max_epochs):
            # Randomize training data
            shuffled_indices = np.random.permutation(len(X_train))
            X_train_shuffled = X_train[shuffled_indices]
            y_train_shuffled = y_train[shuffled_indices]

            # Perform batch training
            for start_idx in range(0, len(X_train), self.batch_size):
                end_idx = start_idx + self.batch_size
                X_batch = X_train_shuffled[start_idx:end_idx]
                y_batch = y_train_shuffled[start_idx:end_idx]

                # Calculate gradients
                gradient_w, gradient_b = self._compute_gradients(X_batch, y_batch)

                # Update weights and bias
                self.weights -= gradient_w
                self.bias -= gradient_b

            # Calculate loss on the validation set
            validation_loss = self._compute_loss(X_val, y_val)
            self.loss_history.append(validation_loss)

            # Early stopping based on validation loss
            if validation_loss < best_loss:
                best_loss = validation_loss
                optimal_weights = self.weights.copy()
                optimal_bias = self.bias
                epochs_without_improvement = 0
            else:
                epochs_without_improvement += 1
                if epochs_without_improvement >= self.patience:
                    break

        # Assign the best found weights and bias
        self.weights = optimal_weights
        self.bias = optimal_bias

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

    def score(self, X, y):
        y_pred = self.predict(X)
        mse = np.mean((y_pred - y) ** 2)
        return mse

    def save(self, file_path):
        np.savez(file_path, weights=self.weights, bias=self.bias)

    def load(self, file_path):
        data = np.load(file_path)
        self.weights = data['weights']
        self.bias = data['bias']

    def _compute_gradients(self, X, y):
        # Calculate gradients for weights and bias using mean squared error
        y_pred = self.predict(X)
        error = y_pred - y
        gradient_weights = np.dot(X.T, error) / len(X) + 2 * self.regularization * self.weights
        gradient_bias = np.mean(error)
        return gradient_weights, gradient_bias

    def _compute_loss(self, X, y):
        # Calculate mean squared error loss
        y_pred = self.predict(X)
        mse = np.mean((y_pred - y) ** 2)
        return mse
