#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
# Apagando os valores Totais do dicionario
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

#pesquisando o maior valor do array
salaryList = []
bonusList = []
for point in data:
    salaryList.append(point[0])
    bonusList.append(point[1])
print salaryList
max_sal = max(salaryList)
print max_sal



#pesquisando os 4 maiores valores
for key in data_dict:
    if (data_dict[key]["salary"] != 'NaN') and (data_dict[key]["bonus"] != 'NaN'):
        if float(data_dict[key]["salary"]) >1000000 and float(data_dict[key]["bonus"])>5000000:
            print key

''''
d = []
for key, value in data_dict.iteritems():
    if value['salary'] != 'NaN' and value['bonus'] != 'NaN':
        d.append((key, value))
d.sort(key=lambda tup : tup[1]['bonus'])
print(d[-1][0])
d.sort(key=lambda tup : tup[1]['salary'])
print(d[-1][0])'''

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


