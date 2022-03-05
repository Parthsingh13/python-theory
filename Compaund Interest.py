""" CAlculate the compaund interest """

p=int(input("Enter the principle amount :"))
r=int(input("Enter the rate :"))
t=int(input("Enter the time"))
c=p*(1+(r/100))**t
print("Compaund Interest",c)
