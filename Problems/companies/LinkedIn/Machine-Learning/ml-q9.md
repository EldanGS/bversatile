- Topic about: Random Forests, bias variance trade off, svm proof, some probability questions, eigen vectors.

### Random Forest

Before we talk about RandomForest, lets consider details of this algorithms.
The RandomForest algorithms consists two machine learning techniques
1. Decision Tree
2. Bootstrap aggregating

- Decision Tree:
    1. Non-parametric, supervised learning algorithms
    2. Decision tree - a condition is written in each inner vertex and a prediction is written in each leaf of the tree.
    3. Given the training data, a decision tree algorithm divides the feature space into regions. 
    For inference, we first see which region does the test data point fall in, and take the mean label values (regression) or the majority label value (classification).
    4. In the general section the decision trees are very easy to overfit. 
    Among other things, you can build a tree where each leaf will correspond to one object of the training sample.
    5. There are two ways to prevent overfitting of trees. 
    First, Stopping Criteria - used to make a decision: separate vertex or make a leaf.
    Competently selected stopping criteria allow to control the overfitting.
    Second, Pruning Trees - is to build a decision trees of maximum complexity and as deep as possible, until there is 1 object in each peak of the tutorial sample.
After that the " pruning" begins, i.e. the removal of leaves in this tree by a certain criteria. 
For example, it is possible to cut as long as the quality of some deferred sampling improves.

- Bootstrap aggregation: 
one of the popular approaches to building subsamples. 
It consists in the fact that L objects are selected from a training sample with the return of L objects. 
In this case, the new sample will also have the size of L, but some objects in it will be repeated, and some objects from the original sample will not get into it. 
It can be shown that a bootstrap sample will contain on average 63% of different objects in the original sample.


- Random Forest:
In the last lesson, decision trees were studied and it was found that they are able to restore very complex patterns, and therefore tend to overfit. 
In other words, the trees are too easily adjusted to the learning sample and are not suitable for making predictions.
But it turns out that the decisive trees are very well suited for combining into a composition and building one untrained algorithm based on a large number of decisive trees.
    1. Paralleling capability - Since each tree is trained independently of all other basic decision trees, it can be trained on a separate kernel or a separate computer.
    In fact, this task allows perfect paralleling: the speed of calculations is proportional to the number of computational cores involved.
    2. Random forest quality evaluation - Each tree from a random forest is trained in a bootstrap sample, which includes approximately 63% of the total sample objects. Thus, about 37% of sample objects were not used in training of this tree, so they can be used to assess the generalization capacity of a random forest.
    This approach is called out-of-bag and allows to estimate forest quality without using delayed sampling or cross-validation.


### SVM


##### links:
1. Decisions Tree: http://www.alanfielding.co.uk/multivar/cart.htm
