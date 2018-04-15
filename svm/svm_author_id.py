#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn import svm
from sklearn.metrics import accuracy_score


##########################################################
#clf = svm.SVC()
##########Resultados com kernel default###################
# Tempo Treinamento: muito lento, desisti de esperar
# Tempo de Previsao: muito lento, desisti de esperar
# Acuracia da previsao: ?????? 
# Reflexao: a precisao e alta sem adicionar features, mas 
# o tempo de prever e treinar e muito lento, inviavel para
# aplicacoes em tempo real
##########################################################
#clf = svm.SVC(kernel = 'linear')
##########Resultados com kernel linear####################
# Tempo Treinamento: 214.522 's'
# Tempo de Previsao:21.211 's'
# Acuracia da previsao:0.984 
# Reflexao: adicionando o kernel o tempo cai incrivelmente
# e a precisao continua alta
##########################################################
#######Resultados com dados reduzidos#####################
#Obs: Os dados serao reduzidos a 1% do tamanho original
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]
# Tempo Treinamento: 0.108 's'
# Tempo de Previsao: 1.1329 's'
# Acuracia da previsao: 0.884
# Reflexao: Com apenas 1% dos dados, mas 88% de precisao.
#######Resultados com dados reduzidos e kernel=RBF########
#clf = svm.SVC(kernel = 'rbf')
# Tempo Treinamento: 0.11 's'
# Tempo de Previsao: 1.329 's'
# Acuracia da previsao: 0.616
# Reflexao: 66% e uma precisao muito baixa
##########Resultados com kernel linear####################
#clf = svm.SVC(kernel = 'rbf', C = 10)
# Tempo Treinamento: 0.148 's'
# Tempo de Previsao: 1.19  's'
# Acuracia da previsao: 0.616 
# Reflexao: 
##########################################################
#clf = svm.SVC(kernel = 'rbf', C = 100)
# Tempo Treinamento: 0.108 's'
# Tempo de Previsao: 1.229  's'
# Acuracia da previsao: 0.616 
# Reflexao: 
##########################################################
#clf = svm.SVC(kernel = 'rbf', C = 1000)
# Tempo Treinamento: 0.105 's'
# Tempo de Previsao: 1.147  's'
# Acuracia da previsao: 0.821
# Reflexao: 
##########################################################
#clf = svm.SVC(kernel = 'rbf', C = 10000)
# Tempo Treinamento: 0.101 's'
# Tempo de Previsao: 0.95  's'
# Acuracia da previsao: 0.892
# Reflexao: 
########Resultados com todos dados, kernel rbf e c=10000##
clf = svm.SVC(kernel = 'rbf', C = 10000)
#clf = svm.SVC(kernel = 'rbf', C = 10)
# Tempo Treinamento: 130.865 's'
# Tempo de Previsao: 12.994  's'
# Acuracia da previsao: 0.99
# Reflexao: 


t = time()
clf.fit(features_train, labels_train)
print("Tempo de treinamento:", round(time()-t, 3), "s")
# predict
t = time()
#pred = clf.predict(features_test)
pred = clf.predict(features_test)
#usuario 0 e 1 correspondem a Sara e Chris respectivamente
print("Tempo de previsao:", round(time()-t, 3), "s")
print("10 e-mail e do usuario: ", pred[10])
print("26 e-mail e do usuario: ", pred[26])
print("26 e-mail e do usuario: ", pred[50])
accuracy = accuracy_score(pred, labels_test)
print("Previsoes com uma precisao de " + str(accuracy * 100) + "%") 
cont = 0
for i in pred:
    if i == 1: 
        cont += 1
print("Total de e-mails de Chris", cont)