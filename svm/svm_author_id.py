#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

t0 = time()
clf = SVC(kernel="rbf", C = 1000000)
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
clf.fit(features_train, labels_train)
print"training time:",round(time() - t0, 3),"s"

t0 = time()
print "10:",(clf.predict(features_test[10]))
print "26:",(clf.predict(features_test[26]))
print "50:",(clf.predict(features_test[50]))
print"prediction time:",round(time() - t0, 3),"s"

# print(accuracy_score(labels_code, labels_test))

#########################################################

