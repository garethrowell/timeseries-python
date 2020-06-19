
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:34:24 2020

@author: GRowell

numpy structured array for climate data

"""

import numpy as np


# this is a first pass, it is almost certainly too small for the values
#

glba_tmax = np.zeros(6, dtype={'names':('datavalue','cdate','jdate','UTM-X','UTM-Y'),
                    'formats':('f8','U10','i4','f8','f8')})

print(glba_tmax.dtype)


