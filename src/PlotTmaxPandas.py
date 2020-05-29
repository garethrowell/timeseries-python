# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:17:55 2020

@author: GRowell
"""
import pandas as pd
#import csv
import matplotlib 

matplotlib.rc_params['figure.figsize']=[12.0, 8.0]

ID = [0]
JDate = [0]
tmax = [0]


data_set = pd.read_csv('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_2018.csv')




#with open('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_2018.csv') as f:
#    csv_reader = csv.reader(f, delimiter =',')
#    for row in csv_reader:
#        JDate.append(row[1])
#        tmax.append(row[3])
        
#plt.plot(JDate, tmax, color='blue', marker='o', linestyle='solid')

#plt.title("Glacier Bay 2018")

#plt.xlabel("Julian Date")
#plt.ylabel("Temp Max F")

#plt.show


