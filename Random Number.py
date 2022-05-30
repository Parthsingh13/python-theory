""" Wap to make a file and the file contains the random numbers between 100- 200 """

import random
f=open("c.txt",'w')
n=int (input("Enter the terms:"))
for i in range(n):
    x=str(random.randint(100,200))
    f.write(x+' ')
f.close()
