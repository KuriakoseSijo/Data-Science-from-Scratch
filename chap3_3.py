#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:25:15 2020

@author: sijokuriakose
"""
from matplotlib import pyplot as plt
from collections import Counter

grades = [83,95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],
        histogram.values(),
        10,
        edgecolor=(0,0,0))

plt.xticks([10* i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()


#------ Figure 3.4

mentions = [ 500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science' ")

# if you don't do this, matplotlib will label the xaxis 0, 1
# and then add a +2.013e3 off in the corner
plt.ticklabel_format(useOffset=False)
#plt.axis([2016.5, 2018.5, 499, 506])
#plt.title("Look at this 'Huge' Increase!")
#plt.show()


# Figure 3-5

plt.axis([2016.5, 2018.5, 0, 506])
plt.title("Not So Huge Anymore")
plt.show()



#------ Figure 3-6

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [ i for i, _ in enumerate(variance)]


# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label = 'bias^2')
plt.plot(xs, total_error, 'b:', label='total error')

# Because we've assigned labels to each series 
# we can get a legend for free (loc=9 means "top center")

plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()

#---------
# Scatterplots
#-------------

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labesl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point 
for label, friend_count, minute_count in zip(labesl, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),
                 xytext=(5,-5),
                 textcoords=('offset points'))

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Arent' Comparable")
plt.xlabel("test 1 grade")
plt.ylabel('test 2 grade')
plt.axis("equal")
plt.show()
