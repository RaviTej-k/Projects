This assignment covers Linear Models for regression and classification. Linear Regression is a method of predicting real values given some input. Logistic Regression is a method of predicting a label or multiple labels.

These models have been implemented over and over again and are available in many popular machine learning frameworks. It is important to implement the models yourself so that you gain a deeper understanding of them.

Implementation of the LinearRegression class
Before evaluating any data, we need some code to actually fit, predict, and score samples. This will be implemented in LinearRegression.py provided in this repository. The skeleton of the class is already there. In part 1, you will need to implement the fit, predict, and score functions.
Preparing the Data
Much of machine learning is in understanding the data you are working with. For our regression task, we want to predict continuous outputs given some input feature(s).

Each sample in the Iris dataset has 4 features:
sepal length
sepal width
petal length
petal width
We may want to know which feature is most predictive of another. Does knowledge of the sepal length provide good estimates of the sepal width? What about the petal width? What if we use the sepal length and width to predict the petal length or width?

In this section of the assignment, you will create 4 different regression models to answer some of these questions. This will be trivial to do once the code for the model is finished.

To begin, load the data using scikit-learn. In order to verify the models that you will create in the following two sections, you will need to take some portion of the dataset and reserve it for testing. Randomly select 10% of the dataset, ensuring an even split of each class. This will be your test set. Note that this is different than the random 10% that is taken from the training set when in the fit method. The rest of the data will serve as your training set.

Training
Select 4 different combinations of input and output features to use to train 4 different models. For example, one model could predict the petal width given petal length and sepal width. Another could predict sepal length using only petal features. It does not matter which combination you choose as long as you have 4 unique combinations.

Your models should be trained using batch gradient descent with a batch size (optional parameter) of 32 using mean squared error as your loss function.

For each model, train for n=100
 steps (optional parameter) OR until the loss on the validation set increases for a number of consecutive epochs determined by patience (default to 3).

As each model trains, record the loss averaged over the batch size for each step. A single step is the processing of a single batch. One way to save this data is to either return an array from the fit method or save it as an internal class member that can be retrieved after training is complete.

After each model trains, plot the loss against the step number and save it. These plots should also be added to your report.

Regularization
To observe the effects of regularization, pick one of your trained models and inspect the weights. Train an identical model again, except this time you will add L2 regularization to the loss. Record the difference in parameters between the regularized and non-regularized model.

Record these values into your report so they can be verified.

Create a separate training script for each model that you created. Name the scripts train_regression1.py, train_regression2.py, etc. This should include training the model, saving the model parameters, and plotting the loss.

Testing
For each model you created, test its performance on unseen data by evaluating the mean squared error against the test dataset that you set aside previously. This should be implemented as 4 separate scripts. Each script should load the model parameters from the respective model and then evaluate the model on the test set. The mean squared error should be printed to the console. Name the scripts eval_regression1.py, eval_regression2.py, etc.

In your report, briefly describe which input feature is most predictive of its corresponding output feature based on your experiments.

Regression with Multiple Outputs
In the previous section, you created 4 different regression models. Each model predicted a single output value given some input features. In this section, you will create a single model that predicts the petal length and width given the sepal length and width.

Use similar data preparation steps that you did in the previous section. The only difference is that you will need to predict 2 output values instead of 1.

Classification
Similar to part 1, you will need to create a class for each classification method. These classes should implement both a predict and fit method.

The fit method should take as input an ndarray of data samples and target values (the classes). It should then optimize the set of parameters following the respective training method for that classification method.

The predict method should take as input an ndarray of samples to predict.

For each classification method that is implemented, you will need to compare 3 variants of input features:

petal length/width
sepal length/width
all features
For the first two, include visualizations of the classifier using plot_decision_regions from mlxtend (https://github.com/rasbt/mlxtend). This plotting function works with your trained classifier, assuming you have implemented a predict method.

Logistic Regression
For the first classifier, implement a LogisticRegression class similar to how the LinearRegression class was implemented. The fit method should use either the normal equations or gradient descent to come up with an optimal set of parameters.

Testing
For each trained model, compute the accuracy on the test set that was set aside for each data variant. Since there are 3 variants, there should be 3 comparisons of Logistic Regression. Implement each variant evaluation as a separate script. Name the scripts eval_classifier1.py, eval_classifier2.py, etc.

These scripts should load the best trained weights, evaluate the accuracy on the test set, and print the accuracy to the console.
