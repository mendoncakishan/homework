# entr two values and check if memory loc is same or not
a=eval(input("enter first input:"))
b=eval(input(" entr second input:"))
if id(a)==id(b):
  print("Same memory location")
else:
  print("Not a same memory loaction")