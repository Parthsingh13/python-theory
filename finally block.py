"""      finally block     """

try:
    f=open("a.txt",'r')
    f.write("Parth")
except IOError:
    print("IOError h")
finally:
    print("Good Morning")
