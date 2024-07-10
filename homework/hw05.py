# consider a tuple of len two & check whether it is tuple is homo or not
a=eval(input("entr a tuple:"))
if(type(a[0])==type(a[1])):
  print("its Homogeneous")
else:
  print("its Heterogeneous")