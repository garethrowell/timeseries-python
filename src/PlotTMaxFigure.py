# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:37:59 2020

@author: GRowell
"""

import matplotlib.pyplot as plt


# load data

ID = [0]
JDate = [0]
tmax = [0]

with open('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_2018_int.csv') as f:
    csv_reader = csv.reader(f, delimiter =',')
    for row in csv_reader:
       JDate.append(row[1])
       tmax.append(row[3])
       
       
fig = plt.figure()
ax = fig.add_axes([0,0,2,2])
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.plot(tmax)
#ax.plot([1,2,3,4,5])
plt.show()




