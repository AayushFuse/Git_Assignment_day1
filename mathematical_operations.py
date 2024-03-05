def add(a,b):
    result = a+b
    return result
    

def substract(a,b):
    result = a-b
    return result
    

def multiply(a,b):
    result = a*b
    return result
    

def divide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Error: Cannot Divide By Zero")
    
