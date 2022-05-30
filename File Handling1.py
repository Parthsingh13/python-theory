"""       wap to print the data from b.txt file to d.txt file       """

f=open("b.txt",'r')
x=f.readlines()
f.close()

p=open("d.txt",'w')
p.writelines(x)
p.close()
