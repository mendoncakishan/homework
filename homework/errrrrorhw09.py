

k = input("Enter a string: ")

if 50 <= ord(k[-1]) <= 60:
    print(k)
elif 61 <= ord(k[-1]) <= 75:
    print(chr(ord(k[-1]) + 5))
elif 76 <= ord(k[-1]) <= 97:
    print(k[0] + k[-1])
else:
    print("nopp.")