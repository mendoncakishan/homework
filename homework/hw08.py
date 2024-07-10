# 

k = input("Enter a string: ")

if 'A' <= k[0] <= 'Z':
    print(ord(k[0]))
elif 'a' <= k[0] <= 'z':
    print(k[-1])
elif '0' <= k[0] <= '9':
    print(int(k) % 3)
else:
    print(k[::-1])
