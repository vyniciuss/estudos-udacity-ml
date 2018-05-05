#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

#obter maior e menor
def printMaxAndMinValue(keyToPrint):
    exercised_stock_options = [item[keyToPrint] for k, item in 
    data_dict.iteritems() if not item[keyToPrint] == "NaN"]
    print "min is %s" % min(exercised_stock_options)
    print "max is %s" % max(exercised_stock_options)

printMaxAndMinValue("exercised_stock_options")
printMaxAndMinValue("salary")



### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
#feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2)
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

#codigo antes do scaling
#kmeans = KMeans(n_clusters = 2).fit(finance_features)
#print "Labels", kmeans.labels_
#print "Cluster Centers", kmeans.cluster_centers_
#pred = kmeans.labels_

#codigo depois do scaling
scaler = MinMaxScaler()
features_rescaled = scaler.fit_transform(finance_features)
clf = KMeans(n_clusters = 2)
pred = clf.fit_predict(features_rescaled)

#Qual seria o valor de um salary de $200.000 na nova escala? 
# e de um exercised_stock_options de $1 milhao?
#test_data = numpy.array([[200000., 1000000.]])
#data_test = scaler.transform(test_data)
#print data_test

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, features_rescaled, poi, mark_poi = False, name = "clusters_after_scaling.pdf", f1_name = feature_1, f2_name = feature_2)
    #Draw(pred, finance_features, poi, mark_poi = False, name = "clusters_before_scaling.pdf", f1_name = feature_1, f2_name = feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
