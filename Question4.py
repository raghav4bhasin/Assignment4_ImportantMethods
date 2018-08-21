str1 = input("Please enter a string: ")
temp = str1

lst = str1.split(' ')

lst.reverse()
str1 = ''.join(lst)

if (temp == str1):
    print("This is a palindromic string.")
else:
    print("Not a palindromic string.")
