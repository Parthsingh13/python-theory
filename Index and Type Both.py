"""            IndexError and TypeError both      """

try:
    a=["GLA","University","Mathura"]
    i=int(input("Enter the number:"))
    print(a[i])
    a=5+"Hello"
except IndexError:
    print("Index Error")
except TypeError:
    print("Type Error")
