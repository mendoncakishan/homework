#wap to reverse positive integer number without typecating.
a=int(input("enter:"))
rev=0
while a!=0:
   lstdig=a%10  #to  fetch last digit
   rev=rev*10+lstdig  #to store lastdigit
   a=a//10  #used for to fetch second digit from last
print(rev)
