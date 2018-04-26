#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# Quantos registros (pessoas) existem no conjunto de dados?
print("Total de registros no dataset: " + str(len(enron_data)))

# Para cada pessoa, quantos atributos estao disponiveis?
print("Total de atributos: " + str(len(enron_data.values()[0])))

# Quantos POIs existem no conjunto de dados E+F
count = 0
for key in enron_data:
    if enron_data[key]['poi'] == True:
        count += 1
print("Total de POIS: " + str(count))

# Qual e o valor total das acoes (stock) pertencentes ao James Prentice?
print("Total de acoes de James Prentice: " + str(enron_data['PRENTICE JAMES']['total_stock_value']))

# Quantos emails nos temos do Wesley Colwell para POIs?
for key in enron_data.keys():
     if "COLWELL WESLEY" in key:
        print("Total de email de Colwell: " + str(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))
        break

# Qual e o valor das opcoes de acoes do Jeffrey K Skilling?
for key in enron_data.keys():
     if "SKILLING JEFFREY K" in key:
        print("Total de acoes de Jeffrey K Skilling: " + str(enron_data['SKILLING JEFFREY K']['exercised_stock_options']))
        break

# Salarios de Lay, Skilling e Fastow?
print("Pagamentos de SKILLING: $" + str(enron_data['SKILLING JEFFREY K']['total_payments']))
print("Pagamentos de FASTOW: $" +  str(enron_data['FASTOW ANDREW S']['total_payments']))
print("Pagamentos de LAY: $ " + str(enron_data['LAY KENNETH L']['total_payments']))

# Qual e a notacao usada quando um atributo nao possui um valor bem definido?
print("Notacao para atributos faltantes: " + str(enron_data['FASTOW ANDREW S']['deferral_payments']))

# Quantas pessoas do conjunto de dados possui um salario quantificado? E quantas possuem um e-mail conhecido?
count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary += 1
    if enron_data[key]['email_address'] != 'NaN':
        count_email += 1
print("Total de pessoas com salario quantificado: " + str(count_salary))
print("Total de pessoas com e-mail: " + str(count_email))


# Quantas pessoas da base E+F (conforme ela esta agora) possuem valores 
# "NaN" para seus pagamentos (total payments)?
count = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count += 1
print("Percentual de pessoas que possuem NaN nos pagamentos: " + str(float(count)/len(enron_data.keys())))
print("Total de pessoas que possuem NaN nos pagamentos: " + str(count))   

 
#Quantos POIs da base E+F (conforme ela esta agora) possuem valores "NaN" para seus pagamentos (total payments)?
#Qual e a porcentagem de pessoas no conjunto de dados estas pessoas representam do total?
count = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        count += 1
print("Percentual de pessoas que possuem NaN nos pagamentos: " + str(float(count)/len(enron_data.keys())))
print("Total de pessoas que possuem NaN nos pagamentos: " + str(count))  
