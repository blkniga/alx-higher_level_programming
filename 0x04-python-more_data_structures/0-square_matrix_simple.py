#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    outside = []
    for row in matrix:
        inside = []
        for element in row:
            inside.append(element**2)
        outside.append(inside)
    return outside
