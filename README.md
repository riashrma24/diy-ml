# diy-ml
writing ml algos implementation from scratch. going one algo at a time :)


## 1. KNN (K-nearest neighbours) algo

Assumptions : 
1. Data is in metric space and there's the notion of distance
2. Usage of labelled data, for every data item we need to have a 'y' value
3. 'k' is predefined, which states the number of neighbours to be considered in the process

We can use Euclidean distance, Manhattan Distance, Minkowski distance, etc.

Though we're using it for 2D space, it works completely fine in higher dimensions as well.

It also works for regression problems.

Disadvantages : 

-Not suitable for noisy data, since labels are very important for the proper functioning of KNN, noisy data really hampers the accuracy of the model.

-Lazy learner : During the training stage, it does only one thing, i.e., storing the training data. All the calculations are done during the predication stage.

Applications : Recommendation systems, Document Retrieval systems, Gene expression.

Methods of finding k : 
Meth1- taking square root of number of data items in training data set
(K should be odd inorder to avoid ambiguity, therefore +1 or -1 is done if necessary)

Meth2- Trial and error