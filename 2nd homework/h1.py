# wap to extract all the vowels and consolents present in a string

# s= input("Enter a string: ")
# vowels = ''
# consonants = ''
# i= 0
# while i< len(s)
#     char = s[i]
#     if char.isalpha():
#         if i==(char):
#             vowels.append(char)
#         else:
#             consonants.append(char)
#     i+=1
# print("Vowels in the string:", vowels)
# print("Consonants in the string:", consonants)





s = input("Enter a string: ")
vowels = ''
consonants = ''
i = 0

while i < len(s):
    char = s[i]
    if char.isalpha():
        if char in 'aeiouAEIOU':
            vowels += char
        else:
            consonants += char
    i += 1

print(f'"Vowels in the string "{s}" is:"', vowels)
print(f'"Consonants in the string "{s}" is:"', consonants)
