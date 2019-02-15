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

print len(enron_data)
dict = enron_data['GLISAN JR BEN F']
print len(dict)
poi_people = 0
for item in enron_data:
    if enron_data[item]['poi'] == 1:
      poi_people += 1
print poi_people
#print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
#print enron_data['SKILLING JEFFREY K']['total_payments']
#print enron_data['LAY KENNETH L']['total_payments']
#print enron_data['FASTOW ANDREW S']['total_payments']
unq_salary = 0
knownemail = 0
for item in enron_data:
    if enron_data[item]['salary'] != 'NaN':
        unq_salary += 1
    if enron_data[item]['email_address'] != 'NaN':
        knownemail += 1
#print unq_salary, knownemail
people_with_Nan_as_tp = 0
for item in enron_data:
    if enron_data[item]['total_payments'] == 'NaN' :
        people_with_Nan_as_tp += 1
per = float(people_with_Nan_as_tp)/poi_people
print people_with_Nan_as_tp
print(per)
print 10/28.0
