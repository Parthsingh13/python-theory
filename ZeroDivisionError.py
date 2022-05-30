"""        ZeroDivisionError      """

try:
    a=int(input("Enter the number:"))
    b=int(input("Enter the number2:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Zero division Error")
