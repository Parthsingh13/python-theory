Unit=float(input("Enter the readings/units you used:"))
if(Unit<=50):
    print("Total amount is:",(0.50*Unit))
elif(50<Unit<=150):
    v=Unit-50
    print("Total amount is:",(25+(0.75*v)))
elif(150<Unit<=250):
    v=Unit-150
    print("Total amount is:",(100+(1.2*v)))
else:
    v=Unit-250
    print("Total amount is:",(220+(1.5*v)))
