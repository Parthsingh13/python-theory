""" Calculate the area of scaletal triangle """

a=int(input("Enter the first side of triangle :"))
b=int(input("Enter the secand side of triangle :"))
c=int(input("Enter the third side of triangle :"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(1/2)
print(" Area of triangle :",area)
