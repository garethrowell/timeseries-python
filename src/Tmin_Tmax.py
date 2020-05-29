# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:39:31 2020

@author: GRowell
"""

import csv
from matplotlib import pyplot as plt

ID = [0]
JDate = [0]
tmax = [0]


with open('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_2018.csv') as f:
    csv_reader = csv.reader(f, delimiter =',')
    for row in csv_reader:
        JDate.append(row[1])
        tmax.append(row[3])
        
        
        