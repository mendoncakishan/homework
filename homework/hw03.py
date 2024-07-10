#  print even index if the value is odd/
# print odd index if the len is even

l=input("enter a string:")
if(len(l)%2==1):
  print("len is odd",l[0::2])
else:
  print("len is even",l[1::2])