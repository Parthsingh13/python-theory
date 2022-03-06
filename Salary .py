""" To calculate the total salary of the employee with the help of Basic salary(HRA,DA...etc) """

Basic=int(input("Enter the basic salary of employee:"))
if(Basic<=10000):
    HRA=(80/100)*Basic
    DA=(90/100)*Basic
    Total=HRA+DA+Basic
    print("Total salary of employee is:" ,Total)
elif(10000<Basic<=20000):
    HRA=(85/100)*Basic
    DA=(90/100)*Basic
    Total=HRA+DA+Basic
    print("Total salary of employee is:" ,Total)
else:
    HRA=(95/100)*Basic
    DA=(95/100)*Basic
    Total=HRA+DA+Basic
    print("Total salary of employee is:" ,Total)

