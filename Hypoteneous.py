""" Calculate the distance between the two coordinates """


print("Enter the first coordinate")
a1,b1=int(input("Enter the first point :")),int(input("Enter the secand point :"))

print("Enter the secand coordinate")
a2,b2=int(input("Enter the first point :")),int(input("Enter the secand point :"))

d=((a1-a2)**2+(b1-b2)**2)**(1/2)
print("Distance are :",d)
