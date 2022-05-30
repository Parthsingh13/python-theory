""" Create a file a.txt and enter the values from 50 to 500 with space"""

f=open("a.txt",'r')
x=f.readlines()
f.close()

p=open("b.txt",'w')
p.writelines(x)
p.close()
