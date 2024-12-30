import numpy as np
import pandas as pd
from knn import knn

data=pd.read_csv('Social_Network_Ads.csv')

X=data.iloc[:,2:4].values
Y=data.iloc[:,-1].values

print(X.shape)
print(Y.shape)

#dividing the entire dataset into training and test data

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

#since the values are varying too much, we will scale them

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
Y_train=scaler.transform(X_test)

#Creating object of our class and testing

k1=knn(k=3)

k1.fit(X_train,Y_train)


