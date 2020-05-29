# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:17:55 2020

@author: GRowell
"""




import csv
from matplotlib import pyplot as plt
from typing import List, Dict
from collections import Counter
import math


tmax = [0]


with open('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_90percentile.csv') as f:
    csv_reader = csv.reader(f, delimiter =',')
    for row in csv_reader:
        tmax.append(row[2])
        
        
def bucketize(point: float, bucket_size: float) -> float:
    """Floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)
    
def make_histogram(points: List[float], bucket_size: float) -> float:
    '''Buckets the points and counts how many are in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)
    
def plot_histogram(points: List[float], bucket_size: float, title: str = ""):
    histogram = make_histogram(points, bucket_size)
    plot.bar(histogram.keys(), histogram_values(), width=bucket_size()
    plt.title(title)
    

plot_histogram( tmax, 10, "tmax")
    


