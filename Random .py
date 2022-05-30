"""    wap to print random number b/w 100-200   """

import random
f=open("c.txt",'w')
n=int(input("Enter the number of terms:"))
for i in range(n):
    x=str(random.randint(100,200))
    f.write(x+' ')
f.close()
