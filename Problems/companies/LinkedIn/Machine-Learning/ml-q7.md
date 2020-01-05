Explain some ML concepts:
- Overfitting / Underfitting
- Regularization
- Bagging / Boosting
- Performance metrics


### What are ensemble methods?
Ensemble learning is a machine learning paradigm where multiple models (often called “weak learners”) are trained to solve the same problem and combined to get better results. 
The main hypothesis is that when weak models are correctly combined we can obtain more accurate and/or robust models.

#### Bagging, Boosting & Stacking
1. bagging, that often considers homogeneous weak learners, learns them independently from each other in parallel and combines them following some kind of deterministic averaging process
2. boosting, that often considers homogeneous weak learners, learns them sequentially in a very adaptative way (a base model depends on the previous ones) and combines them following a deterministic strategy
3. stacking, that often considers heterogeneous weak learners, learns them in parallel and combines them by training a meta-model to output a prediction based on the different weak models predictions


### Regularization
This is a form of regression, that constrains/ regularizes or shrinks the coefficient estimates towards zero. In other words, this technique discourages learning a more complex or flexible model, so as to avoid the risk of overfitting.
A regression model that uses L1 regularization technique is called Lasso Regression and model which uses L2 is called Ridge Regression.
The key difference between these two is the penalty term.
 
 - Ridge regression adds “squared magnitude” of coefficient as penalty term to the loss function. Here the highlighted part represents L2 regularization element.
Here, if lambda is zero then you can imagine we get back OLS. However, if lambda is very large then it will add too much weight and it will lead to under-fitting. 
Having said that it’s important how lambda is chosen. This technique works very well to avoid over-fitting issue.
 
 - Lasso Regression (Least Absolute Shrinkage and Selection Operator) adds “absolute value of magnitude” of coefficient as penalty term to the loss function.
Again, if lambda is zero then we will get back OLS whereas very large value will make coefficients zero hence it will under-fit.

The key difference between these techniques is that Lasso shrinks the less important feature’s coefficient to zero thus, removing some feature altogether. So, this works well for feature selection in case we have a huge number of features.

#### links:
1. Bagging, Boosting, Stacking:
https://towardsdatascience.com/ensemble-methods-bagging-boosting-and-stacking-c9214a10a205
https://mlcourse.ai/articles/topic5-part1-bagging/#3.-Bagging
2. Regularization:
https://towardsdatascience.com/regularization-in-machine-learning-76441ddcf99a
https://towardsdatascience.com/over-fitting-and-regularization-64d16100f45c
3. Metrics:
https://towardsdatascience.com/understanding-the-roc-and-auc-curves-a05b68550b69
