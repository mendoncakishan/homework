# wap to extract the characters present at the even index only if the characters are upper case and having ASCII values divisible by 3
s = input("Enter a string: ")
result= ''
i = 0

while i < len(s):
    char = s[i]
    if i % 2 == 0 and 'A'<=s[i]<='Z' and ord(char) % 3 == 0:
        result += char
    i += 1

print(f'"Characters at even indices that are uppercase and have ASCII values divisible by 3 in string "{s}":', result)
