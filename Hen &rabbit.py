""" Logical question of how many number of rabbits and hen """

head=int(input("Enter the number of heads :"))
legs=int(input("Enter the number of legs :"))
temp=head*2
rabbit=(legs-temp)//2
hen=head-rabbit
print("total no of rabbits and hens are:",(rabbit,hen))
