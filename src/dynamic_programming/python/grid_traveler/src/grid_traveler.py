"""Given the dimensions of a grid, represented by the number of rows num_rows and the number of columns num_columns, the
   task is to find the total number of unique paths that a traveller can take to go from the top left corner of the grid
   to the bottom right corner. The traveller can only move down or right at each step."""

#solution1
""" The numbers of unique paths are equal to combination of number of step down from all of step.
    So the combination formula is used"""
#helper function, finding factorial of n
def fac(n):
    if n == 1:
        return 1
    return n*(fac(n-1))
#main function, a is number steps down, b number steps to right
def gridTraveler(num_rows, num_columns):
    a = num_columns -1
    b = num_rows -1
    return int(((fac(a+b))/fac(b))/fac(a))
    

#solution 2, recursive function
def grid(a,b):
    if a == 1:
        return 1
    if b == 1:
        return 1
    return grid(a-1, b) + grid(a, b-1)
