"""     No Arguement with No retun     """

def no():
    s1=input("Enter the String:")
    s2=input("Enter the string2:")
    if sorted(s1)==sorted(s2):
        print("Anagram")
    else:
        print("Not Anagram")
no()
