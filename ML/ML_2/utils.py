import numpy as np
import pickle

def load_and_prepare_data(as_grayscale=False):
    """Load raw data using pickle."""
    
    # List of file paths for CIFAR-10 training batches
    train_batches = ['data/data_batch_1', 'data/data_batch_2', 'data/data_batch_3', 'data/data_batch_4', 'data/data_batch_5']
    
    # File path for the CIFAR-10 test batch
    test_batch = 'data/test_batch'

    # Try loading the training data
    try:
        for batch in train_batches:
            with open(batch, 'rb') as fo:
                # Unpickle the data from the current batch file
                batch = pickle.load(fo, encoding='bytes')
                
                # Extract the image data and labels from the batch
                data = batch[b'data']
                labels = batch[b'labels']
                
                # If train_data and train_labels already exist, concatenate the new data and labels
                if 'train_data' in locals():
                    train_data = np.concatenate((train_data, data))
                    train_labels = np.concatenate((train_labels, labels))
                else:
                    # If this is the first batch, initialize train_data and train_labels
                    train_data = data
                    train_labels = labels
    except FileNotFoundError:
        # If the dataset files are not found, prompt the user to download and place them correctly
        print("The CIFAR-10 dataset has not been downloaded. Download and extract the dataset from https://www.cs.toronto.edu/~kriz/cifar.html and place the data_batch files in the cifar10 directory.")
        return
    
    # Try loading the test data
    try:
        with open(test_batch, 'rb') as fo:
            # Unpickle the data from the test batch file
            batch = pickle.load(fo, encoding='bytes')
            
            # Extract the image data and labels from the test batch
            test_data = batch[b'data']
            test_labels = batch[b'labels']
    except FileNotFoundError:
        # If the test batch file is not found, prompt the user to download and place it correctly
        print("The CIFAR-10 dataset has not been downloaded. Download and extract the dataset from https://www.cs.toronto.edu/~kriz/cifar.html and place the data_batch files in the cifar10 directory.")
        return
    
    # Reshape the training data to have dimensions (num_samples, 32, 32, 3) and transpose to (num_samples, 32, 32, 3)
    train_data = train_data.reshape((len(train_data), 3, 32, 32)).transpose(0, 2, 3, 1)
    
    # Reshape the test data to have dimensions (num_samples, 32, 32, 3) and transpose to (num_samples, 32, 32, 3)
    test_data = test_data.reshape((len(test_data), 3, 32, 32)).transpose(0, 2, 3, 1)

    # If grayscale conversion is requested
    if as_grayscale:
        # Convert the training and test data to grayscale using the given weights for RGB channels
        train_data = np.dot(train_data, [0.299, 0.587, 0.114])
        test_data = np.dot(test_data, [0.299, 0.587, 0.114])

    # Return the prepared training and test data along with their labels
    return train_data, train_labels, test_data, test_labels


