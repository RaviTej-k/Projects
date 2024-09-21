import numpy as np

class LDAModel:
    def __init__(self):
        # Initialize parameters for LDA
        self.means_ = None          # Mean vectors for each class
        self.covariance_ = None     # Shared covariance matrix
        self.priors_ = None         # Class priors
        self.classes_ = None        # Unique class labels

    def fit(self, X, y):
        # Fit the LDA model to the data
        self.classes_ = np.unique(y)        # Get unique class labels
        n_features = X.shape[1]             # Number of features
        n_classes = len(self.classes_)      # Number of classes
        self.means_ = np.zeros((n_classes, n_features))  # Initialize mean vectors
        self.covariance_ = np.zeros((n_features, n_features))  # Initialize covariance matrix
        self.priors_ = np.zeros(n_classes)  # Initialize class priors

        for idx, cls in enumerate(self.classes_):
            X_cls = X[y == cls]             # Get samples of class `cls`
            self.means_[idx, :] = X_cls.mean(axis=0)  # Compute mean vector for class `cls`
            self.priors_[idx] = X_cls.shape[0] / X.shape[0]  # Compute prior for class `cls`
            self.covariance_ += np.dot((X_cls - self.means_[idx]).T, X_cls - self.means_[idx])  # Accumulate covariance

        self.covariance_ /= X.shape[0] - n_classes  # Average the covariance matrix

    def predict(self, X):
        # Predict class labels for samples in X
        inv_cov = np.linalg.inv(self.covariance_)  # Inverse of the covariance matrix
        linear_term = np.dot(X, inv_cov.dot(self.means_.T))  # Linear term in the decision function
        constant_term = -0.5 * np.diag(np.dot(self.means_, inv_cov.dot(self.means_.T)))  # Constant term in the decision function
        log_priors = np.log(self.priors_)  # Logarithm of class priors

        scores = linear_term + constant_term + log_priors  # Compute scores for each class
        return self.classes_[np.argmax(scores, axis=1)]  # Return class with highest score

class QDAModel:
    def __init__(self):
        # Initialize parameters for QDA
        self.means_ = None           # Mean vectors for each class
        self.covariances_ = None     # Covariance matrices for each class
        self.priors_ = None          # Class priors
        self.classes_ = None         # Unique class labels

    def fit(self, X, y):
        # Fit the QDA model to the data
        self.classes_ = np.unique(y)         # Get unique class labels
        n_features = X.shape[1]              # Number of features
        self.means_ = np.zeros((len(self.classes_), n_features))  # Initialize mean vectors
        self.covariances_ = []               # Initialize list of covariance matrices
        self.priors_ = np.zeros(len(self.classes_))  # Initialize class priors

        for idx, cls in enumerate(self.classes_):
            X_cls = X[y == cls]              # Get samples of class `cls`
            self.means_[idx] = np.mean(X_cls, axis=0)  # Compute mean vector for class `cls`
            cov_matrix = np.cov(X_cls, rowvar=False)  # Compute covariance matrix for class `cls`
            self.covariances_.append(cov_matrix)  # Store covariance matrix
            self.priors_[idx] = X_cls.shape[0] / X.shape[0]  # Compute prior for class `cls`

    def predict(self, X):
        # Predict class labels for samples in X
        n_samples = X.shape[0]
        scores = np.zeros((n_samples, len(self.classes_)))  # Initialize scores matrix
        for idx, cls in enumerate(self.classes_):
            mean = self.means_[idx]           # Mean vector for class `cls`
            cov = self.covariances_[idx]      # Covariance matrix for class `cls`
            inv_cov = np.linalg.inv(cov)      # Inverse of the covariance matrix
            _, log_det_cov = np.linalg.slogdet(cov)  # Log determinant of the covariance matrix
            diff = X - mean                   # Difference between samples and mean
            term = np.sum((diff @ inv_cov) * diff, axis=1)  # Quadratic term in the decision function
            scores[:, idx] = -0.5 * term - 0.5 * log_det_cov + np.log(self.priors_[idx])  # Compute scores

        return self.classes_[np.argmax(scores, axis=1)]  # Return class with highest score

class GaussianNaiveBayes:
    def __init__(self):
        # Initialize parameters for Gaussian Naive Bayes
        self.means_ = None           # Mean vectors for each class
        self.variances_ = None       # Variance vectors for each class
        self.priors_ = None          # Class priors
        self.classes_ = None         # Unique class labels

    def fit(self, X, y):
        # Fit the Gaussian Naive Bayes model to the data
        self.classes_ = np.unique(y)         # Get unique class labels
        n_features = X.shape[1]              # Number of features
        n_classes = len(self.classes_)       # Number of classes
        self.means_ = np.zeros((n_classes, n_features))  # Initialize mean vectors
        self.variances_ = np.zeros((n_classes, n_features))  # Initialize variance vectors
        self.priors_ = np.zeros(n_classes)   # Initialize class priors

        for idx, cls in enumerate(self.classes_):
            X_cls = X[y == cls]              # Get samples of class `cls`
            self.means_[idx] = X_cls.mean(axis=0)  # Compute mean vector for class `cls`
            self.variances_[idx] = X_cls.var(axis=0)  # Compute variance vector for class `cls`
            self.priors_[idx] = X_cls.shape[0] / X.shape[0]  # Compute prior for class `cls`

    def predict(self, X):
        # Predict class labels for samples in X
        n_samples = X.shape[0]
        n_classes = len(self.classes_)
        log_probs = np.zeros((n_samples, n_classes))  # Initialize log probability matrix

        for idx, (mean, var) in enumerate(zip(self.means_, self.variances_)):
            # Compute the log probability of each class
            # Use the Gaussian probability density function formula for log probabilities
            log_prob = -0.5 * np.sum(np.log(2 * np.pi * var)) \
                       -0.5 * np.sum(((X - mean) ** 2) / var, axis=1)
            log_probs[:, idx] = log_prob + np.log(self.priors_[idx])  # Add log prior

        # Return the class with the highest log probability
        return self.classes_[np.argmax(log_probs, axis=1)]
