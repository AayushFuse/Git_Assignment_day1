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
    


