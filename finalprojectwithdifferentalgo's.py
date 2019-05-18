# -*- coding: utf-8 -*-
"""FinalProjectWithDifferentAlgo's.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/raobabar/f148fee4062e1b3246a6845307b8c50a/finalprojectwithdifferentalgo-s.ipynb
"""

#To plot diagrams or visualizations
import matplotlib.pyplot as plt
#A python library for array operations
import numpy as np
#A python library for data analysis
import pandas as pd
#importing ensemble and gradient boosting model from python library sklearn
from sklearn.ensemble import GradientBoostingRegressor
#importing XGBClassifier model from python library xgboost
from xgboost import XGBClassifier
#importing SVM from python library sklearn
from sklearn import svm
#importing logistic regression from python library sklearn
from sklearn.linear_model import LogisticRegression
#importing RandomForestClassifier from python library sklearn
from sklearn.ensemble import RandomForestClassifier
#importing GaussianMixture model from python library sklearn
from sklearn.mixture import GaussianMixture
#For splitting data
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, KFold
#For scaling the data
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
#gives you a single interface for all transformation and resulting estimator
from sklearn.pipeline import Pipeline

df = pd.read_csv("heart_processed.csv")
df.head()

#For splitting data into dependent and independent data
X = df[['age', 'sex', 'cp', 'tresp', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']]
y = df['num']

#For splitting data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

#Apply GradientBoosting model on the data

model=GradientBoostingRegressor()
model=model.fit(X,y)
# print(model.score(np.nan_to_num(X),Y))
print(model.score(np.nan_to_num(X_train),y_train))
print(model.score(np.nan_to_num(X_test),y_test))

#To show the data from trained model
plt.figure(figsize=(10, 5))
plt.title("Gradient Boosting")
plt.plot(X, model.predict(X), color='r')
plt.show()

#To find accuracy of this model
accuracy = model.score(X_test,y_test)
print(accuracy*100)

#Apply Gaussian Naive Bayes model on the data
XGB = XGBClassifier()
XGB.fit(X_train,y_train.values.ravel())

#To show the data from trained model
plt.figure(figsize=(10, 5))
plt.title("Gaussian Naive Bayes")
plt.plot(X, XGB.predict(X), color='g')
plt.show()

#To find accuracy of this model
accuracy = XGB.score(X_test,y_test)
print(accuracy*100)

#Logistic Regression
lr = LogisticRegression(penalty = 'l1')
lr.fit(X_train , y_train.values.ravel())
#print(model.score(np.nan_to_num(X),Y))
print(lr.score(np.nan_to_num(X_train),y_train))
print(lr.score(np.nan_to_num(X_test),y_test))

#To show the data from trained model
plt.figure(figsize=(10, 5))
plt.title("Logistic Regression")
plt.plot(X, lr.predict(X), color='b')
plt.show()

#To find accuracy of this model
accuracy = lr.score(X_test,y_test)
print(accuracy*100)

#SVM
sv = svm.SVC()
sv.fit(X_train , y_train.values.ravel())
print(sv.score(np.nan_to_num(X_train),y_train))
print(sv.score(np.nan_to_num(X_test),y_test))

#To show the data from trained model
plt.figure(figsize=(10, 5))
plt.title("Support Vector Machine")
plt.plot(X, sv.predict(X), color='m')
plt.show()

#To find accuracy of this model
accuracy = sv.score(X_test,y_test)
print(accuracy*100)

#Random Forest
rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
rf.fit(X_train , y_train.values.ravel())
print(rf.score(np.nan_to_num(X_train),y_train))
print(rf.score(np.nan_to_num(X_test),y_test))

#To show the data from trained model
plt.figure(figsize=(10, 5))
plt.title("Random Forest")
plt.plot(X, rf.predict(X), color='c')
plt.show()

#To find accuracy of this model
accuracy = rf.score(X_test,y_test)
print(accuracy*100)

#Gaussian Mixture model
gmm = GaussianMixture()
gmm.fit(X_train,y_train.values.ravel())
print(gmm.score(np.nan_to_num(X_train),y_train))
print(gmm.score(np.nan_to_num(X_test),y_test))

#To show the data from trained model
plt.figure(figsize=(10, 5))
plt.title("Gaussian Mixture Model")
plt.plot(X, gmm.predict(X), color='y')
plt.show()

#To find accuracy of this model
accuracy = gmm.score(X_test,y_test)
print(accuracy*100)

