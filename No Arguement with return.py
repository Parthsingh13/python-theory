"""     No Arguement with return     """

def no():
    s1=input("Enter the String:")
    s2=input("Enter the string2:")
    if sorted(s1)==sorted(s2):
        return("Anagram")
    else:
        return("Not Anagram")
print(no())
