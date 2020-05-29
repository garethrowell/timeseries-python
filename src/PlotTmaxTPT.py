# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:17:55 2020

@author: GRowell
"""

# import

import matplotlib.pyplot as plt
import numpy as np
import csv


# load data

ID = [0]
JDate = [0]
tmax = [0]

with open('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_2018.csv') as f:
    csv_reader = csv.reader(f, delimiter =',')
    for row in csv_reader:
       JDate.append(row[1])
       tmax.append(row[3])
       

fig, axes = plt.plot(JDate, tmax, 'g',lw=2)
x = np.arange(1,11)

#axes[0].plot(JDate, tmax, 'g',lw=2)
axes[0].grid(True)
axes[0].grid(color='b', ls = '-.', lw = 0.25)
axes[0].set_title('tmax - Glacier Bay 2018')
#axes[1].plot(x, np.exp(x), 'r')
#axes[1].grid(color='b', ls = '-.', lw = 0.25)
#axes[1].set_title('custom grid')
#axes[2].plot(x,x)
#axes[2].set_title('no grid')
fig.tight_layout()
plt.show()
#data_set = pd.read_csv('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_2018.csv')




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


