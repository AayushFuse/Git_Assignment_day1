def add(a,b):
    try:
        result = a+b
        return result
    except TypeError:
        print("Please provide valid numeric values for both numbers")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    

def substract(a,b):
    try:
        result = a-b
        return result
    except TypeError:
        print("Please provide valid numeric values for both numbers")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    

def multiply(a,b):
    try:
        result = a*b
        return result
    except TypeError:
        print("Please provide valid numeric values for both numbers")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    

def divide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Error: Cannot Divide By Zero")
    except TypeError:
        print("Please provide valid numeric values for both numbers")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
