# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:17:55 2020

@author: GRowell
"""




import csv
from matplotlib import pyplot as plt


tmax = [0]
JDate = [0]


with open('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_90percentile.csv') as f:
    csv_reader = csv.reader(f, delimiter =',')
    for row in csv_reader:
        JDate.append(row[0])
        tmax.append(row[2])
        
# xs = [i for i, _ in enumerate(tmax)]
        
plt.plot(JDate, tmax, 'b:', label='tmax')  

  

plt.legend(loc=9)
plt.xlabel("JDate")
plt.xticks([])
plt.title("tmax at Glacier Bay: 1989 - 2018")  

plt.show()


