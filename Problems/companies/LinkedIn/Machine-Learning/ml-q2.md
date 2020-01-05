Question about SVM, overfitting, classification methods?

### SVM

The Maximal-Margin Classifier is a hypothetical classifier that best explains how SVM works in practice.
The numeric input variables (x) in your data (the columns) form an n-dimensional space. For example, if you had two input variables, this would form a two-dimensional space.

A hyperplane is a line that splits the input variable space. In SVM, a hyperplane is selected to best separate the points in the input variable space by their class, either class 0 or class 1. In two-dimensions you can visualize this as a line and let’s assume that all of our input points can be completely separated by this line. For example:

B0 + (B1 * X1) + (B2 * X2) = 0

Where the coefficients (B1 and B2) that determine the slope of the line and the intercept (B0) are found by the learning algorithm, and X1 and X2 are the two input variables.

You can make classifications using this line. By plugging in input values into the line equation, you can calculate whether a new point is above or below the line.

Above the line, the equation returns a value greater than 0 and the point belongs to the first class (class 0).
Below the line, the equation returns a value less than 0 and the point belongs to the second class (class 1).
A value close to the line returns a value close to zero and the point may be difficult to classify.
If the magnitude of the value is large, the model may have more confidence in the prediction.
The distance between the line and the closest data points is referred to as the margin. The best or optimal line that can separate the two classes is the line that as the largest margin. This is called the Maximal-Margin hyperplane.

The margin is calculated as the perpendicular distance from the line to only the closest points. Only these points are relevant in defining the line and in the construction of the classifier. These points are called the support vectors. They support or define the hyperplane.

The hyperplane is learned from training data using an optimization procedure that maximizes the margin.



### Overfitting vs Underfitting
* Overfitting is the case where the overall cost is really small, but the generalization of the model is unreliable. This is due to the model learning “too much” from the training data set.
This may sound preposterous, as why would we settle for a higher cost when we can just find the minimal one? Generalization.
The more we leave the model training the higher the chance of overfitting occurring. We always want to find the trend, not fit the line to all the data points. Overfitting (or high variance) leads to more bad than good. 
What use is a model that has learned very well from from the training data but still can’t make reliable predictions for new inputs?

* Underfitting is the case where the model has “ not learned enough” from the training data, resulting in low generalization and unreliable predictions.
As you probably expected, underfitting (i.e. high bias) is just as bad for generalization of the model as overfitting. 
In high bias, the model might not have enough flexibility in terms of line fitting, resulting in a simplistic line that does not generalize well.

* Conclusions; 
A model that is underfit will have high training and high testing error while an overfit model will have extremely low training error but a high testing error.
Overfitting and underfitting is a fundamental problem that trips up even experienced data analysts. In my lab, I have seen many grad students fit a model with extremely low error to their data and then eagerly write a paper with the results. 
Their model looks great, but the problem is they never even used a testing set let alone a validation set! 
The model is nothing more than an overfit representation of the training data, a lesson the student soon learns when someone else tries to apply their model to new data.
Generally, a model that is underfit will have high training and high testing error while an overfit model will have extremely low training error but a high testing error.


