#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
poi = 0
inv_acc = 0
for item in pred:
    if item == 1.0:
        poi +=1
    else:
        inv_acc += 1
#print poi, len(pred)
#print accuracy_score(pred, y_test)
#inv_acc = float(inv_acc) / len(pred)
#print inv_acc
tp = 0
for i in range(len(pred)):
    if pred[i] == 1.0 and pred[i] == y_test[i]:
        tp += 1
#print tp
prec_score = precision_score(y_test, pred, average = 'binary')
#print prec_score
rec_score = recall_score(y_test, pred, average = 'binary')
print rec_score
