""" wap to print the values from 50 to 500 in file a.txt"""

f=open("a.txt",'w')
for i in range(50,501):
    x=str(i)
    f.write(x+'\n')
f.close()
