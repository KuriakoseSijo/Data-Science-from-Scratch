#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:00:48 2020

@author: sijokuriakose
"""

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [ 300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

#add title 
plt.title("Nominal GDP")

#add a label to the y-axis 
plt.ylabel("Billions of $")
plt.show()


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8, 11]

# plot bars with left x-coordinates [0,1,2,3,4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")

# label x-axis with the movies names at bar centers 
plt.xticks(range(len(movies)), movies)

plt.show()