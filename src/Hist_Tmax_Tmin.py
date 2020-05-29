# -*- coding: utf-8 -*-


# simple histogram plots


from typing import List
from typing import Dict

from collections import Counter
import math
import csv
from matplotlib import pyplot as plt



def bucketize(point: float, bucket_size: float) -> float:
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points: List[float], bucket_size: float) -> Dict[float, int]:
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points: List[float], bucket_size: float, title: str = ""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()


    
 tmax = [0]
 tmin = [0]
 with open('C:\\Users\\GRowell\\Python\\sf\\GLBY_tmax_tmin_2018.csv') as f:
     csv_reader = csv.reader(f, delimiter =',')
     for row in csv_reader:
         tmax.append(row[2])
         tmin.append(row[3])
    plot_histogram(tmax, 10, "tmax")
    plot_histogram(tmin, 10, "tmin")     
        

