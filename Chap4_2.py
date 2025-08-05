



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:05:31 2020

@author: sijokuriakose
"""


from typing import List
from typing import Tuple
from typing import Callable



Vector = List[float]

# Matrices 

Matrix = List[List[float]]

A = [[1,2,3],[4,5,6]]
B = [[1,2],[3,4], [5,6]]

def shape(A: Matrix) -> Tuple[int,int]:
    """Returns # of rows of A, # of colums of A"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # number of elements in first row.
    return num_rows, num_cols

print(shape([[1,2,3],[4,5,6]]))

def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A(as a Vector)"""
    return A[i]      # A[i] is already the ith row

def get_column(A: Matrix, j:int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j] for A_i in A]

def make_matrix(num_rows: int ,
                num_cols: int, 
                entry_fn: Callable[[int, int],float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i,j)
    """
    return [[entry_fn(i,j)
             for j in range(num_cols)]
            for i in range(num_rows)]
 

def identify_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

print(identify_matrix(5))



friendship= [(0,1), (0,2), (1,2),(1,3), (2,3), (3,4), (4,5), (5,6), (5,7),
                (6,8),(7,8), (8,9)]

# user 0 1 2 3 4 5 6 7 8 9 

friend_matrix =[[0,1,1,0,0,0,0,0,0,0], # user 0
                [1,0,1,1,0,0,0,0,0,0], # user 1
                [1,1,0,1,0,0,0,0,0,0], # user 2
                [0,1,1,0,1,0,0,0,0,0], # user 3
                [0,0,0,1,0,1,0,0,0,0], # user 4
                [0,0,0,0,1,0,1,1,0,0], # user 5
                [0,0,0,0,0,1,0,0,1,0], # user 6
                [0,0,0,0,0,1,0,0,1,0], # user 7
                [0,0,0,0,0,0,1,1,0,1],  # user 8
                [0,0,0,0,0,0,0,0,1,0]] # user 9
                


print(friend_matrix[0][2])
print(friend_matrix[0][8])


