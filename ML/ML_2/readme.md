For this assignment, we will be using the CIFAR-10 dataset which consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class. 
There are 50,000 training images and 10,000 test images. The dataset is available from many places online, and a direct download link is available in Canvas. 
You can also find more information about the dataset at https://www.cs.toronto.edu/~kriz/cifar.html.
Please download the data set from the above link.

Downloading and Preprocessing the Data
After downloading the data, extract the batch files to the cifar10 directory that is already in this repository.
A function is provided in assignment2/utils.py to extract and load the data to numpy arrays. 

Linear Discriminant Analysis
Complete the class definition of LDA in assignment2/models.py. The fit method should estimate the class means and the shared covariance matrix. 
The predict method should use these estimates to make predictions.

Quadratic Discriminant Analysis
Complete the class definition of QDA in assignment2/models.py. The fit method should estimate the class means and the class covariance matrices. 
The predict method should use these estimates to make predictions.

Gaussian Naive Bayes
Complete the class definition of GaussianNaiveBayes in assignment2/models.py. The fit method should estimate the class means and the class variances. 
The predict method should use these estimates to make predictions.
