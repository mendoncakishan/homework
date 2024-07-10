# wap to check if the int is pallindrome or not

n = input("Enter a string or num : ")
a = n[::-1]
if a == n:
    print("Palindrome")
else:
    print("Not Palindrome")
