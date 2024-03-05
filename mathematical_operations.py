def add(a,b):
    if isinstance(a,(int,float)):
        return a+b
    else:
        raise Exception("Enter a numeric value")
    

def substract(a,b):
    if isinstance(a,(int,float)):
        return a-b
    else:
        raise Exception("Enter a numeric value")
    

def multiply(a,b):
    if isinstance(a,(int,float)):
        return a*b
    else:
        raise Exception("Enter a numeric value")
    


print(multiply(4,6),add(4,6),substract(4,6))