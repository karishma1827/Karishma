# try:
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter the divident:"))
#     print(num1/num2)
    
# except:
#     print("Invalid input")

try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter the divident:"))
    print(num1/num2)
    
except ZeroDivisionError as err:
    print("Division by zero")
    print(err)
    
except ValueError:
    print("Invalid input")    
    