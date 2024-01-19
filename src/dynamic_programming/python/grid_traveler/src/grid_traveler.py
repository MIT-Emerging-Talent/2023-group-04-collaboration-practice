
"""This is a recursive function that finds the number
of paths,by considering the number of paths to the
top left corner of the grid and the number of paths
to the left of the current position."""
# number of row is "a", number of coloumn is b
def grid(a,b):
    if a == 1:
        return 1
    if b == 1:
        return 1
    #the number of steps to the left is "a-1"
    #the number of steps to down are "b-1"
    return grid(a-1, b) + grid(a, b-1)
