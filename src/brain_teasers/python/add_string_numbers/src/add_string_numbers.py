#helper function, that turn a string number to numbers
def strToNumb(a,b):
    if a.find('.') == -1:
        a, b= int(a), int(b)
    else:
        a, b = float(a), float(b)
    return (a,b)
        
def add_string_numbers():
    a = input("enter the first number: ")
    b = input("enter the second number: ")
    x,y = strToNumb(a, b)
    return str(x+y)
