# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:17:55 2020

@author: GRowell
"""


import pandas as pd
import seaborn as sb
import csv
from matplotlib import pyplot as plt


df = sb.load_dataset('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_90percentile.csv')
print(df.head())


# xs = [i for i, _ in enumerate(tmax)]
        
#plt.plot(JDate, tmax, 'b:', label='tmax')  

  

#plt.legend(loc=9)
#plt.xlabel("JDate")
#plt.xticks([])
#plt.title("tmax at Glacier Bay: 1989 - 2018")  

plt.show()


