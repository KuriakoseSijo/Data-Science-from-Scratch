
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:38:03 2020

@author: sijokuriakose
"""

from typing import List
import math

Vector = List[float]

height_weight_age = [70, 170, 40]

grades = [95, 80, 75, 62]


def add(v: Vector, w: Vector) -> Vector:
    """
    Adds corresponding elements
    """
    assert len(v) == len(w), "Vector must be the same length"
    
    return [v_i + w_i for v_i, w_i in zip(v,w)]



def subtract(v: Vector, w: Vector) -> Vector:
    """
    Subtracts corresponding elements
    """
    assert len(v) == len(w), "Vector must be the same length"
    
    return [v_i - w_i for v_i, w_i in zip(v,w)]


print(add([1,2,3], [4,5,6]))
print(subtract([5,7,9], [4,5,6]))

# Sum list of vectors page 57

def vector_sum(vectors: List [Vector]) -> Vector:
    """
    Sums all corresponding elements 
    """
    #Check that vector is not empty
    assert vectors, "no vectors provided."
    
    #Check the vecotrs are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes"
    
    #the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors )
            for i in range(num_elements)]

print(vector_sum([[1,2],[3,4],[5,6],[7,8]]))

# multipy vector by scalar 

def scalar_multiply(c:float, v: Vector) -> Vector:
    """
    Multiplies ecery element by c
    """
    return [c *v_i for v_i in v]

print(scalar_multiply(2,[1,2,3]))

# Vector mean

def vector_mean(vectors: List[Vector]) -> Vector:
    """ Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n,  vector_sum(vectors))

print(vector_mean([[1,2],[3,4],[5,6]]))

# Vector dot product

def dot(v: Vector, w: Vector) -> float:
    """ Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be the same length"
    
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

print(dot([1,2,3], [4,5,6]))


# Vectors sum of squares 

def sum_of_squares(v:Vector) -> float:
    """ Returns v_1 + v_1 + ... + v_n + v_n"""
    return dot(v,v)

print(sum_of_squares([1,2,3]))

# compute magnitude

def magnitude(v:Vector) -> float:
    """ Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))

print(magnitude([3,4]))


# distance between two vectors 
def squared_distance(v: Vector, w: Vector) -> float:
    """ Computes (v_1 - w_1) ** 2 + ... + (v_n-w_n) ** 2"""
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v,w))

# the equivalent
def distance1(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v,w))


