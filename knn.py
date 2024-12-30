import operator
from collections import Counter

class knn:
	def __init__(self,k):
	 self.k=k

	def fit(self,X_train,Y_train):
	 self.X_train=X_train
	 self.Y_train=Y_train
	 print("Training done")

