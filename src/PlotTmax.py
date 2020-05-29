# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:17:55 2020

@author: GRowell
"""

import csv
from matplotlib import pyplot as plt


tmin = [0]
tmax = [0]


with open('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_tmin_2018.csv') as f:
    csv_reader = csv.reader(f, delimiter =',')
    for row in csv_reader:
        tmax.append(row[2])
        tmin.append(row[3])
        
xs = [i for i, _ in enumerate(tmin)]


plt.rc('figure', figsize=(10, 5))
plt.rc('legend', fancybox=True, framealpha=1)
 
plt.plot(xs, tmin, 'r-', label='tmin')       
plt.plot(xs, tmax, 'b:', label='tmax')  

plt.legend(loc=9)
plt.xlabel("day")
plt.xticks([])
plt.title("Temperature degrees F")  

plt.show()


