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

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
import  numpy as np
from collections import Counter

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)



clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
accuracy = accuracy_score(labels_test, pred)
c = Counter( labels_test )
print("Acuracia ", accuracy)
print(c)
total_pessoas = 0
for j in c.items():
    if j[0] == 1.0:
        total_pessoas =  total_pessoas + j[1]
        print("total pois no conjunto de test", j[1])
    else:    
        total_pessoas =  total_pessoas + j[1]

#print("Total de pessoas no conjunto de testes", total_pessoas)
no_cpp = np.sum([1 for j in zip(labels_test, pred) if j[0] == j[1] and j[1] == 1.0])
print("Number of Correct Positive Predictions", no_cpp)
print(no_cpp)

print ("'Precision= ", precision_score(labels_test, pred, average='macro'))
print ("'Recall= ", recall_score(labels_test, pred, average='macro'))
print ("'Precision= ", precision_score(labels_test, pred))
print ("'Recall= ", recall_score(labels_test, pred))


predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

#verdadeiros positivos
count = 0
for i, val in enumerate(predictions):
  if (predictions[i] == 1 and true_labels[i] == 1):
    count+=1
print("Total de verdadeiros positovs", count)

#verdadeiro negativo
count = 0
for i, val in enumerate(predictions):
  if (predictions[i] == 0 and true_labels[i] == 0):
    count+=1

print("Total de verdadeiros negativos", count)

#falsos positivos
count = 0
for i, val in enumerate(predictions):
  if (predictions[i] == 1 and true_labels[i] == 0):
    count+=1

print("Total de falsos positivos", count)

#falsos negativos
count = 0
for i, val in enumerate(predictions):
  if (predictions[i] == 0 and true_labels[i] == 1):
    count+=1

print("Total de falsos negativos", count)


print ("'Precision= ", precision_score(true_labels, predictions))
print ("'Recall= ", recall_score(true_labels, predictions))