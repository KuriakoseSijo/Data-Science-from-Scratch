#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:29:12 2020

@author: sijokuriakose
"""

from collections import Counter
import matplotlib.pyplot as plt
from typing import List
from Chap4 import *
import math


num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,
               13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,
               10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,
               8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,
               6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
               4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,
               3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


friends_counts = Counter(num_friends)
xs = range(101)
ys = [friends_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0,101, 0, 25])
plt.title("Histogram of Friends Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()


num_points = len(num_friends)
print(num_points)

larget_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]


#------
# Central Tendencies 
#-------

def mean(xs: List[float]) -> float:
    return sum(xs)/len(xs)

def _median_odd(xs: List[float]) -> float:
    """if lens(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs)//2]

def _median_even(xs: List[float]) -> float:
    """ If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs)//2 
    return (sorted_xs[hi_midpoint -1])
                  
def median(v: List[float]) -> float: 
    """ Finds the 'middle most' value of v """
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


def quantile(xs: List[float], p: float) -> float:
    """ Returns the pth-percentile value in x """
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

def mode(x: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
           if count == max_count]    

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracing its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    """ Almost the average squared deviation from the mean """
    assert len(xs) >= 2, "Variance requires at least two elements"
    
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations)/(n-1)


def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance """
    return math.sqrt(variance(xs))

def interquartil_range(xs: List[float]) -> float:
    """ Returns the difference between the 75%-ile and the 25%-ile"""
    return quatiles(xs, 0.75)- quatiles(xs, .25)


