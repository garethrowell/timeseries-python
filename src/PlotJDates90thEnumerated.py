# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:17:55 2020

@author: GRowell
"""




import csv
from matplotlib import pyplot as plt



tmax = [0]


with open('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_90percentile.csv') as f:
    csv_reader = csv.reader(f, delimiter =',')
    for row in csv_reader:
        tmax.append(row[2])

        
xs = [i for i, _ in enumerate(tmax)]


plt.rc('figure', figsize=(20, 5))
plt.rc('legend', fancybox=True, framealpha=1)
 
     
plt.plot(xs, tmax, 'b:', label='tmax')  

plt.legend(loc=9)
plt.xlabel("Enumerated...")
plt.xticks([])
plt.title("Temperature degrees F - 90 percentile and above")  

plt.show()


