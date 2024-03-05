from mathematical_operations import add,substract,multiply,divide

try:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a number: "))

    print("Sum: ",add(num1,num2))
    print("Difference: ",substract(num1,num2))
    print("Multiplication: ",multiply(num1,num2))
    print("Division: ",divide(num1,num2))


except Exception as e:
    print("Exception: ",e)